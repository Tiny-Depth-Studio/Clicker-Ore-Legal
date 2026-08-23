"""Pull in-game proper names out of the Unity localization tables.

The guide must never invent its own name for a skill, boss, pet or prestige
parameter: whatever the player sees in the game is what the guide has to say.
So instead of translating those names by hand we read them straight out of
Assets/_Game/Scripts/Systems/LocalizationSystem, once per language, and write
them to names.py for build.py to consume.

English lives in the domain tables (XxxTextTable.cs, `table.Add(key, en)`),
every other language in Translations/XxxTable.cs (`table.AddTranslation(Id,
key, text)`). Spanish (Latin America) has no table of its own on purpose - the
game falls back to Spanish - so the guide mirrors that fallback.

Run:  python guide/extract_names.py
"""

import json
import os
import re

GAME_REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Clicker-Ore-Game")
LOC = os.path.join(GAME_REPO, "Assets", "_Game", "Scripts", "Systems", "LocalizationSystem", "Scripts", "Utils")

TABLES = {
    "tr": "TurkishTable.cs",
    "de": "GermanTable.cs",
    "fr": "FrenchTable.cs",
    "es": "SpanishTable.cs",
    "ru": "RussianTable.cs",
    "ja": "JapaneseTable.cs",
    "zh_hans": "ChineseSimplifiedTable.cs",
    "zh_hant": "ChineseTraditionalTable.cs",
    "pt_br": "PortugueseBrazilTable.cs",
    "pl": "PolishTable.cs",
    "it": "ItalianTable.cs",
    "ko": "KoreanTable.cs",
    "uk": "UkrainianTable.cs",
    "th": "ThaiTable.cs",
    "id": "IndonesianTable.cs",
    "vi": "VietnameseTable.cs",
}

FALLBACK = {"es_la": "es"}

WANTED = {
    "currency_gold": "CurrencyTextKeys.GoldName",
    "currency_diamond": "CurrencyTextKeys.DiamondName",
    "currency_essence": "CurrencyTextKeys.EssenceName",
    "currency_taskium": "CurrencyTextKeys.TaskiumName",
    "currency_dungeon_key": "CurrencyTextKeys.DungeonKeyName",
    "currency_skill_stone": "CurrencyTextKeys.SkillStoneName",
    "currency_ore_stone": "CurrencyTextKeys.OreStoneName",
    "skill_ore_breaker": "SkillTextKeys.OreBreakerName",
    "skill_anger_click": "SkillTextKeys.AngerClickName",
    "skill_critical_strike": "SkillTextKeys.CriticalStrikeName",
    "skill_rampage": "SkillTextKeys.RampageName",
    "skill_heat_resistance": "SkillTextKeys.HeatResistanceName",
    "skill_golden_frenzy": "SkillTextKeys.GoldenFrenzyName",
    "skill_overcharge": "SkillTextKeys.OverchargeName",
    "skill_time_reversal": "SkillTextKeys.TimeReversalName",
    "prestige_dps": "PrestigeTextKeys.DamagePerSecondName",
    "prestige_click": "PrestigeTextKeys.ClickDamageName",
    "prestige_gold": "PrestigeTextKeys.GoldMultiplierName",
    "prestige_crit_chance": "PrestigeTextKeys.CriticalChanceName",
    "prestige_crit_multiplier": "PrestigeTextKeys.CriticalMultiplierName",
    "prestige_heat": "PrestigeTextKeys.HeatResistanceName",
    "prestige_click_from_dps": "PrestigeTextKeys.ClickDamageFromDamagePerSecondName",
    "boss_1": "BossTextKeys.Name(1)",
    "boss_2": "BossTextKeys.Name(2)",
    "boss_3": "BossTextKeys.Name(3)",
    "boss_4": "BossTextKeys.Name(4)",
    "boss_5": "BossTextKeys.Name(5)",
    "boss_6": "BossTextKeys.Name(6)",
    "boss_7": "BossTextKeys.Name(7)",
    "boss_8": "BossTextKeys.Name(8)",
    "boss_9": "BossTextKeys.Name(9)",
    "boss_10": "BossTextKeys.Name(10)",
    "pet_1": "ItemTextKeys.PetName(1)",
    "pet_2": "ItemTextKeys.PetName(2)",
    "pet_3": "ItemTextKeys.PetName(3)",
    "pet_4": "ItemTextKeys.PetName(4)",
    "pet_5": "ItemTextKeys.PetName(5)",
    "infinity_power": "StoreTextKeys.InfinityDamageMultiplierName",
    "infinity_income": "StoreTextKeys.InfinityGoldMultiplierName",
    "infinity_armor": "StoreTextKeys.InfinityHeatResistanceMultiplierName",
    "infinity_speed": "StoreTextKeys.InfinityAttackSpeedName",
    "infinity_clicker": "StoreTextKeys.InfinityClickerName",
    "package_small": "StoreTextKeys.CurrencyPackage1Name",
    "package_big": "StoreTextKeys.CurrencyPackage2Name",
    "rare_ore_1": "OreTextKeys.OreFerrovyxName",
    "rare_ore_2": "OreTextKeys.OreKarnythName",
    "rare_ore_3": "OreTextKeys.OreThalverisName",
    "rare_ore_4": "OreTextKeys.OreUmbryssaName",
    "rare_ore_5": "OreTextKeys.OreZephirisName",
    "ore_gold_crystal": "OreTextKeys.OreGoldCrystalName",
}

# Bir anahtari birden fazla urun paylasiyor: metinde {0} yer tutucusu var ve oyun
# onu calisma aninda dolduruyor. Kilavuz da ayni yer tutucuyu doldurmak zorunda,
# yoksa sayfaya ham "{0}" dusuyor.
FORMATTED = {
    "package_premium_7": ("StoreTextKeys.PremiumPackageName", "7"),
    "package_premium_30": ("StoreTextKeys.PremiumPackageName", "30"),
    "time_skip_2h": ("StoreTextKeys.TimeSkipName", "2"),
    "time_skip_4h": ("StoreTextKeys.TimeSkipName", "4"),
    "time_skip_8h": ("StoreTextKeys.TimeSkipName", "8"),
}


def unescape(text):
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), text).replace('\\"', '"')


def scan(path, pattern):
    found = {}
    with open(path, encoding="utf-8") as handle:
        source = handle.read()
    for match in re.finditer(pattern, source):
        found[match.group(1).strip()] = unescape(match.group(2))
    return found


def collect_english():
    found = {}
    for name in os.listdir(LOC):
        if not name.endswith("TextTable.cs"):
            continue
        found.update(scan(os.path.join(LOC, name), r'table\.Add(?:Shared)?\(\s*([\w.()\d, ]+?),\s*"((?:[^"\\]|\\.)*)"'))
    return found


def collect(language_file):
    path = os.path.join(LOC, "Translations", language_file)
    return scan(path, r'AddTranslation\(Id,\s*([\w.()\d, ]+?),\s*"((?:[^"\\]|\\.)*)"')


def pick(raw, code):
    names = {}
    missing = []
    for key, constant in WANTED.items():
        value = raw.get(constant)
        if value is None or value == "":
            missing.append(key)
        else:
            names[key] = value

    for key, (constant, argument) in FORMATTED.items():
        template = raw.get(constant)

        if template is None or template == "":
            missing.append(key)

            continue

        names[key] = template.replace("{0}", argument)

    if missing:
        print("  {0}: {1} name(s) fall back to English -> {2}".format(code, len(missing), ", ".join(missing)))
    return names


def main():
    english = collect_english()
    result = {"en": pick(english, "en")}
    for code, table in sorted(TABLES.items()):
        result[code] = pick(collect(table), code)
    for code, source in FALLBACK.items():
        result[code] = dict(result[source])
        print("  {0}: mirrors {1} (no table of its own, by design)".format(code, source))

    for code, names in result.items():
        for key in list(WANTED) + list(FORMATTED):
            names.setdefault(key, result["en"].get(key, key))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "names.py")
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("# Generated by extract_names.py - do not edit by hand.\n")
        handle.write("# Source: Clicker-Ore-Game/Assets/_Game/Scripts/Systems/LocalizationSystem\n\n")
        handle.write("NAMES = ")
        handle.write(json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True))
        handle.write("\n")
    print("wrote {0} ({1} languages x {2} names)".format(out, len(result), len(WANTED) + len(FORMATTED)))


if __name__ == "__main__":
    main()
