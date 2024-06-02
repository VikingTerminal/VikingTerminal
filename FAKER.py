from faker import Faker
import random
import time
from colorama import Fore, Style

fake = Faker()

def generate_fake_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100)
    birth_year = birth_date.year
    birth_month = birth_date.month
    birth_place = fake.city()
    residence_city = fake.city()
    postal_code = fake.postcode()
    gender = random.choice(['M', 'F'])
    phone_number = fake.phone_number()
    fiscal_code = generate_fiscal_code(first_name, last_name, birth_year, birth_month, birth_place, gender)
    
    fake_data = {
        'First Name': first_name,
        'Last Name': last_name,
        'Year of Birth': birth_year,
        'Month of Birth': birth_month,
        'Place of Birth': birth_place,
        'City of Residence': residence_city,
        'Postal Code': postal_code,
        'Gender': gender,
        'Phone Number': phone_number,
        'Fiscal Code': fiscal_code
    }
    
    return fake_data

def generate_fiscal_code(first_name, last_name, birth_year, birth_month, birth_place, gender):
    month_codes = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'H',
        7: 'L', 8: 'M', 9: 'P', 10: 'R', 11: 'S', 12: 'T'
    }
    
    surname_code = ''.join(filter(str.isalpha, last_name.upper()))
    name_code = ''.join(filter(str.isalpha, first_name.upper()))
    
    year_code = str(birth_year)[2:]
    month_code = month_codes[birth_month]
    
    if gender == 'M':
        day_code = str(fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100).day)
    else:
        day_code = str(fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100).day + 40)    
    
    if not birth_place or len(''.join(filter(str.isalpha, birth_place))) < 3:
        birth_place_code = 'XXX'
    else:
        birth_place_code = ''.join(filter(str.isalpha, birth_place.upper()))[:3]
    
    fiscal_code = surname_code[:3] + name_code[:3] + year_code + month_code + day_code + birth_place_code
    
    return fiscal_code

def print_banner():
    banner = """
┈┈┈╲┈┈┈┈╱
┈┈┈╱▔▔▔▔╲
┈┈┃┈▇┈┈▇┈┃
╭╮┣━━━━━━┫╭╮
┃┃┃┈┈┈┈┈┈┃┃┃
╰╯┃┈┈┈┈┈┈┃╰╯
┈┈╰┓┏━━┓┏╯
┈┈┈╰╯┈┈╰╯
__        
\\  / | |__/ | |\\ | / _`       
 \\/  | |  \\ | | \\| \\__>
     
powered by t.me/VikingTERMINAL
    """
    for char in banner:
        print(Fore.LIGHTBLUE_EX + char, end='', flush=True)
        time.sleep(0.001)  
    print(Style.RESET_ALL)

if __name__ == "__main__":
    print_banner()
    fake_data = generate_fake_data()
    for key, value in fake_data.items():
        for char in f"{key}: {value}":
            print(Fore.GREEN + char, end='', flush=True)
            time.sleep(0.03)  
        print(Style.RESET_ALL)
