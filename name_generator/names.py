"""
Random Name Library
"""

### Fantasy Names ###
male_fantasy_names = [
    ['Bhezam','Usur','Nergork','Nhekhir','Nhedem','Varstag','Nengork','Edrel',
        'En','Strugnor','Van','Jidur-Zis','Heun-Zis','Brinzauzid','Dreslad',
        'Cha','Low','Hebueri','Fronol','Jehmum','Nhubad','Golvol','Hugreg',], # Human
    ['Cornaith','Ehrendil','Castien','Ayas','Nevarth','Ayred','Eldaerenth',
        'Rychell','Khatar','Ellisar','Sundamar','Khuumal','Hagwin','Althidon',
        'Kymil','Andrathath','Luirlan','Venali','Gormar','Venali','Felaern',
        'Entrydal','Haladavar',], # Elf
    ['Grooghid','Maldrin','Thokorlun','Skastarlig','Jarbem','Nosan','Arakhoum',
        'Whurrouc','Jarfatin','Morfem','Stromrit','Toresil','Grootrorlun',
        'Vothotum','Kindrolin','Gitmeck','Strotorli','Dalorli','Grurdam',
        'Sakgromi','Groutharlum','Khouzzumri','Khoulgouc',], # Dwarf
]

female_fantasy_names = [
    ['Jutihneih','Ahlal','Shirierloh','Hasnosnih','Umuh','Jhaillolseh','Tisvi',
        'Chirmel','Rel','Lemifna','Baga','Sephofre','Suthi','Zirriru','Dafith',
        'Bai','Jia','Lendrb','Endrs','Jiveinal','Heiruh','Caressan','Shorvi',], # Human
    ['Uneathen','Lethhonel','Nephinae','Ildilyntra','Penelo','Nyana','Chalia',
        'Hycis','Siphanien','Ilyrana','Tialha','Vasati','Leilatha','Muelara',
        'Lensa','Isarrel','Ava','Axilya','Sionia','Tisha','Lyndis','Ilsevel',
        'Sorisana',], # Elf
    ['Haghire','Alfowabena','Lofraetaine','Darekhoulin','Kanalin','Noratdraenelyn',
        'Thratheathra','Udroure','Hekaewynn','Grorgrotalin','Snakitain',
        'Thenealin','Reisgrekara','Norargruli','Folmear','Karbek','Nusgreck',
        'Groogromi','Krorsaen','Dafen','Ruddouck','Daloggon','Rusgrouc',], # Dwarf
]

#Still needs work once the above is all set
all_human_names = male_fantasy_names[0] + female_fantasy_names[0]
all_elf_names = male_fantasy_names[1] + female_fantasy_names[1]
all_dwarf_names = male_fantasy_names[2] + female_fantasy_names[2]

fantasy_surnames = [
    ['Hanor','Rheissa','Dayblood','Jastod','Juhlo','Swifthunter','Khuhum',
        'Bhodeil','Willowvalor','Springstriker','Datsk','Sukniv','Dirgebrooke',
        'Redmaul','Mindalahk','Zehpahk','Vreldenzagu','Dyatreki','Liaong','Wuey',
        'Gosqelda','Fasinzon','Sheissur','Bhohom','Wildcutter','Cinderfall',], # Human
    ['Yllatumal','Holafir','Fardan','Adcan','Quibella','Orilamin','Vaydark',
        'Wranbella','Fenrona','Carneiros','Faekrana','Sharora','Wynren','Magdi',
        'Roris','Vallynn','Keyceran','Reydan','Brylen','Yelberos','Jonala',
        'Yllamaris','Olocan','Vennelis','Yelberos','Naehice',], # Elf
    ['Redhorn','Caskchest','Honorspine','Nobledelver','Chaosfinger',
        'Giantmantle','Ingotbrew','Flintmace','Woldchin','Flintfall',
        'Brownshaper','Noblesword','Hornview','Oakclock','Ironmail','Flackhead',
        'Mountainshoulder','Shatterbrow','Barrelguard','Boneshaper',
        'Koboldarmour','Alestone','Irondelver','Leadbreaker','Silverblade',], # Dwarf
]


### Sci-Fi Names ###
scifi_names = [
    ['Ximon','Zandr','Blayse','Yahr','Abrahan','Drayk','Maxwill','Jenzen',
        'Nathn','Xan','Jaeden','Ragan','Julyen','Matzen','Luekas','Jenzen',
        'Pabl','Matzen','Maerlon','Corly',], # Male Human
    ['Emesyn','Saevi','Alaena','Emson','Zarilah','Avaeana','Haennah','Carline',
        'Evanline','Krissa','Julith','Nadira','Catalea','Cathrise','Maesin',
        'Baely','Britella','Roseya','Desree','Abrielle',], # Female Human
    ["Drads","Drirgeoks","Qun",'Crinquix','Zevo','Barzeds',"Dul'oh",'Eeriex',
        'Heli','Traenphiell','Tods',"Cav'eks",'Goscied','Grix',"Dih'id",'Uphe',
        'Edids','Cenzae','Kugneds','Struzad','Qhenkex','Trauqreks',"Ur'ein",
        'Drocciels','Algeat','Oni','Ranid','Thradda','Thraarraell',"Kaar'ids",
        'Erkeks',"Crax'uin",'Elqak','Vrinzans','Algrell','Ahnaell','Dhelgai',
        'Daengro','Ruzads','Bodi',], # Alien
    ['Highpowered Excretion Drone (H.E.D.)','Prime Instruction Prototype (P.I.P.)',
        'Independent Assassination Droid','Primary Piloting Cyborg','Ranger',
        'Cyd','Scythe','Cybel','Osig','Iyil',
        'Sensitive Oceanic Navigation Automaton (S.O.N.A.)',
        'Self-Sufficient Pilot Technology','Secondary Human Control Device',
        'Bionic First Aid Android','Andromeda','Led','Test','Crowby','Oh',
        'Ilitron','Programmed Excevation Automaton (P.E.A.)',
        'Automated Guidance Emulator','Automatic Observer Drone',
        'Automatic Evacuation Bot','Axel','Gearz','Rubber','Sparkle','Iwixx',
        'Ejx','Motorized Exploration Machine','Motorized Servant Juggernaut',
        'Digital Translation Device','General Neutralization Golem','Rubber',
        'Terra','Boomer','Cole','Obnroid','Uwlroid',], #Robot
]
