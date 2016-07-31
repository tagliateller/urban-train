#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: expandtab:tabstop=4:shiftwidth=4
"""
Custom filters for use in paas 
"""

from ansible import errors
from collections import Mapping
from distutils.version import LooseVersion
from operator import itemgetter
import OpenSSL.crypto
import os
import pdb
import pkg_resources
import re
import json
import yaml
from ansible.utils.unicode import to_unicode

# Disabling too-many-public-methods, since filter methods are necessarily
# public
# pylint: disable=too-many-public-methods
class FilterModule(object):
    """ Custom ansible filters """

    @staticmethod
    def get_attr(data, attribute=None):
        """ This looks up dictionary attributes of the form a.b.c and returns
            the value.
            Ex: data = {'a': {'b': {'c': 5}}}
                attribute = "a.b.c"
                returns 5
        """
        if not attribute:
            raise errors.AnsibleFilterError("|failed expects attribute to be set")

        ptr = data
        for attr in attribute.split('.'):
            ptr = ptr[attr]

        return ptr

    @staticmethod
    def paas_collect(data, attribute=None, filters=None):
        """ This takes a list of dict and collects all attributes specified into a
            list. If filter is specified then we will include all items that
            match _ALL_ of filters.  If a dict entry is missing the key in a
            filter it will be excluded from the match.
            Ex: data = [ {'a':1, 'b':5, 'z': 'z'}, # True, return
                         {'a':2, 'z': 'z'},        # True, return
                         {'a':3, 'z': 'z'},        # True, return
                         {'a':4, 'z': 'b'},        # FAILED, obj['z'] != obj['z']
                       ]
                attribute = 'a'
                filters   = {'z': 'z'}
                returns [1, 2, 3]
        """
        if not isinstance(data, list):
            raise errors.AnsibleFilterError("|failed expects to filter on a List")

        if not attribute:
            raise errors.AnsibleFilterError("|failed expects attribute to be set")

        if filters is not None:
            if not isinstance(filters, dict):
                raise errors.AnsibleFilterError("|failed expects filter to be a"
                                                " dict")
            retval = [FilterModule.get_attr(d, attribute) for d in data if (
                all([d.get(key, None) == filters[key] for key in filters]))]
        else:
            retval = [FilterModule.get_attr(d, attribute) for d in data]

        return retval

    @staticmethod
    def paas_prepend_strings_in_list(data, prepend):
        """ This takes a list of strings and prepends a string to each item in the
            list
            Ex: data = ['cart', 'tree']
                prepend = 'apple-'
                returns ['apple-cart', 'apple-tree']
        """
        if not isinstance(data, list):
            raise errors.AnsibleFilterError("|failed expects first param is a list")
        if not all(isinstance(x, basestring) for x in data):
            raise errors.AnsibleFilterError("|failed expects first param is a list"
                                            " of strings")
        retval = [prepend + s for s in data]
        return retval

    def filters(self):
        """ returns a mapping of filters to methods """
        return {
            "paas_collect": self.paas_collect,
            "paas_prepend_strings_in_list": self.paas_prepend_strings_in_list,
        }
