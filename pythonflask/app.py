
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 你的路由和视图函数

# 示例数据
images = [
    {"id": 1, "src": "D:/vsco/vsco-clone/photoappByVue-Python/pythonflask/icon.jpg"},
    {"id": 2, "src": "D:/vsco/vsco-clone/photoappByVue-Python/pythonflask/icon.jpg"},
    # 添加更多图片信息
]

# API端点：获取图片列表
@app.route('/api/images', methods=['GET'])
def get_images():
    return jsonify(images)

# API端点：添加新图片
@app.route('/api/images', methods=['POST'])
def add_image():
    image_data = request.json
    images.append(image_data)
    return jsonify(image_data), 201

# API端点：用户信息
@app.route('/api/userinfo', methods=['GET'])
def get_user_info():
    user_info = {"username": "User", "avatar": "https://example.com/avatar.jpg"}
    return jsonify(user_info)

if __name__ == '__main__':
    app.run(debug=True)
