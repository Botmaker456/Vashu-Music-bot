from FIXXMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = ["🦋🦋🦋🦋🦋",
         "🧚🌸🧋🍬🫖",
         "🥀🌷🌹🌺💐",
         "🌸🌿💮🌱🌵",
         "❤️💚💙💜🖤",
         "💓💕💞💗💖",
         "🌸💐🌺🌹🦋",
         "🍔🦪🍛🍲🥗",
         "🍎🍓🍒🍑🌶️",
         "🧋🥤🧋🥛🍷",
         "🍬🍭🧁🎂🍡💞",
         "🍨🧉🍺☕🍻",
         "🥪🥧🍦🍥🍚",
         "🫖☕🍹🍷🥛",
         "☕🧃🍩🍦🍙",
         "🍁🌾💮🍂🌿",
         "🌨️🌥️⛈️🌩️🌧️",
         "🌷🏵️🌸🌺💐",
         "💮🌼🌻🍀🍁",
         "🧟🦸🦹🧙👸",
         "🧅🍠🥕🌽🥦",
         "🐷🐹🐭🐨🐻‍❄️",
         "🦋🐇🐀🐈🐈‍⬛",
         "🌼🌳🌲🌴🌵",
         "🥩🍋🍐🍈🍇",
         "🍴🍽️🔪🍶🥃",
         "🕌🏰🏩⛩️🏩",
         "🎉🎊🎈🎂🎀",
         "🪴🌵🌴🌳🌲",
         "🎄🎋🎍🎑🎎",
         "🦅🦜🕊️🦤🦢",
         "🦤🦩🦚🦃🦆",
         "🐬🦭🦈🐋🐳",
         "🐔🐟🐠🐡🦐",
         "🦩🦀🦑🐙🦪",
         "🐦🦂🕷️🕸️🐚",
         "🥪🍰🥧🍨🍨",
         " 🥬🍉🧁🧇",
         ]
####

SHAYRI = [
    " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** ",
    " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
    " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀** ",
    " Created by vashu 🌺**।लबों से छू लूँ जिस्म तेरा, साँसों में साँस जगा जाऊँ, तू कहे अगर इक बार मुझे, मैं खुद ही तुझमें समा जाऊँ**🌺 \n\n**🥀labon se chhoo loon jism tera, saanson mein saans jaga jaoon, too kahe agar ik baar mujhe, main khud hee tujhamen sama jaoon.💞** ",
    " 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** ",
    " created by vashu 🌺**मेरी आँखों का ख्वाब बस तुम हो, मेरे दिल का अरमान बस तुम हो, जीते है हम बस तुम्हारे सहारे, क्योकि मेरे दिल की धड्कन बस तुम हो।**🌺 \n\n**💀meree aankhon ka khvaab bas tum ho, mere dil ka aramaan bas tum ho, jeete hai ham bas tumhaare sahaare, kyoki mere dil kee dhadkan bas tum ho💖** ",
    " 🌺**फिक्र तो होगी ना तुम्हारी इकलौती मोहब्बत हो तुम मेरी।**🌺 \n\n**🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀** ",
    " 🌺**सुनो जानू आप सिर्फ किचन संभाल लेना आप को संभालने के लिए मैं हूं ना।**🌺 \n\n**🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀** ",
    " 🌺**सौ बात की एक बात मुझे चाहिए बस तेरा साथ।**🌺 \n\n**🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀** ",
    " Created by vashu 🌺**चाहत तेरी पहचान है मेरी, मोहब्बत तेरी शान है मेरी, होके जुदा तुझसे क्या रह पाउँगा, तू तो जान हैं मेरी।**🌺 \n\n**💕chaahat teree pahachaan hai meree, mohabbat teree shaan hai meree, hoke juda tujhase kya rah paunga, too to jaan hain meree💓** ",
    " 🌺**बेबी बातें तो रोज करते है चलो आज रोमांस करते है।**🌺 \n\n**🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀** ",
    " 🌺**सुबह शाम तुझे याद करते है हम और क्या बताएं की तुमसे कितना प्यार करते है हम।**🌺 \n\n**🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀** ",
    " 🌺**किसी से दिल लग जाने को मोहब्बत नहीं कहते जिसके बिना दिल न लगे उसे मोहब्बत कहते हैं।**🌺 \n\n**🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀** ",
    " 🌺**मेरे दिल के लॉक की चाबी हो तुम क्या बताएं जान मेरे जीने की एकलौती वजह हो तुम।**🌺 \n\n**🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀** ",
    " 🌺**हम आपकी हर चीज़ से प्यार कर लेंगे, आपकी हर बात पर ऐतबार कर लेंगे, बस एक बार कह दो कि तुम सिर्फ मेरे हो, हम ज़िन्दगी भर आपका इंतज़ार कर लेंगे।**🌺 \n\n**🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀** ",
    " Created by vashu 🌺**सुर्ख गुलाब सी तुम हो, जिन्दगी के बहाव सी तुम हो, हर कोई पढ़ने को बेकरार, पढ़ने वाली किताब सी तुम हो।**🌺 \n\n**❤️‍🩹❤️‍surkh gulaab see tum ho, jindagee ke bahaav see tum ho, har koee padhane ko bekaraar, padhane vaalee kitaab see tum ho🖤**",
    " 🌺**तू मेरी जान है इसमें कोई शक नहीं तेरे अलावा मुझ पर किसी और का हक़ नहीं।**🌺 \n\n**🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀** ",
    " 🌺**पहली मोहब्बत मेरी हम जान न सके, प्यार क्या होता है हम पहचान न सके, हमने उन्हें दिल में बसा लिया इस कदर कि, जब चाहा उन्हें दिल से निकाल न सके।**🌺 \n\n**🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀** ",
    " 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** ",
    " 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** ",
    " 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** ",
    " 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀** ",
    " 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** ",
    " 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** ",
    " 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀** ",
    " Created bt vashu🌺**दिल के कोने से एक आवाज़ आती है, हमें हर पल उनकी याद आती है, दिल पूछता है बार — बार हमसे की, जितना हम याद करते है उन्हें, उन्हें क्या उन्हें भी हमारी याद आती है। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**💖dil ke kone se ek aavaaz aatee hai, hamen har pal unakee yaad aatee hai, dil poochhata hai baar — baar hamase kee, jitana ham yaad karate hai unhen, unhen kya unhen bhee hamaaree yaad aatee hai🤔** ",
    " 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** ",
    " 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** ",
    " 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** ",
    " 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** ",
    " 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀** ",
    " 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀** ",
    " 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀** ",
    " 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀** ",
    " 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद 
    "Created by vashu ","kahata hai pal pal tumase ho kar dil ye divaana, ek pal bhee jaane jaana hamase door nahee jaana.🤧"
    "Created by vashu ","होती नहीं है मोहब्बत सूरत से, मोहब्बत तो दिल से होती है, सूरत उनकी खुद-ब-खुद लगती है प्यारी, कदर जिनकी दिल में होती है💕"
    "Created by vashu ","लबों से छू लूँ जिस्म तेरा, साँसों में साँस जगा जाऊँ, तू कहे अगर इक बार मुझे, मैं खुद ही तुझमें समा जाऊँ❤️"
    "Created by vashu ","लबों से छू लूँ जिस्म तेरा, साँसों में साँस जगा जाऊँ, तू कहे अगर इक बार मुझे, मैं खुद ही तुझमें समा जाऊँ👻"