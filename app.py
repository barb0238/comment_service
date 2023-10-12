
# comment_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

comments = {
    '1': {'user_id': '1', 'post_id': '1', 'comment': 'Amazing post!'},
    '2': {'user_id': '2', 'post_id': '2', 'comment': 'I did not know that!'},
}

@app.route('/comment/<id>', methods=['GET'])
def get_comment(id):
    return jsonify(comments.get(id, {}))

@app.route('/comment', methods=['POST'])
def create_comment():
    id = request.json.get('id')
    userId = request.json.get('user_id')
    postId = request.json.get('post_id')
    comment = request.json.get('comment')
    comments[id] = {'user_id': userId, 'post_id': postId, 'comment': comment}
    return jsonify(comments[id]), 201

if __name__ == '__main__':
    app.run(debug=True, port=5002)
