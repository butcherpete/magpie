#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tes <tes@C02T72XNG8WL-lm>
#
# Distributed under terms of the MIT license.

from docutils import nodes

def setup(app):
    app.add_role('github', autolink('https://github.com/%s'))
    app.add_role('module', autolink('https://github.com/bemusic/bemuse/tree/master/src/%s'))
    app.add_role('tree', autolink('https://github.com/bemusic/bemuse/tree/master/%s'))

def autolink(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        url = pattern % (text,)
        node = nodes.reference(rawtext, text, refuri=url, **options)
        return [node], []
    return role
