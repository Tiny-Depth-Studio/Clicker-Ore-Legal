"""Balance numbers for the player guide, read out of the game once and kept here.

Every value below was verified against Clicker-Ore-Game on 2026-09-14 (asset or
script path given per block) and describes the 1.7.16 release. Language files
never hard-code a number: they use {token} placeholders that build.py fills from
this file, so a balance change is a one-line edit here instead of an 18-file sweep.

Values are stored as real numbers, never as pre-formatted strings, because the
thousands separator and the decimal mark differ per language (1.000 / 0,5 in
Turkish, 1,000 / 0.5 in English). build.py formats them with the locale each
language file declares.
"""

DATE = "2026-09-21"

# CurrencySystem/Data/Enums/CurrencyType.cs (released currencies)
CURRENCY_COUNT = 7

# PickaxeSystem/Data/ScriptableObjects/PickaxeGeneralDataSo.asset
# Unlock floor = floor(15 * (order - 1) ^ 1.8), buy cost = 50 * 8 ^ (order - 2).
PICKAXE_COUNT = 45
PICKAXE_FIRST_COST = 5
PICKAXE_SECOND_COST = 50
PICKAXE_COST_GROWTH = 8
PICKAXE_UPGRADE_GROWTH_PERCENT = 6
PICKAXE_SECOND_FLOOR = 15
PICKAXE_TENTH_FLOOR = 782
PICKAXE_LAST_FLOOR = 13624
PICKAXE_SKILL_COUNT = 6

# Pickaxe, suit and pet skill assets: previewLevel / requiredLevel (330 assets)
ITEM_SKILL_LEVELS = [5, 25, 125, 625, 3125, 15625]

# exponentBonusStartLevel / exponentBonusLevelStepPerThreshold / exponentBonusPerThreshold,
# identical in the pickaxe, suit and pet general assets.
BONUS_START_LEVEL = 100
BONUS_LEVEL_STEP = 150
BONUS_POWER_STEP = 0.05

# SuitSystem/Data/ScriptableObjects/SuitGeneralDataSo.asset
SUIT_COUNT = 5
SUIT_BASE_HEAT_RESISTANCE = 50
SUIT_HEAT_PER_LEVEL_PERCENT = 5
SUIT_UPGRADE_GROWTH_PERCENT = 8.4
SUIT_PANEL_FLOOR = 130
SUIT_SKILL_COUNT = 6

# TemperatureSystem: TemperatureGeneralDataSo.asset + TemperatureController.cs
TEMPERATURE_GROWTH = 1.04
TEMPERATURE_SAFE_RATIO = 1.5
TEMPERATURE_WORST_RATIO = 0.5
TEMPERATURE_WORST_DAMAGE_PERCENT = 95

# PetSystem/Data/ScriptableObjects/PetGeneralDataSo.asset + supabase/v3/schema/05_seed_shop.sql
PET_COUNT = 5
PET_COSTS = [150, 175, 200, 225, 250]
PET_DPS_PERCENT_PER_LEVEL = 1
PET_UPGRADE_GROWTH_PERCENT = 20
PET_PANEL_FLOOR = 30
PET_SKILL_COUNT = 6

# WorkerSystem/Data/ScriptableObjects/WorkerGeneralDataSo.asset + Worker/*.asset
WORKER_COUNT = 5
WORKER_SLOT_FLOORS = [600, 800, 1000, 1200, 1400]
WORKER_TICK_SECONDS = 1
WORKER_INCOME_GROWTH_PERCENT = 1
WORKER_UPGRADE_COST = 100
WORKER_UPGRADE_GROWTH_PERCENT = 2

# CriticalSystem/Data/ScriptableObjects/CriticalGeneralDataSo.asset
CRIT_CHANCE_PERCENT = 5
CRIT_MULTIPLIER = 1.5
CRIT_CHANCE_CAP = 100

# SkillSystem/Data/ScriptableObjects/SkillData/*.asset + SkillGeneralDataSo.asset
SKILL_COUNT = 8
SKILL_LEVELS = 7
SKILL_TOTAL_COST = 63
SKILL_ALL_TOTAL_COST = 504
SKILL_LINE_FLOOR = 50
SKILL_TREE_FLOOR = 180
SKILLS = [
    ("skill_ore_breaker", 50, (30, 540), (90, 180), ("hits", 7, 13)),
    ("skill_anger_click", 100, (40, 660), (210, 300), ("multiplier", 2, 5)),
    ("skill_critical_strike", 150, (30, 600), (150, 240), ("multiplier", 1.3, 1.9)),
    ("skill_rampage", 200, (40, 840), (160, 480), ("multiplier", 2, 3.5)),
    ("skill_golden_frenzy", 250, (50, 1020), (290, 660), ("multiplier", 2, 5)),
    ("skill_heat_resistance", 300, (30, 660), (140, 300), ("multiplier", 2, 5)),
    ("skill_overcharge", 350, (20, 1200), (20, 840), ("multiplier", 1.5, 3)),
    ("skill_time_reversal", 400, (0, 1200), (0, 840), ("cut", 300, 1020)),
]

# OreSystem/Data/ScriptableObjects/OreGeneralDataSo.asset + DepthGeneralDataSo.asset
ORE_TYPE_COUNT = 40
ORE_STONE_MIN = 1
ORE_STONE_MAX = 5
DURATION_FLOOR_INTERVAL = 10
DURATION_FLOOR_SECONDS = 20
DURATION_FLOOR_HEALTH_MULTIPLIER = 5
DURATION_FLOOR_GOLD_MULTIPLIER = 2
DIFFICULTY_CYCLE_FLOORS = 100
DEPTH_TIERS = [
    ((0, 100), 9, 54),
    ((100, 500), 20, 129),
    ((500, 1500), 30, 196),
    ((1500, None), 40, None),
]

# OreSystem/Data/ScriptableObjects/Rare/RareOreDataSo_*.asset
RARE_ORE_COUNT = 5
RARE_ORE_BEST_ODDS = 10000
RARE_ORE_WORST_ODDS = 1000000
RARE_ORE_NAME_KEYS = ["rare_ore_1", "rare_ore_2", "rare_ore_3", "rare_ore_4", "rare_ore_5"]

# PrestigeSystem/Data/ScriptableObjects/*.asset
# Essence = floor(100 * 20 ^ (0.004 * (highest floor - 100))).
PRESTIGE_FIRST_FLOOR = 100
PRESTIGE_PANEL_FLOOR = 70
PRESTIGE_ESSENCE_AT_200 = 331
PRESTIGE_ESSENCE_AT_300 = 1098
PRESTIGE_ESSENCE_AT_500 = 12068
PRESTIGE_ESSENCE_AT_1000 = 4827341
PRESTIGE_PARAMETER_COUNT = 7
PRESTIGE_PARAMETER_FIRST_COST = 2
PRESTIGE_PARAMETER_COST_GROWTH_PERCENT = 2.5
PRESTIGE_PARAMETERS = [
    ("prestige_dps", "effect_dps", 2.5),
    ("prestige_click", "effect_click", 2.5),
    ("prestige_gold", "effect_gold", 1),
    ("prestige_crit_chance", "effect_crit_chance", 0.1),
    ("prestige_crit_multiplier", "effect_crit_multiplier", 0.1),
    ("prestige_heat", "effect_heat", 1),
    ("prestige_click_from_dps", "effect_click_from_dps", 0.1),
]

# BossSystem/Data/ScriptableObjects/*.asset
# (boss, health exponent, seconds, essence, ore stone)
BOSS_COUNT = 10
BOSS_FLOOR = 350
BOSS_KEY_COST = 1
BOSSES = [
    ("boss_1", 15, 30, 1000, 50000),
    ("boss_2", 18, 25, 2000, 75000),
    ("boss_3", 22, 20, 3000, 100000),
    ("boss_4", 27, 20, 4000, 125000),
    ("boss_5", 33, 20, 5000, 150000),
    ("boss_6", 40, 20, 6000, 175000),
    ("boss_7", 48, 15, 7000, 200000),
    ("boss_8", 57, 15, 8000, 225000),
    ("boss_9", 67, 15, 9000, 250000),
    ("boss_10", 78, 10, 10000, 275000),
]

# TitleSystem/Data/ScriptableObjects/Title/*.asset
TITLE_COUNT = 100
TITLE_FIRST_FLOOR = 1
TITLE_LAST_FLOOR = 50000
TITLE_EFFECT_STEP = 0.1
TITLE_EFFECT_UNLOCKS = [2, 6, 11, 16, 21, 26, 31]

# TaskSystem/Data/ScriptableObjects/TaskGeneralDataSo.asset + TaskSlot/*.asset + Task/**/*.asset
TASK_PANEL_FLOOR = 125
TASK_SLOT_FLOORS = [125, 225, 325, 425, 525, 625]
TASK_SLOT_COUNT = 6
TASK_ACCEPT_COST = 200
TASK_REFRESH_COST = 25
TASK_DURATION_MINUTES = 60
TASK_TYPE_COUNT = 10
TASK_RARITY_COUNT = 6
TASK_REWARD_MIN = 50
TASK_REWARD_MAX = 500
TASKIUM_PER_CLICK = 1

# MissionSystem/Data/ScriptableObjects/*.asset
DAILY_MISSION_COUNT = 5
DAILY_MISSION_BOOST_MINUTES = 10
DAILY_MISSION_BOOST_MULTIPLIER = 2

# TradeSystem/Data/ScriptableObjects/TradeOfferDataSo_*.asset
TRADE_FLOOR = 200
TRADE_SKILL_STONE_TO_ORE_STONE = 5000
TRADE_ORE_STONE_TO_ESSENCE = 2000
TRADE_ORE_STONE_TO_SKILL_STONE = 5000
TRADE_GOLD_FEE = 100000
TRADE_TIER_RATIO = 10

# EnchantmentSystem/Data/ScriptableObjects/EnchantmentGeneralDataSo.asset + EnchantmentDataSo_*.asset
# (rarity, min affixes, max affixes, drop floor, dust %, piece %, craft dust, craft fee in ore stone,
#  dismantle dust refund, power multiplier)
ENCHANT_TIERS = [
    ("rarity_common", 1, 1, 500, 5, 0.5, 10, 40, 5, 1),
    ("rarity_rare", 1, 2, 1000, 2, 0.1, 20, 200, 10, 2),
    ("rarity_epic", 2, 3, 2000, 1, 0.03, 30, 1000, 15, 4),
    ("rarity_legendary", 3, 4, 4000, 0.5, 0.01, 50, 5000, 25, 6),
]
ENCHANT_TIER_COUNT = 4
ENCHANT_SLOT_COUNT = 8
ENCHANT_SLOT_FLOORS = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000]
ENCHANT_FALLOFF_FLOORS = 100
ENCHANT_FALLOFF_MIN_PERCENT = 10
INVENTORY_FLOOR = 500

# PickupSystem/Data/ScriptableObjects/*.asset + OreSystem/Data/ScriptableObjects/Bonus/BonusOreDataSo_GoldCrystal.asset
BALLOON_FLOOR = 50
BALLOON_MIN_SECONDS = 500
BALLOON_MAX_SECONDS = 700
BALLOON_MULTIPLIER = 6
CRYSTAL_FLOOR = 100
CRYSTAL_MIN_SECONDS = 800
CRYSTAL_MAX_SECONDS = 1300
CRYSTAL_BONUS_SECONDS = 10
CRYSTAL_BONUS_HEALTH_MULTIPLIER = 10
CRYSTAL_BONUS_GOLD_MULTIPLIER = 14

# OfflineEarnSystem + PlaytimeRewardSystem
OFFLINE_MIN_MINUTES = 60
OFFLINE_MAX_HOURS = 12
PLAYTIME_REWARD_MINUTES = 60
PLAYTIME_REWARD_MULTIPLIER = 100

# LuckyWheelSystem/Data/ScriptableObjects/LuckyWheelGeneralDataSo.asset + supabase/v3/schema/16_events.sql
LUCKY_FLOOR = 100
LUCKY_SLOT_COUNT = 8
LUCKY_CYCLE_HOURS = 3
LUCKY_FREE_SPINS = 1
LUCKY_FIRST_PAID_SPIN = 10
LUCKY_DIAMOND_REWARD = 50

# AchievementSystem/Data/ScriptableObjects
ACHIEVEMENT_TYPE_COUNT = 31
ACHIEVEMENT_COUNT = 100

# DailyRewardSystem + supabase/v3/schema/06_seed_daily_rewards.sql
DAILY_KEY_AMOUNT = 1

# StoreSystem/Data/ScriptableObjects/Products + supabase/v3/schema/05_seed_shop.sql
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
TIME_SKIP_HOURS = [8, 16, 24]
TIME_SKIP_PRICES = [100, 190, 370]
CHEST_PRICE = 100
# (rarity, "dust" or "piece", amount, weight out of 1000)
CHEST_REWARDS = [
    ("rarity_common", "dust", 250, 170),
    ("rarity_common", "piece", 26, 160),
    ("rarity_rare", "dust", 180, 150),
    ("rarity_rare", "piece", 9, 150),
    ("rarity_epic", "dust", 150, 100),
    ("rarity_epic", "piece", 5, 100),
    ("rarity_legendary", "dust", 130, 90),
    ("rarity_legendary", "piece", 3, 80),
]

# SaveSystem/Scripts/Core/SaveManager.cs (cloud every third local save)
SAVE_SECONDS = 15
CLOUD_SAVE_SECONDS = 45

# LanguageSystem/Data/ScriptableObjects
LANGUAGE_COUNT = 18

SCALARS = [key for key, value in list(globals().items()) if key.isupper() and isinstance(value, (int, float))]
