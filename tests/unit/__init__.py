# tests/unit/__init__.py
# NVDA add-on: Outlook Extended
# Copyright (C) 2020 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import unittest
import os
import sys

import cases
from fakeObjects import FakeRootWindow

# The path to the unit tests.
UNIT_DIR = os.path.dirname(os.path.abspath(__file__))
# The path to the top of the repo.
TOP_DIR = os.path.dirname(os.path.dirname(UNIT_DIR))
# The path to the NVDA "source" directory.
SOURCE_DIR = os.path.join(TOP_DIR, "addon", "appModules", "outlook")
# Let us import modules from the add-on source.
sys.path.insert(1, SOURCE_DIR)

from itemWindow import OutlookItemWindow  # noqa: E402 - Needed here after path modification.


class TestOutlookItemWindow(unittest.TestCase):

	def makeTestIsWindowType(test):
		def test_function(self):
			fakeRoot = FakeRootWindow(test)
			oiw = OutlookItemWindow(rootDialog=fakeRoot)
			windowType = test.split('_')[0]
			self.assertTrue(getattr(oiw, 'is' + windowType)())
		return test_function

	for test in cases.tcObjectPropertyDic.keys():
		locals()['testIs%s' % test] = makeTestIsWindowType(test)
	del makeTestIsWindowType

	def makeTestGetWindowTypeFields(test):
		def test_function(self):
			fakeRoot = FakeRootWindow(test)
			oiw = OutlookItemWindow(rootDialog=fakeRoot)
			windowType = test.split('_')[0]
			cid = getattr(oiw, 'get' + windowType + 'HeaderFields')()
			cids = cases.tcHeaderFieldDic[test]
			if not isinstance(cid, tuple):
				cids = (cids,)
			try:
				self.assertTrue(cid in cids)
			except Exception:
				print('=== cid ===')
				print(cid)
				print('=== cids ===')
				print(cids)
				raise
		return test_function

	for test in cases.tcObjectPropertyDic.keys():
		locals()['testGet%sHeaderFields' % test] = makeTestGetWindowTypeFields(test)
	del makeTestGetWindowTypeFields


if __name__ == '__main__':
	unittest.main()
