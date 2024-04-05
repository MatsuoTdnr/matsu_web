import requests
import folium
import logging

def log_list_elements(lst):
    """
    リスト用ログファイル書き出し関数
    """
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    for item in lst:
        logging.info(item)

def quakeInfoData(quake_data):
    '''
    取得データから成形し出力する関数
    '''
    response_list = [];

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
            murl = f"map_{i}"
            
            low_list = []
            low_list.append(f"{i}|{time}|震源地:{name}|最大震度:{maxScale}|マグニチュード:{magnitude}")
            low_list.append(f"          |緯度:{latitude}|経度:{longitude}|（情報ソース: 気象庁|)")
            low_list.append(murl)
            
            log_list_elements(low_list)
            # 入れ子になっているので取り出すとき注意
            response_list.append(low_list)
            # 地図の作成
            m = folium.Map(location=[latitude, longitude], tiles='cartodbdark_matter', zoom_start=8)
            folium.Marker([latitude, longitude]).add_to(m)
            m.save(f"views/map_{i}.html")
    
    return response_list


def quake_command(command):
    # APIから情報取得
    p2papi_quake = "https://api.p2pquake.net/v2/history?codes=551&limit=10"

    # Jsonデータを配列に
    quake_data = requests.get(p2papi_quake).json()
    
    if '揺れた' in command:
        response = quakeInfoData(quake_data)
    elif '地震' in command:
        response = quakeInfoData(quake_data)
    else:
        response = "何言ッテルカワカラナイ"
    return response
