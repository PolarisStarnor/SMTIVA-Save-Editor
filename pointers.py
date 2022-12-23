
STAT_TXT = ("Str", "Dex", "Mag", "Agi", "Lck")

# Nanashi
MC_STAT1 = ["0x122", 2]
MC_MAX_HP = ("0x12C", 2)
MC_MAX_MP = ("0x12E", 2)
MC_STAT2 = ["0x130", 2]
MC_CURR_HP = ("0x13A", 2)
MC_CURR_MP = ("0x13C", 2)
MC_SKILL = ("0x144", 2, 8)
MC_LVL = ("0x172", 2)

# Miscellaneous
MISC_MACCA = ("0x10C", 4)
MISC_APP_PTS = ("0x2E38", 2)

# Demons
DE_NUM_MAX = 24
DE_START = "0x174"
DE_NEXT_OFFSET = "0x12C"
DE_SIZE = "0x65"
DE_STAT1 = ("0x4", 2)
DE_MAX_HP = ("0xE", 2)
DE_MAX_MP = ("0x10", 2)
DE_STAT2 = ("0x12", 2)
DE_CURR_HP = ("0x2A", 2)
DE_CURR_MP = ("0x2C", 2)
DE_SKILL = ("0x34", 2, 8)
DE_ID = ("0x62", 2, 8)
DE_LVL = ("0x64", 1)


# Open the skills data because I'm not dealing with that stuff.
try:
    file = open("skills.txt", "r")
except:
    print("Could not find skills file!")
    exit()
data = file.read().splitlines()
ALL_SKILLS = {}

for line in data:
    skill = line.split(": ")
    ALL_SKILLS.update({skill[0]: skill[1]})

file.close()

# Full Demons List
ALL_DEMONS = {
    "0": ("Empty", "Null", "(?)"),
    "1": ("Reserved", "Godly", "(?)"),
    "2": ("Reserved", "Godly", "(?)"),
    "3": ("Reserved", "Godly", "(?)"),
    "4": ("Reserved", "Godly", "(?)"),
    "5": ("Reserved", "Godly", "(?)"),
    "6": ("???", "???", "(?)"),
    "7": ("Reserved", "Godly", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1, Multi-enemies)"),
    "8": ("Reserved", "???", "(?)"),
    "9": ("Reserved", "Godly", "(?) (Attack: Phys x2, Multi-enemies)"),
    "a": ("Satan", "Primal", ""),
    "b": ("Merkabah", "Herald", ""),
    "c": ("Seraph", "Herald", ""),
    "d": ("Reserved", "???", "(?)"),
    "e": ("Metatron", "Herald", ""),
    "f": ("Reserved", "???", "(?)"),
    "10": ("Mastema", "Herald", ""),
    "11": ("Aniel", "Herald", ""),
    "12": ("Sraosha", "Herald", ""),
    "13": ("Reserved", "???", "(?)"),
    "14": ("Azrael", "Herald", ""),
    "15": ("Kazfiel", "Herald", ""),
    "16": ("0", "Herald", "(?)"),
    "17": ("Israfel", "Herald", ""),
    "18": ("Victor", "Herald", ""),
    "19": ("Lailah", "Herald", ""),
    "1a": ("Reserved", "Herald", "(?)"),
    "1b": ("Dummy", "Herald", "(?)"),
    "1c": ("Dummy", "Herald", "(?)"),
    "1d": ("Dummy", "Herald", "(?)"),
    "1c": ("Dummy", "Herald", "(?)"),
    "1e": ("Dummy", "Herald", "(?)"),
    "1f": ("Lakshmi", "Megami", ""),
    "20": ("Norn", "Megami", ""),
    "21": ("Anat", "Megami", ""),
    "22": ("Tlazolteotl", "Megami", ""),
    "23": ("Pallas Athena", "Megami", ""),
    "24": ("Ishtar", "Megami", ""),
    "25": ("Scathach", "Megami", ""),
    "26": ("Reserved", "Megami", "(?)"),
    "27": ("Parvati", "Megami", ""),
    "28": ("Fortuna", "Megami", ""),
    "29": ("Hathor", "Megami", ""),
    "2a": ("Brigid", "Megami", ""),
    "2b": ("Izanami", "Megami", ""),
    "2c": ("Cleopatra", "Megami", ""),
    "2d": ("Reserved", "Megami", "(?)"),
    "2e": ("Reserved", "Megami", "(?)"),
    "2f": ("Garuda", "Avian", ""),
    "30": ("Yatagarasu", "Avian", ""),
    "31": ("Feng Huang", "Avian", ""),
    "32": ("Thunderbird", "Avian", ""),
    "33": ("Vidofnir", "Avian", ""),
    "34": ("Phoenix", "Avian", ""),
    "35": ("Suparna", "Avian", ""),
    "36": ("Hamsa", "Avian", ""),
    "37": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "38": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "39": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3a": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3b": ("Reserved", "Avian", "(?) (Attack: Phys x1, All enemies)"),
    "3c": ("Yggdrasil", "Tree", ""),
    "3d": ("Haoma", "Tree", ""),
    "3e": ("Kukunochi", "Tree", ""),
    "3f": ("Mayahuel", "Tree", ""),
    "40": ("Narcissus", "Tree", ""),
    "41": ("Daphne", "Tree", ""),
    "42": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "43": ("Reserved", "Tree", "(?) (Attack: Phys x1, All enemies)"),
    "44": ("Reserved", "Tree", "(?)"),
    "45": ("Reserved", "Tree", "(?)"),
    "46": ("Reserved", "Tree", "(?)"),
    "47": ("Cherub", "Divine", ""),
    "48": ("Throne", "Divine", ""),
    "49": ("Dominion", "Divine", ""),
    "4a": ("Virtue", "Divine", ""),
    "4b": ("Power", "Divine", ""),
    "4c": ("Principality", "Divine", ""),
    "4d": ("Archangel", "Divine", ""),
    "4e": ("Angel", "Divine", "(Lvl 10)"),
    "4f": ("Reserved", "Divine", "(?)"),
    "50": ("Angel", "Divine", "(Lvl 82)"),
    "51": ("Reserved", "Divine", "(?)"),
    "52": ("Reserved", "Divine", "(?)"),
    "53": ("Reserved", "Divine", "(?)"),
    "54": ("Reserved", "Divine", "(?)"),
    "55": ("Da Peng", "Flight", ""),
    "56": ("Rukh", "Flight", ""),
    "57": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "58": ("Reserved", "Flight", "(?) (Attack: Gun x1, 1 enemy)"),
    "59": ("Tuofei", "Flight", ""),
    "5a": ("Caladrius", "Flight", ""),
    "5b": ("Gu Huo Niao", "Flight", ""),
    "5c": ("Harpy", "Flight", ""),
    "5d": ("Tangata Manu", "Flight", ""),
    "5e": ("Reserved", "Flight", "(?)"),
    "5f": ("Reserved", "Flight", "(?)"),
    "60": ("Reserved", "Flight", "(?)"),
    "61": ("Reserved", "Flight", "(?)"),
    "62": ("Reserved", "Flight", "(?)"),
    "63": ("Ganesha", "Yoma", ""),
    "64": ("Master Therion", "Yoma", ""),
    "65": ("Xiuhtecuhtli", "Yoma", ""),
    "66": ("Valkyrie", "Yoma", ""),
    "67": ("Shiwanna", "Yoma", ""),
    "68": ("Dis", "Yoma", ""),
    "69": ("Karasu Tengu", "Yoma", ""),
    "6a": ("Koppa Tengu", "Yoma", ""),
    "6b": ("Agathion", "Yoma", ""),
    "6c": ("Vodyanik", "Yoma", ""),
    "6d": ("Centaur", "Yoma", ""),
    "6e": ("Reserved", "Yoma", "(?)"),
    "6f": ("Reserved", "Yoma", "(?)"),
    "70": ("Reserved", "Yoma", "(?)"),
    "71": ("Reserved", "Yoma", "(?)"),
    "72": ("Peri", "Nymph", ""),
    "73": ("Sarasvati", "Nymph", ""),
    "74": ("Reserved", "Nymph", "(?)"),
    "75": ("Senri", "Nymph", ""),
    "76": ("Apsaras", "Nymph", ""),
    "77": ("Kikuri-Hime", "Nymph", ""),
    "78": ("Reserved", "Nymph", "(?)"),
    "79": ("Reserved", "Nymph", "(?)"),
    "7a": ("Reserved", "Nymph", "(?)"),
    "7b": ("Reserved", "Nymph", "(?)"),
    "7c": ("Demiurge", "Vile", ""),
    "7d": ("Seth", "Vile", ""),
    "7e": ("Pales", "Viles", ""),
    "7f": ("Alciel", "Vile", ""),
    "80": ("Taotie", "Vile", ""),
    "81": ("Pachacamac", "Vile", ""),
    "82": ("Reserved", "Vile", "(?)"),
    "83": ("Mishaguji", "Vile", ""),
    "84": ("Baphomet", "Vile", ""),
    "85": ("Reserved", "Vile", "(?)"),
    "86": ("Reserved", "Vile", "(?)"),
    "87": ("Reserved", "Vile", "(?)"),
    "88": ("Reserved", "Vile", "(?)"),
    "89": ("Reserved", "Vile", "(?)"),
    "8a": ("Hresvelgr", "Raptor", ""),
    "8b": ("Huoniao", "Raptor", ""),
    "8c": ("Anzu", "Raptor", ""),
    "8d": ("Gurr", "Raptor", ""),
    "8e": ("Zhen", "Raptor", ""),
    "8f": ("Itsumade", "Raptor", ""),
    "90": ("Moh Shuvuu", "Raptor", ""),
    "91": ("Camazotz", "Raptor", ""),
    "92": ("Fuxi", "Raptor", ""),
    "93": ("Reserved", "Raptor", "(?)"),
    "94": ("Reserved", "Raptor", "(?)"),
    "95": ("Reserved", "Raptor", "(?)"),
    "96": ("Reserved", "Raptor", "(?)"),
    "97": ("Reserved", "Raptor", "(?)"),
    "98": ("Erikonig", "Wood", ""),
    "99": ("Alraune", "Wood", ""),
    "9a": ("Zaccoum", "Wood", ""),
    "9b": ("Skogsra", "Wood", ""),
    "9c": ("Mandrake", "Wood", ""),
    "9d": ("Shan Xiao", "Wood", ""),
    "9e": ("Reserved", "Wood", "(?)"),
    "9f": ("Reserved", "Wood", "(?)"),
    "a0": ("Reserved", "Wood", "(?)"),
    "a1": ("Reserved", "Wood", "(?)"),
    "a2": ("Reserved", "Wood", "(?)"),
    "a3": ("Reserved", "Deity", "(?) (Resist: Charm/Daze/Mute) (Attack: Phys x1~2, 1 enemy)"),
    "a4": ("Reserved", "Deity", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "a5": ("Hachiman", "Deity", ""),
    "a6": ("Apsu", "Deity", ""),
    "a7": ("Baal", "Deity", ""),
    "a8": ("Odin", "Deity", ""),
    "a9": ("Ometeotl", "Deity", ""),
    "aa": ("Lord Nandou", "Deity", ""),
    "ab": ("Prometheus", "Deity", ""),
    "ac": ("Inti", "Deity", ""),
    "ad": ("Thoth", "Deity", ""),
    "ae": ("Krishna", "Deity", ""),
    "af": ("Mahamayuri", "Deity", ""),
    "b0": ("Osiris", "Deity", ""),
    "b1": ("Maitreya", "Deity", ""),
    "b2": ("Reserved", "Deity", "(?)"),
    "b3": ("Reserved", "Deity", "(?)"),
    "b4": ("Amaterasu", "Amatsu", ""),
    "b5": ("Take-Mikazuchi", "Amatsu", ""),
    "b6": ("Reserved", "Amatsu", "(?) (Weak: Sick)"),
    "b7": ("Reserved", "Amatsu", "(?)"),
    "b8": ("Ame no Uzume", "Amatsu", ""),
    "b9": ("Reserved", "Amatsu", "(?)"),
    "ba": ("Reserved", "Kunitsu", "(?)"),
    "bb": ("Reserved", "Famed", "(?)"),
    "bc": ("Reserved", "Human", "(?)"),
    "bd": ("Reserved", "Human", "(?)"),
    "be": ("Barong", "Avatar", ""),
    "bf": ("Anubis", "Avatar", ""),
    "c0": ("Ukano Mitama", "Avatar", ""),
    "c1": ("Chimera", "Avatar", ""),
    "c2": ("Kaiming Shou", "Avatar", ""),
    "c3": ("Makami", "Avatar", ""),
    "c4": ("Kamapua'a", "Avatar", ""),
    "c5": ("Shiisa", "Avatar", ""),
    "c6": ("Reserved", "Avatar", "(?)"),
    "c7": ("Reserved", "Avatar", "(?)"),
    "c8": ("Reserved", "Avatar", "(?)"),
    "c9": ("Reserved", "Avatar", "(?)"),
    "ca": ("Reserved", "Avatar", "(?)"),
    "cb": ("Sphinx", "Holy", ""),
    "cc": ("Sleipnir", "Holy", ""),
    "cd": ("Baihu", "Holy", ""),
    "ce": ("Airavata", "Holy", ""),
    "cf": ("Chironnupu", "Holy", ""),
    "d0": ("Qing Niuguai", "Holy", ""),
    "d1": ("Pabilsag", "Holy", ""),
    "d2": ("Apis", "Holy", ""),
    "d3": ("Heqet", "Holy", ""),
    "d4": ("Reserved", "Holy", "(?)"),
    "d5": ("Reserved", "Holy", "(?)"),
    "d6": ("Reserved", "Holy", "(?)"),
    "d7": ("Reserved", "Holy", "(?)"),
    "d8": ("Reserved", "Holy", "(?)"),
    "d9": ("Heimdall", "Genma", ""),
    "da": ("Hanuman", "Genma", ""),
    "db": ("Jarilo", "Genma", ""),
    "dc": ("Kresnik", "Genma", ""),
    "dd": ("Cu Chulainn", "Genma", ""),
    "de": ("Kurama Tengu", "Genma", ""),
    "df": ("Tlaloc", "Genma", ""),
    "e0": ("Frost Ace", "Genma", ""),
    "e1": ("Nata Taishi", "Genma", ""),
    "e2": ("Tam Lin", "Genma", ""),
    "e3": ("Ictinike", "Genma", ""),
    "e4": ("Baldur", "Genma", ""),
    "e5": ("Reserved", "Genma", "(?)"),
    "e6": ("Reserved", "Genma", "(?)"),
    "e7": ("Reserved", "Genma", "(?)"),
    "e8": ("Reserved", "Genma", "(?)"),
    "e9": ("Demonee-ho", "Fairy", ""),
    "ea": ("Titania", "Fairy", ""),
    "eb": ("Oberon", "Fairy", ""),
    "ec": ("Vivian", "Fairy", ""),
    "ed": ("Spriggan", "Fairy", ""),
    "ee": ("Nadja", "Fairy", ""),
    "ef": ("Lorelei", "Fairy", ""),
    "f0": ("Kelpie", "Fairy", ""),
    "f1": ("Silky", "Fairy", ""),
    "f2": ("High Pixie", "Fairy", ""),
    "f3": ("Setanta", "Fairy", ""),
    "f4": ("Pyro Jack", "Fairy", ""),
    "f5": ("Jack Frost", "Fairy", ""),
    "f6": ("Goblin", "Fairy", ""),
    "f7": ("Reserved", "Fairy", "(?)"),
    "f8": ("Pixie", "Fairy", ""),
    "f9": ("Napaea", "Fairy", ""),
    "fa": ("Reserved", "???", "(?)"),
    "fb": ("Reserved", "Fairy", "(?)"),
    "fc": ("Reserved", "Fairy", "(?)"),
    "fd": ("Reserved", "Fairy", "(?)"),
    "fe": ("Cerberus", "Beast", ""),
    "ff": ("Ammut", "Beast", ""),
    "100": ("Orthus", "Beast", ""),
    "101": ("Dormath", "Beast", ""),
    "102": ("Hsing-Hsing", "Beast", ""),
    "103": ("Nekomata", "Beast", ""),
    "104": ("Reserved", "Beast", "(?)"),
    "105": ("Inugami", "Beast", ""),
    "106": ("Kabuso", "Beast", ""),
    "107": ("Kaso", "Beast", ""),
    "108": ("Stonka", "Beast", ""),
    "109": ("Gryphon", "Beast", ""),
    "10a": ("Hairy Jack", "Beast", ""),
    "10b": ("Reserved", "Beast", "(?)"),
    "10c": ("Reserved", "???", "(?)"),
    "10d": ("Reserved", "Beast", "(?)"),
    "10e": ("Reserved", "Beast", "(?)"),
    "10f": ("Gogmagog", "Jirae", ""),
    "110": ("Tlaltecuhtli", "Jirae", ""),
    "111": ("Titan", "Jirae", ""),
    "112": ("Tsuchigumo", "Jirae", ""),
    "113": ("Kwancha", "Jirae", ""),
    "114": ("Sudama", "Jirae", ""),
    "115": ("Hua Po", "Jirae", ""),
    "116": ("Knocker", "Jirae", ""),
    "117": ("Dwarf", "Jirae", ""),
    "118": ("Reserved", "Jirae", "(?)"),
    "119": ("Reserved", "Jirae", "(?)"),
    "11a": ("Reserved", "Jirae", "(?)"),
    "11b": ("Reserved", "Jirae", "(?)"),
    "11c": ("Reserved", "Jirae", "(?)"),
    "11d": ("Reserved", "Snake", "(?) (Attack: Phys x1~3, 1 enemy)"),
    "11e": ("Pendragon", "Snake", ""),
    "11f": ("Orochi", "Snake", ""),
    "120": ("Ouroboros", "Snake", ""),
    "121": ("Gui Xian", "Snake", ""),
    "122": ("Yurlungur", "Snake", ""),
    "123": ("Vouivre", "Snake", ""),
    "124": ("Nozuchi", "Snake", ""),
    "125": ("Naga", "Snake", ""),
    "126": ("Reserved", "Snake", "(?)"),
    "127": ("Reserved", "Snake", "(?)"),
    "128": ("Reserved", "Snake", "(?)"),
    "129": ("Reserved", "Snake", "(?)"),
    "12a": ("Reserved", "Snake", "(?)"),
    "12b": ("Mot", "Reaper", ""),
    "12c": ("Nergal", "Reaper", ""),
    "12d": ("Guedhe", "Reaper", ""),
    "12e": ("Persephone", "Reaper", ""),
    "12f": ("Orcus", "Reaper", ""),
    "130": ("Hel", "Reaper", ""),
    "131": ("Ixtab", "Reaper", ""),
    "132": ("Cernunnos", "Reaper", ""),
    "133": ("Reserved", "Reaper", "(?)"),
    "134": ("Reserved", "Reaper", "(?)"),
    "135": ("Reserved", "Reaper", "(?)"),
    "136": ("Fenrir", "Wilder", ""),
    "137": ("Taowu", "Wilder", ""),
    "138": ("Cabracan", "Wilder", ""),
    "139": ("Catoblepas", "Wilder", ""),
    "13a": ("Manticore", "Wilder", ""),
    "13b": ("Porewit", "Wilder", ""),
    "13c": ("Peallaidh", "Wilder", ""),
    "13d": ("Nue", "Wilder", ""),
    "13e": ("Raiju", "Wilder", ""),
    "13f": ("Jueyuan", "Wilder", ""),
    "140": ("Chagrin", "Wilder", ""),
    "141": ("Reserved", "Wilder", "(?)"),
    "142": ("Reserved", "Wilder", "(?)"),
    "143": ("Reserved", "Wilder", "(?)"),
    "144": ("Reserved", "Wilder", "(?)"),
    "145": ("Reserved", "Wilder", "(?)"),
    "146": ("Hekatoncheires", "Jaki", ""),
    "147": ("Girimehkala", "Jaki", ""),
    "148": ("Grendel", "Jaki", ""),
    "149": ("Reserved", "Jaki", "(?)"),
    "14a": ("Rakshasa", "Jaki", ""),
    "14b": ("Black Frost", "Jaki", ""),
    "14c": ("Wendigo", "Jaki", ""),
    "14d": ("Ippon-Datara", "Jaki", ""),
    "14e": ("Gremlin", "Jaki", ""),
    "14f": ("Lham Dearg", "Jaki", ""),
    "150": ("Ogre", "Jaki", ""),
    "151": ("Reserved", "Jaki", "(?)"),
    "152": ("Reserved", "Jaki", "(?)"),
    "153": ("Reserved", "Jaki", "(?)"),
    "154": ("Reserved", "Jaki", "(?)"),
    "155": ("Arachne", "Vermin", ""),
    "156": ("Okiku-Mushi", "Vermin", ""),
    "157": ("Ubu", "Vermin", ""),
    "158": ("Mothman", "Vermin", ""),
    "159": ("Myrmecolion", "Vermin", ""),
    "15a": ("Reserved", "Vermin", "(?)"),
    "15b": ("Reserved", "Vermin", "(?)"),
    "15c": ("Reserved", "Vermin", "(?)"),
    "15d": ("Reserved", "Vermin", "(?)"),
    "15e": ("Reserved", "Vermin", "(?)"),
    "15f": ("Shiva", "Fury", ""),
    "160": ("Susano-o", "Fury", ""),
    "161": ("Kartikeya", "Fury", ""),
    "162": ("Beiji-Weng", "Fury", ""),
    "163": ("Wu Kong", "Fury", ""),
    "164": ("Chernobog", "Fury", ""),
    "165": ("Asura", "Fury", ""),
    "166": ("Tonatiuh", "Fury", ""),
    "167": ("Ares", "Fury", ""),
    "168": ("Mitra-Buddha", "Fury", ""),
    "169": ("Reserved", "???", "(?)"),
    "16a": ("Reserved", "Fury", "(?)"),
    "16b": ("Reserved", "Fury", "(?)"),
    "16c": ("Reserved", "Fury", "(?)"),
    "16d": ("Xi Wangmu", "Lady", ""),
    "16e": ("Skadi", "Lady", ""),
    "16f": ("Black Maria", "Lady", ""),
    "170": ("Inanna", "Lady", ""),
    "171": ("Asherah", "Lady", ""),
    "172": ("Diana", "Lady", ""),
    "173": ("Hariti", "Lady", ""),
    "174": ("Sedna", "Lady", ""),
    "175": ("Dzelarhons", "Lady", ""),
    "176": ("Pele", "Lady", ""),
    "177": ("Isis", "Lady", ""),
    "178": ("Reserved", "Lady", "(?)"),
    "179": ("Reserved", "Lady", "(?)"),
    "17a": ("Reserved", "Lady", "(?)"),
    "17b": ("Reserved", "Lady", "(?)"),
    "17c": ("Huang Long", "Dragon", ""),
    "17d": ("Quetzalcoatl", "Dragon", ""),
    "17e": ("Zhu Yin", "Dragon", ""),
    "17f": ("Illuyanka", "Dragon", ""),
    "180": ("Long", "Dragon", ""),
    "181": ("Gucumatz", "Dragon", ""),
    "182": ("Patrimpas", "Dragon", ""),
    "183": ("Makara", "Dragon", ""),
    "184": ("Reserved", "Dragon", "(?) (Attack: Phys x2, 1 enemy)"),
    "185": ("Reserved", "Dragon", "(?)"),
    "186": ("Reserved", "Dragon", "(?)"),
    "187": ("Reserved", "Dragon", "(?)"),
    "188": ("Reserved", "Dragon", "(?)"),
    "189": ("Thor", "Kishin", ""),
    "18a": ("Marishiten", "Kishin", ""),
    "18b": ("Bishamonten", "Kishin", ""),
    "18c": ("Jikokuten", "Kishin", ""),
    "18d": ("Zhong Kui", "Kishin", ""),
    "18e": ("Koumokuten", "Kishin", ""),
    "18f": ("Zouchouten", "Kishin", ""),
    "190": ("Reserved", "Kishin", "(?)"),
    "191": ("Reserved", "Kishin", "(?)"),
    "192": ("Reserved", "Kishin", "(?)"),
    "193": ("Reserved", "Kishin", "(?)"),
    "194": ("Reserved", "Kishin", "(?)"),
    "195": ("Arahabaki", "Kunitsu", ""),
    "196": ("Kushinada-hime", "Kunitsu", ""),
    "197": ("Okuninushi", "Kunitsu", ""),
    "198": ("Take-Minakata", "Kunitsu", ""),
    "199": ("Oumitsunu", "Kunitsu", ""),
    "19a": ("Hitokotonushi", "Kunitsu", ""),
    "19b": ("Sukuna-Hikona", "Kunitsu", ""),
    "19c": ("Reserved", "Kunitsu", "(?)"),
    "19d": ("Reserved", "Kunitsu", "(?)"),
    "19e": ("Samael", "Fallen", ""),
    "19f": ("Murmur", "Fallen", ""),
    "1a0": ("Gemori", "Fallen", ""),
    "1a1": ("Adramelech", "Fallen", ""),
    "1a2": ("Reserved", "Fallen", "(?)"),
    "1a3": ("Decarabia", "Fallen", ""),
    "1a4": ("Nebiros", "Fallen", ""),
    "1a5": ("Ose", "Fallen", ""),
    "1a6": ("Dantalian", "Fallen", ""),
    "1a7": ("Orias", "Fallen", ""),
    "1a8": ("Halphas", "Fallen", ""),
    "1a9": ("Bifrons", "Fallen", ""),
    "1aa": ("Melchom", "Fallen", ""),
    "1ab": ("Azazel->moved to Tyant", "Fallen", "(?)"),
    "1ac": ("Shax", "Fallen", ""),
    "1ad": ("Barbatos", "Fallen", ""),
    "1ae": ("Botis", "Fallen", ""),
    "1af": ("Reserved", "Fallen", "(?)"),
    "1b0": ("Ongyo-Ki", "Brute", ""),
    "1b1": ("Berserker", "Brute", ""),
    "1b2": ("Sui-Ki", "Brute", ""),
    "1b3": ("Fuu-Ki", "Brute", ""),
    "1b4": ("Kin-Ki", "Brute", ""),
    "1b5": ("Yomotsu Ikusa", "Brute", ""),
    "1b6": ("Yamawaro", "Brute", ""),
    "1b7": ("Momunofu", "Brute", ""),
    "1b8": ("Azumi", "Brute", ""),
    "1b9": ("Oni", "Brute", ""),
    "1ba": ("Reserved", "Brute", "(?)"),
    "1bb": ("Yaksha", "Brute", ""),
    "1bc": ("Bilwis", "Brute", ""),
    "1bd": ("Reserved", "Brute", "(?)"),
    "1be": ("Reserved", "Brute", "(?)"),
    "1bf": ("Reserved", "Brute", "(?)"),
    "1c0": ("Rangda", "Femme", ""),
    "1c1": ("Dakini", "Femme", ""),
    "1c2": ("Atropos", "Femme", ""),
    "1c3": ("Lachesis", "Femme", ""),
    "1c4": ("Clotho", "Femme", ""),
    "1c5": ("Yuki Jyorou", "Femme", ""),
    "1c6": ("Shikome", "Femme", ""),
    "1c7": ("Strix", "Femme", ""),
    "1c8": ("Leanan Sidhe", "Femme", ""),
    "1c9": ("Mermaid", "Femme", ""),
    "1ca": ("Taraka", "Femme", ""),
    "1cb": ("Kali", "Femme", ""),
    "1cc": ("Medusa", "Femme", ""),
    "1cd": ("Reserved", "Femme", "(?)"),
    "1ce": ("Maya", "Night", ""),
    "1cf": ("Reserved", "Night", "(?)"),
    "1d0": ("Reserved", "Night", "(?)"),
    "1d1": ("Queen Mab", "Night", ""),
    "1d2": ("Wild Hunt", "Night", ""),
    "1d3": ("Succubus", "Night", ""),
    "1d4": ("Kaiwan", "Night", ""),
    "1d5": ("Incubus", "Night", ""),
    "1d6": ("Kikimora", "Night", ""),
    "1d7": ("Lilim", "Night", ""),
    "1d8": ("Sandman", "Night", ""),
    "1d9": ("Fomorian", "Night", ""),
    "1da": ("Mokoi", "Night", ""),
    "1db": ("Reserved", "Night", "(?)"),
    "1dc": ("Reserved", "Night", "(?)"),
    "1dd": ("Reserved", "Night", "(?)"),
    "1de": ("Reserved", "Night", "(?)"),
    "1df": ("Reserved", "Night", "(?)"),
    "1e0": ("Lucifer", "Tyrant", ""),
    "1e1": ("Mara", "Tyrant", ""),
    "1e2": ("Chi You", "Tyrant", ""),
    "1e3": ("Surt", "Tyrant", ""),
    "1e4": ("Tzitzimitl", "Tyrant", ""),
    "1e5": ("Beelzebub", "Tyrant", ""),
    "1e6": ("Abaddon", "Tyrant", ""),
    "1e7": ("Loki", "Tyrant", ""),
    "1e8": ("Belial", "Tyrant", ""),
    "1e9": ("Astaroth", "Tyrant", "(?) (Dummied out leftover from SMTIV)"),
    "1ea": ("Balor", "Tyrant", ""),
    "1eb": ("King Frost", "Tyrant", ""),
    "1ec": ("Samyaza", "Tyrant", ""),
    "1ed": ("Horkos", "Tyrant", ""),
    "1ee": ("Mithras", "Tyrant", ""),
    "1ef": ("Morax", "Tyrant", ""),
    "1f0": ("Azazel", "Tyrant", ""),
    "1f1": ("Mephisto", "Tyrant", ""),
    "1f2": ("Lucifuge", "Tyrant", ""),
    "1f3": ("Reserved", "Tyrant", "(?)"),
    "1f4": ("Reserved", "Tyrant", "(?)"),
    "1f5": ("Fafnir", "Drake", ""),
    "1f6": ("Ym", "Drake", ""),
    "1f7": ("Nidhoggr", "Drake", ""),
    "1f8": ("Tiamat", "Drake", ""),
    "1f9": ("Mushussu", "Drake", ""),
    "1fa": ("Kingu", "Drake", ""),
    "1fb": ("Basilisk", "Drake", ""),
    "1fc": ("Bai Suzhen", "Drake", ""),
    "1fd": ("Toubyou", "Drake", ""),
    "1fe": ("Zhu Tun She", "Drake", ""),
    "1ff": ("Vasuki", "Drake", ""),
    "200": ("Phython", "Drake", ""),
    "201": ("Reserved", "Drake", "(?)"),
    "202": ("Reserved", "Drake", "(?)"),
    "203": ("Reserved", "Drake", "(?)"),
    "204": ("Legion", "Spirit", ""),
    "205": ("Pisaca", "Spirit", ""),
    "206": ("Inferno", "Spirit", ""),
    "207": ("Macabre", "Spirit", ""),
    "208": ("Quicksilver", "Spirit", ""),
    "209": ("Poltergeist", "Spirit", ""),
    "20a": ("Wicker Man", "Spirit", ""),
    "20b": ("Dybbuk", "Spirit", ""),
    "20c": ("Garrote", "Spirit", ""),
    "20d": ("Reserved", "Spirit", "(?)"),
    "20e": ("Reserved", "Spirit", "(?)"),
    "20f": ("Reserved", "Spirit", "(?)"),
    "210": ("Reserved", "Spirit", "(?)"),
    "211": ("Reserved", "Foul", "(?)"),
    "212": ("Reserved", "Foul", "(?)"),
    "213": ("Mad Gasser", "Foul", ""),
    "214": ("Reserved", "Foul", ""),
    "215": ("Night Stalker", "Foul", ""),
    "216": ("Hooligan", "Foul", ""),
    "217": ("Jack the Ripper", "Foul", ""),
    "218": ("Slime", "Foul", ""),
    "219": ("Tattooed Man", "Foul", ""),
    "21a": ("Reserved", "Foul", "(?)"),
    "21b": ("Reserved", "Foul", "(?)"),
    "21c": ("Reserved", "Foul", "(?)"),
    "21d": ("Reserved", "Foul", "(?)"),
    "21e": ("Vetala", "Ghost", ""),
    "21f": ("Kudlak", "Ghost", ""),
    "220": ("Ghoul", "Ghost", ""),
    "221": ("Enku", "Ghost", ""),
    "222": ("Churel", "Ghost", ""),
    "223": ("Mou-Ryo", "Ghost", ""),
    "224": ("Obariyon", "Ghost", ""),
    "225": ("Preta", "Ghost", ""),
    "226": ("Strigoii", "Ghost", ""),
    "227": ("Dullahan", "Ghost", "(?) (Dummied out leftover from SMTIV)"),
    "228": ("Reserved", "Ghost", "(?)"),
    "229": ("Reserved", "Ghost", "(?)"),
    "22a": ("Reserved", "Ghost", "(?)"),
    "22b": ("Reserved", "Ghost", "(?)"),
    "22c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "22d": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "22e": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "22f": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "230": ("Reserved", "Mitama", "(?)"),
    "231": ("Reserved", "Mitama", "(?)"),
    "232": ("Reserved", "Mitama", "(?)"),
    "233": ("Reserved", "Mitama", "(?)"),
    "234": ("Reserved", "Mitama", "(?)"),
    "235": ("Salamander", "Element", ""),
    "236": ("Undine", "Element", ""),
    "237": ("Sylph", "Element", ""),
    "238": ("Gnome", "Element", ""),
    "239": ("Flaemis", "Element", ""),
    "23a": ("Aquans", "Element", ""),
    "23b": ("Aeros", "Element", ""),
    "23c": ("Erthys", "Element", ""),
    "23d": ("Reserved", "Element", "(?)"),
    "23e": ("Reserved", "Element", "(?)"),
    "23f": ("Reserved", "Element", "(?)"),
    "240": ("Reserved", "Element", "(?)"),
    "241": ("Reserved", "Element", "(?)"),
    "242": ("Mother Harlot", "Fiend", ""),
    "243": ("Trumpeter", "Fiend", ""),
    "244": ("Pale Rider", "Fiend", ""),
    "245": ("Black Rider", "Fiend", ""),
    "246": ("Red Rider", "Fiend", ""),
    "247": ("White Rider", "Fiend", ""),
    "248": ("Reserved", "Fiend", "(?)"),
    "249": ("Matador", "Fiend", ""),
    "24a": ("David", "Fiend", ""),
    "24b": ("Reserved", "Fiend", "(?)"),
    "24c": ("Reserved", "???", "(?)"),
    "24d": ("Reserved", "Fiend", "(?)"),
    "24e": ("Reserved", "Fiend", "(?)"),
    "24f": ("Reserved", "Fiend", "(?)"),
    "250": ("Kangiten", "Enigma", ""),
    "251": ("Kama", "Enigma", ""),
    "252": ("Kinmamon", "Enigma", ""),
    "253": ("Futotama", "Enigma", ""),
    "254": ("Kanbari", "Enigma", ""),
    "255": ("Reserved", "Enigma", "(?)"),
    "256": ("Reserved", "Enigma", "(?)"),
    "257": ("Reserved", "Enigma", "(?)"),
    "258": ("Reserved", "Enigma", "(?)"),
    "259": ("Reserved", "Enigma", "(?)"),
    "25a": ("Hare of Inaba", "Food", ""),
    "25b": ("Kuda", "Food", ""),
    "25c": ("Chupacabra", "Food", ""),
    "25d": ("Mamedanuki", "Food", ""),
    "25e": ("Katakirauwa", "Food", ""),
    "25f": ("Onmoraki", "Food", ""),
    "260": ("Reserved", "Food", "(?)"),
    "261": ("Reserved", "Food", "(?)"),
    "262": ("Reserved", "Food", "(?)"),
    "263": ("Reserved", "Food", "(?)"),
    "264": ("Reserved", "Food", "(?)"),
    "265": ("Moved to Diff Race: Masakado", "Zealot", "(?) (Entire portrait is solid white)"),
    "266": ("Tezcatlipoca", "Zealot", ""),
    "267": ("Attis", "Zealot", ""),
    "268": ("Aramisaki", "Zealot", ""),
    "269": ("Dionysus", "Zealot", ""),
    "26a": ("Ogun", "Zealot", ""),
    "26b": ("Reserved", "Zealot", "(?)"),
    "26c": ("Reserved", "Zealot", "(?)"),
    "26d": ("Reserved", "Zealot", "(?)"),
    "26e": ("Reserved", "Zealot", "(?)"),
    "26f": ("Reserved", "Zealot", "(?)"),
    "270": ("Alilat", "Entity", ""),
    "271": ("Reserved", "Entity", "(?)"),
    "272": ("Reserved", "Entity", "(?)"),
    "273": ("Reserved", "Entity", "(?)"),
    "274": ("Reserved", "Entity", "(?)"),
    "275": ("Reserved", "Entity", "(?)"),
    "276": ("Huang Di", "Famed", ""),
    "277": ("Tokisada", "Famed", ""),
    "278": ("Rama", "Famed", ""),
    "279": ("Kanseiteikun", "Famed", ""),
    "27a": ("Siegfried", "Famed", ""),
    "27b": ("Hagen", "Famed", ""),
    "27c": ("Jeanne d'Arc", "Famed", ""),
    "27d": ("Lanling Wang", "Famed", ""),
    "27e": ("Yoshitsune", "Famed", ""),
    "27f": ("Tenkai", "Famed", ""),
    "280": ("Reserved", "Famed", "(?)"),
    "281": ("Reserved", "Famed", "(?)"),
    "282": ("DLC Stock", "Famed", "(?) (Resist: Charm/Daze/Mute)"),
    "283": ("Reserved", "Famed", "(?)"),
    "284": ("Ashura-kai Man", "Human", "(Enemy-only)"),
    "285": ("Ashura-kai Woman", "Human", "(Enemy-only)"),
    "286": ("Reserved", "Human", "(?)"),
    "287": ("Reserved", "Human", "(?)"),
    "288": ("Reserved", "Human", "(?)"),
    "289": ("Reserved", "Human", "(?)"),
    "28a": ("Reserved", "Human", "(?)"),
    "28b": ("Reserved", "Human", "(?)"),
    "28c": ("Reserved", "Human", "(?)"),
    "28d": ("Gaea Man", "Human", "(Enemy-only)"),
    "28e": ("Gaea Woman", "Human", "(Enemy-only)"),
    "28f": ("Reserved", "Human", "(?)"),
    "290": ("Reserved", "Human", "(?)"),
    "291": ("Samurai Zombie", "Undead", "(Male) (Enemy-only, unused leftover from SMTIV)"),
    "292": ("Samurai Zombie", "Undead", "(Female) (Enemy-only, unused leftover from SMTIV)"),
    "293": ("Zombie", "Undead", "(Enemy-only, unused leftover from SMTIV)"),
    "294": ("Alice", "Undead", ""),
    "295": ("Reserved", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "296": ("Zombie Cop", "Undead", ""),
    "297": ("Deleted", "Undead", "(?) (Resist: Gun, Weak: Fire/Light, Null: Dark)"),
    "298": ("Deleted", "Undead", "(?)"),
    "299": ("Patriot", "Undead", ""),
    "29a": ("Corpse", "Undead", ""),
    "29b": ("Reserved", "Cyber", "(?)"),
    "29c": ("Reserved", "Cyber", "(?)"),
    "29d": ("Flynn", "Human", "(YHVH Fight, Bonds Flynn?)"),
    "29e": ("Flynn", "Human", "(YHVH Fight, Massacre Flynn?)"),
    "29f": ("Walter", "Human", "(YHVH Fight)"),
    "2a0": ("Jonathan", "Human", "(YHVH Fight)"),
    "2a1": ("Isabeau", "Human", "(YHVH Fight)"),
    "2a2": ("Satan", "Primal", "(YHVH Fight)"),
    "2a3": ("Timothy", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a4": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a5": ("Navarre", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a6": ("Portable Cannon", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a7": ("Nozomi", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a8": ("Orb of the Gates", "Undead", "(?) (Null: Poison/Panic/Sleep/Bind/Sick)"),
    "2a9": ("Giant Horde", "Horde", "(Unused)"),
    "2aa": ("Innocent Horde", "Horde", "(Enemy-only)"),
    "2ab": ("Oni Horde", "Horde", "(Enemy-only)"),
    "2ac": ("Dragon Horde", "Horde", "(Enemy-only)"),
    "2ad": ("Dead Horde", "Horde", "(Enemy-only)"),
    "2ae": ("Wildfire Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2af": ("Demon Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2b0": ("Azteca Force", "Horde", "(Enemy-only)"),
    "2b1": ("Jaki Horde", "Horde", "(Enemy-only)"),
    "2b2": ("Greek Force", "Horde", "(Enemy-only)"),
    "2b3": ("Angel Army", "Horde", "(Enemy-only)"),
    "2b4": ("Defiant Horde", "Horde", "(Enemy-only)"),
    "2b5": ("Freezing Horde", "Horde", "(Enemy-only)"),
    "2b6": ("Gale Horde", "Horde", "(Unused)"),
    "2b7": ("Fallen Horde", "Horde", "(Enemy-only)"),
    "2b8": ("Demon Army", "Horde", "(Enemy-only)"),
    "2b9": ("Not Used", "Horde", ""),
    "2ba": ("Thunder Horde", "Horde", "(Enemy-only)"),
    "2bb": ("Blazing Horde", "Horde", "(Enemy-only)"),
    "2bc": ("Indian Horde", "Horde", "(Enemy-only)"),
    "2bd": ("Not Used", "Horde", ""),
    "2be": ("Not Used", "Horde", ""),
    "2bf": ("Inferno Horde", "Horde", "(Enemy-only)"),
    "2c0": ("Blizzard Horde", "Horde", "(Enemy-only)"),
    "2c1": ("Tengu Horde", "Horde", "(Enemy-only)"),
    "2c2": ("Jack Union", "Horde", "(Enemy-only)"),
    "2c3": ("Frosts", "Horde", "(Unused leftover from SMTIV)"),
    "2c4": ("Norse Force", "Horde", "(Enemy-only)"),
    "2c5": ("Not Used", "Horde", ""),
    "2c6": ("Pirate Horde", "Horde", "(Unused leftover from SMTIV)"),
    "2c7": ("A. Demon Army", "Horde", "(Enemy-only)"),
    "2c8": ("A. Angel Army", "Horde", "(Enemy-only)"),
    "2c9": ("A. Angel Horde", "Horde", "(Enemy-only)"),
    "2ca": ("Herald Army", "Horde", "(Enemy-only)"),
    "2cb": ("Seraph Army", "Horde", "(Enemy-only)"),
    "2cc": ("Metatron Army", "Horde", "(Enemy-only)"),
    "2cd": ("Angel Army", "Horde", "(Enemy-only)"),
    "2ce": ("Not Used", "Horde", ""),
    "2cf": ("Not Used", "Horde", ""),
    "2d0": ("Not Used", "Horde", ""),
    "2d1": ("Not Used", "Horde", ""),
    "2d2": ("Not Used", "Horde", ""),
    "2d3": ("Itsumade Horde", "Horde", "(Enemy-only)"),
    "2d4": ("Not Used", "Horde", ""),
    "2d5": ("Strix Horde", "Horde", "(Enemy-only)"),
    "2d6": ("Demonstrators", "Horde", "(Enemy-only)"),
    "2d7": ("Obsessed Horde", "Horde", "(Enemy-only)"),
    "2d8": ("Greedy Horde", "Horde", "(Enemy-only)"),
    "2d9": ("Maruo Faction", "Horde", "(Enemy-only)"),
    "2da": ("Zaccoum Horde", "Horde", "(Enemy-only)"),
    "2db": ("Corpse Army", "Horde", "(Enemy-only)"),
    "2dc": ("Yomi Army", "Horde", "(Enemy-only)"),
    "2dd": ("Rakshasa", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2de": ("Ares", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2df": ("Long", "Horde", "(?) (Unfinished hoarde, appropriate resist/attack)"),
    "2e0": ("Black Frost", "Jaki", "(Boss version)"),
    "2e1": ("Tlaltecuhtli", "Jirae", "(Boss version)"),
    "2e2": ("Prometheus", "Deity", "(Boss version)"),
    "2e3": ("Dormarth", "Beast", "(Boss version)"),
    "2e4": ("Loki", "Tyrant", "(Boss version)"),
    "2e5": ("Lanling Wang", "Famed", "(Boss version)"),
    "2e6": ("Girimehkala", "Jaki", "(Boss version)"),
    "2e7": ("Aramisaki", "Zealot", "(Boss version)"),
    "2e8": ("Ashura-kai Man", "Human", "(Boss version)"),
    "2e9": ("Shax", "Fallen", "(Boss version)"),
    "2ea": ("Futotama", "Enigma", "(Boss version)"),
    "2eb": ("Arahabaki", "Kunitsu", "(Boss version)"),
    "2ec": ("Mara", "Tyrant", "(Boss version)"),
    "2ed": ("Hagen", "Famed", "(Boss version)"),
    "2ee": ("Ongyo-Ki", "Brute", "(Boss version)"),
    "2ef": ("Izanami", "Megami", "(Boss version)"),
    "2f0": ("Maruo", "Human", "(Enemy-only)"),
    "2f1": ("Zhen", "Raptor", "(Boss version)"),
    "2f2": ("Tamagami", "Ghost", "(Enemy-only)"),
    "2f3": ("Okuninushi", "Kunitsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f4": ("Kanseiteikun", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f5": ("Manticore", "Wilder", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f6": ("Abaddon", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f7": ("Demonee-ho", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f8": ("Taowu", "Wilder", "(?)  (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2f9": ("Prisoner Yokota", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fa": ("Fusou Fujio", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fb": ("Hiro Jingu", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fc": ("G.H. Hills", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "2fd": ("Take-Mikazuchi", "Amatsu", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2fe": ("Dionysus", "Zealot", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "2ff": ("Silky", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "300": ("Lorelei", "Fairy", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "301": ("Persephone", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "302": ("Tiamat", "Drake", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "303": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "304": ("Anzu", "Raptor", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "305": ("Astaroth", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "306": ("Cernunnos", "Reaper", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "307": ("Grendel", "Jaki", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "308": ("Dormarth", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "309": ("Marishiten", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30a": ("Throne", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30b": ("Dominion", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30c": ("Power", "Divine", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30d": ("Kazfiel", "Herald", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "30e": ("Hunter Man", "Human", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "30f": ("Hunter Woman", "Human", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "310": ("Thor", "Kishin", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "311": ("Morax", "Tyrant", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "312": ("Chimera", "Avatar", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "313": ("Tokisada", "Famed", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "314": ("Gaston", "Human", "(Plain spear) (Partner)"),
    "315": ("Gaston", "Human", "(Gungnir) (Partner)"),
    "316": ("Toki", "Human", "(Unmasked) (Partner)"),
    "317": ("Isabeau", "Human", "(Partner)"),
    "318": ("Asahi", "Human", "(Partner)"),
    "319": ("Navarre", "Ghost", "(Partner)"),
    "31a": ("Nozomi", "Human", "(Partner)"),
    "31b": ("Gaston", "Human", "(Spear of Michael) (Partner)"),
    "31c": ("Hallelujah", "Human", "(Partner)"),
    "31d": ("Hallelujah", "Hybrid", "(Partner)"),
    "31e": ("Toki", "Human", "(Masked) (Partner)"),
    "31f": ("Flynn", "Samurai", "(Aniel fight ally)"),
    "320": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "321": ("Katakirauwa", "Food", "(Tutorial version)"),
    "322": ("Lucifer's Minions", "Horde", "(Enemy-only)"),
    "323": ("Angel", "Divine", "(Boss version)"),
    "324": ("Aniel", "Herald", "(Boss version)"),
    "325": ("King Frost", "Tyrant", "(Boss version)"),
    "326": ("Sukuna-Hikona", "Kunitsu", "(Boss version)"),
    "327": ("Shesha", "Snake", "(Encounter 1)"),
    "328": ("Minotaur", "Beast", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "329": ("Medusa", "Femme", "(?) (Boss version, unused leftover from SMTIV, appropriate resist/attack)"),
    "32a": ("Titan", "Jirae", "(Boss version)"),
    "32b": ("Medusa", "Femme", "(Boss version)"),
    "32c": ("Shesha", "Snake", "(Encounter 2)"),
    "32d": ("Gaea Woman", "Human", "(Boss version)"),
    "32e": ("Zhong Kui", "Kishin", "(Boss version)"),
    "32f": ("Toki", "Human", "(Masked, boss version)"),
    "330": ("Odin", "Deity", "(Boss version, encounter 1)"),
    "331": ("Not Used", "Horde", ""),
    "332": ("Gaea Man", "Human", "(Boss version)"),
    "333": ("Quetzalcoatl", "Dragon", "(Boss version)"),
    "334": ("Jikokuten", "Kishin", "(Boss version)"),
    "335": ("Koumokuten", "Kishin", "(Boss version)"),
    "336": ("Zouchouten", "Kishin", "(Boss version)"),
    "337": ("Bishamonten", "Kishin", "(Boss version)"),
    "338": ("Marishiten", "Kishin", "(Boss version)"),
    "339": ("Inanna Remnant", "Lady", "(Enemy-only)"),
    "33a": ("Maitreya", "Deity", "(Boss version)"),
    "33b": ("Shesha", "Snake", "(Encounter 3)"),
    "33c": ("Krishna", "Deity", "(Boss version)"),
    "33d": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33e": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "33f": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "340": ("Not Used", "Archaic", "(?) (Null: Light/Dark)"),
    "341": ("Gaea Man", "Human", "(Boss version)"),
    "342": ("Gaea Woman", "Human", "(Boss version)"),
    "343": ("Adramelech", "Fallen", "(Boss version)"),
    "344": ("Angel Army", "Horde", "(Boss version)"),
    "345": ("Azrael", "Herald", "(Boss version)"),
    "346": ("Belial", "Tyrant", "(Boss version)"),
    "347": ("Lucifuge", "Tyrant", "(Boss version)"),
    "348": ("Samyaza", "Tyrant", "(Boss version)"),
    "349": ("Lucifer", "Tyrant", "(Boss version)"),
    "34a": ("Merkabah", "Herald", "(Boss version)"),
    "34b": ("Not Used", "Drake", "(?) (Repel: Phys, Resist: Gun, Weak: Ice/Elec)"),
    "34c": ("Not Used", "Vile", "(?) (Null: Ice/Dark, Resist: Light, Weak: Fire)"),
    "34d": ("Not Used", "Horde", "(?) (Resist: Dark, Weak: Fire/Force/Light) (Attack: Phys x3~4, 1 enemy)"),
    "34e": ("Odin", "Deity", "(Boss version, encounter 2)"),
    "34f": ("Baal", "Deity", "(Boss version)"),
    "350": ("Apsu", "Deity", "(Boss version)"),
    "351": ("Seth", "Vile", "(Boss version)"),
    "352": ("Inanna", "Lady", "(Boss version)"),
    "353": ("Mitra-Buddha", "Fury", "(Boss version)"),
    "354": ("Dagda", "Deity", "(Enemy-only)"),
    "355": ("Vishnu-Flynn", "Deity", "(1st form) (Enemy-only)"),
    "356": ("Metatron", "Herald", "(Boss version)"),
    "357": ("Metatron Army", "Horde", "(Boss version)"),
    "358": ("Not Used", "Human", "(?) (Null: Light/Dark)"),
    "359": ("Not Used", "Megami", "(?) (Repel: Gun, Null: Dark, Resist: Phys/Light)"),
    "35a": ("Satan", "Primal", "(Boss version)"),
    "35b": ("YHVH", "Godly", "(1st form) (Enemy-only)"),
    "35c": ("YHVH", "Godly", "(2nd form) (Enemy-only)"),
    "35d": ("Vishnu-Flynn", "Deity", "(2nd form) (Enemy-only)"),
    "35e": ("Angel Army", "Horde", "(Boss version)"),
    "35f": ("Rukh", "Flight", "(Boss version)"),
    "360": ("Navarre", "Ghost", "(Boss version)"),
    "361": ("Nozomi", "Human", "(Boss version)"),
    "362": ("Hallelujah", "Hybrid", "(Boss version)"),
    "363": ("Gaston", "Human", "(Boss version)"),
    "364": ("Toki", "Human", "(Unmasked, boss version)"),
    "365": ("Isabeau", "Human", "(Boss version)"),
    "366": ("Human Army", "Horde", "(Wave 1) (Enemy-only)"),
    "367": ("Human Army", "Horde", "(Wave 2) (Enemy-only)"),
    "368": ("Human Army", "Horde", "(Wave 3) (Enemy-only)"),
    "369": ("Human Army", "Horde", "(Wave 4) (Enemy-only)"),
    "36a": ("Human Army", "Horde", "(Wave 5) (Enemy-only)"),
    "36b": ("A. Lucifer", "Tyrant", ""),
    "36c": ("A. Beelzebub", "Tyrant", ""),
    "36d": ("A. Lucifuge", "Tyrant", ""),
    "36e": ("A. Merkabah", "Herald", ""),
    "36f": ("A. Aniel", "Herald", ""),
    "370": ("A. Azrael", "Herald", ""),
    "371": ("Pachacamac", "Vile", "(Boss version)"),
    "372": ("Mushussu", "Drake", "(Boss version)"),
    "373": ("Gemori", "Fallen", "(Boss version)"),
    "374": ("Murmur", "Fallen", "(Boss version)"),
    "375": ("Master Therion", "Yoma", "(Boss version)"),
    "376": ("Dominion", "Divine", "(Boss version)"),
    "377": ("Throne", "Divine", "(Boss version)"),
    "378": ("Abaddon", "Tyrant", "(Boss version)"),
    "379": ("Barbatos", "Fallen", "(Boss version)"),
    "37a": ("Fafnir", "Drake", "(Boss version)"),
    "37b": ("Pales", "Vile", "(Boss version)"),
    "37c": ("Michizane", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37d": ("Yamato Takeru", "Famed", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "37e": ("Merkabah", "Tyrant", "(?) (Tyrant? No idea what this was supposed to be.)"),
    "37f": ("Belial", "Tyrant", "(?) (Unused leftover boss from SMTIV, appropriate resist/attack)"),
    "380": ("Karasu Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "381": ("Koppa Tengu", "Yoma", "(?) (Boss version, appropriate resist/attack)"),
    "382": ("Ose", "Fallen", "(?) (Boss version, appropriate resist/attack)"),
    "383": ("Kaiwan", "Night", "(?) (Boss version, appropriate resist/attack)"),
    "384": ("A. Nebiros", "Fallen", ""),
    "385": ("A. Adramelech", "Fallen", ""),
    "386": ("A. Barbatos", "Fallen", ""),
    "387": ("A. Murmur", "Fallen", ""),
    "388": ("A. Dantalian", "Fallen", ""),
    "389": ("A. Belial", "Tyrant", ""),
    "38a": ("A. Alciel", "Vile", ""),
    "38b": ("A. Cherub", "Divine", ""),
    "38c": ("A. Throne", "Divine", ""),
    "38d": ("A. Dominion", "Divine", ""),
    "38e": ("A. Virtue", "Divine", ""),
    "38f": ("A. Power", "Divine", ""),
    "390": ("A. Angel", "Divine", ""),
    "391": ("Chimera", "Avatar", "(Twisted Tokyo version)"),
    "392": ("Legion", "Spirit", "(Twisted Tokyo version)"),
    "393": ("Inferno", "Spirit", "(Twisted Tokyo version)"),
    "394": ("Hitokotonuchi", "Kunitsu", "(Twisted Tokyo version)"),
    "395": ("Corpse", "Undead", "(Twisted Tokyo version)"),
    "396": ("Slime", "Foul", "(Twisted Tokyo version)"),
    "397": ("Attis", "Zealot", "(Twisted Tokyo version)"),
    "398": ("Kaiming Shou", "Avatar", "(Twisted Tokyo version)"),
    "399": ("Itsumade", "Raptor", "(Twisted Tokyo version)"),
    "39a": ("Vetala", "Ghost", "(Twisted Tokyo version)"),
    "39b": ("Chernobog", "Fury", "(Twisted Tokyo version)"),
    "39c": ("Yatagarasu", "Avian", "(Twisted Tokyo version)"),
    "39d": ("Orthrus", "Beast", "(Twisted Tokyo version)"),
    "39e": ("Black Maria", "Lady", "(Twisted Tokyo version)"),
    "39f": ("Tlazolteotl", "Megami", "(Twisted Tokyo version)"),
    "3a0": ("Kanbari", "Enigma", "(Twisted Tokyo version)"),
    "3a1": ("Peallaidh", "Wilder", "(Twisted Tokyo version)"),
    "3a2": ("Ogun", "Zealot", "(Twisted Tokyo version)"),
    "3a3": ("Ometeotl", "Deity", "(Twisted Tokyo version)"),
    "3a4": ("Ukano Mitama", "Avatar", "(Twisted Tokyo version)"),
    "3a5": ("Centaur", "Yoma", "(Twisted Tokyo version)"),
    "3a6": ("Yggdrasil", "Tree", "(Twisted Tokyo version)"),
    "3a7": ("Skadi", "Lady", "(Twisted Tokyo version)"),
    "3a8": ("Taotie", "Vile", "(Twisted Tokyo version)"),
    "3a9": ("Kingu", "Drake", "(Twisted Tokyo version)"),
    "3aa": ("Azazel", "Tyrant", "(Twisted Tokyo version)"),
    "3ab": ("Hachiman", "Deity", "(Twisted Tokyo version)"),
    "3ac": ("Kartikeya", "Fury", "(Twisted Tokyo version)"),
    "3ad": ("Tezcatilipoca", "Zealot", "(Twisted Tokyo version)"),
    "3ae": ("Girimehkala", "Jaki", "(Twisted Tokyo version)"),
    "3af": ("Nergal", "Reaper", "(Twisted Tokyo version)"),
    "3b0": ("Botis", "Fallen", "(Twisted Tokyo version)"),
    "3b1": ("Kangiten", "Enigma", "(Twisted Tokyo version)"),
    "3b2": ("Surt", "Tyrant", "(Twisted Tokyo version)"),
    "3b3": ("Python", "Drake", "(Twisted Tokyo version)"),
    "3b4": ("", "Mot", "(Twisted Tokyo version)"),
    "3b5": ("Vasuki", "Drake", "(Twisted Tokyo version)"),
    "3b6": ("Samael", "Fallen", "(Twisted Tokyo version)"),
    "3b7": ("Itsumade Horde", "Horde", "(Twisted Tokyo version)"),
    "3b8": ("Wildfire Horde", "Horde", "(Twisted Tokyo version)"),
    "3b9": ("Pirate Horde", "Horde", "(Twisted Tokyo version)"),
    "3ba": ("Yomi Army", "Horde", "(Twisted Tokyo version)"),
    "3bb": ("Frosts", "Horde", "(Twisted Tokyo version)"),
    "3bc": ("Defiant Horde", "Horde", "(Twisted Tokyo version)"),
    "3bd": ("Demon Horde", "Horde", "(Twisted Tokyo version)"),
    "3be": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3bf": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3c0": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3c1": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3c2": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3c3": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3c4": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3c5": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3c6": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3c7": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3c8": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3c9": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3ca": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "3cb": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "3cc": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "3cd": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "3ce": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "3cf": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "3d0": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "3d1": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "3d2": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "3d3": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "3d4": ("Formorian", "Night", "(Tir Na Nog version)"),
    "3d5": ("Mother Harlot", "Fiend", "(Boss version)"),
    "3d6": ("Trumpeter", "Fiend", "(Boss version)"),
    "3d7": ("Pale Rider", "Fiend", "(Boss version)"),
    "3d8": ("Black Rider", "Fiend", "(Boss version)"),
    "3d9": ("Red Rider", "Fiend", "(Boss version)"),
    "3da": ("White Rider", "Fiend", "(Boss version)"),
    "3db": ("Not Used", "Fiend", "(?) (Entire portrait is solid white) (Null: Dark, Resist: Light) (Probably used to be Chemtrail)"),
    "3dc": ("Matador", "Fiend", "(Boss version)"),
    "3dd": ("David", "Fiend", "(Boss version)"),
    "3de": ("Not Used", "Tree", "(?)"),
    "3df": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e0": ("Lucifer", "Tyrant", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e1": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e2": ("Merkabah", "Herald", "(?) (Unused leftover from SMTIV, guest ally version?)"),
    "3e3": ("Adramelech", "Fallen", "(Shesha fight ally)"),
    "3e4": ("Archangel", "Divine", "(Shesha fight ally)"),
    "3e5": ("Principality", "Divine", "(Boss version)"),
    "3e6": ("Ose", "Fallen", "(Boss version)"),
    "3e7": ("Fortuna", "Megami", "(Boss version)"),
    "3e8": ("Not Used", "Tree", "(?)"),
    "3e9": ("Ippon-Datara", "Jaki", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ea": ("Horkos", "Tyrant", "(Godslayer Training version)"),
    "3eb": ("Dionysus", "Zealot", "(Godslayer Training version)"),
    "3ec": ("Anubis", "Avatar", "(Godslayer Training version)"),
    "3ed": ("Demonee-ho", "Fairy", "(Godslayer Training version)"),
    "3ee": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3ef": ("Raiju", "Wilder", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f0": ("Toubyou", "Drake", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f1": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f2": ("Jack Frost", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f3": ("Jack the Ripper", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f4": ("Demonee-ho", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f5": ("Demonstrators", "Horde", ""),
    "3f6": ("Lanling Wang", "Famed", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f7": ("Pyro Jack", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "3f8": ("Asahi", "Human", ""),
    "3f9": ("Navarre", "Ghost", ""),
    "3fa": ("Nozomi", "Human", ""),
    "3fb": ("Parvati", "Megami", "(Asahi's?)"),
    "3fc": ("Stonka", "Beast", ""),
    "3fd": ("Navarre", "Ghost", ""),
    "3fe": ("Mushussu", "Drake", ""),
    "3ff": ("Sarasvati", "Nymph", "(Asahi's?)"),
    "400": ("Navarre", "Ghost", ""),
    "401": ("Master Therion", "Yoma", "(Godslayer Training version)"),
    "402": ("Aramisaki", "Zealot", "(Godslayer Training version)"),
    "403": ("Ometeotl", "Deity", "(Godslayer Training version)"),
    "404": ("Huoniao", "Raptor", "(Godslayer Training version)"),
    "405": ("Long", "Dragon", "(Godslayer Training version)"),
    "406": ("Ym", "Drake", "(Godslayer Training version)"),
    "407": ("Gaston", "Samurai", ""),
    "408": ("", "Surt", "(Godslayer Training version)"),
    "409": ("Hachiman", "Deity", "(Godslayer Training version)"),
    "40a": ("Vasuki", "Drake", "(Godslayer Training version)"),
    "40b": ("Yaksha", "Brute", "(Godslayer Training version)"),
    "40c": ("Mara", "Tyrant", "(Godslayer Training version)"),
    "40d": ("Botis", "Fallen", "(Godslayer Training version)"),
    "40e": ("Oberon", "Fairy", "(Godslayer Training version)"),
    "40f": ("Cherub", "Divine", "(Godslayer Training version)"),
    "410": ("Zhong Kui", "Kishin", "(?) (Unused SMTIV Training Battle leftover)"),
    "411": ("Nata Taishi", "Genma", "(?) (Unused SMTIV Training Battle leftover)"),
    "412": ("Samyaza", "Tyrant", "(?) (Unused SMTIV Training Battle leftover)"),
    "413": ("Dakini", "Femme", "(?) (Unused SMTIV Training Battle leftover)"),
    "414": ("Nadja", "Fairy", "(?) (Unused SMTIV Training Battle leftover)"),
    "415": ("Kushinada-hime", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "416": ("Principality", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "417": ("Power", "Divine", "(?) (Unused SMTIV Training Battle leftover)"),
    "418": ("Momunofu", "Brute", "(?) (Unused SMTIV Training Battle leftover)"),
    "419": ("Okuninushi", "Kunitsu", "(?) (Unused SMTIV Training Battle leftover)"),
    "41a": ("Mad Gasser", "Foul", "(?) (Unused SMTIV Training Battle leftover)"),
    "41b": ("Krishna", "Tyrant", "(Test demon?)"),
    "41c": ("Odin", "King", ""),
    "41d": ("Maitreya", "Cyber", ""),
    "41e": ("Chironnupu", "Archaic", ""),
    "41f": ("Shesha 1st Form", "Archaic", ""),
    "420": ("Inanna Remnant", "Archaic", ""),
    "421": ("Shesha 2nd Form", "Archaic", ""),
    "422": ("Krishna", "Herald", "(Actually Gaston with Gungnir)"),
    "423": ("Merkabah", "Tree", "(Cutscene-related stuff below. Character sprites that appear briefly during battles have to be saved as demons, I guess.)"),
    "424": ("Lucifer", "Tree", ""),
    "425": ("Inanna", "Tree", ""),
    "426": ("Mitra-Buddha", "Tree", "(Portrait shows Inanna, but sprite shows Mitra-Buddha)"),
    "427": ("Dagda", "Tree", "(Portrait shows Mitra-Buddha, sprite shows Dagda)"),
    "428": ("Vishnu-Flynn 1", "Tree", "(Portrait is Dagda, sprite is Vishnu-Flynn)"),
    "429": ("YHVH 1", "Tree", "(Portrait is Vishnu-Flynn, sprite is...Frost Ace)"),
    "42a": ("YHVH 2", "Tree", ""),
    "42b": ("Vishnu-Flynn 2", "Tree", ""),
    "42c": ("Nanashi", "Tree", "(No art, not even a question mark)"),
    "42d": ("Binding Field", "Tree", "(Sprite is the purple field surrounding Flynn when he's crucified)"),
    "42e": ("Crucified Flynn", "Tree", ""),
    "42f": ("Danu", "Tree", ""),
    "430": ("St. Germain Hole", "Tree", ""),
    "431": ("Pillar of Light", "Tree", ""),
    "432": ("Lucifer", "Tree", "(2nd Form Normal) (Sprite is Asahi as your Goddess. Seems like they replaced stuff from SMTIV without actually changing the names.)"),
    "433": ("Michael", "Tree", "(Giant) (Goddess Navarre)"),
    "434": ("Gabriel", "Tree", "(Giant) (Goddess Nozomi)"),
    "435": ("Raphael", "Tree", "(Giant) (Goddess Gaston)"),
    "436": ("Uriel", "Tree", "(Giant) (Goddess Hallelujah)"),
    "437": ("Masakado", "Tree", "(Giant) (Goddess Toki)"),
    "438": ("Charon", "Tree", "(Event) (Goddess Isabeau)"),
    "439": ("Asterius", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43a": ("Aeshma", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43b": ("Ancient of Days", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43c": ("Sanat", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43d": ("Lucifer Hikaru", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43e": ("Silhouette Lucif", "Tree", "(?) (Unused leftover from SMTIV)"),
    "43f": ("Trial Cyber", "Tree", "(?)"),
    "440": ("Trial Cyber", "Tree", "(?)"),
    "441": ("Trial Cyber", "Tree", "(?)"),
    "442": ("Trial Cyber", "Tree", "(?)"),
    "443": ("Trial Cyber", "Tree", "(?)"),
    "444": ("Trial Cyber", "Tree", "(?)"),
    "445": ("Trial Cyber", "Tree", "(?)"),
    "446": ("Trial Cyber", "Tree", "(?)"),
    "447": ("Trial Cyber", "Tree", "(?)"),
    "448": ("Trial Cyber", "Tree", "(?)"),
    "449": ("Mii", "Tree", ""),
    "44a": ("Kei", "Tree", ""),
    "44b": ("Warp Hole", "Tree", ""),
    "44c": ("Trial Cyber", "Tree", "(?)"),
    "44d": ("Egyptian Horde", "Horde", "(Enemy-only)"),
    "44e": ("Demonic Samurai", "???", "(Enemy-only)"),
    "44f": ("Demonic Hope", "???", "(Enemy-only)"),
    "450": ("Demonic Hugo", "???", "(Enemy-only)"),
    "451": ("A. Law Horde", "Horde", "(Enemy-only)"),
    "452": ("A. Chaos Horde", "Horde", "(Enemy-only)"),
    "453": ("En no Ozuno", "Fiend", "(Enemy-only)"),
    "454": ("Cleopatra", "Megami", "(Boss version)"),
    "455": ("Mephisto", "Tyrant", "(Boss version)"),
    "456": ("Stephen", "Meta", "(Sitting) (Enemy-only)"),
    "457": ("Stephen", "Meta", "(Standing) (Enemy-only)"),
    "458": ("A. Neutral Horde", "Horde", "(Enemy-only)"),
    "459": ("Ara Mitama", "Mitama", "(Enemy-only)"),
    "45a": ("Nigi Mitama", "Mitama", "(Enemy-only)"),
    "45b": ("Kushi Mitama", "Mitama", "(Enemy-only)"),
    "45c": ("Saki Mitama", "Mitama", "(Enemy-only)"),
    "45d": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "45e": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "45f": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "460": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "461": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "462": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "463": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "464": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "465": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "466": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "467": ("Formorian", "Night", "(Tir Na Nog version)"),
    "468": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "469": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "46a": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "46b": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "46c": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "46d": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "46e": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "46f": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "470": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "471": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "472": ("Formorian", "Night", "(Tir Na Nog version)"),
    "473": ("Dormarth", "Beast", "(Tir Na Nog version)"),
    "474": ("Setanta", "Fairy", "(Tir Na Nog version)"),
    "475": ("Wicker Man", "Spirit", "(Tir Na Nog version)"),
    "476": ("Skadi", "Lady", "(Tir Na Nog version)"),
    "477": ("Scathach", "Megami", "(Tir Na Nog version)"),
    "478": ("Brigid", "Megami", "(Tir Na Nog version)"),
    "479": ("Balor", "Tyrant", "(Tir Na Nog version)"),
    "47a": ("Cu Chulainn", "Genma", "(Tir Na Nog version)"),
    "47b": ("Queen Mab", "Night", "(Tir Na Nog version)"),
    "47c": ("Cernunnos", "Reaper", "(Tir Na Nog version)"),
    "47d": ("Trial Cyber", "Tree", "(?)"),
    "47e": ("Trial:Single:Sword", "Tree", "(These are all Mitamas with different attack animations for testing purposes)"),
    "47f": ("Trial:Single:Scimitar", "Tree", ""),
    "480": ("Trial:Single:Spear", "Tree", ""),
    "481": ("Trial:Single:Blunt", "Tree", ""),
    "482": ("Trial:Single:Fist", "Tree", ""),
    "483": ("Trial:Single:Scratch", "Tree", ""),
    "484": ("Trial:Single:Bite", "Tree", ""),
    "485": ("Trial:Single:Gun", "Tree", ""),
    "486": ("Trial:Single:Heavy", "Tree", ""),
    "487": ("Trial:Single:Rifle", "Tree", ""),
    "488": ("Trial:Single:Machinga", "Tree", ""),
    "489": ("Trial:Single:Sword", "Tree", ""),
    "48a": ("Trial:Single:Scimitar", "Tree", ""),
    "48b": ("Trial:Single:Spear", "Tree", ""),
    "48c": ("Trial:Single:Blunt", "Tree", ""),
    "48d": ("Trial:Single:Fist", "Tree", ""),
    "48e": ("Trial:Single:Scratch", "Tree", ""),
    "48f": ("Trial:Single:Bite", "Tree", ""),
    "490": ("Trial:Single:Gun", "Tree", ""),
    "491": ("Trial:Single:Heavy", "Tree", ""),
    "492": ("Trial:Single:Rifle", "Tree", ""),
    "493": ("Erthys", "Element", "(Diamond Realm version)"),
    "494": ("Aeros", "Element", "(Diamond Realm version)"),
    "495": ("Aquans", "Element", "(Diamond Realm version)"),
    "496": ("Flaemis", "Element", "(Diamond Realm version)"),
    "497": ("Demonic Citizens", "???", "(Enemy-only)"),
    "498": ("Demonic Citizens", "???", "(Enemy-only)"),
    "499": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49a": ("Demonic Citizens", "???", "(Enemy-only)"),
    "49b": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49c": ("Demonic Horde", "Horde", "(Enemy-only)"),
    "49d": ("The Hero", "Human", ""),
    "49e": ("Aleph", "Replicant", ""),
    "49f": ("Demi-fiend", "Chaos", ""),
    "4a0": ("Flynn", "Human", "(Stephen Fight)"),
}


class Save:
    # Class to represent an opened SMTIVA save.

    def __init__(self, filename):
        self._data = self.loadFileHex(filename)

    def loadFileHex(self, filename):
        # Returns the bytearray of a user-given file.
        try: 
            fh = open(filename, "rb")
        except:
            byte_arr = None
        else:
            byte_arr = bytearray(fh.read())
            fh.close()
        return byte_arr

    def uploadFile(self, filename):
        # uploads Save's data to a given file.

        with open(filename, "wb") as fh:
            fh.write(self._data)
            fh.close()

    def loadSave(self, filename):
        self._data = self.loadFileHex(filename)

    def saveDe(self, filename, slot):
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)
        
        demon = self._data[address : address+int(DE_SIZE, 16)]

        with open(filename, "wb") as fh:
            fh.write(demon)
            fh.close()

    def loadDe(self, de_filename, slot):
        # Loads a file containing a demon, and replaces the demon in "slot" with that demon.

        try:
            de_arr = self.loadFileHex(de_filename)
        except:
            print("Error loading Demon File")

        demon_str = self.getHexStr(de_arr, "0x0", int(DE_SIZE, 16))

        address = hex(int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1))
        self.writeHexBytes(self._data, demon_str, address, int(DE_SIZE, 16))

    def getDemonList(self):
        demons = []
        i = 0
        while i < DE_NUM_MAX:
            
            address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * i
            demonId = self.getHexStr(self._data, address, DE_ID[1], int(DE_ID[0], 16), True), 16
            try:
                demonName = ALL_DEMONS[demonId[0]]
            except:
                demonName = "NULL"

            demons.append(f"{demonName[0]}")

            i += 1
        
        demons += f"0. exit"

        return demons

    def mcStr(self):
        # Returns a string containing all of the MC's stats and skills.
        level_int = int(self.getHexStr(self._data, MC_LVL[0], MC_LVL[1]), 16)
        max_hp_int = int(self.getHexStr(self._data, MC_MAX_HP[0], MC_MAX_HP[1]), 16)
        max_mp_int = int(self.getHexStr(self._data, MC_MAX_MP[0], MC_MAX_MP[1]), 16)
        curr_hp_int = int(self.getHexStr(self._data, MC_CURR_HP[0], MC_CURR_HP[1]), 16)
        curr_mp_int = int(self.getHexStr(self._data, MC_CURR_MP[0], MC_CURR_MP[1]), 16)

        stats = []
        i = 0
        while (i < 5):
            stats.append(int(self.getHexStr(self._data, int(MC_STAT2[0], 16), MC_STAT2[1], i * 2, True), 16))
            i += 1
        
        skills = []
        i = 0
        while (i < 8):
            skill_id = self.getHexStr(self._data, int(MC_SKILL[0], 16), MC_SKILL[1], i * 2, True)
            while len(skill_id) < 4:
                skill_id = "0" + skill_id

            skills.append(ALL_SKILLS[skill_id.upper()])
            i += 1

        output = "Main Character: \n"
        output += f"Level: {level_int} - HP: {max_hp_int}/{curr_hp_int} - MP: {max_mp_int}/{curr_mp_int}\n"
        output += f"Strength: {stats[0]} - Dexterity: {stats[1]} - Magic: {stats[2]} - Agility: {stats[3]} - Luck: {stats[4]}\n"
        output += f"Skills: {skills[0]}, {skills[1]}, {skills[2]}, {skills[3]}, {skills[4]}, {skills[5]}, {skills[6]}, {skills[7]}"

        return output

    def deStr(self, slot):
        # Returns a string representation of a demon's stats.

        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)

        demonId = self.getHexStr(self._data, address, 2, int(DE_ID[0], 16), True), 16
        name = ALL_DEMONS[demonId[0]]

        # For 1st Tab (Main Character)
        level_int = int(self.getHexStr(self._data, address, DE_LVL[1], int(DE_LVL[0], 16), True), 16)
        max_hp_int = int(self.getHexStr(self._data, address, DE_MAX_HP[1], int(DE_MAX_HP[0], 16), True), 16)
        max_mp_int = int(self.getHexStr(self._data, address, DE_MAX_MP[1], int(DE_MAX_MP[0], 16), True), 16)
        curr_hp_int = int(self.getHexStr(self._data, address, DE_CURR_HP[1], int(DE_CURR_HP[0], 16), True), 16)
        curr_mp_int = int(self.getHexStr(self._data, address, DE_CURR_MP[1], int(DE_CURR_MP[0], 16), True), 16)

        stats = []
        i = 0
        while (i < 5):
            stats.append(int(self.getHexStr(self._data, address, DE_STAT2[1], int(DE_STAT2[0], 16) + i*2, True), 16))
            i += 1
        
        skills = []
        i = 0
        while (i < 8):
            skill_id = self.getHexStr(self._data, address, DE_SKILL[1], int(DE_SKILL[0], 16) + i * 2, True)
            while len(skill_id) < 4:
                skill_id = "0" + skill_id

            skills.append(ALL_SKILLS[skill_id.upper()])
            i += 1

        output = ""
        output += f"{name[0]} - {name[1]}\n"
        output += f"Level: {level_int} - HP: {curr_hp_int}/{max_hp_int} - MP: {curr_mp_int}/{max_mp_int}\n"
        output += f"Strength: {stats[0]} - Dexterity: {stats[1]} - Magic: {stats[2]} - Agility: {stats[3]} - Luck: {stats[4]}\n"
        output += f"Skills: {skills[0]}, {skills[1]}, {skills[2]}, {skills[3]}, {skills[4]}, {skills[5]}, {skills[6]}, {skills[7]}"

        return output

    def deListStr(self):
        # Returns a formatted string listing all the demons in the save's stock.
        demons = self.getDemonList()
        row = 0
        max_row = 4
        max_col = 6
        empty_line = ("+" + "-" * 20) * max_col + "+\n"
        output = empty_line
        while row < max_row:
            col = 0
            while col < max_col:
                index = col + row * max_col
                output = output + f"|{index+1: ^2}. {demons[index]: ^16}"
                col += 1
            output = output + "|\n" + empty_line
            row += 1
        return output

    def etcStr(self):
        # Returns Miscellanious Data on the save (Macca and App Points)
        macca = int(self.getHexStr(self._data, MISC_MACCA[0], MISC_MACCA[1]), 16)
        app_pts = int(self.getHexStr(self._data, MISC_APP_PTS[0], MISC_APP_PTS[1]), 16)

        return f"Macca: {macca} - App Points: {app_pts}"

    def writeMcLvl(self, value):
        # Changes the Level of the demon at "slot" to match "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, MC_LVL[0], MC_LVL[1])

    def writeMcHp(self, value):
        # Changes the HP of the demon at "slot" to match "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, MC_MAX_HP[0], MC_MAX_HP[1])
        self.writeHexBytes(self._data, value, MC_CURR_HP[0], MC_CURR_HP[1])

    def writeMcMp(self, value):
        # Changes the MP of the demon at "slot" to match "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, MC_MAX_MP[0], MC_MAX_MP[1])
        self.writeHexBytes(self._data, value, MC_CURR_MP[0], MC_CURR_MP[1])

    def writeMcStat(self, value, stat):
        # Changes the a selected stat of the demon to be equal to "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, int(MC_STAT1[0], 16) + (stat-1) * MC_STAT1[1], MC_STAT1[1], None, True)
        self.writeHexBytes(self._data, value, int(MC_STAT2[0], 16) + (stat-1) * MC_STAT2[1], MC_STAT2[1], None, True)

    def writeMcSkill(self, code, skill):
        self.writeHexBytes(self._data, code, int(MC_SKILL[0], 16) + (skill-1) * MC_SKILL[1], DE_SKILL[1], None, True)

    def swapMcSkill(self, skill1, skill2):
        self.swapHexBytes(self._data, int(MC_SKILL[0], 16) + MC_SKILL[1] * (skill1-1), int(MC_SKILL[0], 16) + MC_SKILL[1] * (skill2-1), DE_SKILL[1], True)


    def writeDeId(self, slot, code):
        # Changes the ID of the demon at "slot" to match "value"
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)
        self.writeHexBytes(self._data, code, address, DE_ID[1], int(DE_ID[0], 16), True)

    def writeDeLvl(self, slot, value):
        # Changes the Level of the demon at "slot" to match "value"
        value = hex(value)[2:]
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)
        self.writeHexBytes(self._data, value, address, DE_LVL[1], int(DE_LVL[0], 16), True)

    def writeDeHp(self, slot, value):
        # Changes the HP of the demon at "slot" to match "value"
        value = hex(value)[2:]
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)
        self.writeHexBytes(self._data, value, address, DE_MAX_HP[1], int(DE_MAX_HP[0], 16), True)
        self.writeHexBytes(self._data, value, address, DE_CURR_HP[1], int(DE_CURR_HP[0], 16), True)

    def writeDeMp(self, slot, value):
        # Changes the MP of the demon at "slot" to match "value"
        value = hex(value)[2:]
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1)
        self.writeHexBytes(self._data, value, address, DE_MAX_MP[1], int(DE_MAX_MP[0], 16), True)
        self.writeHexBytes(self._data, value, address, DE_CURR_MP[1], int(DE_CURR_MP[0], 16), True)

    def writeDeStat(self, slot, value, stat):
        # Changes the a selected stat of the demon to be equal to "value"
        value = hex(value)[2:]
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1) + DE_STAT1[1] * (stat - 1)
        self.writeHexBytes(self._data, value, address, DE_STAT1[1], int(DE_STAT1[0], 16), True)
        self.writeHexBytes(self._data, value, address, DE_STAT2[1], int(DE_STAT2[0], 16), True)

    def writeDeSkill(self, slot, code, skill):
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1) + DE_SKILL[1] * (skill - 1)
        self.writeHexBytes(self._data, code, address, DE_SKILL[1], int(DE_SKILL[0], 16), True)

    def swapDeSkill(self, slot, skill1, skill2):
        address = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (slot - 1) + int(DE_SKILL[0], 16)
        self.swapHexBytes(self._data, address + DE_SKILL[1] * (skill1-1), address + DE_SKILL[1] * (skill2-1), DE_SKILL[1], True)

    def swapDeSlot(self, demon1, demon2):
        address1 = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (demon1 - 1)
        address2 = int(DE_START, 16) + int(DE_NEXT_OFFSET, 16) * (demon2 - 1)
        self.swapHexBytes(self._data, address1, address2, int(DE_SIZE, 16), True)

    def writeMacca(self, value):
        # Changes the loaded save's data to match "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, MISC_MACCA[0], MISC_MACCA[1])

    def writeApp(self, value):
        # Changes the loaded save's data to match "value"
        value = hex(value)[2:]
        self.writeHexBytes(self._data, value, MISC_APP_PTS[0], MISC_APP_PTS[1])

    def getHexStr(self, byte_arr, start_add, num_bytes, skip_bytes = None, add_is_dec = False):
        # Returns a String representation of target addresses in byte_arr
        # byte_arr is the target byte array.
        # start_add is the address where the reading starts.
        # num_bytes is how many bytes are being counted.
        # skip_bytes adds to the starting address (Why? I don't know, I took this off the internet.)
        # if add_is_dec is true, start_add is treated as a decimal form integer.
        hex_str = ""

        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)

        if skip_bytes:
            curr_add += skip_bytes

        while num_bytes > 0:
            hex_str = format(byte_arr[curr_add], '02x') + hex_str
            num_bytes -= 1
            curr_add += 1

        hex_str = hex_str.lstrip("0")

        return hex_str if hex_str else "0"

    def writeHexBytes(self, byte_arr, hex_str, start_add, num_bytes, skip_bytes = None, add_is_dec = False):
        # Writes bytes into byte_arr based on hex_str's contents.
        # byte_arr is the target byte array.
        # hex_str is the string being loaded into
        # start_add is the first address being written on
        # skip_bytes adds to the starting address (Why? I don't know, I took this off the internet.)
        # if add_is_dec is true, start_add is treated as a decimal form integer.
        hex_str = hex_str.zfill(num_bytes * 2)
        hex_bytes = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        hex_bytes.reverse()
        if add_is_dec:
            curr_add = start_add
        else:
            curr_add = int(start_add, 16)
        if skip_bytes:
            curr_add += skip_bytes
        for val in hex_bytes:
            byte_arr[curr_add] = int(val, 16)
            curr_add += 1

    def swapHexBytes(self, byte_arr, addr_1, addr_2, num_bytes, dec = False):
        # Swaps bytes in byte_arr at addr_1 and addr_2
        # byte_arr is the array being adjusted
        # addr_1 is the first address
        # addr_2 is the second address
        # numbytes is the bytes being changed
        # if dec is true then treat the addresses as decimal form, otherwise treat addresses as hex values.
        if dec:
            curr_addr1 = addr_1
            curr_addr2 = addr_2
        else:
            curr_addr1 = int(addr_1, 16)
            curr_addr2 = int(addr_2, 16)

        while num_bytes > 0:
            swapper = byte_arr[curr_addr1]
            byte_arr[curr_addr1] = byte_arr[curr_addr2]
            byte_arr[curr_addr2] = swapper

            curr_addr1 += 1
            curr_addr2 += 1
            num_bytes -= 1

    def loaded(self):
        #Returns True if save data is loaded into self._data, otherwise return False
        if self._data is None:
            return False
        else:
            return True

    def __str__(self):
        # Returns a string representation of data in the savefile.
        if self._data == None:
            return None
        output = ""

        output += self.mcStr() + '\n'
        output += self.deListStr()
        output += self.etcStr()
        
        return output
