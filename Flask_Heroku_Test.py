from flask import Flask

app=Flask(__name__) #創建一個Flask物件

#函式的裝飾器:以函式為基礎，提供附加的功能
@app.route("/")
def home():
    return "Hello Flask!"

#代表我們要處理的網站路徑
@app.route("/test")
def test():
    return "This is Test!"

if __name__=="__main__":
    app.run()