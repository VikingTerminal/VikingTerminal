import requests
from bs4 import BeautifulSoup
import time
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}

def get_metadata(link):
    try:
        response = requests.get(link, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tags = soup.find_all('meta')

        metadata = {}
        for tag in meta_tags:
            attributes = tag.attrs
            key = attributes.get('name', attributes.get('property', '')).capitalize() 
            if key and 'content' in attributes:
                metadata[key] = attributes['content']

        return metadata

    except Exception as e:
        print(f"\033[1;31;40mOops! Something went wrong: {e}\033[0m")
        return None

def convert_to_nested_structure(metadata):
    nested_result = {}

    for key, value in metadata.items():
        keys = key.split('.')
        current_level = nested_result

        for i, partial_key in enumerate(keys):
            if i == len(keys) - 1:
                current_level[partial_key] = value
            else:
                if partial_key not in current_level:
                    current_level[partial_key] = {}
                current_level = current_level[partial_key]

    return nested_result

def print_nested_structure(nested_metadata, level=0):
    for key, value in nested_metadata.items():
        if isinstance(value, dict):
            print(f"{'  ' * level}{key}:")
            print_nested_structure(value, level + 1)
        else:
            print(f"{'  ' * level}{key}: {value}")

def typewriter_effect(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)  
    print()

def print_progress_bar(percentage):
    bar_width = 50
    completion = int(bar_width * percentage / 100)
    bar = '=' * completion + '-' * (bar_width - completion)
    sys.stdout.write(f'\r[{bar}] {percentage}%')
    sys.stdout.flush()

def main():
    try:
        link_input = input("\033[1;34;40m🌐 Enter the link to examine: \033[0m")
        metadata = get_metadata(link_input)

        if metadata:
            typewriter_effect("\n\033[1;32;40m🌟 Metadata successfully obtained! Here are the details:\033[0m")
            for key, value in metadata.items():
                typewriter_effect(f"\033[1;36;40m{key}:\033[0m {value}")
                time.sleep(0.1)  

            typewriter_effect("\n\033[1;33;40m🚀 Nested structured metadata:\033[0m")
            nested_metadata = convert_to_nested_structure(metadata)
            print_nested_structure(nested_metadata)

        else:
            typewriter_effect("\033[1;31;40m😿 Unable to retrieve metadata from the link. Maybe there's an issue with the site.\033[0m")

    except Exception as e:
        typewriter_effect(f"\033[1;31;40mOops! Something went wrong: {e}\033[0m")

if __name__ == '__main__':
    main()
    
    print("\nPress ENTER to close the program.")
    
    try:
        input()
        print("\033[1;34;40m🌐 Visit https://github.com/VikingTerminal to try out other utilities.\033[0m")
    except KeyboardInterrupt:
        pass