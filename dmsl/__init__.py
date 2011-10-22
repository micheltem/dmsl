# -*- coding: utf-8 -*-
"""
import dmsl
dmsl.set_template_dir('my/templates')
dmsl.parse('index.dmsl', {'content': 'Hello World!'})
"""
__version__ = '3'
from _parse import Template
import _sandbox
from _sandbox import extensions

def set_template_dir(value):
    _sandbox._open.template_dir = value

def parse(t, context={}):
    return Template(t).render(context)


