# -*- coding: UTF-8 -*-
# tests/unit/fakeRootWindow.py
# NVDA add-on: Outlook Extended
# Copyright (C) 2020 Cyrille Bougot
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.

import cases

class FakeNVDAObject(object):
	def __init__(self, **attributes):
		super(FakeNVDAObject, self).__init__()
		for (k,v) in attributes.items():
			if k == 'cid':
				k = 'windowControlID'
			setattr(self, k, v)

class FakeRootWindow(object):
	def __init__(self, test):
		super(FakeRootWindow, self).__init__()
		objList = cases.tcObjectPropertyDic[test]
		self.children = [FakeNVDAObject(**d) for d in objList]
