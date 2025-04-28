import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import date

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://streamlit.io/community',
        'Report a bug': 'https://github.com/streamlit/streamlit/issues',
        'About': '# Streamlit 初心者向けデモ\nこのアプリはStreamlitの基本的な機能を学ぶためのデモです。'
    }
)

# カスタムCSS
st.markdown("""
<style>
    /* 全体のフォント設定 */
    * {
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* ヘッダーのスタイル */
    h1 {
        color: #1E88E5;
        font-weight: 700;
        padding-bottom: 10px;
        border-bottom: 2px solid #1E88E5;
    }
    
    h2 {
        color: #0D47A1;
        font-weight: 600;
        margin-top: 30px;
    }
    
    h3 {
        color: #1565C0;
        font-weight: 500;
    }
    
    /* サイドバーのスタイル */
    .css-1d391kg {
        background-color: #f5f7f9;
    }
    
    /* カードスタイル */
    .card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* ボタンスタイル */
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 8px 16px;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: #0D47A1;
    }
    
    /* 成功メッセージ */
    .success-msg {
        background-color: #EEFAE7;
        color: #2E7D32;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #2E7D32;
    }
    
    /* 情報メッセージ */
    .info-msg {
        background-color: #E3F2FD;
        color: #0D47A1;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #0D47A1;
    }
    
    /* コードブロック */
    code {
        border-radius: 5px;
        background-color: #f5f7f9;
    }
    
    /* タブのスタイル */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 4px 4px 0px 0px;
        padding: 10px 20px;
        background-color: #f0f2f6;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1E88E5 !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# サイドバー 
# ============================================
with st.sidebar:
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    st.title("Streamlit デモ")
    
    st.divider()
    
    st.header("デモのガイド")
    st.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")
    
    # サイドバーにナビゲーションを追加
    demo_section = st.radio(
        "セクション選択",
        ["基本的なUI要素", "レイアウト", "データ表示", "グラフ表示", "インタラクティブ機能", "カスタマイズ"]
    )
    
    st.divider()
    
    # サイドバーの下部に日付と時間を表示
    today = date.today().strftime("%Y年%m月%d日")
    st.markdown(f"**今日の日付:** {today}")
    
    # テーマ切り替え
    theme = st.selectbox("テーマを選択", ["ライト", "ダーク", "ブルー"])

# ============================================
# メインコンテンツ
# ============================================
st.title("Streamlit 初心者向けデモ")
st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")

# 説明カード
st.markdown("""
<div class="card info-msg">
    <h4>ようこそ！</h4>
    <p>このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。以下のセクションを操作して、Streamlitの魅力を体験してみてください。</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# 基本的なUI要素
# ============================================
if demo_section == "基本的なUI要素":
    st.header("基本的なUI要素")
    
    # テキスト入力
    st.subheader("テキスト入力")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        name = st.text_input("あなたの名前", "ゲスト")
        st.write(f"こんにちは、**{name}**さん！")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ボタン
    st.subheader("ボタン")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if st.button("クリックしてください"):
            st.markdown('<div class="success-msg">ボタンがクリックされました！</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # チェックボックス
    st.subheader("チェックボックス")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
            st.markdown('<div class="info-msg">これは隠れたコンテンツです！</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # スライダー
    st.subheader("スライダー")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        age = st.slider("年齢", 0, 100, 25)
        st.write(f"あなたの年齢: **{age}**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # セレクトボックス
    st.subheader("セレクトボックス")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        option = st.selectbox(
            "好きなプログラミング言語は?",
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
        )
        st.write(f"あなたは**{option}**を選びました")
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# レイアウト
# ============================================
elif demo_section == "レイアウト":
    st.header("レイアウト")
    
    # カラム
    st.subheader("カラムレイアウト")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**左カラム**")
        st.number_input("数値を入力", value=10)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write("**右カラム**")
        st.metric("メトリクス", "42", "2%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # タブ
    st.subheader("タブ")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
    with tab1:
        st.write("これは第1タブの内容です")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.write("これは第2タブの内容です")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # エクスパンダー
    st.subheader("エクスパンダー")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    with st.expander("詳細を表示"):
        st.write("これはエクスパンダー内の隠れたコンテンツです")
        st.code("print('Hello, Streamlit！')")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# データ表示
# ============================================
elif demo_section == "データ表示":
    st.header("データの表示")
    
    # サンプルデータフレームを作成
    df = pd.DataFrame({
        '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
        '年齢': [25, 30, 22, 28, 33],
        '都市': ['東京', '大阪', '福岡', '札幌', '名古屋'],
        '売上': [120000, 85000, 210000, 96000, 175000]
    })
    
    # データフレーム表示
    st.subheader("データフレーム")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.dataframe(df.style.highlight_max(axis=0, color='#E3F2FD'), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # テーブル表示
    st.subheader("テーブル")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.table(df)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # メトリクス表示
    st.subheader("メトリクス")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("温度", "23°C", "1.5°C")
    col2.metric("湿度", "45%", "-5%")
    col3.metric("気圧", "1013hPa", "0.1hPa")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# グラフ表示
# ============================================
elif demo_section == "グラフ表示":
    st.header("グラフの表示")
    
    # ラインチャート
    st.subheader("ラインチャート")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C'])
    st.line_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # バーチャート
    st.subheader("バーチャート")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'カテゴリ': ['A', 'B', 'C', 'D'],
        '値': [10, 25, 15, 30]
    }).set_index('カテゴリ')
    st.bar_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # エリアチャート
    st.subheader("エリアチャート")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    area_data = pd.DataFrame(
        np.random.randn(20, 3).cumsum(axis=0),
        columns=['X', 'Y', 'Z'])
    st.area_chart(area_data)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# インタラクティブ機能
# ============================================
elif demo_section == "インタラクティブ機能":
    st.header("インタラクティブ機能")
    
    # プログレスバー
    st.subheader("プログレスバー")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    progress = st.progress(0)
    if st.button("進捗をシミュレート"):
        for i in range(101):
            time.sleep(0.01)
            progress.progress(i / 100)
        st.balloons()
        st.success("完了しました！")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ファイルアップロード
    st.subheader("ファイルアップロード")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
    if uploaded_file is not None:
        # ファイルのデータを表示
        bytes_data = uploaded_file.getvalue()
        st.write(f"ファイルサイズ: **{len(bytes_data)}** bytes")
        
        # CSVの場合はデータフレームとして読み込む
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.write("CSVデータのプレビュー:")
            st.dataframe(df.head(), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 日付選択
    st.subheader("日付選択")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    selected_date = st.date_input("日付を選択")
    st.write(f"選択された日付: **{selected_date}**")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# カスタマイズ
# ============================================
elif demo_section == "カスタマイズ":
    st.header("スタイルのカスタマイズ")
    
    # カスタムCSS
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #1E88E5;
        background: linear-gradient(45deg, #1E88E5, #5E35B1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px 0;
    }
    .animated-text {
        animation: fadeIn 2s infinite alternate;
    }
    @keyframes fadeIn {
        from { opacity: 0.7; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font animated-text">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)
    
    # カードスタイル
    st.subheader("カスタムカード")
    st.markdown("""
    <div style="background: linear-gradient(45deg, #1E88E5, #5E35B1); border-radius: 10px; padding: 20px; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
        <h3 style="margin-top: 0;">グラデーションカード</h3>
        <p>このカードはカスタムCSSでグラデーション背景を適用しています。</p>
        <button style="background: white; color: #1E88E5; border: none; padding: 8px 16px; border-radius: 5px; font-weight: bold; cursor: pointer;">アクション</button>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# デモの使用方法
# ============================================
st.divider()
st.subheader("このデモの使い方")
st.markdown("""
<div class="card info-msg">
    <ol>
        <li>コードエディタでコメントアウトされた部分を見つけます（#で始まる行）</li>
        <li>確認したい機能のコメントを解除します（先頭の#を削除）</li>
        <li>変更を保存して、ブラウザで結果を確認します</li>
        <li>様々な組み合わせを試して、UIがどのように変化するか確認しましょう</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.code("""
# コメントアウトされた例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")

# コメントを解除した例:
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")
""")

# フッター
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 1px solid #e6e6e6; color: #666;">
    <p>Streamlit デモアプリケーション</p>
    <p style="font-size: 0.8em;">© 2025 Streamlit Demo</p>
</div>
""", unsafe_allow_html=True)