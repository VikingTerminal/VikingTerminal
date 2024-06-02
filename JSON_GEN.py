import os
import time
import json
import re

banner = """.----.
   |C>_ |
 __|____|__
| ______--|
`-/.::::.\\-'a
 `--------'"""

def is_valid_domain(host):
    return bool(re.match(r"^(http(s)?://)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$", host))

def animate():
    animation = """☆ ⋆｡°✩﹒ʬʬ﹒⪩⪨﹒⟡﹒ᐢ. ᶻz﹒⊂⊃﹒␥﹒⿸﹒ꔠ﹒ ✶﹒◍﹒▿﹒⤸﹒⬚﹒៶៸﹒△﹒→﹒✶﹒（）﹒▥﹒▤﹒▦﹒▧﹒▨﹒▩﹒░﹒▒﹒▓﹒⿴ ﹒◫﹒⬚﹒▣﹒≧≦ ﹒ㄑ﹒⎙﹒➜﹒★﹒⨳﹒✿﹒❀﹒✶﹒✸﹕☆﹒◐﹒◉ ﹒◖◗﹒▽﹒ᶻz﹒‹𝟹﹒♡﹒ᐢ..ᐢ ﹒﹫﹒⿴﹒→﹒☓﹕ ﹒ ＞＜﹒◌﹒⿴﹒✧﹒ . ﹒✹﹒﹢﹒✶﹑〇﹐罒﹢ ♡﹒⇆﹑⬚﹐ᶻ﹒❀﹐✶﹒▹﹒◖﹒✩﹒∇﹒▨﹐◌﹐❀﹒⿴﹒✿ ﹢﹐░﹒ᶻz﹐☆﹒⊂⊃ ﹑ ⵌ﹒▦﹒✿﹒⺌﹒◂﹒ ⿴﹒❰❰﹒♡﹒ᶻz﹒❥﹒⩇﹒⊞﹐ʬʬ﹒♢﹐ᐢ..ᐢ﹐✩﹒ᶻz﹒❥﹒⟡﹒✷﹒✕﹐〇﹐✿﹒ Ꜣ﹒⟡﹒˃̵ᴗ˂̵﹒♡ ﹐≋﹒⊂⊃﹒ᐢᗜᐢ﹒❀﹒ ﹢﹒⇵﹒⪨﹕↺﹐✿﹒Ꜣ﹒ ✶﹐≋﹒⇆﹐ʬʬ﹒﹗﹐➜﹒⬦﹕ᶻz﹒✦﹒﹢﹒▢﹒░﹒⭔﹒ʬʬ﹒✿﹒☰﹐◖◗﹒？﹒✶﹒ ✿ ᐢ﹒░﹒𖦹﹐゛✿﹑（｀δ´ ） ﹒イ。ꕀ﹑リ﹐⊂⊃﹒ꔠ ﹒口﹐･ᴗ･﹒░﹑リ﹒◐﹐、﹕✧﹒✶﹔？﹐ʬʬ﹒▹﹒❀﹒⭔﹒ ▿﹒⺡﹒✿﹒﹢﹒░﹑ ⬦ ﹒૪ ﹒〹﹒罒﹒ᶻ"""
    for char in animation:
        print(char, end='', flush=True)
        time.sleep(0.02)
    time.sleep(2)
    os.system('clear')

def is_valid_domain(host):
    return bool(re.match(r"^(http(s)?://)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$", host))

def main():
    animate()
    print("\033[91m" + banner + "\033[0m" + " \033[91mviking terminal\n\033[0m")

    while True:
        try:
            print("\033[92mEnter credentials:\033[0m")  
            host = input("\033[96mHost:\033[0m ").strip()
            
            while not host or not is_valid_domain(host):
                print("\033[91mThe host field cannot be empty and must contain a valid domain.\033[0m")
                host = input("\033[96mHost:\033[0m ").strip()
            
            port = input("\033[96mPort:\033[0m ").strip()
            
            while not port or not port.isdigit():
                print("\033[91mThe port field cannot be empty and must contain an integer.\033[0m")
                port = input("\033[96mPort:\033[0m ").strip()
                
            user = input("\033[96mUser:\033[0m ").strip()
            
            while not user:
                print("\033[91mThe user field cannot be empty.\033[0m")
                user = input("\033[96mUser:\033[0m ").strip()
                
            password = input("\033[96mPassword:\033[0m ").strip()
            
            while not password:
                print("\033[91mThe password field cannot be empty.\033[0m")
                password = input("\033[96mPassword:\033[0m ").strip()

            account = {
                "HOST": host,
                "PORT": int(port),
                "USER": user,
                "PASS": password
            }

            with open('accounts.json', 'w') as f:
                json.dump(account, f, indent=4)
            print("\033[92mThe accounts.json file has been created successfully.\033[0m")  
            break  
        except Exception as e:
            print("\033[91mError writing the file:", str(e), "\033[0m")

if __name__ == "__main__":
    main()
