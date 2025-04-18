import requests, sys

while True:
    print('Please enter a URL to check status: (type exit to quit)\n')
    url = input()
    try:
        if url == 'exit':
            print('Goodbye.')
            sys.exit()
        if url == '':
            print('No URL entered.')
            continue
        else:
            if not url.startswith('http'):
                url = 'https://' + url
            status = requests.get(url)
            status_time = status.elapsed.total_seconds()
            if status.status_code == 200:
                print('\n-- Site is online! --')
                print(f'Time taken for response: {status_time}s\n')
            else:
                print('Site is down or unreachable!')
    except requests.exceptions.RequestException as errex:
        print('Not a valid URL.\n')
        continue