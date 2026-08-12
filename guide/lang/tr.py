LANG = {
    "code": "tr",
    "name": "Türkçe",
    "html_lang": "tr",
    "locale": {"group": ".", "decimal": ","},
    "title": "Clicker Ore Game - Oyuncu Rehberi",
    "description": "Madende ne nasıl işliyor: para birimleri, kazmalar, petler, yetenekler, prestij, bosslar ve mağaza - formül olmadan.",
    "brand": "Clicker Ore Game",
    "brand_sub": "Oyuncu Rehberi",
    "eyebrow": "Oyuncu Rehberi - {date}",
    "headline": "Madenin Tamamı,<br>Sade Anlatımla",
    "subtitle": "Hangi sistem ne yapar, kaçıncı katta açılır ve bir sonraki saatini nereye harcamalısın. Formül yok - sadece işine yarayan kararlar.",
    "footer": "Buradaki sayılar oyunun güncel dengesine göredir ve güncellemelerle değişebilir. Mağaza fiyatları Steam tarafından belirlenip kendi para biriminde gösterildiği için burada yazılmıyor.",
    "labels": {
        "contents": "İçindekiler",
        "per_second": "/sn",
        "second_short": " sn",
        "meter_short": "m",
        "language": "Dil",
        "skill": "Yetenek",
        "unlock_floor": "Kat",
        "level_first": "1. kademe (süre / bekleme)",
        "level_last": "7. kademe (süre / bekleme)",
        "effect": "Etki",
        "boss": "Boss",
        "health": "Can",
        "time_limit": "Süre",
        "reward": "Ödül",
        "parameter": "Parametre",
        "per_level": "Seviye başına",
        "effect_dps": "Saniyede otomatik hasar",
        "effect_click": "Tıklama hasarı",
        "effect_gold": "Altın kazancı",
        "effect_crit_chance": "Kritik şansı",
        "effect_crit_multiplier": "Kritik çarpanı",
        "effect_heat": "Isı direnci",
        "effect_click_from_dps": "Tıklamaya eklenen SBH payı",
        "depth": "Derinlik",
        "ore_types": "Cevher türü",
        "around_floor": "Yaklaşık kat",
        "item": "Eşya",
        "cost": "Fiyat",
    },
    "currencies": {
        "gold": ["<b>Cevher kırarak</b> kazanılır.", "Kazma ve zırh yükseltmelerine gider - ana iş gücün."],
        "diamond": ["Yalnızca <b>gerçek para alışverişiyle</b> gelir.", "Petlere ve kalıcı Sonsuz eşyalara harcanır."],
        "essence": ["<b>Prestijden</b> ve boss zaferlerinden gelir.", "{prestige_parameter_count} kalıcı prestij parametresine harcanır."],
        "taskium": ["Her başarılı tıklamada <b>+{taskium_per_click}</b>.", "Görev kabul etmeye ve görev yenilemeye gider."],
        "dungeon_key": ["Günde bir bedava anahtar, ayrıca mağaza paketleri.", "Boss dövüşüne girmek için - deneme başına {boss_key_cost} anahtar."],
        "skill_stone": ["Mağaza paketlerinden ve takas panelinden gelir.", "{skill_count} aktif yeteneğin kademelerine harcanır."],
        "ore_stone": ["Kırdığın her cevherden <b>{ore_stone_min}-{ore_stone_max}</b> tane, ayrıca başarımlardan.", "Takas panelinde Öz'e ya da Yetenek Taşı'na çevrilir."],
    },
    "sections": [
        {
            "id": "start",
            "title": "Nereden Başlamalı",
            "dek": "Oyunun sistemleri açma sırasına göre üç aşama.",
            "blocks": [
                ("stages", [
                    ["Başlangıç - kat 1 ile {prestige_first_floor} arası", [
                        "Kazmanı durmadan yükselt; yenisi açıldığı anda al.",
                        "{skill_ore_breaker} {skill_line_floor}. katta, {skill_anger_click} 70. katta gelir.",
                        "Elmasın yeterse ilk pet olarak {pet_1} alınır.",
                    ]],
                    ["Orta - kat {prestige_first_floor} ile {boss_floor} arası", [
                        "İlk prestiji {prestige_first_floor}. katta yaparsın.",
                        "Öz'ü tek parametrede yığma, {prestige_parameter_count} parametreye dağıt.",
                        "Görevler {task_panel_floor}. katta, yetenek ağacı ve takas paneli {skill_tree_floor}. katta açılır.",
                    ]],
                    ["İleri - kat {boss_floor} ve sonrası", [
                        "Elinde anahtar oldukça boss dövüş; Öz'ün asıl kaynağı orası.",
                        "Sonsuz eşyaları al - kalıcıdır, prestijde bile sıfırlanmaz.",
                        "Zırhı yükseltmeyi bırakma; ısı hasarını sessizce yiyor.",
                    ]],
                ]),
                ("note", ["Bilmen iyi olur", "Sayılar hızla uzuyor, bu yüzden oyun önce kısaltmalara sonra <strong>1.23e45</strong> gibi bilimsel gösterime geçer. Bir üst sınır yok - bu yalnızca gösterim değişikliği."]),
            ],
        },
        {
            "id": "currencies",
            "title": "{currency_count} Para Birimi",
            "dek": "Her biri farklı bir sistemi besler. Yeni oyuncunun en sık hatası, doğru parayı yanlış yere harcamak.",
            "blocks": [
                ("currencies", None),
                ("note", ["Elmas", "Boss, başarım ve görevler elmas VERMEZ. Elmas ve zindan anahtarı sunucuda tutulur; bu yüzden pet almak için çevrimiçi olman gerekir."]),
            ],
        },
        {
            "id": "damage",
            "title": "Tıklama Hasarı ve Otomatik Hasar",
            "dek": "İki ayrı hasar kaynağı, ikisini besleyen şeyler farklı.",
            "blocks": [
                ("p", "<strong>Tıklama hasarı</strong> bir dokunuşun verdiği hasardır. İlk kazmanın seviyesi ve skill'leri, {skill_anger_click} yeteneği, unvanın ve {prestige_click} prestij parametresi bunu büyütür. {prestige_click_from_dps} yükseltildikçe otomatik hasarının bir payı da her tıklamaya eklenir."),
                ("p", "<strong>Otomatik hasar</strong> (saniyede) ikinci kazmadan itibaren tüm kazmalardan, {skill_rampage} yeteneğinden, {prestige_dps} parametresinden ve petlerinden gelir."),
                ("note", ["Petler istisna", "Pet hasarı tüm çarpanlar uygulandıktan <strong>sonra</strong> eklenir, onlarla büyümez. Yani ileri oyunda pet seviyesi tek başına yetmez; kazma ve skill çarpanları da büyümek zorunda."]),
            ],
        },
        {
            "id": "critical",
            "title": "Kritik Vuruşlar",
            "dek": "Her tıklama kritik gelip daha sert vurabilir.",
            "blocks": [
                ("p", "Başlangıç değerleri <strong>%{crit_chance_percent}</strong> şans ve <strong>x{crit_multiplier}</strong> çarpandır. Dört şey bunları büyütür: {skill_critical_strike} yeteneği, kazma skill'leri, {prestige_crit_chance} ile {prestige_crit_multiplier} prestij parametreleri ve unvanlar."),
            ],
        },
        {
            "id": "pickaxes",
            "title": "Kazmalar",
            "dek": "Sırayla açılan {pickaxe_count} kazma. Hasarının belkemiği.",
            "blocks": [
                ("ul", [
                    "İlk kazma <strong>{pickaxe_first_cost} altın</strong>; sonraki her kazma bir öncekinin yaklaşık <strong>{pickaxe_cost_growth} katı</strong> tutar.",
                    "Kazma kendiliğinden açılır: bu prestijte yeterince altın kazanmak yeter - yani yeni kazmayı açan şey mevcut kazmayı yükseltmek.",
                    "Her seviye bir öncekinden yaklaşık <strong>%{pickaxe_upgrade_growth_percent}</strong> pahalıdır.",
                    "Tıklama hasarını yalnızca <strong>ilk</strong> kazma besler. Geri kalan hepsi saniyedeki otomatik hasarı besler.",
                    "Her kazmanın {pickaxe_skill_count} skill'i var; {pickaxe_skill_levels} seviyelerinde açılır. Bazısı yalnız o kazmaya, bazısı tüm kazmalara etki eder - tümüne etki edenler daha değerlidir.",
                ]),
                ("note", ["Büyük sıçrama", "Bir kazma her <strong>{pickaxe_bonus_interval} seviyede</strong> kendi çıktısını <strong>x{pickaxe_bonus_multiplier}</strong> katına çıkarır. Tek bir kazmayı sonraki yüzlüğe taşımak, elindeki en büyük güç artışıdır."]),
            ],
        },
        {
            "id": "suits",
            "title": "Zırhlar",
            "dek": "Baştan sahip olduğun {suit_count} zırh. Görevleri ısıyı üstünden almak.",
            "blocks": [
                ("ul", [
                    "Zırh satın alınmaz, yalnızca yükseltilir. Her seviye ısı direncine yaklaşık <strong>%{suit_heat_per_level_percent}</strong> ekler; taban {suit_base_heat_resistance}.",
                    "Her {suit_bonus_interval} seviyede zırhın direnci <strong>x{suit_bonus_multiplier}</strong> katına çıkar.",
                    "Her zırhın ayrıca seviye ilerledikçe açılan {suit_skill_count} skill'i var.",
                    "Zırh paneli, ısı göstergesiyle birlikte <strong>{suit_panel_floor}.</strong> katta açılır.",
                ]),
            ],
        },
        {
            "id": "temperature",
            "title": "Isı",
            "dek": "Derine indikçe sıcaklık artar ve ısı hasarını sessizce kırpar.",
            "blocks": [
                ("ul", [
                    "Kat sıcaklığı istikrarlı biçimde tırmanır - kat başına yaklaşık <strong>{temperature_growth} kat</strong>, yani her yirmi katta bir ikiye katlanır.",
                    "Direncin kat sıcaklığının en az <strong>{temperature_safe_ratio} katı</strong> olduğu sürece gösterge temiz kalır, hiçbir şey kaybetmezsin.",
                    "Direnç sıcaklığın altına düştüğü an hasar sızmaya başlar; <strong>{temperature_worst_ratio} kat</strong> seviyesinde hasarın yalnızca yirmide biri kalır - yani <strong>%{temperature_worst_damage_percent}</strong> kayıp.",
                    "Zırh panelinde direnci otomatik satın alma anahtarı var; sık derine iniyorsan açık bırak.",
                ]),
                ("warn", ["İlerleme tıkandıysa", "Cevherin bir anda bitmez olması neredeyse her zaman hasar değil ısı sorunudur. Başka bir şeye para harcamadan önce göstergeye bak."]),
            ],
        },
        {
            "id": "pets",
            "title": "Petler",
            "dek": "Elmasla alınıp altınla yükseltilen {pet_count} pet.",
            "blocks": [
                ("ul", [
                    "Fiyatlar <strong>{pet_cost_first}</strong> elmastan <strong>{pet_cost_last}</strong> elmasa kadar ({pet_cost_list}).",
                    "Her seviye, kazma tıklama hasarının yaklaşık <strong>%{pet_dps_percent_per_level}</strong> kadarını otomatik hasar olarak ekler ve bu pet'in sırasıyla çarpılır - yani aynı seviyede {pet_5}, {pet_1} pet'inin beş katını verir.",
                    "Seviyeler her adımda yaklaşık <strong>%{pet_upgrade_growth_percent}</strong> pahalanır; her {pet_bonus_interval} seviyede pet kendi çıktısını <strong>x{pet_bonus_multiplier}</strong> katına çıkarır.",
                    "Her pet'in {pet_skill_count} skill'i var; bazısı yalnız o pet'e, bazısı hepsine etki eder.",
                    "Pet paneli <strong>{pet_panel_floor}.</strong> katta, ya da elinde bir pet olduğu anda açılır.",
                ]),
                ("warn", ["Prestij ve petler", "Prestij her pet'i <strong>1. seviyeye</strong> döndürür ve skill'lerini siler. Ama sahiplik kalıcıdır - pet'i bir daha satın almazsın."]),
            ],
        },
        {
            "id": "floors",
            "title": "Katlar, Cevher ve Derinlik",
            "dek": "Cevherin ne kadar sert olduğunu ve ne kadar altın verdiğini kat belirler; nasıl göründüğünü derinlik.",
            "blocks": [
                ("ul", [
                    "Her katın canı ve altını bir öncekinden biraz fazladır; eğri ilerledikçe dikleşir.",
                    "Her <strong>{duration_floor_interval}. kat</strong> süreli kattır: <strong>{duration_floor_seconds} saniyelik</strong> sayaç başlar, can yaklaşık %{duration_floor_health_percent}, altın yaklaşık %{duration_floor_gold_percent} artar.",
                    "Zorluk ayrıca yaklaşık {difficulty_cycle_floors} katlık döngülerle işler - bir döngünün ilk katları canına göre en iyi altını verir.",
                    "Her cevher altınının üstüne <strong>{ore_stone_min}-{ore_stone_max}</strong> Cevher Taşı düşürür.",
                ]),
                ("warn", ["Süreli kat ceza keser", "Sayaç dolarsa <strong>bir alt kata</strong> geri gönderilirsin. Hasarın yetmiyorsa süreli katta başarısız olmak yerine o katı atla."]),
                ("p", "Bu prestijte ulaştığın herhangi bir kata inip orada farm yapabilirsin. Kat elle seçmek otomatik ilerlemeyi kapatır; yeniden tırmanmak isteyince geri aç."),
                ("p", "Oyunda toplam <strong>{ore_type_count}</strong> cevher türü var ve hangisinin çıkacağını derinlik belirler. Cevher türü yalnızca görüntüyü ve tozunu değiştirir - can ve altın kattan gelir."),
                ("table", "depth"),
            ],
        },
        {
            "id": "skills",
            "title": "Aktif Yetenekler",
            "dek": "Her biri süreli bir güçlendirme, ardından bekleme süresi olan {skill_count} yetenek.",
            "blocks": [
                ("p", "Yetenek, katı geldiğinde <strong>bedava</strong> açılır ve 1. kademede kullanılmaya başlar. {skill_levels}. kademeye çıkarmak toplam <strong>{skill_total_cost} Yetenek Taşı</strong> tutar; {skill_count} yeteneğin hepsi için <strong>{skill_all_total_cost}</strong>. Kademe yükseldikçe süre uzar, bekleme kısalır."),
                ("table", "skills"),
                ("p", "İlk yetenek hattı {skill_line_floor}. katta açılır; Yetenek Taşı harcadığın yetenek ağacı paneli <strong>{skill_tree_floor}.</strong> katta açılır. Yeteneği kullanmak için panele gerek yok."),
                ("note", ["Kombo", "Önce {skill_overcharge} kullan, sonra asıl güçlendirmek istediğin yeteneği - örneğin {skill_golden_frenzy}. {skill_time_reversal} ise en son kullandığın yeteneğin beklemesini kısaltır, yani onu daha erken geri alırsın."]),
            ],
        },
        {
            "id": "titles",
            "title": "Unvanlar",
            "dek": "Tırmandıkça kendiliğinden gelen {title_count} unvan.",
            "blocks": [
                ("ul", [
                    "Unvanlar {title_first_floor}. kattan <strong>{title_last_floor}.</strong> kata kadar yayılır ve bu prestijteki en yüksek kata göre otomatik seçilir.",
                    "Her unvan taşıdığı bonuslara yaklaşık <strong>+{title_effect_step}</strong> ekler.",
                    "Bonuslar kademeli gelir: ilk unvandan tıklama hasarı, sonra otomatik hasar, ısı direnci, altın, kritik çarpanı, kritik şansı ve tıklamaya eklenen SBH payı ({title_effect_unlocks}. unvanlar).",
                ]),
            ],
        },
        {
            "id": "tasks",
            "title": "Görevler ve {currency_taskium}",
            "dek": "Tıklamanı ikinci bir gelire çeviren yan hat.",
            "blocks": [
                ("ul", [
                    "Her başarılı tıklama <strong>+{taskium_per_click} {currency_taskium}</strong> verir.",
                    "Görev kabul etmek <strong>{task_accept_cost}</strong>, görev yenilemek <strong>{task_refresh_cost}</strong> tutar.",
                    "Görev paneli {task_panel_floor}. katta açılır; {task_slot_count} yuva {task_slot_floors}. katlarda açılır.",
                    "{task_rarity_count} nadirlikte {task_type_count} görev türü var. Her görev {task_duration_minutes} dakika sürer, kabul edilmeyenler saat başı yenilenir.",
                    "Ödül nadirlikle büyür: o anki katın cevher altınının <strong>{task_reward_range}</strong> katı arası. En nadir görevler ayrıca Öz verir.",
                ]),
            ],
        },
        {
            "id": "trade",
            "title": "Takas Paneli",
            "dek": "{trade_floor}. katta açılır. Cevher Taşı'nın bir işe yaradığı tek yer.",
            "blocks": [
                ("ul", [
                    "1 Yetenek Taşı <strong>{trade_skill_stone_to_ore_stone} Cevher Taşı</strong> olur - işlem başına en fazla {trade_skill_stone_max}.",
                    "<strong>{trade_ore_stone_to_essence} Cevher Taşı</strong> 1 Öz olur.",
                    "<strong>{trade_ore_stone_to_skill_stone} Cevher Taşı</strong> 1 Yetenek Taşı olur.",
                ]),
                ("p", "Sonuncusu önemli: uzun bir farm seansını boss dövüşmeden yetenek kademesine çeviren yol budur."),
            ],
        },
        {
            "id": "extras",
            "title": "Bedava Altın",
            "dek": "Sadece oyunda olmanı isteyen üç kaynak.",
            "blocks": [
                ("ul", [
                    "<strong>Altın balonu</strong> - {balloon_floor}. kattan itibaren her {balloon_min_seconds}-{balloon_max_seconds} saniyede bir süzülüp gelir. Tıklayınca bu prestijteki en iyi katın cevher altınının <strong>x{balloon_multiplier}</strong> katını verir.",
                    "<strong>Çevrimdışı kazanç</strong> - {offline_min_minutes} dakikadan sonra saymaya başlar, {offline_max_hours} saatte kesilir. Premium bunu iki katına çıkarır.",
                    "<strong>Oyun süresi ödülü</strong> - her {playtime_reward_minutes} dakikalık oyun için en iyi katındaki bir dakikalık altının yaklaşık {playtime_reward_multiplier} katı.",
                ]),
            ],
        },
        {
            "id": "prestige",
            "title": "Prestij",
            "dek": "Bu turdaki ilerlemeyi kalıcı güce çevirmek. Zamanlaması doğruysa oyundaki en hızlı hamle.",
            "blocks": [
                ("p", "Prestij paneli, <strong>{prestige_first_floor}.</strong> kata ilk kez ulaştığında açılır. Sonrasında her prestij {prestige_floor_step} kat daha ister: {prestige_second_floor}, ardından {prestige_third_floor} ve böyle sürer."),
                ("ul", [
                    "<strong>Sıfırlanır:</strong> altın, {currency_taskium}, kat ilerlemesi, kazma ve zırh yükseltmeleri, pet seviyeleri, satın alınmış tüm skill'ler ve boss seviyesi.",
                    "<strong>Kalır:</strong> prestij seviyesi, Öz, {prestige_parameter_count} parametrenin seviyeleri, pet sahipliği, Sonsuz eşyalar, başarımlar.",
                    "Kat 1'den başlamazsın: yeni tur <strong>{prestige_floor_step} x prestij seviyesi</strong> katından açılır ve yanına yaklaşık {prestige_gold_multiplier} cevher değerinde başlangıç altını gelir.",
                    "Tüm yetenek beklemeleri temizlenir, yani tura hepsi hazırken başlarsın.",
                ]),
                ("p", "Öz ödülü yalnızca iki şeyden gelir: ulaştığın <strong>en yüksek kat</strong> (her biri {prestige_essence_per_floor}) ve <strong>kırdığın cevher</strong> (her biri {prestige_essence_per_ore})."),
                ("note", ["Koşma, cevher kır", "Cevher sayısı daha büyük terim olduğu için, son dakikaları zar zor hasar verdiğin bir kata tırmanmakla geçirmek yerine rahat bir katta farm yapmak daha çok Öz getirir."]),
                ("table", "prestige"),
                ("p", "Bonuslar bileşik değil, seviye seviye toplanır; Öz maliyeti de yavaş yükselir. Yani Öz'ü biriktirmek yerine düzenli harcamak kazandırır."),
            ],
        },
        {
            "id": "bosses",
            "title": "Bosslar",
            "dek": "Öz için süreli hasar yarışı. {boss_floor}. katta açılır.",
            "blocks": [
                ("ul", [
                    "Bir boss seçip <strong>{boss_key_cost} zindan anahtarı</strong> harcayarak başlatırsın. Kendiliğinden başlayan bir şey yok.",
                    "Bosslar sırayla açılır - birini geçmeden sonrakini görmezsin. Her adımda can bini aşkın katına çıkar, süre kısalır.",
                    "Ödüller prestij seviyenle büyür: seviye başına yaklaşık <strong>%{boss_prestige_bonus_percent}</strong>.",
                    "Prestij boss seviyeni ilk bossa döndürür.",
                ]),
                ("table", "bosses"),
                ("warn", ["Kaybetmek pahalı", "Süre dolduğunda boss ayaktaysa <strong>hiçbir ödül almazsın</strong> ve anahtar geri gelmez. Başarısız denemeden sonra ne kadar can kaldığını görebilirsin - bir dahaki sefere ne kadar hasar gerektiğini oradan kestir."]),
            ],
        },
        {
            "id": "achievements",
            "title": "Başarımlar",
            "dek": "{achievement_type_count} kategoride {achievement_count} başarım - tıklama, cevher, boss, prestij, derinlik ve dahası.",
            "blocks": [
                ("p", "Her başarım <strong>Cevher Taşı</strong> öder; hem hedef hem ödül kademe başına kabaca on katına çıkar. Kategorilerin çoğu üç kademelidir, altın ve hasar kategorileri daha uzun gider."),
                ("note", ["Toplamayı unutma", "Ödüller <strong>otomatik yatmaz</strong>. Bir süredir başarım sekmesini açmadıysan orada birikmiş bir yığın var."]),
            ],
        },
        {
            "id": "daily",
            "title": "Günlük Ödül",
            "dek": "Küçük, basit ve bir günü kaçırmanın cezası yok.",
            "blocks": [
                ("p", "Günde bir kez giriş yapmak <strong>{daily_key_amount} zindan anahtarı</strong> verir. Her gün aynıdır - takvim yok, korunacak bir seri yok. Almak için çevrimiçi olman gerekir."),
            ],
        },
        {
            "id": "store",
            "title": "Mağaza",
            "dek": "Elmas, anahtar, paketler, premium süresi ve kalıcı Sonsuz eşyalar.",
            "blocks": [
                ("ul", [
                    "<strong>Elmas paketleri:</strong> {diamond_pack_list} elmas. Paket büyüdükçe birim fiyat düşer.",
                    "<strong>Anahtar paketleri:</strong> {key_pack_list} zindan anahtarı.",
                    "<strong>{package_small}:</strong> {package_small_contents}.",
                    "<strong>{package_big}:</strong> {package_big_contents}.",
                    "<strong>{package_premium}:</strong> {premium_days} gün boyunca x{premium_click_multiplier} tıklama hasarı, x{premium_dps_multiplier} otomatik hasar, x{premium_gold_multiplier} altın, x{premium_heat_multiplier} ısı direnci ve x{premium_offline_multiplier} çevrimdışı kazanç.",
                ]),
                ("p", "Sonsuz eşyalar <strong>elmasla bir kez</strong> alınır ve hiç sıfırlanmaz, prestijte bile. İleri oyunda genelde elmasın en verimli harcandığı yer burasıdır."),
                ("table", "infinity"),
                ("note", ["Fiyatlar", "Mağaza fiyatları Steam'den kendi para biriminde gelir, bu yüzden burada yazılmıyor. Bir paketin içeriği hiç değişmez; fiyatı bölgene göre değişir."]),
            ],
        },
        {
            "id": "progress",
            "title": "Liderlik Tabloları ve İstatistikler",
            "dek": "Turun nasıl gittiğini görebileceğin iki yer.",
            "blocks": [
                ("ul", [
                    "Steam liderlik tabloları tıklama sayısını, tıklama hasarını, prestij sayısını, öldürülen bossları ve en yüksek katı tutar.",
                    "İstatistik ekranı daha uzun bir kayıt tutar - kazanç, harcama, tıklama, oynanan süre ve dahası.",
                ]),
            ],
        },
        {
            "id": "save",
            "title": "Kayıtlar",
            "dek": "Kısa cevap: ilerlemen aynı anda birkaç katmanla korunuyor.",
            "blocks": [
                ("ul", [
                    "Oyun kendini her <strong>{save_seconds} saniyede</strong> şifreli olarak kaydeder.",
                    "Yaklaşık her <strong>{cloud_save_seconds} saniyede</strong> bir Steam Cloud'a yedekler; oyunu kapattığında ve duraklattığında da her zaman - yani başka bir bilgisayarda kaldığın yerden devam edersin.",
                    "Kayıt dosyası bozulursa oyun kendiliğinden yedeğine düşer.",
                    "Kaydını panoya kopyalayıp başka bir cihazda geri yapıştırabilirsin.",
                ]),
            ],
        },
        {
            "id": "languages",
            "title": "Diller",
            "dek": "Oyun {language_count} dilde çıkıyor.",
            "blocks": [
                ("p", "İngilizce, Türkçe, Almanca, Fransızca, İspanyolca, Latin Amerika İspanyolcası, İtalyanca, Lehçe, Brezilya Portekizcesi, Rusça, Ukraynaca, Japonca, Korece, Basitleştirilmiş Çince, Geleneksel Çince, Tayca, Endonezce ve Vietnamca. Oyun ilk açılışta senin dilini seçer, ayarlardan dilediğin an değiştirebilirsin - bu rehber de hepsinde var, sayfanın başındaki bağlantılardan."),
            ],
        },
    ],
}

