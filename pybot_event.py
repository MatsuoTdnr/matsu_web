import requests

def event_command(command):
    cmd, keyword = command.split()
    base_url = 'https://connpass.com/api/v1/event/'
    url = f'{base_url}?keyword={keyword}'
    r = requests.get(url)
    event_data = r.json()
    
    title = event_data['events'][0]['title']
    place = event_data['events'][0]['place']
    event_url = event_data['events'][0]['event_url']

    response = f'「{title}」ノ会場ハ{place}デス({event_url})'
    return response
