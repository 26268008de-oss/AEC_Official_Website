from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPIの本体を立ち上げる
app = FastAPI()

# 🔴 CORSの設定（ここから追加）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 全ての場所からのアクセスを許可（開発中のみ）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ブラウザから「/（トップページ）」にアクセスが来たら、下の関数を実行する
@app.get("/")
def read_root():
    return {"message": "サークルサイトの裏側へようこそ！だぜ！"}

@app.get("/about")
def read_about():
    return {
        "overall": "当サークルは、楽曲制作から音響機材の自作、イベント運営まで『音』に関する全てを突き詰める音楽集団だぜ！",
        "dtm": "主に部員によるオリジナル楽曲の作成や、M3などの同人即売会でのCD・データ販売を行なっています！",
        "speaker": "音響機器の設計・作成から展示までを行なっています。市販品に負けない最高のスピーカーを自作するぜ！",
        "pa": "サークル内外のライブやイベントの際に、音響コントロールを行うPA（音響エンジニア）として現場を支えています！",
        "dj": "学外のイベントに積極的に参加し、他大学のDJサークルとの交流や、実際のクラブイベントへの出場を果たしています！"
    }

# 既存のコードの下に追記してくれ！

@app.get("/schedule")
def read_schedule():
    # 🔵 企業アピール：実務っぽいJSONの配列（リスト型データ）を返すぜ
    return [
        {"date": "2026年 6月", "title": "新歓DJイベント", "description": "他大学のDJサークルと合同でクラブを貸し切って、新入生歓迎イベントを開催するぜ！"},
        {"date": "2026年 8月", "title": "夏合宿（楽曲制作＆スピーカービルド）", "description": "山小屋にこもって2泊3日で爆音で曲を作り、スピーカーを自作する最高にテックな合宿だぜ！"},
        {"date": "2026年 11月", "title": "大学祭（メインステージPA＆ブース展示）", "description": "学祭のメインステージの音響（PA）をサークルで完全ジャック。DTM班のCD販売や自作スピーカー展示も行うぜ！"},
        {"date": "2026年 12月", "title": "同人即売会「M3」出展", "description": "音系メディアミックス同人即売会「M3」にサークル出展。部員が作ったコンピレーションアルバムを一般販売するぜ！"}
    ]