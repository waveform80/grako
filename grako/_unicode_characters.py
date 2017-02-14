# -*- coding: utf-8 -*-
# Copyright (C) 2017      by Juancarlo Añez
# Copyright (C) 2012-2016 by Juancarlo Añez and Thomas Bragg
from __future__ import absolute_import, division, print_function, unicode_literals

from grako.util import is_posix

U_LARROW = '\u2190'
U_DLARROW = '\u2199'
U_LDARROW = '\u21D0'
U_UDARROW = '\u21D1'
U_RDARROW = '\u21D2'
U_DDARROW = '\u21D3'
U_L_TRIPPLE_ARROW = '\u21DA'

U_WARNING = '\u26A0'

U_NOT_EQUAL_TO = '\u2260'
U_IDENTICAL_TO = '\u2261'
U_NOT_IDENTICAL_TO = '\u2262'

U_CHECK_MARK = '\u2713'

U_POWER_SYMBOL = '\u23FB'
U_POWER_ON_SYMBOL = '\u23FC'
U_POWER_OFF_SYMBOL = '\u23FD'

U_GREEK_SMALL_LETTER_EPSILON = '\u03B5'
U_REGISTERED_SIGN = '\u00AE'
U_RIENNMAN = '\u211D'

U_ANTICLOCKWISE_OPEN_CIRCLE_ARROW = '\u21BA'
U_ANTICLOCKWISE_GAPPED_CIRCLE_ARROW = '\u27F2'

U_PUNCTUATION_SPACE = '\u2008'
U_FOUR_PER_EM_SPACE = '\u2005'
U_MEDIUM_MATHEMATICAL_SPACE = '\u205F'
U_ZERO_WIDTH_NO_BREAK_SPACE = '\uFEFF'


if not is_posix():
    C_DERIVE = '<'
    C_ENTRY = '<'
    C_SUCCESS = '>'
    C_FAILURE = '!'
    C_RECURSION = 'r '
else:
    C_DERIVE = U_DLARROW
    C_ENTRY = C_DERIVE
    C_SUCCESS = U_IDENTICAL_TO
    C_FAILURE = U_NOT_IDENTICAL_TO
    C_RECURSION = U_ANTICLOCKWISE_GAPPED_CIRCLE_ARROW + U_FOUR_PER_EM_SPACE
