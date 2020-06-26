# tests/unit/__init__.py
# A part of NonVisual Desktop Access (NVDA)
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.
# Copyright (C) 2017-2019 NV Access Limited, Babbage B.V.

import unittest
import os
import sys

import cases

# The path to the unit tests.
UNIT_DIR = os.path.dirname(os.path.abspath(__file__))
# The path to the top of the repo.
TOP_DIR = os.path.dirname(os.path.dirname(UNIT_DIR))
# The path to the NVDA "source" directory.
SOURCE_DIR = os.path.join(TOP_DIR, "addon", "appModules", "outlook")
# Let us import modules from the NVDA source.
sys.path.insert(1, SOURCE_DIR)

from itemWindow import OutlookItemWindow

class FakeObject(object):
	def __init__(self, **attributes):
		super(FakeObject, self).__init__()
		for (k,v) in attributes.items():
			if k == 'cid':
				k = 'windowControlID'
			setattr(self, k, v)

class FakeRootWindow(object):
	def __init__(self, test):
		super(FakeRootWindow, self).__init__()
		objList = cases.tcObjectList[test]
		self.children = [FakeObject(**d) for d in objList]
		

class TestOutlookItemWindow(unittest.TestCase):

	def makeTest(test):
		def test_function(self):
			fakeRoot = FakeRootWindow(test)
			oiw = OutlookItemWindow(rootDialog=fakeRoot)
			windowType = test.split('_')[0]
			self.assertTrue(getattr(oiw, 'is' + windowType)())
		return test_function
		
	for test in cases.tcObjectList.keys():
		locals()['test_' + test] = makeTest(test)
	del makeTest

if __name__ == '__main__':
	unittest.main()
