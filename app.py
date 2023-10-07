import folium
from streamlit_folium import folium_static
import streamlit as st

import folium
from streamlit_folium import folium_static
import streamlit as st

# 京都市のエリアごとの座標を指定（各区の座標を7つ以上に増やしました）
areas = {
    "左京区": [
        [35.050, 135.760], [35.080, 135.780], [35.070, 135.820], [35.040, 135.810]
    ],
    "下京区": [
        [34.970, 135.750], [35.000, 135.770], [34.990, 135.810], [34.960, 135.790]
    ],
    "右京区": [
        [35.000, 135.670], [35.030, 135.710], [34.990, 135.740], [34.960, 135.700]
    ],
    "中京区": [
        [35.000, 135.740], [35.030, 135.760], [35.020, 135.790], [34.990, 135.780]
    ],
    "北区": [
        [35.070, 135.720], [35.100, 135.760], [35.090, 135.800], [35.060, 135.780]
    ],
}

# データを地図に渡す関数を作成する
def AreaMarker(m):
    for area, coords in areas.items():
        # ポリゴンを作成して地図に追加
        folium.Polygon(locations=coords, color=get_color(area), fill=True, fill_opacity=0.2).add_to(m)

        # エリア名の座標を取得
        centroid = [sum([coord[0] for coord in coords]) / len(coords),
                    sum([coord[1] for coord in coords]) / len(coords)]

        # エリア名を直接テキストとして配置
        folium.Marker(location=centroid, popup=area, icon=folium.DivIcon(icon_size=(50,12), icon_anchor=(0,0),
                      html=f'<div style="font-size: 0.2pt; background-color: {get_color(area)}; '
                           f'color: white; text-align: center; vertical-align: middle; line-height: 36px; '
                           f'border-radius: 5px;">{area}</div>')).add_to(m)

# エリアごとの色を返す関数
def get_color(area):
    colors = {
        "左京区": "red",
        "下京区": "blue",
        "右京区": "green",
        "中京区": "orange",
        "北区": "purple",
    }
    return colors.get(area, "gray")

# ------------------------画面作成------------------------

st.title("京都市の地図")  # タイトル
m = folium.Map(location=[35.0116, 135.7681], zoom_start=13)  # 地図の初期設定（中京区を中心に）
AreaMarker(m)  # データを地図に渡す
folium_static(m)  # 地図情報を表示
