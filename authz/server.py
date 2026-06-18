from flask import Flask, Response

app = Flask(__name__)

# Thêm route "/" để xử lý request mà Envoy đang gửi tới
@app.route("/", methods=["GET", "POST"])
@app.route("/check", methods=["GET", "POST"])
def check():
    print("Đã nhận request từ Envoy!")
    return Response("Authorized", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)