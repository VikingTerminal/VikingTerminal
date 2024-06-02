import requests
import random
import time

def find_cdn(hostname):
    url = f"http://{hostname}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        cache_control = response.headers.get('Cache-Control', None)
        if cache_control:
            cache_control = cache_control.split(", ")
        
        cookies = response.cookies
        
        cdn_header = response.headers.get('X-Cache', None)
        if cdn_header:
            return cdn_header.split()[0], response.headers.get('Server', None), cache_control, cookies
        
        server_header = response.headers.get('Server', None)
        if server_header:
            server_header_lower = server_header.lower()
            if 'cloudflare' in server_header_lower:
                return 'Cloudflare', server_header, cache_control, cookies
            elif 'akamai' in server_header_lower:
                return 'Akamai', server_header, cache_control, cookies
            elif 'varnish' in server_header_lower:
                return 'Fastly', server_header, cache_control, cookies
        
        return "CDN not found", server_header, cache_control, cookies
    
    except requests.RequestException as e:
        return f"Error in request for {hostname}: {e}", None, None, None

def main():
    banner = '''
    \033[{}m┈┈┈╲┈┈┈┈╱
    ┈┈┈╱▔▔▔▔╲
    ┈┈┃┈▇┈┈▇┈┃
    ╭╮┣━━━━━━┫╭╮
    ┃┃┃┈┈┈┈┈┈┃┃┃
    ╰╯┃┈┈┈┈┈┈┃╰╯
    ┈┈╰┓┏━━┓┏╯
    ┈┈┈╰╯┈┈╰╯
    __        
    \  / | |__/ | |\ | / _`       
     \/  | |  \ | | \| \__>
     
    powered by t.me/VikingTERMINAL\033[0m'''
    print(banner.format(random.randint(91, 96)))
    hostname = input("\033[{}mEnter a hostname (e.g., example.com): \033[0m".format(random.randint(91, 96)))
    cdn, server_name, cache_control, cookies = find_cdn(hostname)
    if server_name:
        print("\033[{}mThe hostname {} is using the CDN: {} and server: {}\033[0m".format(random.randint(91, 96), hostname, cdn, server_name))
    else:
        print("\033[{}mThe hostname {} is using the CDN: {}\033[0m".format(random.randint(91, 96), hostname, cdn))

    if cache_control:
        print("\033[{}mCache-Control:\033[0m".format(random.randint(91, 96)), cache_control)
    
    if cookies:
        print("\033[{}mCookies:\033[0m".format(random.randint(91, 96)), cookies)

if __name__ == "__main__":
    main()
