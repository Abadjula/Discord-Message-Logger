import discord  # Import discord package
from discord.ext import commands  # From discord.ext package import commands class
from tkinter import *  # From tkinter import everything
from PIL import Image, ImageTk  # Import pillow image library
import datetime  # Import date and time
import os  # Import os for pictures
import asyncio  # Import asyncio for timeouts

root = Tk()  # Variable for screen
root.geometry("1000x500")  # Screen resoloution
root.title("Discord message logger gui")   # App title
root.iconbitmap(os.path.join("Icon.ico"))  # App icon

client = commands.Bot(command_prefix="!", help_command=None, self_bot=True, case_insensitive=True)  # Variable for discord bot

main_color = 0xFF0000 # Main hex color for discord

def check_for_token():  # Function where it gets the user id and bot token and puts them in the event where it will get you deleted messages
    try:
        Token = Token_box.get()
        Channel_id = int(Channel_id_box.get())
        check_for_i.config(text="Success!")
        @client.event
        async def on_message_delete(message):
            user = message.author
            Date = "Date: "
            Time = "Time: "
            date_and_time = datetime.datetime.now()
            me = await client.fetch_channel(Channel_id)
            delete_message_embed_for_me = discord.Embed(color=main_color)
            delete_message_embed_for_me.set_author(name=user, icon_url=user.avatar_url)
            delete_message_embed_for_me.add_field(name="Deleted Info", value=f"{user.mention} has deleted a message\nMessage: ***```\n{message.content}```***")
            delete_message_embed_for_me.set_footer(text=Date + date_and_time.strftime(f"%y-%m-%d\n{Time}%H:%M:%S"))
            await me.send(embed=delete_message_embed_for_me)
        @client.event
        async def on_message_edit(before, after):
            me = await client.fetch_channel(Channel_id)
            user = before.author
            guild = before.guild
            Date = "Date: "
            Time = "Time: "
            date_and_time = datetime.datetime.now()
            edited_message_embed_for_me = discord.Embed(color=main_color)
            edited_message_embed_for_me.set_author(name=user, icon_url=user.avatar_url)
            edited_message_embed_for_me.add_field(name="Edited Info", value=f"{user.mention} has edited thier message\nOriginal message: ***```\n{before.content}```*** \u200b\nEdited message: ***```\n{after.content}```*** \u200b")
            edited_message_embed_for_me.set_footer(text=Date + date_and_time.strftime(f"%y-%m-%d\n{Time}%H:%M:%S"))
            await me.send(embed=edited_message_embed_for_me)
        @client.event
        async def on_ready():
            print("""
            ----------------------------
            Loading. . . . . . . . . . .
            """)
            await asyncio.sleep(3)
            print(f"""
            Authentikating your token... {Token}
            Accessing your channel id... {Channel_id}
            """)
            await asyncio.sleep(1)
            print("""
            Connected!
            Name... {0.user}
            You can now receive deleted messages and original edited messages!
            Enjoy.
            -----------------------------
            """.format(client))
        root.destroy() # Closes the gui when you entered the credentials
        client.run(Token, bot=False)
    except ValueError:
        check_for_i.config(text="Invalid channel id")
    except OSError:
        check_for_i.config(text="You are not connected to the internet")
    except:
        check_for_i.config(text="Invalid token")

'''
Gui customzation
'''

img = ImageTk.PhotoImage(Image.open("Discord.png")) # Image

panel = Label(root, image=img)
panel.pack()

Instruction_for_user_id = Label(root, text="⬇Your channel id here⬇")
Instruction_for_user_id.pack()

Channel_id_box = Entry(root)
Channel_id_box.pack()

Insruction_for_token = Label(root, text="⬇Your token here⬇")
Insruction_for_token.pack()

Token_box = Entry(root)
Token_box.pack()

button = Button(root, text="Submit", height=2, width=20, command=check_for_token)
button.pack()

check_for_i = Label(root, text="")
check_for_i.pack()

root.mainloop() # Loop through the script
