import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

viking = '\033[30m'  
terminal = '\033[1;31m'
rapid = '\033[1;32m'
rapid85 = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)

    return wrapper

@is_option
def IP_Track():
    ip = input(f"{Cy}\n Enter IP target : {rapid}")  
    print()
    print(f' {Wh}============= {rapid}SHOW INFORMATION IP ADDRESS {Wh}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}")  
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{Wh}\n IP target       :{rapid}", ip)
    print(f"{Wh} Type IP         :{rapid}", ip_data["type"])
    print(f"{Wh} Country         :{rapid}", ip_data["country"])
    print(f"{Wh} Country Code    :{rapid}", ip_data["country_code"])
    print(f"{Wh} City            :{rapid}", ip_data["city"])
    print(f"{Wh} Continent       :{rapid}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{rapid}", ip_data["continent_code"])
    print(f"{Wh} Region          :{rapid}", ip_data["region"])
    print(f"{Wh} Region Code     :{rapid}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{rapid}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{rapid}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{rapid}", f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{Wh} EU              :{rapid}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{rapid}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{rapid}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{rapid}", ip_data["capital"])
    print(f"{Wh} Borders         :{rapid}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{rapid}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{rapid}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{rapid}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{rapid}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{rapid}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{rapid}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{rapid}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{rapid}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{rapid}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{rapid}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{rapid}", ip_data["timezone"]["current_time"])

@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {rapid}Ex [+3933xxxxxxxx] {Wh}: {rapid}")  
    default_region = "IT"  

    parsed_number = phonenumbers.parse(User_phone, default_region)  
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "it")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {rapid}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{rapid} {location}")
    print(f" {Wh}Region Code          :{rapid} {region_code}")
    print(f" {Wh}Timezone             :{rapid} {timezoneF}")
    print(f" {Wh}Operator             :{rapid} {jenis_provider}")
    print(f" {Wh}Valid number         :{rapid} {is_valid_number}")
    print(f" {Wh}Possible number      :{rapid} {is_possible_number}")
    print(f" {Wh}International format :{rapid} {formatted_number}")
    print(f" {Wh}Mobile format        :{rapid} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{rapid} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{rapid} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{rapid} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{rapid} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{rapid} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{rapid} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{rapid} This is another type of number")

@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {rapid}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.periscope.tv/{}", "name": "Periscope"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.stumbleupon.com/stumbler/{}", "name": "StumbleUpon"},
            {"url": "https://www.ello.co/{}", "name": "Ello"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.telegram.me/{}", "name": "Telegram"},
            {"url": "https://www.weheartit.com/{}", "name": "We Heart It"}
        ]
        for site in social_media:
            url = site['url'].format(username)
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = (f"{rapid85}Username not found {rapid85}!")
    except Exception as e:
        print(f"{terminal}Error : {e}")
        return

    print(f"\n {Cy}========== {rapid}SHOW INFORMATION USERNAME {Wh}==========")
    print()
    for site, url in results.items():
        print(f" {Wh}[ {rapid}+ {Wh}] {site} : {rapid}{url}")

@is_option
def showIP():
    response = requests.get('https://api.ipify.org/')
    Show_IP = response.text

    print(f"\n {Cy}========== {rapid}SHOW INFORMATION YOUR IP {Wh}==========")
    print(f"\n {Wh}[{rapid} + {Wh}] Your IP Address : {rapid}{Show_IP}")
    print(f"\n {Wh}==============================================")

options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP

    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {rapid}+ {Wh}] {rapid}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {terminal}! {Wh}] {terminal}Exit')
        time.sleep(2)
        exit()

def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {rapid}{opt["text"]}\n'
    return text

def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False

def option():
    clear()
    stderr.writelines(f"""
__        
\  / | |__/ | |\ | / _`       
 \/  | |  \ | | \| \__>

              {Wh}[ * ] C O D E D   BY T.ME/VIKINGTERMINAL [ * ]
    """)

    stderr.writelines(f"\n{option_text()}")

def run_banner():
    clear()
    time.sleep(1)
    stderr.writelines(f"""{Wh}
 __        
 \  / | |__/ | |\ | / _`       
  \/  | |  \ | | \| \__>        
{Cy}--------------------------------
{Wh}| {rapid}visit t.me/VikingTERMINAL    {Wh}|
{Wh}| {rapid}for new tools and updates   {Wh}|
{Cy}--------------------------------
        """)
    time.sleep(0.5)

def main():
    clear()
    option()
    time.sleep(1)
    try:
        opt = int(input(f"{Wh}\n [ + ] {rapid}Select Option : {Cy}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[ {terminal}! {Wh}] {terminal}Please input number')
        time.sleep(2)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {terminal}! {Wh}] {terminal}Exit')
        time.sleep(2)
        exit()