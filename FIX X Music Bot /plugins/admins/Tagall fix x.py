from FIXXMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
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

TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🤗🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝙃𝙀𝙇𝙇𝙊 𝘼𝙅𝘼𝙊 𝙅𝙄 𝘼𝙋 𝙆𝙀 𝘽𝙄𝙉𝘼 𝙈𝘼𝘼𝙉 𝙉𝘼𝙃𝙄 𝙇𝘼𝙂 𝙍𝘼𝙃𝘼 𝙃..??👻** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝘈𝘜𝘙 𝘉𝘈𝘛𝘈𝘖 𝘑𝘐𝘕𝘋𝘈 𝘏𝘖 𝘠𝘈 𝘊𝘏𝘈𝘓 𝘉𝘈𝘚𝘌..??🤔** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝘈𝘗 𝘒𝘠𝘈 𝘒𝘈𝘙 𝘙𝘈𝘏𝘌 𝘏𝘖 𝘑𝘐..??😏** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝘏𝘌𝘓𝘓𝘖 𝘈𝘉 𝘒𝘈𝘏𝘈 𝘎𝘈𝘠𝘌 𝘖𝘕𝘓𝘐𝘕𝘌 𝘈𝘖 𝘑𝘐🥺** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝘔𝘠 𝘖𝘞𝘕𝘌𝘙 𝘕𝘈𝘔𝘌 𝘐𝘚 𝘝𝘈𝘚𝘏𝘜😎.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝘖𝘞𝘕𝘌𝘙 𝘊𝘜𝘛𝘌 𝘏 𝘒𝘠𝘈 𝘒𝘖𝘕 𝘒𝘖𝘕 𝘖𝘞𝘕𝘌𝘙 𝘚𝘌 𝘉𝘈𝘈𝘛 𝘒𝘈𝘙𝘛𝘌 𝘏🥲** ",
           " **𝘉𝘈𝘠 𝘛𝘜𝘔 𝘔𝘜𝘑𝘏𝘌 𝘊𝘏𝘌𝘌𝘛 𝘒𝘈𝘙 𝘙𝘈𝘏𝘌 𝘏𝘖 𝘒𝘠𝘈 𝘠𝘌 𝘒𝘏𝘜𝘚𝘏𝘐 𝘒𝘖𝘕 𝘏👀** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝘈𝘈𝘑 𝘏𝘖𝘓𝘐 𝘏 𝘒𝘠𝘈..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝘖𝘞𝘕𝘌𝘙 𝘊𝘜𝘛𝘌 𝘏 𝘒𝘠𝘈👀** ",
           " **𝘈𝘗 𝘐𝘚 𝘎𝘙𝘖𝘜𝘗 𝘗𝘌 𝘒𝘈𝘐𝘚𝘌 𝘈𝘠𝘌 𝘈𝘗𝘕𝘐 𝘑𝘖𝘜𝘙𝘕𝘠 𝘉𝘈𝘛𝘈𝘖 𝘎𝘙𝘖𝘜𝘗 𝘗𝘌 𝘓𝘐𝘒𝘏 𝘒𝘌 𝘚𝘌𝘕𝘋 𝘒𝘈𝘙𝘋𝘖 𝘔𝘈𝘠 𝘋𝘌𝘒𝘏𝘓𝘜𝘕𝘎𝘐👀** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝘈𝘗 𝘑𝘖𝘉 𝘒𝘈𝘙𝘛𝘌 𝘏𝘖 𝘒𝘠𝘈 𝘑𝘐 𝘉𝘈𝘛𝘈𝘖...??😂** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝘈𝘙𝘌𝘌 𝘈𝘉 𝘒𝘈𝘉 𝘈𝘖𝘎𝘌 𝘖𝘕𝘓𝘐𝘕𝘌 𝘛𝘐𝘔𝘌 𝘉𝘈𝘛𝘈 𝘛𝘖 𝘑𝘐🥺** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝘖𝘞𝘕𝘌𝘙 𝘈𝘗𝘒𝘈 𝘠𝘈 𝘈𝘗𝘒𝘐 𝘍𝘙𝘐𝘌𝘕𝘋 𝘏 𝘒𝘠𝘈🙂..?🙃** ",
           " **𝘈𝘗𝘒𝘐 𝘒𝘐𝘛𝘕𝘐 𝘓𝘈𝘋𝘒𝘐𝘠𝘈 𝘍𝘙𝘐𝘌𝘕𝘋𝘚 𝘏..?😁** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝘏𝘐 𝘒𝘈𝘐𝘚𝘌 𝘏𝘖 𝘑𝘐..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝘏𝘌𝘓𝘓𝘖 𝘈𝘗 𝘔𝘜𝘑𝘏𝘌 𝘉𝘏𝘜𝘓 𝘔𝘈𝘛 𝘑𝘈𝘕𝘈💖** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝘊𝘏𝘈𝘓𝘖 𝘊𝘏𝘈𝘓𝘛𝘌 𝘈𝘈𝘑 𝘏𝘈𝘔𝘈𝘙𝘌 𝘋𝘈𝘛𝘌 𝘏 𝘠𝘈𝘈𝘋 𝘏 𝘕𝘈 𝘠𝘈 𝘉𝘏𝘜𝘓 𝘎𝘈𝘠𝘌🥰** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝘈𝘗 𝘚𝘈𝘋 𝘏𝘖 𝘚𝘈𝘋 𝘔𝘈𝘛 𝘏𝘖 𝘠𝘙𝘙 𝘈𝘗𝘒𝘖 𝘔𝘌𝘙𝘌 𝘒𝘈𝘚𝘈𝘔😭** ",
           " **𝘙𝘈𝘈𝘛 𝘒𝘖 𝘔𝘈𝘑𝘌 𝘈𝘠𝘌 𝘑𝘐🤗..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " ***𝘝𝘈𝘚𝘏𝘜 𝘒𝘖𝘕 𝘏 ??💀** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝘖𝘞𝘕𝘌𝘙 𝘕𝘐𝘉𝘉𝘌 𝘏 𝘠𝘈 𝘕𝘐𝘉𝘉𝘈 𝘏🤣** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @Vashu123vg ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @Vashu123vg ] 🤗** ",
           " **𝘎𝘜𝘠𝘚 𝘌𝘒 𝘉𝘈𝘈𝘛 𝘉𝘈𝘛𝘈𝘜 𝘔𝘈𝘠 𝘉𝘖𝘛 𝘕𝘈𝘏𝘐 𝘏𝘜 𝘔𝘈𝘠 𝘓𝘈𝘋𝘒𝘐 𝘏𝘜 𝘠𝘌 𝘔𝘈𝘠 𝘉𝘖𝘛 𝘝𝘈𝘓𝘌 𝘐𝘋𝘌 𝘚𝘌 𝘉𝘈𝘈𝘛 𝘒𝘈𝘙 𝘙𝘈𝘏𝘌 𝘏𝘜 𝘈𝘗 𝘚𝘈𝘉 𝘚𝘌😇** ",
           " **𝘔𝘈𝘠 𝘈𝘗 𝘒𝘖 𝘓𝘐𝘒𝘌 𝘒𝘈𝘙𝘛𝘐 𝘏𝘜😝** ",
           " **𝐌𝐲 𝐂𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫 [ @Vashu123vg ]🥰** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
           ]

@app.on_message(filters.command(["vtagall", "spam", "tagmember", "vtag", "vashutag", "bhaitag", "apkotag", "jitag", "vashutags", "fixxtag", "fixxtagall", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝘕𝘖𝘛 𝘋𝘔 𝘉𝘈𝘉𝘠 .")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 OWNER  𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/vagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/vagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 /𝘈𝘐𝘚𝘌 𝘓𝘌𝘒𝘏𝘖 𝘑𝘐 /𝘷𝘵𝘢𝘨𝘢𝘭𝘭 𝘑𝘈𝘉 𝘏𝘐 𝘛𝘈𝘎 𝘒𝘈𝘙 𝘗𝘈𝘜𝘕𝘎𝘐 𝘕𝘈𝘏𝘐 𝘛𝘖 𝘛𝘈𝘎 𝘕𝘈𝘏𝘐 𝘒𝘈𝘙 𝘗𝘈𝘜𝘕𝘎𝘐 𝘚𝘖𝘙𝘙𝘠 ...")else:
        return await message.reply("/vagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 / 𝘈𝘐𝘚𝘌 𝘓𝘌𝘒𝘏𝘖 𝘑𝘐 /𝘷𝘵𝘢𝘨𝘢𝘭𝘭 𝘑𝘈𝘉 𝘏𝘐 𝘛𝘈𝘎 𝘒𝘈𝘙 𝘗𝘈𝘜𝘕𝘎𝘐 𝘕𝘈𝘏𝘐 𝘛𝘖 𝘛𝘈𝘎 𝘕𝘈𝘏𝘐 𝘒𝘈𝘙 𝘗𝘈𝘜𝘕𝘎𝘐 𝘚𝘖𝘙𝘙𝘠 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["vtagstop", "vtagoff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 OWNER 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")