import binascii
import pyperclip
import fade
import os
import sys
import time

def to_hex(s):
    return binascii.hexlify(s.encode()).decode()

def ween_hex(hex_str):
    return '%'.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2))

def process_link(url):
    if url.startswith('http://') or url.startswith('https://'):
        p = url.split('/', 3)[-1]
    else:
        p = url

    hex_string = to_hex(p)
    encoded_string = ween_hex(hex_string).replace('%2f', '/')
    content = f"<ht\ntp\ns:/\\%{encoded_string}>"
    pyperclip.copy(content)
    print("[OK] Link copied to your clipboard (use: ctrl + v)")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()

text = fade.greenblue("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                             ███    ███         
                                                           Anti Link Bypass""")
print(text)

def main():
    while True:
        colored_prompt = fade.greenblue("[CLI] Please enter the link to send (ex., discord.gg/searchx): ")
        url = input(colored_prompt).strip()
        if not url:
            print("[OK] No URL entered.")
            os.system('cls' if os.name == 'nt' else 'clear')
            
            return  
        process_link(url)

if __name__ == '__main__':
    main()
