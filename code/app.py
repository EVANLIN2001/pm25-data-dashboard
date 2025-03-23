from flask import Flask, render_template
import requests

pm25_url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?language=zh&api_key=4114df9b-6af6-43f5-9eb8-ab89e5e6aadd"

# 對網址背後伺服器發送請求，已取得回應
response = requests.get(pm25_url)

# 將json格式轉換成字典dict{}
data = response.json()
# 將字典中的records列表取出
records_list = data.get("records", [])

#透過Flask建立一個簡易的網頁伺服器
app = Flask(__name__)

# 設定首頁路由
@app.route("/")
def home_page():
    # 使用render_template函式，將index.html渲染成完整的HTML文件
    # 並將渲染後的HTML文件傳遞給瀏覽器
    # 將records_list傳遞給index.html
    return render_template("index.html", records_list=records_list)


if __name__ == "__main__":
    # 啟動Flask伺服器，並設定debug模式
    # debug模式會在程式碼修改時自動重新啟動伺服器
    # port=5001 設定伺服器埠號為5001
    app.run(debug=True, port=5002)