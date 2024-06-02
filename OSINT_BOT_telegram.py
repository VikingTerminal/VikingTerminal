import requests
import random
import logging

logging.basicConfig(level=logging.INFO)

def main():
    try:
        telegram_token = input('\033[{}mTelegram Token (bot1xxx): \033[0m'.format(random_color())).strip()
        telegram_chat_id = input('\033[{}mTelegram Chat ID (-100xxx): \033[0m'.format(random_color())).strip()

        if telegram_token.startswith('bot'):
            telegram_token = telegram_token[3:]

        analyze_telegram(telegram_token, telegram_chat_id)
    
    except requests.RequestException as e:
        logging.error('Request failed: %s', str(e))

def analyze_telegram(token, chat_id):
    with requests.Session() as session:
        telegram_get_me = get_telegram_info(session, f"https://api.telegram.org/bot{token}/getMe")
        if telegram_get_me:
            print_info(telegram_get_me)

            chat_info = get_telegram_info(session, f"https://api.telegram.org/bot{token}/getChat?chat_id={chat_id}")
            if chat_info:
                print_info(chat_info)
                print_chat_details(session, token, chat_id)

def get_telegram_info(session, url):
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.json().get('result')
    except requests.RequestException as e:
        logging.error('Request failed: %s', str(e))
        return None

def print_info(data):
    for key, value in data.items():
        print("\033[{}m{}: {}\033[0m".format(random_color(), key.capitalize(), value))

def print_chat_details(session, token, chat_id):
    urls = [
        f"https://api.telegram.org/bot{token}/exportChatInviteLink?chat_id={chat_id}",
        f"https://api.telegram.org/bot{token}/createChatInviteLink?chat_id={chat_id}",
        f"https://api.telegram.org/bot{token}/getChatMemberCount?chat_id={chat_id}",
        f"https://api.telegram.org/bot{token}/getChatAdministrators?chat_id={chat_id}"
    ]

    for url in urls:
        data = get_telegram_info(session, url)
        if data:
            if 'invite_link' in data:
                print("\033[{}m{}: {}\033[0m".format(random_color(), 'Chat Invite Link', data['invite_link']))
            elif 'result' in data:
                if isinstance(data['result'], list):
                    print_admins(data['result'])
                else:
                    print("\033[{}m{}: {}\033[0m".format(random_color(), 'Number of users in the chat', data['result']))

def print_admins(admins):
    print("\033[{}mAdministrators in the chat:\033[0m".format(random_color()))
    for admin in admins:
        print_info(admin['user'])

def random_color():
    colors = ['31', '32', '33', '34', '35', '36']
    return random.choice(colors)

if __name__ == '__main__':
    main()
