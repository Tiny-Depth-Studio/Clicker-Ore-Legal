LANG = {
    "code": "en",
    "name": "English",
    "html_lang": "en",
    "locale": {"group": ",", "decimal": "."},
    "title": "Clicker Ore Game - Player Guide",
    "description": "How the mine works: currencies, pickaxes, pets, skills, prestige, bosses and the store, explained without the maths.",
    "brand": "Clicker Ore Game",
    "brand_sub": "Player Guide",
    "eyebrow": "Player Guide - {date}",
    "headline": "Everything In The Mine,<br>In Plain Words",
    "subtitle": "What each system does, when it opens up, and where your next hour is best spent. No formulas - just the decisions that matter.",
    "footer": "Numbers here follow the game's current balance and can change with updates. Store prices are set on Steam and shown in your own currency, so they are not listed here.",
    "labels": {
        "contents": "Contents",
        "per_second": "/s",
        "second_short": "s",
        "meter_short": "m",
        "language": "Language",
        "skill": "Skill",
        "unlock_floor": "Floor",
        "level_first": "Level 1 (duration / cooldown)",
        "level_last": "Level 7 (duration / cooldown)",
        "effect": "Effect",
        "boss": "Boss",
        "health": "Health",
        "time_limit": "Time",
        "reward": "Reward",
        "parameter": "Parameter",
        "per_level": "Per level",
        "effect_dps": "Auto damage per second",
        "effect_click": "Click damage",
        "effect_gold": "Gold income",
        "effect_crit_chance": "Critical chance",
        "effect_crit_multiplier": "Critical multiplier",
        "effect_heat": "Heat resistance",
        "effect_click_from_dps": "Share of DPS added to clicks",
        "depth": "Depth",
        "ore_types": "Ore types",
        "around_floor": "Around floor",
        "item": "Item",
        "cost": "Cost",
    },
    "currencies": {
        "gold": ["Earned by <b>breaking ore</b>.", "Spent on pickaxe and armour upgrades - your main workhorse."],
        "diamond": ["Comes from <b>real-money purchases only</b>.", "Spent on pets and the permanent Infinity items."],
        "essence": ["From <b>prestige</b> and boss wins.", "Spent on the {prestige_parameter_count} permanent prestige parameters."],
        "taskium": ["<b>+{taskium_per_click}</b> for every successful click.", "Spent on accepting and rerolling tasks."],
        "dungeon_key": ["One free key a day, plus store packs.", "Spent to enter a boss fight - {boss_key_cost} per attempt."],
        "skill_stone": ["From store packages and the trade panel.", "Spent on levelling the {skill_count} active skills."],
        "ore_stone": ["<b>{ore_stone_min}-{ore_stone_max}</b> from every ore you break, plus achievements.", "Traded for Essence or Skill Stone at the trade panel."],
    },
    "sections": [
        {
            "id": "start",
            "title": "Where To Start",
            "dek": "Three stages, following the order the game opens things up in.",
            "blocks": [
                ("stages", [
                    ["Early - floor 1 to {prestige_first_floor}", [
                        "Upgrade your pickaxe constantly; buy the next one as soon as it unlocks.",
                        "{skill_ore_breaker} arrives at floor {skill_line_floor}, {skill_anger_click} at floor 70.",
                        "Buy {pet_1} as soon as you can spare the diamonds.",
                    ]],
                    ["Middle - floor {prestige_first_floor} to {boss_floor}", [
                        "Prestige for the first time at floor {prestige_first_floor}.",
                        "Spread Essence across the {prestige_parameter_count} parameters instead of maxing one.",
                        "Tasks open at floor {task_panel_floor}, the skill tree and trade panel at floor {skill_tree_floor}.",
                    ]],
                    ["Late - floor {boss_floor} and beyond", [
                        "Fight bosses whenever you hold a key; they are your Essence engine.",
                        "Buy the Infinity items - they are permanent and never reset.",
                        "Keep armour levelled so heat never eats your damage.",
                    ]],
                ]),
                ("note", ["Good to know", "Numbers get long fast, so the game switches to short forms and then to scientific notation like <strong>1.23e45</strong>. Nothing is capped - that is only a change of notation."]),
            ],
        },
        {
            "id": "currencies",
            "title": "The {currency_count} Currencies",
            "dek": "Each one feeds a different system. Spending the right currency in the wrong place is the most common early mistake.",
            "blocks": [
                ("currencies", None),
                ("note", ["Diamonds", "Bosses, achievements and tasks never pay diamonds. Diamonds and dungeon keys are held on the server, so buying a pet needs you to be online."]),
            ],
        },
        {
            "id": "damage",
            "title": "Click Damage And Auto Damage",
            "dek": "Two separate damage sources, fed by different things.",
            "blocks": [
                ("p", "<strong>Click damage</strong> is what a tap does. It grows with your first pickaxe's level and skills, the {skill_anger_click} skill, your title, and the {prestige_click} prestige parameter. A slice of your auto damage is also folded into every click once {prestige_click_from_dps} is levelled."),
                ("p", "<strong>Auto damage</strong> (per second) comes from the second pickaxe onward, the {skill_rampage} skill, the {prestige_dps} parameter, and your pets."),
                ("note", ["Pets are the exception", "Pet damage is added <strong>after</strong> every multiplier, not scaled by them. Pet levels alone will not carry you late game - the pickaxe and skill multipliers still have to grow."]),
            ],
        },
        {
            "id": "critical",
            "title": "Critical Hits",
            "dek": "Every click can land as a critical and hit harder.",
            "blocks": [
                ("p", "You start with a <strong>{crit_chance_percent}%</strong> chance and a <strong>x{crit_multiplier}</strong> multiplier. Four things raise those: the {skill_critical_strike} skill, pickaxe skills, the {prestige_crit_chance} and {prestige_crit_multiplier} prestige parameters, and titles."),
            ],
        },
        {
            "id": "pickaxes",
            "title": "Pickaxes",
            "dek": "{pickaxe_count} pickaxes, unlocked in order. They are the backbone of your damage.",
            "blocks": [
                ("ul", [
                    "The first pickaxe costs <strong>{pickaxe_first_cost} gold</strong>; each following one costs about <strong>{pickaxe_cost_growth} times</strong> more than the last.",
                    "A pickaxe unlocks by itself once you have earned enough gold this run - so upgrading is what opens the next one.",
                    "Every level costs about <strong>{pickaxe_upgrade_growth_percent}%</strong> more than the previous one.",
                    "Only the <strong>first</strong> pickaxe feeds click damage. All the others feed auto damage per second.",
                    "Each pickaxe has {pickaxe_skill_count} skills, unlocking at levels {pickaxe_skill_levels}. Some help that pickaxe, some help all of them - the global ones are worth more.",
                ]),
                ("note", ["The big jump", "Every <strong>{pickaxe_bonus_interval} levels</strong> a pickaxe multiplies its own output by <strong>x{pickaxe_bonus_multiplier}</strong>. Pushing one pickaxe to the next hundred is usually the largest single power gain available to you."]),
            ],
        },
        {
            "id": "suits",
            "title": "Armour",
            "dek": "{suit_count} suits, all owned from the start. They exist to keep the heat off you.",
            "blocks": [
                ("ul", [
                    "You never buy armour - you only level it. Each level adds about <strong>{suit_heat_per_level_percent}%</strong> heat resistance, starting from {suit_base_heat_resistance}.",
                    "Every {suit_bonus_interval} levels the suit's resistance is multiplied by <strong>x{suit_bonus_multiplier}</strong>.",
                    "Each suit also has {suit_skill_count} skills that unlock as it levels.",
                    "The armour panel opens at floor <strong>{suit_panel_floor}</strong>, together with the heat gauge.",
                ]),
            ],
        },
        {
            "id": "temperature",
            "title": "Heat",
            "dek": "The deeper you go the hotter it gets, and heat quietly cuts your damage.",
            "blocks": [
                ("ul", [
                    "Floor temperature climbs steadily - roughly <strong>{temperature_growth}x per floor</strong>, so it doubles every couple of dozen floors.",
                    "While your resistance is at least <strong>{temperature_safe_ratio}x</strong> the floor temperature, the gauge stays clear and nothing is lost.",
                    "Once resistance drops below the temperature, damage starts bleeding away; at <strong>{temperature_worst_ratio}x</strong> you keep only a twentieth of it - a <strong>{temperature_worst_damage_percent}%</strong> loss.",
                    "The armour panel has an auto-buy switch for resistance; leave it on if you push depth often.",
                ]),
                ("warn", ["If progress stalls", "A sudden wall where ore takes forever is almost always heat, not damage. Check the gauge before you spend anything else."]),
            ],
        },
        {
            "id": "pets",
            "title": "Pets",
            "dek": "{pet_count} pets, bought with diamonds and then levelled with gold.",
            "blocks": [
                ("ul", [
                    "Prices run from <strong>{pet_cost_first}</strong> to <strong>{pet_cost_last}</strong> diamonds ({pet_cost_list}).",
                    "Each level adds about <strong>{pet_dps_percent_per_level}%</strong> of your pickaxe click damage as auto damage, multiplied by the pet's order - so {pet_5} gives five times what {pet_1} gives at the same level.",
                    "Levels get about <strong>{pet_upgrade_growth_percent}%</strong> more expensive each time, and every {pet_bonus_interval} levels the pet multiplies its own output by <strong>x{pet_bonus_multiplier}</strong>.",
                    "Each pet has {pet_skill_count} skills; some help only that pet, some help all of them.",
                    "The pet panel opens at floor <strong>{pet_panel_floor}</strong>, or as soon as you own a pet.",
                ]),
                ("warn", ["Prestige and pets", "Prestige puts every pet back to <strong>level 1</strong> and clears their skills. Ownership is permanent though - you never rebuy a pet."]),
            ],
        },
        {
            "id": "floors",
            "title": "Floors, Ore And Depth",
            "dek": "Floors decide how tough ore is and how much gold it pays. Depth decides what the ore looks like.",
            "blocks": [
                ("ul", [
                    "Every floor has a little more health and a little more gold than the one before, and the curve steepens as you go.",
                    "Every <strong>{duration_floor_interval}th floor</strong> is a timed floor: a <strong>{duration_floor_seconds} second</strong> clock starts, health is up about {duration_floor_health_percent}% and gold about {duration_floor_gold_percent}%.",
                    "Difficulty also runs in cycles of about {difficulty_cycle_floors} floors - the first floors of a cycle pay best relative to their health.",
                    "Every ore drops <strong>{ore_stone_min}-{ore_stone_max}</strong> Ore Stone on top of its gold.",
                ]),
                ("warn", ["Timed floors bite", "If the clock runs out you are pushed back <strong>one floor</strong>. Skip the timed floor rather than fail it if your damage is short."]),
                ("p", "You can drop back to any floor you have already reached this run and farm there. Picking a floor by hand turns auto-advance off; turn it back on when you want to climb again."),
                ("p", "There are <strong>{ore_type_count}</strong> ore types in total, and depth decides which ones appear. Ore type only changes the look and its dust - health and gold come from the floor."),
                ("table", "depth"),
            ],
        },
        {
            "id": "skills",
            "title": "Active Skills",
            "dek": "{skill_count} skills, each a timed boost followed by a cooldown.",
            "blocks": [
                ("p", "A skill is <strong>free</strong> when its floor arrives - you start using it at level 1. Levelling it up to level {skill_levels} costs <strong>{skill_total_cost} Skill Stone</strong> in total, or <strong>{skill_all_total_cost}</strong> for all {skill_count}. Higher levels mean longer duration and shorter cooldown."),
                ("table", "skills"),
                ("p", "The first skill line opens at floor {skill_line_floor}; the skill tree panel where you spend Skill Stone opens at floor <strong>{skill_tree_floor}</strong>. You do not need the panel to use a skill."),
                ("note", ["The combo", "Fire {skill_overcharge} first, then the skill you actually want boosted - for example {skill_golden_frenzy}. {skill_time_reversal} then cuts the cooldown of whatever you used last, so you get it back sooner."]),
            ],
        },
        {
            "id": "titles",
            "title": "Titles",
            "dek": "{title_count} titles that pick themselves up as you climb.",
            "blocks": [
                ("ul", [
                    "Titles run from floor {title_first_floor} to floor <strong>{title_last_floor}</strong> and are chosen automatically from the highest floor you reached this run.",
                    "Each title adds about <strong>+{title_effect_step}</strong> to the bonuses it carries.",
                    "The bonuses arrive in stages - click damage from the first title, then auto damage, heat resistance, gold, critical multiplier, critical chance and the DPS-to-click share (titles {title_effect_unlocks}).",
                ]),
            ],
        },
        {
            "id": "tasks",
            "title": "Tasks And {currency_taskium}",
            "dek": "A side track that turns your clicking into a second income.",
            "blocks": [
                ("ul", [
                    "Every successful click gives <strong>+{taskium_per_click} {currency_taskium}</strong>.",
                    "Accepting a task costs <strong>{task_accept_cost}</strong>, rerolling one costs <strong>{task_refresh_cost}</strong>.",
                    "The task panel opens at floor {task_panel_floor}; the {task_slot_count} slots open across floors {task_slot_floors}.",
                    "There are {task_type_count} task types in {task_rarity_count} rarities. Each task lasts {task_duration_minutes} minutes, and unaccepted ones are replaced every hour.",
                    "The reward scales with rarity - between <strong>{task_reward_range}</strong> times the current floor's ore gold. The rarest ones also pay Essence.",
                ]),
            ],
        },
        {
            "id": "trade",
            "title": "Trade Panel",
            "dek": "Opens at floor {trade_floor}. The only place Ore Stone is worth anything.",
            "blocks": [
                ("ul", [
                    "1 Skill Stone becomes <strong>{trade_skill_stone_to_ore_stone} Ore Stone</strong> - up to {trade_skill_stone_max} per trade.",
                    "<strong>{trade_ore_stone_to_essence} Ore Stone</strong> becomes 1 Essence.",
                    "<strong>{trade_ore_stone_to_skill_stone} Ore Stone</strong> becomes 1 Skill Stone.",
                ]),
                ("p", "That last one matters: it is how a long farming session turns into skill levels without a boss fight."),
            ],
        },
        {
            "id": "extras",
            "title": "Free Gold",
            "dek": "Three sources that ask for nothing but showing up.",
            "blocks": [
                ("ul", [
                    "<strong>Gold balloon</strong> - from floor {balloon_floor}, one drifts in every {balloon_min_seconds}-{balloon_max_seconds} seconds. Clicking it pays <strong>x{balloon_multiplier}</strong> the ore gold of your best floor this run.",
                    "<strong>Offline earnings</strong> - counted after {offline_min_minutes} minutes away and capped at {offline_max_hours} hours. Premium doubles it.",
                    "<strong>Play time reward</strong> - every {playtime_reward_minutes} minutes of play pays about {playtime_reward_multiplier} times a minute's worth of gold at your best floor.",
                ]),
            ],
        },
        {
            "id": "prestige",
            "title": "Prestige",
            "dek": "Trade this run's progress for permanent power. Timed well, it is the fastest thing in the game.",
            "blocks": [
                ("p", "The prestige panel opens the first time you reach floor <strong>{prestige_first_floor}</strong>. After that each prestige asks for {prestige_floor_step} floors more - {prestige_second_floor}, then 400, and so on."),
                ("ul", [
                    "<strong>Reset:</strong> gold, {currency_taskium}, floor progress, pickaxe and armour upgrades, pet levels, all bought skills, and your boss level.",
                    "<strong>Kept:</strong> prestige level, Essence, the {prestige_parameter_count} parameter levels, pet ownership, Infinity items, achievements.",
                    "You do not restart at floor 1: your next run starts at <strong>{prestige_floor_step} x your prestige level</strong>, with a pile of starting gold worth about {prestige_gold_multiplier} ore.",
                    "Every skill cooldown is cleared, so you begin the run with all of them ready.",
                ]),
                ("p", "The Essence reward comes from two things only: the <strong>highest floor</strong> you reached ({prestige_essence_per_floor} each) and the <strong>ore you broke</strong> ({prestige_essence_per_ore} each)."),
                ("note", ["Break ore, do not sprint", "Because ore count is the bigger term, farming a comfortable floor for the last stretch beats racing upward to a floor you can barely damage."]),
                ("table", "prestige"),
                ("p", "The bonuses add up level by level rather than compounding, and Essence costs rise slowly - so spending Essence often beats hoarding it."),
            ],
        },
        {
            "id": "bosses",
            "title": "Bosses",
            "dek": "A timed damage race for Essence. Opens at floor {boss_floor}.",
            "blocks": [
                ("ul", [
                    "You pick a boss and spend <strong>{boss_key_cost} dungeon key</strong> to start. Nothing starts by itself.",
                    "Bosses unlock in order - beat one to see the next. Health goes up about a thousandfold each step while the clock gets shorter.",
                    "Rewards grow with your prestige level: about <strong>+{boss_prestige_bonus_percent}%</strong> per level.",
                    "Prestige sends your boss level back to the first one.",
                ]),
                ("table", "bosses"),
                ("warn", ["Losing costs you", "If the timer ends first you get <strong>nothing</strong> and the key is gone. After a failed attempt you can see how much health was left - use that to judge how much more damage you need."]),
            ],
        },
        {
            "id": "achievements",
            "title": "Achievements",
            "dek": "{achievement_count} achievements across {achievement_type_count} categories - clicks, ore, bosses, prestiges, depth and more.",
            "blocks": [
                ("p", "Every achievement pays <strong>Ore Stone</strong>, and both the target and the reward grow roughly tenfold per tier. Most categories have three tiers; the gold and damage ones go further."),
                ("note", ["Claim them", "Rewards are <strong>not automatic</strong>. If you have not opened the achievements tab in a while, there is a pile waiting there."]),
            ],
        },
        {
            "id": "daily",
            "title": "Daily Reward",
            "dek": "Small, simple, and no penalty for missing a day.",
            "blocks": [
                ("p", "Logging in once a day gives <strong>{daily_key_amount} dungeon key</strong>. It is the same every day - there is no calendar and no streak to protect. You need to be online to claim it."),
            ],
        },
        {
            "id": "store",
            "title": "Store",
            "dek": "Diamonds, keys, packages, premium time, and the permanent Infinity items.",
            "blocks": [
                ("ul", [
                    "<strong>Diamond packs:</strong> {diamond_pack_list} diamonds. The bigger the pack, the better the rate.",
                    "<strong>Key packs:</strong> {key_pack_list} dungeon keys.",
                    "<strong>{package_small}:</strong> {package_small_contents}.",
                    "<strong>{package_big}:</strong> {package_big_contents}.",
                    "<strong>{package_premium}:</strong> {premium_days} days of x{premium_click_multiplier} click damage, x{premium_dps_multiplier} auto damage, x{premium_gold_multiplier} gold, x{premium_heat_multiplier} heat resistance and x{premium_offline_multiplier} offline earnings.",
                ]),
                ("p", "The Infinity items are bought <strong>once with diamonds</strong> and never reset, not even on prestige. Late game they are usually the best diamond spend you have."),
                ("table", "infinity"),
                ("note", ["Prices", "Store prices come from Steam in your own currency, so they are not printed here. What a pack contains never changes; what it costs depends on your region."]),
            ],
        },
        {
            "id": "progress",
            "title": "Leaderboards And Statistics",
            "dek": "Two places to see how the run is going.",
            "blocks": [
                ("ul", [
                    "Steam leaderboards track clicks, click damage, prestige count, bosses killed and highest floor.",
                    "The statistics screen keeps a longer record - earnings, spending, clicks, time played and more.",
                ]),
            ],
        },
        {
            "id": "save",
            "title": "Saves",
            "dek": "Short answer: your progress is safe in several ways at once.",
            "blocks": [
                ("ul", [
                    "The game saves itself, encrypted, every <strong>{save_seconds} seconds</strong>.",
                    "It backs up to Steam Cloud about every <strong>{cloud_save_seconds} seconds</strong>, and always when you close or pause - so another computer picks up where you left off.",
                    "If a save file is damaged the game falls back to its backup by itself.",
                    "You can also copy your save to the clipboard and paste it back in on another device.",
                ]),
            ],
        },
        {
            "id": "languages",
            "title": "Languages",
            "dek": "The game ships in {language_count} languages.",
            "blocks": [
                ("p", "English, Turkish, German, French, Spanish, Latin American Spanish, Italian, Polish, Brazilian Portuguese, Russian, Ukrainian, Japanese, Korean, Simplified Chinese, Traditional Chinese, Thai, Indonesian and Vietnamese. The game picks yours on first launch and you can change it any time in settings - this guide is available in all of them, linked at the top of the page."),
            ],
        },
    ],
}

