import requests
import fade
import os

def create_html_content():
    """Crée le contenu HTML avec le texte et l'ASCII art demandés."""
    html_content = """
    <html>
    <head>
        <title>Website Defaced by HxH Community</title>
        <style>
            body {
                background-color: red;
                color: black;
                text-align: center;
                font-family: Enchanted Land, sans-serif;
                margin-top: 0%;
            }
            .ascii-art {
                white-space: pre-wrap; /* Preserve whitespace formatting */
                font-size: 16px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <h1>Website Defaced by HxH Community and ChocolatSQL </h1>
        <div class="ascii-art">
                                                                                                                       
 @@@@@@@@@@@@@@@@@@@@@@%-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@=#=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=-@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@=@%*+#@@@@@@@@@@@@@@@@@%####%@@@@@@@@@@@#=%=@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@=@@@@#=*@@@@@@##******#%@@@@#****#%@@@@**@@=@@@@@@@@%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@-%@@@@@@=@@@@@@%+*#+-*%@@@@@@@@@@@@@@@@@@@###+=+@@@=@@@@@@@%.@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#-=#@@@@@%=@@@@@@@=:+**%@@@@@@@@@@@@@@@@@@@@%=#@@#+=+@@@@@@@==@@@@@@@@@@@@@@@
@@@@@@@@@@@@@*#-+#@@@@@#+@@@@#--@@@@%@@@@@@@@@@@@@@@@@@@+*@@@@@#+#=@@@@#.@=@@@@@@@@@@@@@@@
@@@@@@@@@@@@@+@%=+*@@@@@#=%%+#+%@@@@@@@@@@@@@@@@@@@@@@#+@@@@@@%+@@#*@%+#=@=@@@@@@@@@@@@@@@
@@@@@@@@@@@@@+@@#*#+%@@@@@=:%%+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=@@@@=+*@#**#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@#*@@+*@=#@@%@-@+-%@@@@@@@@%%@@@@@##@@@@@@@@@@@@@+@@@@@**@++@=@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@+%@@*+@*+=#=%@@%*%@@@@@@@@+*@@@%+@@@@@@@@@@%*#**@@@@@#:#@@*%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+*@@@+*@-+@@@@@%#**%@@@@@@@*@@@@@@@@@#***:%@@@@@@@@@@+@@%+@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%*+%@+- +@@@@@@@@@*+*@@@@@@+@=@@@%++%@@@+*@*%@@@@@+@+@@=@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@++-.  +%@@@@@@@%=@++@@@%+@#+@****##**%%+*@@@@@@:@=@=#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@=: +.:%@@@@@@%+#%#-#*+@@@**%@@@@@@@@@@@@@@@@%.=%=%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@#= :+@@@@@@@@@@%%#%#%@@@@@@@@@@@@@@@@@@@@@@@+ *+@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@*..#@@@@@@@@@@@@@@@@-@@@%+@@@@@+*%%@@@@@@@@--#@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@-:%@@@@@@@@@@@@@@+#@@@@=@@@@@@:.+#@@@@@@@=-@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:*@@@@@@##@@@@@@-@@@@@=@@@@#=%=@@@@@@@@@%:@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@=-#@@@@@@@:-#@@@@@*+@@#*@@%=#@#*@@@@@@@@@@-+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@--%@@@@@@@@@=#****%@#*@+@@*=@@#=@@@@@@@@@@#:+@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@+@@@@@@@@@@@%+@@@@#+*+*=@**@@++@@@@@@@@@*-=%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%=%@@@@@@@@@@=@@-@++#*--+*@%:*@@@@@@@@=-*@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@***%@@@@@=@*+%%==%=#=*+++-@@#=@@@%+=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+*##%#=@@***%@@+@**#*@#=#@#+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=:#@@@%++*+#@@@+#@#=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=%@@@@@@@@@@@@=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@#@@@@@@@#*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@@+*##@@@%+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@@@@@@@@@%+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+########*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                            ............:?#%;........................................................;%#?:............
                                             ..........,?#%:...........................,,,,,,...........................:%#?,..........
                                             ...........+#S;.......:;;,..........,,,:::::;::::;:::::,,,..........,;+:.......;S#+.........
                                             .......,%@+......;?##*,.......,,:::::::,,::,::,::,,:::::::,,.......,*##?;......+@%,.......
                                             ......;#S:..,+;:%@@S:......,:::,,,::,,..::..::..::..,,::,,,:::,......:S@@%:;+,..:S#;......
                                             .....+@%,..+#?;#@#*:.....,::::,,,::....::...::...:,....::,,,::::,.....:*#@#;?#+..,%@+.....
                                             ....+@?..,*@#,SS*+%;...,::,..,,:;:::,,,;,..,;+:,.,;,,,:::;:,,..,::,...;%+*SS,#@*,..?@+....
                                             ...;@?.,+;@@*:**S@+..,::,.....::,.,,,,:::;SS+*#@S:::,,,,.,::.....,::,..+@S**:*@@;+,.?@;...
                                             ..:@%.:#*+@#;%@@%:..,:,......,;,......:,.:S%:,%@@:,:......,;,......,:,..:%@@%;#@+*#:.%@:..
                                             .,S#,.S@+;@S@S*+...::,......,;,......,;,....:?#%:.,;,......,;,......,::...+*S@S@;+@S.,#S..
                                             .+@+.:@@?;@%++S+..:;:::,,,,.::.......::.....;?,....::.......::.,,,,:::;:..+S++%@;?@@:.+@+.
                                             ,#S..;@@S:**#@?..,;,..,,,:::;::,,,,,,::....,++,....::,,,,,,::;:::,,,..,;,..?@#**:S@@;..S#,
                                             +@+.::@@S:S@@*..,;,........::,,,,,,::;:::::*@@*:::::;::,,,,,,::........,;,..*@@S:S@@::.+@;
                                             %@,,S,*@S#@S;:..::........,;,........;,.....++.....,;........,;,........::..:;S@#S@*,S,,@%
                                             ##.:@+,##@*,%*..:,........,;........,;,..,,;++;,,..,;,.......,;,........,:..*%,*@##,+@:.##
                                             @%.:@#,;@+,S@:.,;,........,:........,:,++:*S@@S*:++,:,........:,........,;,.:@S,+@;:#@:.%@
                                             @%.,#@#,+:#@%..,;::::::::::;:,,,,::;+?#@*..;@@;..*@#?+;::,,,,:;::::::::::;,..%@#:+,#@#,.%@
                                             @%..*@@S,S@@;..,;,........,::*?%%S#@@@@#,.,;%%;,.,#@@@@#S%%?*::,........,;,..;@@S,S@@*..%@
                                             ##.::%@@*#@*:+..:,........,:%@@@@@@@@@@%...,##,...%@@@@@@@@@@%:,........,:..+:*@#*@@%::.##
                                             %@,;%,*@#@#,*@,.::........,;@@@@@@@@@@@#,..+@@+..,#@@@@@@@@@@@;,........::.,@*,#@#@*,%;,@%
                                             +@+,@S::S@%.S@+.,;,........+@@@@@@@@@@@@*..*@@*..*@@@@@@@@@@@@+........,;,.+@S.%@S::S@,+@;
                                             ,#S.+@@?:**:@@?..,;,.,,,,::%@@@@@@@@@@@@@+.?@@?.+@@@@@@@@@@@@@%::,,,,.,;,..?@@:**:?@@+.##,
                                             .+@+.+#@@?:;@@%,+.:;:::,,,,S@@@@@@@@@@@@@@*?@@?*@@@@@@@@@@@@@@S,,,,:::;:.+,%@@;:?@@#+.+@+.
                                             ..S#,.:%@@#+S@S.SS,::,....:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:....,::,SS.S@S+#@@%:.,#S..
                                             ..:@%.:+;?#@S@@,+@S,,:,...+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+...,:,,S@+,@@S@#?;+:.%@:..
                                             ...;@?.*S+:;?S@?,@@S,,::,.?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?.,::,,S@@,?@S?;:+S*.?@;...
                                             ....+@?.+@@%+;;?:?@@?:;:::S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@S:::;:?@@?:?;;+%@@+.?@+....
                                             .....+@%.,*#@@#%*:%@@;*#+:#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:+#*;@@%:*%#@@#*,.%@+.....
                                             ......;#S:.,+%#@@@SS@@:*@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@*:@@SS@@@#%+,.:S#;......
                                             .......,%@+..;+++*%%S##;+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+;##S%%*+++;..+@%,.......
                                             ...........+#S:.;%%?**+**?+;?S#@@@@@@@@@@@@@@@@@@@@@@@@?%S##@@@@@@@@#S*:.:%#?,............
                                             ............:?#%:.:*S#@@@@@@@@##S%?@@@@@@@@@@@@@@@@@@@@@@@@%S##@@@@@@@@#S*:.:%#?,.........
                                             ..............:?#S+,,+?%%%SS#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#SS%%%?+,,+S#?:..............
                                             ................,+%#%;,:;*????*+*@@@@@@@@@@@@@@@@@@@@@@@@*+*????*;:,;%#%+,................
                                             ...................:+%S%+:......+@@@@@@@@@@@@@@@@@@@@@@@@+......:+%S%+:...................
                                             ......................,;?SS%*;:,?@@@@@@@@@@@@@@@@@@@@@@@@?,:;*%SS?;,......................
                                             ..........................,;*%SS#@@@@@@@@@@@@@@@@@@@@@@@@#SS%*;,..........................
                                             ...............................,:;+?%S##@@@@@@@@@@##S%?+;:,...............................
        </div>
        </div>
    </body>
    </html>
    """
    return html_content

def send_to_discord_webhook(webhook_url, html_content):
    """Envoie le contenu HTML au webhook Discord."""
    files = {
        'file': ('hacked.html', html_content, 'text/html')
    }
    response = requests.post(webhook_url, files=files)
    if response.status_code == 204:
        print(f"{fade.greenblue('File successfully sent to the webhook.')}")
    else:
        print(f"{fade.red(f'Failed to send file. Status code: {response.status_code}, Response: {response.text}')}")
    
def clear_screen():
    """Efface l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

text = fade.greenblue ("""
       ▄████████    ▄████████    ▄████████    ▄████████  ▄████████    ▄█    █▄    ▀████    ▐████▀ 
      ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███     ███▌   ████▀  
      ███    █▀    ███    █▀    ███    ███   ███    ███ ███    █▀    ███    ███      ███  ▐███    
      ███         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄    ▀███▄███▀    
    ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀     ████▀██▄     
             ███   ███    █▄    ███    ███ ▀███████████ ███    █▄    ███    ███     ▐███  ▀███    
       ▄█    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███    ▄███     ███▄  
     ▄████████▀    ██████████   ███    █▀    ███    ███ ████████▀    ███    █▀    ████       ███▄ 
                                             ███    ███                                          
    """)
print (text)

def main():
    clear_screen()  

    webhook_url = input(f"{fade.greenblue('Enter the Discord webhook URL: ')}").strip()


    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            print(f"{fade.greenblue('Webhook URL is valid. Sending file...')}")
            html_content = create_html_content()
            send_to_discord_webhook(webhook_url, html_content)

           
            clear_screen()

           
            input(f"{fade.greenblue('Press Enter to return to the previous menu...')}")
            clear_screen() 
        else:
            print(f"{fade.red('Invalid webhook URL or failed to connect. Please check the URL and try again.')}")
    except requests.RequestException as e:
        print(f"{fade.greenblue(f'An error occurred: {e}')}")
    
if __name__ == "__main__":
    main()