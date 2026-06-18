from flask import Flask, Response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/check", methods=["GET", "POST"])
def check():
    print("Envoy đã gửi yêu cầu tới Authz-service!")
    # Trả về 200 để Envoy cho phép truy cập tới Backend
    return Response("Authorized", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)