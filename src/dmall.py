import discord
import asyncio
import os
import sys

RESET = '\033[0m'
MAGENTA_BRIGHT = '\033[95m'

def center_text(text):
    columns = os.get_terminal_size().columns
    return '\n'.join([line.center(columns) for line in text.splitlines()])

def display_ascii_art():
    art = r"""   ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
  ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
  ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
         ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
   ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
 ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                         ███    ███               DMALL                       """
    return MAGENTA_BRIGHT + center_text(art) + RESET

def decorative_and_creator_line():
    return MAGENTA_BRIGHT + "═════════•°•▶▪ Created by: VENZOT ▪◀•°•═════════" + RESET

def display_decorative_and_creator_info():
    return center_text(decorative_and_creator_line())

def get_token_and_display():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_ascii_art())
    print("\n" + display_decorative_and_creator_info())
    print("\n")
    print(MAGENTA_BRIGHT + "Please enter your bot token: " + RESET, end="")
    token = input().strip()
    
    if not token:
        print(MAGENTA_BRIGHT + "\nError: The token cannot be empty. Please restart the script." + RESET)
        input("Press Enter to close...")
        sys.exit()
    
    return token

def get_message():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_ascii_art())
    print("\n" + display_decorative_and_creator_info())
    print("\n")
    print(MAGENTA_BRIGHT + "Please enter the message to send: " + RESET, end="")
    message = input().strip()
    
    if not message:
        print(MAGENTA_BRIGHT + "\nError: The message cannot be empty. Please restart the script." + RESET)
        input("Press Enter to close...")
        sys.exit()
    
    return message

async def send_direct_messages(token, message):
    intents = discord.Intents.default()
    intents.members = True 

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(MAGENTA_BRIGHT + f'We have logged in as {client.user}' + RESET)
        
        sent_users = set()
        for guild in client.guilds:
            print(MAGENTA_BRIGHT + f'Sending messages in the server: {guild.name}' + RESET)
            for member in guild.members:
                if not member.bot and member.id not in sent_users:
                    try:
                        print(MAGENTA_BRIGHT + f'Sending message to {member.name} ({member.id})' + RESET)
                        await member.send(message)
                        print(MAGENTA_BRIGHT + f'Message sent to {member.name}' + RESET)
                        sent_users.add(member.id)
                    except discord.Forbidden:
                        print(MAGENTA_BRIGHT + f'Unable to send message to {member.name} ({member.id}): Insufficient permissions' + RESET)
                    except discord.HTTPException as e:
                        print(MAGENTA_BRIGHT + f'HTTP error while sending message to {member.name} ({member.id}): {e}' + RESET)
                    except Exception as e:
                        print(MAGENTA_BRIGHT + f'Unknown error while sending message to {member.name} ({member.id}): {e}' + RESET)
                    await asyncio.sleep(1)
        
        print(MAGENTA_BRIGHT + 'All messages have been sent.' + RESET)
        await client.close()

    try:
        await client.start(token)
    except discord.LoginFailure:
        print(MAGENTA_BRIGHT + 'Login failed: check the bot token.' + RESET)
    except discord.errors.PrivilegedIntentsRequired as e:
        print(MAGENTA_BRIGHT + f'Error: {e}' + RESET)
    finally:
        if not client.is_closed():
            await client.close()
        input("Press Enter to continue...")

if __name__ == "__main__":
    token = get_token_and_display()
    while True:
        message = get_message()
        asyncio.run(send_direct_messages(token, message))
        os.system('cls' if os.name == 'nt' else 'clear')
