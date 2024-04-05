from bottle import route, run, template, request
from pybot import pybot

@route('/map_0')
def map_01():
    return template('map_0.html')
@route('/map_1')
def map_01():
    return template('map_1.html')
@route('/map_2')
def map_01():
    return template('map_2.html')
@route('/map_3')
def map_01():
    return template('map_3.html')
@route('/map_4')
def map_01():
    return template('map_4.html')
@route('/map_5')
def map_01():
    return template('map_5.html')
@route('/map_6')
def map_01():
    return template('map_6.html')
@route('/map_7')
def map_01():
    return template('map_7.html')
@route('/map_8')
def map_01():
    return template('map_8.html')
@route('/map_9')
def map_01():
    return template('map_9.html')


@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text='', list_flag=False)


@route('/hello', method='POST')
def do_hello():
    input_text = request.forms.input_text

    
    # 地震 テキスト入力時用のフラグ（Trueだと出力値はリストデータ、デフォルトFalseは文字列データ）
    list_flag=False
    if "地震" in input_text:
        list_flag=True
        output_list = []
        output_list = pybot(input_text)
        return template('pybot_template', input_text=input_text, output_text=output_list, list_flag=list_flag)
    else:
        output_text = pybot(input_text)
        return template('pybot_template', input_text=input_text, output_text=output_text, list_flag=list_flag)

run(host='localhost', port=8080, debug=True)
