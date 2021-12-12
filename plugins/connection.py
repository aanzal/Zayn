from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

@Client.on_message((filters.private | filters.group) & filters.command('cchat'))
async def addconnection(client,message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are Anonymous Admin. Use /cchat {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Enter in Correct format!</b>\n\n"
                "<code>/cchat [GroupID]</code>\n\n",
                quote=True
            )
            return

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            await message.reply_text("<b>Try not to fool me!\nFirst be an Admin in this Group!</b>", quote=True)
            return
    except Exception as e:
        logger.exception(e)
        await message.reply_text(
            "<b>Error</b>\n\n× Maybe the ID you have given is Wrong!\n**<i>OR</i>**\n× Check i'm in this group. If not, Add me by Clicking <a href='http://t.me/XaynBot?startgroup=true'>Here</a> & Make me admin!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Sucessfully connected to **{title}**\nNow manage your Group from my PM!\n\n❣️ From 𝗭𝗮𝘆𝗻",
                    quote=True,
                    parse_mode="md"
                )
                if chat_type in ["group", "supergroup"]:
                    await client.send_message(
                        userid,
                        f"Connected to **{title}**\n\n❣️ From 𝗭𝗮𝘆𝗻",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "Already <b>Connected</b>!",
                    quote=True
                )
        else:
            await message.reply_text("Add me as an Admin in group.", quote=True)
    except Exception as e:
        logger.exception(e)
        await message.reply_text('Some Error occured! Try again later.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('dchat'))
async def deleteconnection(client,message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"You are Anonymous Admin. Use /cchat {message.chat.id} in PM")
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Run /myconnections to VIEW or DISCONNECT from groups!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
            st.status != "administrator"
            and st.status != "creator"
            and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Successfully DISCONNECTED from this chat", quote=True)
        else:
            await message.reply_text("This chat isn't CONNECTED to me!\nDo /cchat to CONNECT.", quote=True)



@Client.on_message(filters.private & filters.command(["myconnections"]))
async def connections(client,message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "<b>Connect Some Group First!</b>",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - Active" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Your connected group details :\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await message.reply_text(
            "There are no active connections!! Connect to some groups first.",
            quote=True
        )
