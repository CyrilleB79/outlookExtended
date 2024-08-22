# -*- coding: UTF-8 -*-
# NVDA add-on: Outlook Extended
# Copyright (C) 2021-2023 Cyrille Bougot
# This file is covered by the GNU General Public License.

# Reworked compatibility wrapper for controlTypes. Original author: Łukasz Golonka

import controlTypes
import operator


class EnhancedGetter(object):

	def __init__(self, modWithAttrs, attrCommonPrefix, alternativeNameFactories):
		super(EnhancedGetter, self).__init__()
		self.mod = modWithAttrs
		self.attrCommonPrefix = attrCommonPrefix
		self.alternativeNameFactories = alternativeNameFactories

	def __getattr__(self, attrName):
		for aliasNameMaker in self.alternativeNameFactories:
			try:
				return operator.attrgetter(aliasNameMaker(self.attrCommonPrefix, attrName))(self.mod)
			except AttributeError:
				continue
		raise AttributeError("Attribute {} not found!".format(attrName))

	def __call__(self, *args, **kwargs):
		enum = getattr(self.mod, self.attrCommonPrefix.capitalize())
		return enum(*args, **kwargs)


class ControlTypesCompatWrapper(object):

	_ALIAS_FACTORIES = (
		lambda attrPrefix, attrName: ".".join((attrPrefix.capitalize(), attrName.upper())),
		lambda attrPrefix, attrName: "_".join((attrPrefix.upper(), attrName.upper()))
	)

	def __init__(self):
		super(ControlTypesCompatWrapper, self).__init__()
		self.Role = EnhancedGetter(
			controlTypes,
			"role",
			self._ALIAS_FACTORIES
		)
		self.State = EnhancedGetter(
			controlTypes,
			"state",
			self._ALIAS_FACTORIES
		)


CTWRAPPER = ControlTypesCompatWrapper()
