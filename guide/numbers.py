"""Balance numbers for the player guide, read out of the game once and kept here.

Every value below was verified against Clicker-Ore-Game on 2026-08-12 (asset or
script path given per block). Language files never hard-code a number: they use
{token} placeholders that build.py fills from this file, so a balance change is
a one-line edit here instead of an 18-file sweep.

Values are stored as real numbers, never as pre-formatted strings, because the
thousands separator and the decimal mark differ per language (1.000 / 0,5 in
Turkish, 1,000 / 0.5 in English). build.py formats them with the locale each
language file declares.
"""

DATE = "2026-08-23"

# CurrencySystem/Data/Enums/CurrencyType.cs
CURRENCY_COUNT = 7

# PickaxeSystem/Data/ScriptableObjects/PickaxeGeneralDataSo.asset + Pickaxe/*.asset
PICKAXE_COUNT = 45
PICKAXE_FIRST_COST = 5
PICKAXE_COST_GROWTH = 8
PICKAXE_UPGRADE_GROWTH_PERCENT = 7
PICKAXE_BONUS_INTERVAL = 100
PICKAXE_BONUS_MULTIPLIER = 10
PICKAXE_SKILL_COUNT = 6
PICKAXE_SKILL_LEVELS = [5, 10, 25, 50, 100, 200]

# SuitSystem/Data/ScriptableObjects/SuitGeneralDataSo.asset
SUIT_COUNT = 5
SUIT_BASE_HEAT_RESISTANCE = 50
SUIT_HEAT_PER_LEVEL_PERCENT = 5
SUIT_BONUS_INTERVAL = 100
SUIT_BONUS_MULTIPLIER = 2
SUIT_PANEL_FLOOR = 130
SUIT_SKILL_COUNT = 6

# TemperatureSystem/Scripts/Core/TemperatureController.cs
TEMPERATURE_GROWTH = 1.04
TEMPERATURE_SAFE_RATIO = 1.5
TEMPERATURE_WORST_RATIO = 0.5
TEMPERATURE_WORST_DAMAGE_PERCENT = 95

# PetSystem/Data/ScriptableObjects/PetGeneralDataSo.asset + StoreSystem Pet products
PET_COUNT = 5
PET_COSTS = [150, 175, 200, 225, 250]
PET_DPS_PERCENT_PER_LEVEL = 1
PET_UPGRADE_GROWTH_PERCENT = 20
PET_BONUS_INTERVAL = 100
PET_BONUS_MULTIPLIER = 5
PET_PANEL_FLOOR = 30
PET_SKILL_COUNT = 6

# CriticalSystem/Data/ScriptableObjects/CriticalGeneralDataSo.asset
CRIT_CHANCE_PERCENT = 5
CRIT_MULTIPLIER = 1.5

# SkillSystem/Data/ScriptableObjects/SkillData/*.asset + SkillGeneralDataSo.asset
SKILL_COUNT = 8
SKILL_LEVELS = 7
SKILL_TOTAL_COST = 63
SKILL_ALL_TOTAL_COST = 504
SKILL_LINE_FLOOR = 50
SKILL_TREE_FLOOR = 180
SKILLS = [
    ("skill_ore_breaker", 50, (30, 540), (90, 180), ("hits", 7, 13)),
    ("skill_anger_click", 70, (40, 660), (210, 300), ("multiplier", 2, 5)),
    ("skill_critical_strike", 100, (30, 600), (150, 240), ("multiplier", 1.3, 1.9)),
    ("skill_rampage", 170, (40, 840), (160, 480), ("multiplier", 2, 3.5)),
    ("skill_golden_frenzy", 240, (50, 1020), (290, 660), ("multiplier", 2, 5)),
    ("skill_heat_resistance", 280, (30, 660), (140, 300), ("multiplier", 2, 5)),
    ("skill_overcharge", 330, (20, 1200), (20, 840), ("multiplier", 1.5, 3)),
    ("skill_time_reversal", 400, (0, 1200), (0, 840), ("cut", 300, 1020)),
]

# OreSystem/Data/ScriptableObjects/OreGeneralDataSo.asset + DepthSystem
ORE_TYPE_COUNT = 40
ORE_STONE_MIN = 1
ORE_STONE_MAX = 5
DURATION_FLOOR_INTERVAL = 10
DURATION_FLOOR_SECONDS = 20
DURATION_FLOOR_HEALTH_PERCENT = 50
DURATION_FLOOR_GOLD_PERCENT = 51
DIFFICULTY_CYCLE_FLOORS = 100
DEPTH_TIERS = [
    ((0, 100), 9, 54),
    ((100, 500), 20, 129),
    ((500, 1500), 30, 196),
    ((1500, None), 40, None),
]

# PrestigeSystem/Data/ScriptableObjects/*.asset + PrestigeController.cs
PRESTIGE_FIRST_FLOOR = 200
PRESTIGE_FLOOR_STEP = 100
PRESTIGE_ESSENCE_PER_FLOOR = 0.5
PRESTIGE_ESSENCE_PER_ORE = 0.25
PRESTIGE_GOLD_MULTIPLIER = 500
PRESTIGE_PARAMETER_COUNT = 7
PRESTIGE_PARAMETERS = [
    ("prestige_dps", "effect_dps", 20),
    ("prestige_click", "effect_click", 25),
    ("prestige_gold", "effect_gold", 10),
    ("prestige_crit_chance", "effect_crit_chance", 5),
    ("prestige_crit_multiplier", "effect_crit_multiplier", 5),
    ("prestige_heat", "effect_heat", 10),
    ("prestige_click_from_dps", "effect_click_from_dps", 1),
]

# BossSystem/Data/ScriptableObjects/*.asset
BOSS_COUNT = 10
BOSS_FLOOR = 350
BOSS_KEY_COST = 1
BOSS_PRESTIGE_BONUS_PERCENT = 15
BOSSES = [
    ("boss_1", 13, 30, 50, 5000),
    ("boss_2", 16, 25, 75, 7500),
    ("boss_3", 19, 20, 100, 10000),
    ("boss_4", 22, 20, 125, 12500),
    ("boss_5", 25, 20, 150, 15000),
    ("boss_6", 28, 20, 175, 17500),
    ("boss_7", 31, 15, 200, 20000),
    ("boss_8", 34, 15, 225, 22500),
    ("boss_9", 37, 15, 250, 25000),
    ("boss_10", 40, 10, 275, 27500),
]

# TitleSystem/Data/ScriptableObjects/Title/*.asset
TITLE_COUNT = 100
TITLE_FIRST_FLOOR = 1
TITLE_LAST_FLOOR = 50000
TITLE_EFFECT_STEP = 0.1
TITLE_EFFECT_UNLOCKS = [1, 5, 10, 15, 20, 25, 30]

# TaskSystem/Data/ScriptableObjects/TaskGeneralDataSo.asset
TASK_PANEL_FLOOR = 160
TASK_SLOT_FLOORS = [160, 170, 180, 190, 200, 210]
TASK_SLOT_COUNT = 6
TASK_ACCEPT_COST = 200
TASK_REFRESH_COST = 25
TASK_DURATION_MINUTES = 60
TASK_TYPE_COUNT = 10
TASK_RARITY_COUNT = 6
TASK_REWARD_MIN = 50
TASK_REWARD_MAX = 500
TASKIUM_PER_CLICK = 1

# TradeSystem
TRADE_FLOOR = 180
TRADE_SKILL_STONE_TO_ORE_STONE = 5000
TRADE_SKILL_STONE_MAX = 100000
TRADE_ORE_STONE_TO_ESSENCE = 2000
TRADE_ORE_STONE_TO_SKILL_STONE = 5000
TRADE_ESSENCE_MAX = 1000

# GoldBalloonSystem/Prefabs/Core/GoldBalloon.prefab
BALLOON_FLOOR = 200
BALLOON_MIN_SECONDS = 900
BALLOON_MAX_SECONDS = 1300
BALLOON_VISIBLE_SECONDS = 20
BALLOON_MULTIPLIER = 6

# OfflineEarnSystem + PlaytimeRewardSystem
OFFLINE_MIN_MINUTES = 60
OFFLINE_MAX_HOURS = 12
PLAYTIME_REWARD_MINUTES = 60
PLAYTIME_REWARD_MULTIPLIER = 100

# AchievementSystem/Data/ScriptableObjects
ACHIEVEMENT_TYPE_COUNT = 24
ACHIEVEMENT_COUNT = 86

# DailyRewardSystem + supabase/v3/schema/06_seed_daily_rewards.sql
DAILY_KEY_AMOUNT = 1

# StoreSystem/Data/ScriptableObjects/Products
DIAMOND_PACKS = [200, 550, 1150, 2400, 6250, 14000]
KEY_PACKS = [3, 7, 15]
PACKAGE_SMALL_CONTENTS = [500, 100, 10, 3]
PACKAGE_BIG_CONTENTS = [1000, 200, 20, 5]
PREMIUM7_DAYS = 7
PREMIUM7_CLICK_MULTIPLIER = 5
PREMIUM7_DPS_MULTIPLIER = 5
PREMIUM7_GOLD_MULTIPLIER = 3
PREMIUM7_HEAT_MULTIPLIER = 3
PREMIUM7_OFFLINE_MULTIPLIER = 2

PREMIUM30_DAYS = 30
PREMIUM30_CLICK_MULTIPLIER = 7
PREMIUM30_DPS_MULTIPLIER = 7
PREMIUM30_GOLD_MULTIPLIER = 4.5
PREMIUM30_HEAT_MULTIPLIER = 3.5
PREMIUM30_OFFLINE_MULTIPLIER = 2.5
INFINITY_ITEMS = [
    ("infinity_power", 350, ("multiplier", 4)),
    ("infinity_income", 350, ("multiplier", 3)),
    ("infinity_armor", 350, ("multiplier", 2)),
    ("infinity_speed", 550, ("multiplier", 1.5)),
    ("infinity_clicker", 600, ("clicks", 7)),
]

# SaveSystem/Scripts/Core/SaveManager.cs
SAVE_SECONDS = 15
CLOUD_SAVE_SECONDS = 45

# LanguageSystem/Data/ScriptableObjects
LANGUAGE_COUNT = 18

# PickupSystem/Data/ScriptableObjects/GoldCrystalPickupDataSo.asset
# + OreSystem/Data/ScriptableObjects/Bonus/BonusOreDataSo_GoldCrystal.asset
CRYSTAL_FLOOR = 100
CRYSTAL_MIN_SECONDS = 900
CRYSTAL_MAX_SECONDS = 1300
CRYSTAL_VISIBLE_SECONDS = 20
CRYSTAL_BONUS_SECONDS = 10
CRYSTAL_BONUS_HEALTH_MULTIPLIER = 10
CRYSTAL_BONUS_GOLD_MULTIPLIER = 14

# OreSystem/Data/ScriptableObjects/Rare/RareOreDataSo_*.asset
RARE_ORE_COUNT = 5
RARE_ORE_BEST_ODDS = 10000
RARE_ORE_WORST_ODDS = 1000000
RARE_ORE_NAME_KEYS = ["rare_ore_1", "rare_ore_2", "rare_ore_3", "rare_ore_4", "rare_ore_5"]

# StoreSystem/Data/ScriptableObjects/Products/TimeSkip/*.asset
# Elmas fiyati sunucudan gelir (game.shop_items), bu yuzden burada yok.
TIME_SKIP_HOURS = [2, 4, 8]

SCALARS = [key for key, value in list(globals().items()) if key.isupper() and isinstance(value, (int, float))]
