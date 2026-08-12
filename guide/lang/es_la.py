"""Latin American Spanish reuses the European Spanish prose on purpose.

The game does the same thing: SpanishLatinAmerica has no translation table of
its own and falls back to Spanish, so the guide would drift from the game if it
carried a separate text. Only the label, the html lang tag and the number format
differ here (Mexico and most of the region group with commas and use a dot for
decimals). If the two variants ever need different wording, copy the sections
dict out of es.py and edit it here.
"""

import copy

from lang.es import LANG as SPANISH

LANG = copy.deepcopy(SPANISH)
LANG["code"] = "es_la"
LANG["name"] = "Español (Latinoamérica)"
LANG["html_lang"] = "es-419"
LANG["locale"] = {"group": ",", "decimal": "."}
