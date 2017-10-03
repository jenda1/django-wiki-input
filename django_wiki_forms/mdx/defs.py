# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re
import markdown

from .. import utils
#
DEFFN_RE = re.compile(
    r'(?P<prefix>.*?)\[\s*def\s+(?P<target>\w+?)\((?P<args>.*)\)(?P<inline>\s*:\s*(?P<expr>.+?))\s*\](?P<suffix>.*)$',
    re.IGNORECASE
)

DEFVAR_RE = re.compile(
    r'(?P<prefix>.*?)\[\s*def\s+(?P<target>\w+?)\s*\](?P<suffix>.*)$',
    re.IGNORECASE
)

DEFVAR_INLINE_RE = re.compile(
    r'(?P<prefix>.*?)\[\s*def\s+(?P<target>\w+?)\s*=\s*(?P<expr>.+?)\s*\](?P<suffix>.*)$',
    re.IGNORECASE
)


DEF_END_RE = re.compile(
    r'(?P<prefix>.*?)\[\s*enddef\s*\](?P<suffix>.*)$',
    re.IGNORECASE
)


class DefExtension(markdown.Extension):

    """ Defs plugin markdown extension for django-wiki. """

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('dw-def', DefPreprocessor(md), '<dw-input')


class DefPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, *args, **kwargs):
        super(DefPreprocessor, self).__init__(*args, **kwargs)
        self.in_def = None

        if self.markdown:
            self.markdown.defs = dict()


    def process_line(self, line):
        if self.in_def:
            m = DEF_END_RE.match(line)
            if m:
                self.in_def.append(m.group('prefix'))
                self.in_def = None

                return self.process_line(m.group('suffix'))

            else:
                self.in_def.append(line+"\n")
                return ""

        # m = DEFFN_RE.match(line)
        # if m:
        #    o = utils.DefFn(m.group('args'))

        m = DEFVAR_INLINE_RE.match(line)
        if m:
            o = utils.DefVarExpr(m.group('expr'))
            self.markdown.defs[m.group('target')] = o

            return m.group('prefix') + self.process_line(m.group('suffix'))


        m = DEFVAR_RE.match(line)
        if m:
            self.in_def = utils.DefVarStr()
            self.markdown.defs[m.group('target')] = self.in_def

            return m.group('prefix') + self.process_line(m.group('suffix'))

        return line

        return m.group('prefix') + self.process_line(m.group('suffix'))


    def run(self, lines):
        return [self.process_line(l) for l in lines]