import requests
import folium

def quakeDataPrint(quake_data):
    '''
    取得データから成形し出力する関数
    '''
    for i in range(len(quake_data)):
        if quake_data[i]['earthquake']['hypocenter']['name'] != '':
            name = str(quake_data[i]['earthquake']['hypocenter']['name'])
            maxScale_raw = str(quake_data[i]['earthquake']['maxScale'])
            time = str(quake_data[i]['earthquake']['time'])
            magnitude = str(quake_data[i]['earthquake']['hypocenter']['magnitude'])
            latitude = str(quake_data[i]['earthquake']['hypocenter']['latitude'])
            longitude = str(quake_data[i]['earthquake']['hypocenter']['longitude'])
            # API用震度データと震度表記の対応の辞書
            ms = {
                '-1': 'None',
                '10': '1',
                '20': '2',
                '30': '3',
                '40': '4',
                '45': '5-',
                '50': '5+',
                '55': '6-',
                '60': '6+',
                '70': '7',
            }
            maxScale = ms[maxScale_raw]
            if name == "":
                name = "None"
            
            if magnitude == "-1":
                magnitude = "None"
            
            print(f"{i}|{time}|震源地:{name}|最大震度:{maxScale}|マグニチュード:{magnitude}")
            print(f"　　　　　　　　　　  |緯度:{latitude}|経度:{longitude}|source: 気象庁|\n")

def maxData(quake_data):
    '''
    取得データから一番最大だったデータだけ表示する関数
    '''
    # 最大値を保持するための変数
    max_value = None
    # 最大値のインデックスを保持するための変数
    max_index = None
    
    # 震度だけのリストを用意
    quake_scale_list = []
    
    for i in range(len(quake_data)):
        # データがある時
        if quake_data[i]['earthquake']['hypocenter']['name'] != '':
            maxScale_raw = str(quake_data[i]['earthquake']['maxScale'])
            # max_valueが初期値またはmax_value保持データより大きかった時の処理
            if max_value is None or maxScale_raw > max_value:
                # このデータを使う
                max_value = maxScale_raw
                max_quake_data = quake_data[i]
    
                
    # 最大値のindexが保持されているのを前提に取得　forの後
    name = str(max_quake_data['earthquake']['hypocenter']['name'])
    time = str(max_quake_data['earthquake']['time'])
    magnitude = str(max_quake_data['earthquake']['hypocenter']['magnitude'])
    latitude = str(max_quake_data['earthquake']['hypocenter']['latitude'])
    longitude = str(max_quake_data['earthquake']['hypocenter']['longitude'])
    
    ms = {
        '-1': 'None',
        '10': '1',
        '20': '2',
        '30': '3',
        '40': '4',
        '45': '5-',
        '50': '5+',
        '55': '6-',
        '60': '6+',
        '70': '7',
    }
    
    maxScale = ms[max_value]
    if name == "":
        name = "None"
                
    if magnitude == "-1":
        magnitude = "None"
    # 地図の作成
    m = folium.Map(location=[latitude, longitude], tiles='cartodbdark_matter', zoom_start=8)
    folium.Marker([latitude, longitude]).add_to(m)
    
    m.save("map/index.html")
    
    print(f"{time}|震源地:{name}|最大震度:{maxScale}|マグニチュード:{magnitude}")
    print(f"　　　　　　　　　  |緯度:{latitude}|経度:{longitude}|source: 気象庁|")
    print("⇒地図\n")
    # print(max_value)
    # print(max_index)


# 日付指定
#p2papi_quake = "https://api.p2pquake.net/v2/jma/quake?limit=10&order=1&since_date=20240401&until_date=20240402"
p2papi_quake = "https://api.p2pquake.net/v2/history?codes=551&limit=10"

# Jsonデータを配列に
quake_data = requests.get(p2papi_quake).json()

'''
デバッグ用コマンド
「デバッグ」で全jsonデータ表示

'''
first_msg = "コマンド案内｜地震：最新地震情報10件   終了:さようなら\n　　　　　　｜最大:10件中の最大震度1件と地図生成"
print(first_msg)

while True:
    command = input('pybot>')
    
    if 'こんにちは' in command:
        print('コンニチハ')
    elif '最大' in command:
        maxData(quake_data)
    elif '地震' in command:
        quakeDataPrint(quake_data)
    elif 'デバッグ' in command:
        print("デバッグ用データを表示します")
        print("現在は未使用です")
    elif 'ありがとう' in command:
        print('ドウイタシマシテ')
    elif 'さようなら' in command:
        print('サヨウナラ')
        break
    else:
        print('何言ッテルカワカラナイ')

print("チャットボットは終了しました")



















