import wikipedia

def wikipedia_command(command):
    cmd, keyword = command.split(maxsplit=1)
    wikipedia.set_lang('ja')
    try:
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        response = f'タイトル: {title}\n{summary}'
    except wikipedia.exceptions.PageError:
        response = f'「{keyword}」ノ意味ガ見ツカリマセンデシタ'
    return response
