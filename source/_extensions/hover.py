#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tes <tes@C02T72XNG8WL-lm>
#
# Distributed under terms of the MIT license.
#
#"""
#Copy of abbr_role with hover substituted for abbr
#"""
#
#from docutils import nodes
#import re
#
#
#hover_re = re.compile(r'\((.*)\)$', re.S)
#
#
#def hover_role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
#    # type: (unicode, unicode, unicode, int, Inliner, Dict, List[unicode]) -> Tuple[List[nodes.Node], List[nodes.Node]]  # NOQA
#    text = utils.unescape(text)
#    m = _hover_re.search(text)  # type: ignore
#    if m is None:
#        return [addnodes.hover-box(text, text, **options)], []
#    abbr = text[:m.start()].strip()
#    expl = m.group(1)
#    options = options.copy()
#    options['explanation'] = expl
#    return [addnodes.hover-box(abbr, abbr, **options)], []
