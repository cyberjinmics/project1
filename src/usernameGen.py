#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
import random
import string


min_length = 3


def usernameGen(length, add_adjective):
    if length < min_length:
        length = min_length
    adjectives = [
        "5_Speed", "Easy_Drive", "Highgility", "Scientific", "6_Speed", "Economical", "Hybrid", "Sleek",
        "Acclaimed", "Effective", "Innovative", "Fasthorse", "Advanced", "Electric", "Legendary", "Speedy",
        "Affordable", "Elegant", "Limitless", "Sporty", "Agile", "Engineered", "Low_emission", "Standard",
        "All_wheels", "Enhanced", "Luxurious", "Stylish", "Astonishing", "Luxury", "Top_dollar", "Automatic",
        "Ergonomic", "Low_dollar", "Top_level", "Automotive", "Cheapies", "Tuned", "Beyond_Compare", "Extreme",
        "Exotic", "Ultimate", "Classic", "Noteworthy", "Ultraspeed", "Crash_tested", "Fast_wheels", "Carformance",
        "Unparalled", "Custom_built", "Fastrack", "Drivepoint", "Custom_designed", "Four_wheels", "Powerful",
        "Versatile", "Customized", "Front_wheel", "Progressive", "Vintage", "Distinctive", "Fuel_efficient",
        "Quick_shifting", "Drivetrain", "Ready_to_cruise", "Drivel", "Functional", "Reinforced"
    ]
    names = [
        'Aarin', 'Aarinade', 'Aarinola', 'Abayomi', 'Abejide', 'Abidemi', 'Abidoye', 'Abiodun', 'Abiona', 'Abisogun',
        'Abisuga', 'Abodunrin', 'Adaramola', 'Adebajo', 'Adebambo', 'Adebanjo', 'Adebanke', 'Adebankole', 'Adebayo',
        'Adebimpe',
        'Adebisi', 'Adebiyi', 'Adebola', 'Adeboro', 'Adebowale', 'Adeboye', 'Adeboyejo', 'Adebukola', 'Adebusoye',
        'Adedamola',
        'Adedapo', 'Adedaramola', 'Adedayo', 'Adedeji', 'Adediji', 'Adediran', 'Adedoja', 'Adedokun', 'Adedolapo',
        'Adedotun',
        'Adedoyin', 'Adefemi', 'Adefolake', 'Adefolarin', 'Adefoluke', 'Adefoyeke', 'Adegbenga', 'Adegbenro',
        'Adegbola', 'Adegboyega',
        'Adegoke', 'Adegunte', 'Adeiye', 'Adejare', 'Adejobi', 'Adejoke', 'Adejoro', 'Adejumo', 'Adejumobi',
        'Adejumoke',
        'Adejuwon', 'Adekanmi', 'Adekemi', 'Adekilekun', 'Adekitan', 'Adekola', 'Adekoyejo', 'Adekunle', 'Adelabi',
        'Adelana',
        'Adelani', 'Adelanwa', 'Adeleke', 'Adelodun', 'Adelowo', 'Adeloye', 'Ademola', 'Ademolu', 'Adeniji', 'Adenike',
        'Adeniran', 'Adeniyi', 'Adenola', 'Adenrele', 'Adenuga', 'Adeoba', 'Adeola', 'Adeolu', 'Adeoti', 'Adeoye',
        'Adepeju', 'Adepero', 'Adepitan', 'Adepoju', 'Aderemilekun', 'Aderinsola', 'Aderiyike', 'Aderonke', 'Aderoju',
        'Aderopo',
        'Adesanmi', 'Adesewa', 'Adesile', 'Adesina', 'Adesoji', 'Adesokan', 'Adesola', 'Adesoro', 'Adesoye', 'Adesupo',
        'Adetola', 'Adetolu', 'Adetona', 'Adetoro', 'Adetoun', 'Adetoyebi', 'Adetoyese', 'Adetunji', 'Adetutu',
        'Adewale',
        'Adewetan', 'Adewonuola', 'Adewunmi', 'Adeyanju', 'Adeyato', 'Adeyemi', 'Adeyemo', 'Adeyiga', 'Adeyinka',
        'Adeyeye',
        'Adeyoye', 'Adunade', 'Adunbi', 'Adunke', 'Adunni', 'Adura', 'Aduramigba', 'Afolabi', 'Afolami', 'Afolarin',
        'Afolorunso', 'Agboola', 'Aibinuola', 'Ajibola', 'Ajibade', 'Ajibike', 'Ajirola', 'Akin', 'Akinbiyi',
        'Akinbode',
        'Akinbola', 'Akindele', 'Akinkunmi', 'Akinlabi', 'Akinleye', 'Akinlolu', 'Akinloye', 'Akinmade', 'Akinniyi',
        'Akinola',
        'Akinpelu', 'Akinrinnola', 'Akinsanmi', 'Akintayo', 'Akintola', 'Akintoye', 'Akintunde', 'Akinwunmi',
        'Akinyele', 'Akinyemi',
        'Akeju', 'Anjolaoluwa', 'Alaba', 'Alade', 'Alayo', 'Alarape', 'Aralola', 'Aramide', 'Araoye', 'Aremu',
        'Ariyo', 'Asikooluwaloju', 'Atinuke', 'Ayan', 'Ayanbadejo', 'Ayandele', 'Ayantola', 'Ayantuge', 'Ayanyinka',
        'Ayoade',
        'Ayobade', 'Ayobami', 'Ayodabo', 'Ayodele', 'Ayodiran', 'Ayoku', 'Ayokunle', 'Ayokunnumitetete', 'Ayoola',
        'Ayorinde',
        'Ayotomi', 'Ayotola', 'Ayotunde', 'Baba', 'Bababunmi', 'Babajide', 'Babalola', 'Babarinsa', 'Babasola',
        'Babatola',
        'Babatunde', 'Babatunji', 'Babawale', 'Babayeju', 'Badejoko', 'Bolajoko', 'Bolatito', 'Bolutife',
        'Botiwunoluwa', 'Dideolu',
        'Durodola', 'Durojaiye', 'Durosinmi', 'Ebudola', 'Ebunoluwa', 'Emiola', 'Enilo', 'Eniola', 'Enitan',
        'Eniolurunda',
        'Eniolorunopa', 'Enitanwa', 'Ekundayo', 'Ereola', 'Erioluwa', 'Etoade', 'Ewaoluwa', 'Eyiloreoluwa', 'Eyitola',
        'Faramade',
        'Fadekemi', 'Fadesewafunmi', 'Fehintiola', 'Feyifoluwa', 'Fijinoluwa', 'Fiyinfoluwa', 'Folagbade', 'Folashade',
        'Fowosade', 'Gbekelolu',
        'Gbadewole', 'Gbolagunte', 'Gbolahan', 'Gbowoade', 'Ibidokun', 'Ibidun', 'Ibijoke', 'Ibikeye', 'Ibikunle',
        'Ibilola',
        'Ibisola', 'Ibiyemi', 'Ibirinade', 'Ibiolagbajosi', 'Ibukunoluwa', 'Idowu', 'Idurotioluwa', 'Ifeade',
        'Ifedolapo', 'Ifejobi',
        'Ifeoluwakusi', 'Ifetayo', 'Igbagboluwa', 'Ikeolu', 'Ilesanmi', 'Imoleoluwa', 'Inioluwa', 'Ipadeola',
        'Ipinuoluwa', 'Iremide',
        'Iretiola', 'Iretioluwa', 'itanife', 'Iteoluwakiisi', 'Itunuoluwa', 'Iwalewa', 'Iyanda', 'Iyabo', 'Iyadunni',
        'Iyaniwura',
        'Iyatunde', 'Iyanuoluwa', 'Iyiola', 'Iyunadeoluwa', 'Jejelaiyegba', 'Jejeolaoluwa', 'Jenrola', 'Jokotade',
        'Jokotola', 'Kalejaye',
        'Kasimawo', 'Kikelomo', 'Kofoworade', 'Kokumo', 'Koledowo', 'Kosoko', 'Koyinsola', 'Kukoyi', 'Magbagbeoluwa',
        'Majekodunmi',
        'Majemuoluwa', 'Makanjuola', 'Malomo', 'Matanmi', 'Meraola', 'Mobiyina', 'Mobolaji', 'Modupe', 'Mofaderera',
        'Mofeoluwa',
        'Mofeyisade', 'Mofeyisola', 'Mofogofolorun', 'Mofolami', 'Mofopefolorun', 'Mogbadunola', 'Mogbolade',
        'Mojirayo', 'Mojirola', 'Mojisola',
        'Mojolaoluwa', 'Mojoyin', 'Mokolade', 'Molayo', 'Monilola', 'Mopelola', 'Moradeke', 'Moradeun', 'Moradeyo',
        'Morakinyo',
        'Morayo', 'Morenike', 'Morenikeji', 'Moriojurereoluwagba', 'Morohundiya', 'Morohunfola', 'Morohunfolu',
        'Morohunkolafun', 'Morohunmubo', 'Morolake',
        'Morolayo', 'Mosopefunolorun', 'Mosunmola', 'Motilewa', 'Motunrayo', 'Moyoade', 'Moyosoreoluwa', 'Obafemi',
        'Obasola', 'Obileye',
        'Odun', 'Odunayo', 'Oduntan', 'Ojuolape', 'Okanlanwon', 'Okiki', 'Okikiade', 'Okikiimole', 'Okikiola',
        'Olabamidele',
        'Olabanwo', 'Olabimtan', 'Olabisi', 'Olabode', 'Olabosipo', 'Olabukunola', 'Oladahunsi', 'Oladapo', 'Oladayo',
        'Oladega',
        'Oladejo', 'Oladele', 'Oladepo', 'Oladiji', 'Oladipupo', 'Oladiran', 'Oladitan', 'Oladokun', 'Oladotun',
        'Oladunjoye',
        'Oladunni', 'Oladurotoye', 'Olafimihan', 'Olagoke', 'Olagunjoye', 'Olagunte', 'Olaide', 'Olaitan', 'Olaiya',
        'Olajide',
        'Olajire', 'Olajumoke', 'Olakanmi', 'Olakitan', 'Olalekan', 'Olalere', 'Olamakinde', 'Olamide', 'Olamiji',
        'Olanifesi',
        'Olanipekun', 'Olaniyan', 'Olaniyi', 'Olanlesi', 'Olanrele', 'Olanrewaju', 'Olansile', 'Olaoluwa',
        'Olaosebikan', 'Olaoti',
        'Olaoye', 'Olapademi', 'Olapeju', 'Olapitan', 'Olasimbo', 'Olasubomi', 'Olasunmbo', 'Olasunkanmi', 'Olasupo',
        'Olatelemi',
        'Olatemina', 'Olateju', 'Olatidoye', 'Olatokunbo', 'Olatoun', 'Olatunbosun', 'Olatunji', 'Olawale', 'Olawuwo',
        'Olayemi',
        'Olayikanmi', 'Olayiwola', 'Olayinka', 'Olayonu', 'Ololade', 'Oluade', 'Olubajo', 'Olubamise', 'Olubanke',
        'Oluwabukola',
        'Olubukumi', 'Olubukunade', 'Oluwabunmi', 'Oluwabusayo', 'Oluwabusola', 'Oludahunsi', 'Oluwadairo',
        'Oluwadamilare', 'Oluwadamisi', 'Oluwadarasimi',
        'Oluwadayisi', 'Oludemilade', 'Oluwadetan', 'Oludolamu', 'Oludotun', 'Olufadeke', 'Olufela', 'Oluwafemi',
        'Olufeyikemi', 'Olufeyisayo',
        'Olufikunayo', 'Oluwafiresayo', 'Olufisayo', 'Olufolake', 'Olufolasade', 'Oluwafoyinsolami', 'Olufumiso',
        'Olufunke', 'Olufunmbi', 'Olufunmilade',
        'Olufunmilola', 'Oluwafunmilorinotun', 'Olufunto', 'Olugbayilo', 'Olugbemileke', 'Oluwagbeminiyi',
        'Oluwajomiloju', 'Olukayode', 'Oluwakemi', 'Olukolade',
        'Olukorede', 'Olukunmi', 'Olulaanu', 'Oluwaleti', 'Oluwalomose', 'Oluwalonike', 'Oluwalonimi', 'Olumayokun',
        'Olumayowa', 'Olumide',
        'Olumoyebo', 'Oluwanifemi', 'Oluwapamilerinayo', 'Oluranti', 'Oluropo', 'Oluwarotimi', 'Olusaanu', 'Olusanmi',
        'Olusanya', 'Olusayo',
        'Olusegun', 'Oluwasemilore', 'Oluwaseteminirere', 'Oluwaseun', 'Oluwaseunbabaralaiyemi', 'Oluwaseunayo',
        'Oluseye', 'Oluwaseyi', 'Olusoga', 'Olusoji',
        'Olusola', 'Oluwatemilorun', 'Oluwatimilehin', 'Oluwatisetan', 'Oluwatobi', 'Oluwatofunmi', 'Olutomilola',
        'Olutomiwa', 'Oluwatosin', 'Olutoyelo',
        'Oluwatoyosi', 'Olutumibi', 'Olutunde', 'Oluwawapelumi', 'Oluwemimo', 'Oluwole', 'Oluwayemisi', 'Oluyomi',
        'Omobayi', 'Omobolade',
        'Omobolaji', 'Omobolanle', 'Omobonike', 'Omoborode', 'Omodarani', 'Omodele', 'Omodunbi', 'Omodunni',
        'Omofolabo', 'Omojola',
        'Omokeyinwa', 'Omokeyede', 'Omokorede', 'Omolabake', 'Omolabi', 'Omolebi', 'Omolayo', 'Omolere', 'Omolewa',
        'Omoleye',
        'Omolola', 'Omololu', 'Omoloro', 'Omoloso', 'Omoluwabi', 'Omoniyi', 'Omoniyun', 'Omopariola', 'Omosalewa',
        'Omosunsola',
        'Omotade', 'Omotara', 'Omotayo', 'Omotoso', 'Omotunde', 'Omowafola', 'Omowon', 'Omowunmi', 'Omoyeni', 'Onifede',
        'Onipede', 'Oniyide', 'Opemipo', 'Opeoluwa', 'Opetunde', 'Opeyemi', 'Oreofe', 'Oreolu', 'Oriade', 'Oridola',
        'Orimolade', 'Oriola', 'Oromidayo', 'Otito', 'Otitoju', 'Otitoluwa', 'Owodunni', 'Owolabi', 'Owoseni',
        'Oyebode',
        'Oyebola', 'Oyebolujo', 'Oyedele', 'Oyediran', 'Oyegoke', 'Oyekanmi', 'Oyekunle', 'Oyelakin', 'Oyelowo',
        'Oyemade',
        'Oyenike', 'Oyeniran', 'Oyeniyi', 'Oyenola', 'Oyenuga', 'Oyerinde', 'Oyesanya', 'Oyesina', 'Oyeyemi', 'Oyeyipo',
        'Oyin', 'Oyindamola', 'Oyindasola', 'Oyinkansola', 'Popoola', 'Segilade', 'Segilola', 'Similolaoluwa',
        'Sijuade', 'Sijuwola',
        'Tanimola', 'Taraoluwa', 'Tejumade', 'Temidayo', 'Temilade', 'Temilayo', 'Temilolu', 'Temitayo', 'Temitope',
        'Tewogbola',
        'Tirenioluwa', 'Tinuade', 'Titilola', 'Titilayo', 'Tiwalade', 'Tiwalolu', 'Tiwatope', 'Tolulope', 'Tolulore',
        'Toluwalase',
        'Toluwani', 'Towobola', 'Wura', 'Wurade', 'Wuraola', 'Yejide', 'Yetunde', 'Yewande'
    ]
    alphabets = string.ascii_lowercase
    vowels = 'aeiou'
    consonants = "".join(set(alphabets) - set(vowels))
    username = random.choice(names)
    if add_adjective:
        adjective = "".join(sample(adjectives, 1))
        username = username+'_'+adjective+'.'
    else:
        username = username+'.'
    for i in range(length):
        if i % 2 == 0:
            username += random.choice(consonants)
        else:
            username += random.choice(vowels)
    return username