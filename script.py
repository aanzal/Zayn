class Script(object):
    START_TXT = """<b>Heyy {}.
I'm Zayn Malik. An Advanced Telegram Filter Bot :)
I was Actually Made for <a href=https://t.me/CinemaGround>Cinema Ground</a>
Add me to your Groups & Enjoy!
Tap <code>Help</code> If you have any Doubt about how to use me in your Groups!</b>"""

    HELP_TXT = """Hey {}

𝐇𝐄𝐋𝐏 : <b>How to use me?</b>

- Add me to your Group, Promote me as an Admin. 

That's it! <b>Bot is now Ready!</b>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    ABOUT_TXT = """🤖 𝐁𝐎𝐓 : <a href=https://t.me/ZaynAndMillie>𝗭𝗔𝗬𝗡</a>
    
👨‍💻 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 : <a href=https://t.me/axnzal>𝗛𝗨𝗠𝗔𝗡</a>

📚 𝐋𝐈𝐁𝐑𝐀𝐑𝐘 : <a href=https://github.com/pyrogram/pyrogram>𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠</a>

📝 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : <a href=https://www.python.org/>𝗣𝗬𝗧𝗛𝗢𝗡</a>

📡 𝐁𝐎𝐓 𝐒𝐄𝐑𝐕𝐄𝐑 : <a href=http://heroku.com/>𝗛𝗘𝗥𝗢𝗞𝗨</a>

📂 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 : <a href=https://www.mongodb.com/>𝗠𝗢𝗡𝗚𝗢 𝗗𝗕</a>

👣 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : <a href=https://t.me/ZaynAndMillie>𝗭𝗔𝗬𝗡 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>

👤 𝐒𝐈𝐒𝐓𝐄𝐑 : <a href=https://t.me/CGProBot>𝗠𝗜𝗟𝗟𝗜𝗘</a>"""

    SOURCE_TXT = """𝐇𝐄𝐋𝐏 : <b>Source Code</b>

- Zayn Bot is a Private Source Project.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    MANUALFILTER_TXT = """𝐇𝐄𝐋𝐏 : <b>Filters</b>
    
- Filter is the feature were users can set automated Replies for a particular keyword and Zayn will respond whenever a keyword is found in the message.

𝐍𝐎𝐓𝐄 :

○ <b>Zayn Bot</b> should have Admin.
○ Only <b>Admins</b> can Add filters in the Connected chat.
○ Alert buttons have a limit of <b>64 characters.</b>

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

○ /filter - <code>Adds a filter in the Connected Chat.</code>
○ /viewfilters - <code>Lists all the filters of the Connected Chat.</code>
○ /delf - <code>Deletes a Specific Filter in the Connected Chat.</code>
○ /delallf - <code>Deletes the whole Filters in the Connected Chat ( For Chat Owner Only ).</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    BUTTON_TXT = """𝐇𝐄𝐋𝐏 : <b>Buttons</b>

- Zayn Supports Both URL and ALERT Inline Buttons.

𝐍𝐎𝐓𝐄 :

○ <b>Zayn Bot</b> supports buttons with any telegram media type.
○ Telegram will not Allows you to send Buttons Without any <b>Content</b>, So Content is Mandatory.
○ Buttons should be properly parsed as <b>Markdown format.</b>

𝐁𝐔𝐓𝐓𝐎𝐍𝐒 𝐔𝐒𝐀𝐆𝐄 :
○ <b>URL Buttons :</b>
<code>[Button Text](buttonurl:https://t.me/XaynBot)</code>
○ <b>Alert Buttons :</b>
<code>[Button Text](buttonalert:This is an Alert message)</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    AUTOFILTER_TXT = """𝐇𝐄𝐋𝐏 : <b>Auto Filter</b>
    
○ Make me the <b>Admin</b> of your channel if it's private.
○ Make sure that your Channel does not contains <b>Camrips, Porn or Fake </b>files.
○ <b>Forward</b> the last message to me with quotes. I'll Add all the files in that channel to my <b>DataBase.</b>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    CONNECTION_TXT = """<b>𝐇𝐄𝐋𝐏 : <b>Connections</b>
    
- Used to connect Bot to PM for managing filters.
- It helps to avoid spamming in groups.

𝐍𝐎𝐓𝐄 :

○ Only admins can Add a connection.
○ Send <code>/connectit</code> in your Group for connecting me to your PM. ( Only After making me Admin )

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

○ /connectit  - <code>Connect a Particular chat to your PM.</code>
○ /disconnectit  - <code>Disconnect from a Particular Chat.</code>
○ /myconnections - <code>List of all your Connections.</code></b>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    PASTE_TXT = """<b>𝐇𝐄𝐋𝐏 : <b>Paste</b>

- Paste some texts or documents on a website!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>

"""

    TGRAPH_TXT = """<b>𝐇𝐄𝐋𝐏 : TGraph & Paste</b>

- Do as you wish with telegra.ph module!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    INFO_TXT = """𝐇𝐄𝐋𝐏 : <b>Information</b>

- Get information about something!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    GTRANS_TXT = """𝐇𝐄𝐋𝐏 : <b>Google Translator</b>

- Translate texts to a specific language!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /tr [language code][reply] - translate replied message to specific language.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    SEARCH_TXT = """𝐇𝐄𝐋𝐏 : <b>IMDb</b>

- Search many things without leaving telegram!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    PURGE_TXT = """𝐇𝐄𝐋𝐏 : <b>Purge</b>

- Need to delete lots of messages? That's what purges are for!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /purge - delete all messages from the replied to message, to the current message.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    RESTRIC_TXT = """𝐇𝐄𝐋𝐏 : <b>Restrictions</b>

- Some people need to be publicly banned; spammers, annoyances, or just trolls.
- This module allows you to do that easily, by exposing some common actions, so everyone will see!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /ban - ban a user.
• /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - unmute a user & unban a user.

<b>Examples :</b>

- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    PIN_MESSAGE_TXT = """𝐇𝐄𝐋𝐏 : <b>Pin Message</b>

- All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works only group.
• These commands can be used by Only admin.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    ADMIN_TXT = """𝐇𝐄𝐋𝐏 : <b>Admin Mods</b>

𝐍𝐎𝐓𝐄 :

- This module only works for my admins

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /cchat - To connect a chat.
• /dchat - To disconnect from a chat.
• /leave - To leave from a chat.
• /disable - To disable a chat.
• /ban - To ban a user.
• /unban - To unban a user.
• /channel - To get list of total connected channels.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    STATUS_TXT = """» 𝗧𝗢𝗧𝗔𝗟 𝗙𝗜𝗟𝗘𝗦 : <code>{}</code>
» 𝗧𝗢𝗧𝗔𝗟 𝗨𝗦𝗘𝗥𝗦 : <code>{}</code>
» 𝗧𝗢𝗧𝗔𝗟 𝗖𝗛𝗔𝗧𝗦 : <code>{}</code>
» 𝗨𝗦𝗘𝗗 𝗦𝗧𝗢𝗥𝗔𝗚𝗘 : <code>{}</code>
» 𝗙𝗥𝗘𝗘 𝗦𝗧𝗢𝗥𝗔𝗚𝗘 : <code>{}</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    FORCESUB_TXT = """**READ THIS INSTRUCTION**

🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately

**JOIN THE CHANNEL & TRY AGAIN**

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    MEMES_TXT = """𝐇𝐄𝐋𝐏 : <b>Memes</b>

- Some dank memes for fun or whatever!

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /throw or /dart - t𝗈 m𝖺𝗄𝖾 drat.
• /roll or /dice - roll the dice.
• /goal or /shoot - to make a goal or shoot.
• /luck or /cownd - Spin the Lucky.
• /runs strings

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    URL_SHORTNER_TXT = """𝐇𝐄𝐋𝐏 : <b>URL Shortner</b>

- Some URLs is Shortner

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /short <code>(link)</code> - I will send the shorted links.

<b>Example :</b>
<code>/short https://t.me/ZaynAndMillie</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    TTS_TXT = """𝐇𝐄𝐋𝐏 : <b>Text to Speech</b>

- A module to convert text to voice with language support.

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /tts - Reply to any text message with language code to convert as audio.

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    MUSIC_TXT = """𝐇𝐄𝐋𝐏 : <b>Music</b>

- Music download modules, for those who love music.

𝐍𝐎𝐓𝐄 :

• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download :</b>

• /ytthumb (youtube link)

<b>Example :</b> <code>/ytthumb [link]</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    PASSWORD_GEN_TXT = """𝐇𝐄𝐋𝐏 : <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

𝐍𝐎𝐓𝐄 :

• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /genpassword or /genpw <code>20</code>

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>"""

    LOG_TEXT_G = """#NewGroup
Group - {} (<code>{}</code>)
Total Members - <code>{}</code>
Added By - {}

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}

<a href=https://t.me/ZaynAndMillie>𝗭𝗮𝘆𝗻</a>
"""

    ZOMBIES_TXT = """𝐇𝐄𝐋𝐏 : <b>Zombies</b>

𝐍𝐎𝐓𝐄 :

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 𝐀𝐍𝐃 𝐔𝐒𝐀𝐆𝐄 :

• /inkick - Command with required arguments and i will kick members from group.
• /instatus - To check current status of chat member from group.
• /inkick within_month long_time_ago - To kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - To kick members who are offline for more than a month and Deleted Accounts.
• /dkick - To kick deleted accounts."""

    CREATOR_REQUIRED = """❗ **You have to be the group creator to do that.**"""
      
    INPUT_REQUIRED = "❗ **Arguments Required.**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while.."""
      
    ADMIN_REQUIRED = """❗ I am not an admin here\nLeaving this chat, Add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
