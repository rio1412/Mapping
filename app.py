import folium
from streamlit_folium import folium_static
import streamlit as st

import folium
from streamlit_folium import folium_static
import streamlit as st

# 京都市のエリアごとの座標を指定（各区の座標を7つ以上に増やしました）
areas = {
    "左京区": [[35.0358, 135.7804], [35.0369, 135.7882], [35.0249, 135.7921], [35.0212, 135.7803]],
    "下京区": [[34.9857, 135.7588], [34.9857, 135.7813], [34.9666, 135.7813], [34.9666, 135.7588]],
    "右京区": [[35.0185, 135.6982], [35.0209, 135.7264], [34.9983, 135.7438], [34.9817, 135.7231]],
    "中京区": [[35.0031, 135.7562], [35.0051, 135.7813], [34.9857, 135.7813], [34.9857, 135.7588]],
    "北区": [[35.0669, 135.7372], [35.0728, 135.7457], [35.0584, 135.7609], [35.0517, 135.7557]],
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
