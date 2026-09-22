"""Rendering half of the guide builder: locale-aware numbers, tables, sections.

Kept apart from build.py so the long CSS block does not bury the logic.
"""

import numbers as numbers_module

CURRENCY_ROWS = [
    ("currency_gold", "cur-gold", "gold"),
    ("currency_diamond", "cur-diamond", "diamond"),
    ("currency_essence", "cur-essence", "essence"),
    ("currency_taskium", "cur-taskium", "taskium"),
    ("currency_dungeon_key", "cur-key", "dungeon_key"),
    ("currency_skill_stone", "cur-skillstone", "skill_stone"),
    ("currency_ore_stone", "cur-orestone", "ore_stone"),
    ("currency_abyss_key", "cur-abysskey", "abyss_key"),
    ("currency_pure_essence", "cur-pureessence", "pure_essence"),
]

PACKAGE_CURRENCIES = ["currency_diamond", "currency_essence", "currency_skill_stone", "currency_dungeon_key"]

RARITIES = ["common", "rare", "epic", "legendary"]

ARROW = " → "


def group_digits(digits, separator):
    if len(digits) < 4 or not separator:
        return digits
    parts = []
    while len(digits) > 3:
        parts.insert(0, digits[-3:])
        digits = digits[:-3]
    parts.insert(0, digits)
    return separator.join(parts)


class Locale(object):
    def __init__(self, spec):
        self.group = spec.get("group", ",")
        self.decimal = spec.get("decimal", ".")
        self.percent_format = spec.get("percent", "{0}%")

    def number(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, float) and value != int(value):
            text = "{0:g}".format(value)
            whole, _, fraction = text.partition(".")
            return group_digits(whole, self.group) + self.decimal + fraction
        return group_digits(str(int(value)), self.group)

    def percent(self, value):
        return self.percent_format.format(self.number(value))

    def joined(self, values):
        return " / ".join(self.number(value) for value in values)


def effect_text(spec, locale, labels):
    kind = spec[0]
    if kind == "multiplier":
        if len(spec) == 2:
            return "x{0}".format(locale.number(spec[1]))
        return "x{0}{1}x{2}".format(locale.number(spec[1]), ARROW, locale.number(spec[2]))
    if kind == "hits":
        return "{0}{1}{2} {3}".format(
            locale.number(spec[1]), ARROW, locale.number(spec[2]), labels["per_second"])
    if kind == "clicks":
        return "{0} {1}".format(locale.number(spec[1]), labels["per_second"])
    if kind == "cut":
        return "-{0}{1}{2}-{3}{4}".format(
            locale.number(spec[1]), labels["second_short"], ARROW,
            locale.number(spec[2]), labels["second_short"])
    raise KeyError(kind)


def duration_text(pair, locale, labels):
    duration, cooldown = pair
    second = labels["second_short"]
    if duration == 0:
        return "{0}{1}".format(locale.number(cooldown), second)
    return "{0}{1} / {2}{3}".format(
        locale.number(duration), second, locale.number(cooldown), second)


def material_name(names, rarity_key, kind):
    template = names["enchantment_dust_format"] if kind == "dust" else names["enchantment_piece_format"]
    return template.replace("{0}", names[rarity_key])


def enchantment_name(names, rarity_key):
    return names["enchantment_name_format"].replace("{0}", names[rarity_key]).replace("{1}", names["enchantment_item"])


def build_tokens(lang, names):
    locale = Locale(lang.get("locale", {}))
    labels = lang["labels"]
    values = {}
    for key in numbers_module.SCALARS:
        values[key.lower()] = locale.number(getattr(numbers_module, key))
    values["date"] = numbers_module.DATE
    values["item_skill_levels"] = locale.joined(numbers_module.ITEM_SKILL_LEVELS)
    values["item_skill_first_level"] = locale.number(numbers_module.ITEM_SKILL_LEVELS[0])
    values["item_skill_last_level"] = locale.number(numbers_module.ITEM_SKILL_LEVELS[-1])
    values["bonus_second_level"] = locale.number(
        numbers_module.BONUS_START_LEVEL + numbers_module.BONUS_LEVEL_STEP)
    values["bonus_third_level"] = locale.number(
        numbers_module.BONUS_START_LEVEL + 2 * numbers_module.BONUS_LEVEL_STEP)
    values["bonus_first_power"] = locale.number(1 + numbers_module.BONUS_POWER_STEP)
    values["bonus_second_power"] = locale.number(round(1 + 2 * numbers_module.BONUS_POWER_STEP, 4))
    values["task_slot_floors"] = locale.joined(numbers_module.TASK_SLOT_FLOORS)
    values["worker_slot_floors"] = locale.joined(numbers_module.WORKER_SLOT_FLOORS)
    values["worker_first_floor"] = locale.number(numbers_module.WORKER_SLOT_FLOORS[0])
    values["enchant_slot_floors"] = locale.joined(numbers_module.ENCHANT_SLOT_FLOORS)
    values["enchant_first_slot_floor"] = locale.number(numbers_module.ENCHANT_SLOT_FLOORS[0])
    values["title_effect_unlocks"] = locale.joined(numbers_module.TITLE_EFFECT_UNLOCKS)
    values["pet_cost_list"] = locale.joined(numbers_module.PET_COSTS)
    values["pet_cost_first"] = locale.number(numbers_module.PET_COSTS[0])
    values["pet_cost_last"] = locale.number(numbers_module.PET_COSTS[-1])
    values["diamond_pack_list"] = locale.joined(numbers_module.DIAMOND_PACKS)
    values["key_pack_list"] = locale.joined(numbers_module.KEY_PACKS)
    values["time_skip_hour_list"] = locale.joined(numbers_module.TIME_SKIP_HOURS)
    values["time_skip_price_list"] = locale.joined(numbers_module.TIME_SKIP_PRICES)
    values["dismantle_refund_list"] = locale.joined([tier[8] for tier in numbers_module.ENCHANT_TIERS])
    values["enchant_power_list"] = " / ".join(
        "x{0}".format(locale.number(tier[9])) for tier in numbers_module.ENCHANT_TIERS)
    values["task_reward_range"] = "{0}-{1}".format(
        locale.number(numbers_module.TASK_REWARD_MIN),
        locale.number(numbers_module.TASK_REWARD_MAX))
    values["boss_first_health"] = "1e{0}".format(numbers_module.BOSSES[0][1])
    values["boss_last_health"] = "1e{0}".format(numbers_module.BOSSES[-1][1])
    values["boss_first_timer"] = locale.number(numbers_module.BOSSES[0][2])
    values["boss_last_timer"] = locale.number(numbers_module.BOSSES[-1][2])
    for slug, contents in (("small", numbers_module.PACKAGE_SMALL_CONTENTS),
                           ("big", numbers_module.PACKAGE_BIG_CONTENTS)):
        parts = [
            "{0} {1}".format(locale.number(amount), names[currency])
            for amount, currency in zip(contents, PACKAGE_CURRENCIES)
        ]
        values["package_{0}_contents".format(slug)] = ", ".join(parts)
    values["rare_ore_names"] = ", ".join(names[key] for key in numbers_module.RARE_ORE_NAME_KEYS)
    for rarity in RARITIES:
        rarity_key = "rarity_" + rarity
        values["enchantment_" + rarity] = enchantment_name(names, rarity_key)
        values["dust_" + rarity] = material_name(names, rarity_key, "dust")
        values["piece_" + rarity] = material_name(names, rarity_key, "piece")
    values.update(names)
    values.update(lang.get("extra_tokens", {}))
    return values, locale, labels


def fill(text, values):
    return text.format(**values)


def table_html(head, rows, numeric_columns=()):
    parts = ['<div class="table-wrap">', "<table>", "<thead><tr>"]
    for index, label in enumerate(head):
        css = ' class="num"' if index in numeric_columns else ""
        parts.append("<th{0}>{1}</th>".format(css, label))
    parts.append("</tr></thead>")
    parts.append("<tbody>")
    for row in rows:
        parts.append("<tr>")
        for index, cell in enumerate(row):
            css = ' class="num"' if index in numeric_columns else ""
            parts.append("<td{0}>{1}</td>".format(css, cell))
        parts.append("</tr>")
    parts.append("</tbody></table></div>")
    return "\n        ".join(parts)


def generated_table(key, lang, values, names, locale, labels):
    if key == "skills":
        head = [labels["skill"], labels["unlock_floor"], labels["level_first"],
                labels["level_last"], labels["effect"]]
        rows = []
        for skill, floor, first, last, effect in numbers_module.SKILLS:
            rows.append([
                names[skill],
                locale.number(floor),
                duration_text(first, locale, labels),
                duration_text(last, locale, labels),
                effect_text(effect, locale, labels),
            ])
        return table_html(head, rows, numeric_columns=(1, 2, 3, 4))
    if key == "bosses":
        head = [labels["boss"], labels["health"], labels["time_limit"], labels["reward"]]
        rows = []
        for boss, exponent, timer, essence, ore_stone in numbers_module.BOSSES:
            reward = "{0} {1} + {2} {3}".format(
                locale.number(essence), names["currency_essence"],
                locale.number(ore_stone), names["currency_ore_stone"])
            rows.append([
                names[boss],
                "1e{0}".format(exponent),
                "{0}{1}".format(locale.number(timer), labels["second_short"]),
                reward,
            ])
        return table_html(head, rows, numeric_columns=(1, 2))
    if key == "prestige":
        head = [labels["parameter"], labels["effect"], labels["per_level"]]
        rows = [
            [names[parameter], labels[effect], "+" + locale.percent(per_level)]
            for parameter, effect, per_level in numbers_module.PRESTIGE_PARAMETERS
        ]
        return table_html(head, rows, numeric_columns=(2,))
    if key == "depth":
        head = [labels["depth"], labels["ore_types"], labels["around_floor"]]
        rows = []
        for (start, end), ore_types, floor in numbers_module.DEPTH_TIERS:
            if end is None:
                depth = "{0} {1}+".format(locale.number(start), labels["meter_short"])
            else:
                depth = "{0}-{1} {2}".format(locale.number(start), locale.number(end), labels["meter_short"])
            rows.append([
                depth,
                locale.number(ore_types),
                "~{0}".format(locale.number(floor)) if floor else "-",
            ])
        return table_html(head, rows, numeric_columns=(0, 1, 2))
    if key == "infinity":
        head = [labels["item"], labels["effect"], labels["cost"]]
        rows = [
            [names[item], effect_text(effect, locale, labels),
             "{0} \U0001F48E".format(locale.number(cost))]
            for item, cost, effect in numbers_module.INFINITY_ITEMS
        ]
        return table_html(head, rows, numeric_columns=(1, 2))
    if key == "enchantments":
        head = [labels["tier"], labels["affixes"], labels["drop_floor"], labels["dust_chance"],
                labels["piece_chance"], labels["craft_cost"]]
        rows = []
        for rarity, low, high, floor, dust, piece, craft_dust, fee, refund, power in numbers_module.ENCHANT_TIERS:
            affixes = locale.number(low) if low == high else "{0}-{1}".format(locale.number(low), locale.number(high))
            rows.append([
                names[rarity],
                affixes,
                locale.number(floor),
                locale.percent(dust),
                locale.percent(piece),
                "{0} / 1 / {1}".format(locale.number(craft_dust), locale.number(fee)),
            ])
        return table_html(head, rows, numeric_columns=(1, 2, 3, 4, 5))
    if key == "chest":
        head = [labels["item"], labels["amount"], labels["chance"]]
        total = float(sum(weight for _, _, _, weight in numbers_module.CHEST_REWARDS))
        rows = [
            [material_name(names, rarity, kind), locale.number(amount),
             locale.percent(round(weight / total * 100, 2))]
            for rarity, kind, amount, weight in numbers_module.CHEST_REWARDS
        ]
        return table_html(head, rows, numeric_columns=(1, 2))
    raise KeyError(key)


def currency_cards(lang, values, names):
    cards = []
    for name_key, color, slug in CURRENCY_ROWS:
        if slug not in lang["currencies"]:
            continue
        entry = lang["currencies"][slug]
        cards.append(
            '<div class="cur-card" style="--dot:var(--{0})">\n'
            '          <h4><span class="dot"></span>{1}</h4>\n'
            '          <p>{2}</p>\n'
            '          <p>{3}</p>\n'
            '        </div>'.format(color, names[name_key], fill(entry[0], values), fill(entry[1], values))
        )
    return '<div class="currency-grid">\n        ' + "\n        ".join(cards) + "\n      </div>"


def render_block(block, lang, values, names, locale, labels):
    kind, body = block
    if kind == "p":
        return "<p>{0}</p>".format(fill(body, values))
    if kind == "ul":
        items = "\n          ".join("<li>{0}</li>".format(fill(item, values)) for item in body)
        return "<ul>\n          {0}\n        </ul>".format(items)
    if kind in ("note", "warn"):
        css = "callout warn" if kind == "warn" else "callout"
        return (
            '<div class="{0}">\n'
            '          <div class="callout-label">{1}</div>\n'
            '          {2}\n'
            '        </div>'.format(css, fill(body[0], values), fill(body[1], values))
        )
    if kind == "stages":
        stages = []
        for label, items in body:
            lines = "\n              ".join("<li>{0}</li>".format(fill(item, values)) for item in items)
            stages.append(
                '<div class="strategy-stage">\n'
                '            <div class="stage-label">{0}</div>\n'
                '            <ul>\n              {1}\n            </ul>\n'
                '          </div>'.format(fill(label, values), lines)
            )
        return '<div class="strategy-track">\n          ' + "\n          ".join(stages) + "\n        </div>"
    if kind == "table":
        return generated_table(body, lang, values, names, locale, labels)
    if kind == "currencies":
        return currency_cards(lang, values, names)
    raise KeyError(kind)
