from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check():
    # 1. In log để xem Envoy đang gửi cái gì sang
    headers = request.headers
    print(f"Headers nhận từ Envoy: {dict(headers)}")
    
    # 2. Logic kiểm tra giả lập:
    # Sau này chúng ta sẽ kiểm tra token ở đây
    # Hiện tại: Chỉ cho phép nếu có header 'x-auth-test'
    if headers.get("x-auth-test") == "secret":
        return jsonify({"allowed": True}), 200
    
    return jsonify({"allowed": False}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)