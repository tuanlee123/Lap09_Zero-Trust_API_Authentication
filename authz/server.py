from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check():
    # 1. In ra toàn bộ header mà Envoy gửi sang để debug
    print("Headers received from Envoy:", request.headers)
    
    # 2. Logic kiểm tra giả lập
    # Nếu client có header "Authorization", ta cho qua (tạm thời)
    if "Authorization" in request.headers:
        return jsonify({"allowed": True}), 200
    
    return jsonify({"allowed": False}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)