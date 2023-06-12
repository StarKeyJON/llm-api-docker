from flask import Flask, jsonify, request
from gpt4all import GPT4All

app = Flask(__name__)
gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy")

@app.route('/v0/language-models/chat-completions', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages')
    response = gptj.chat_completion(messages)
    return jsonify(response)

@app.route('/v0/language-models/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data['prompt']
    response = gptj.generate(prompt)
    return jsonify(response)

# @app.route('/v0/language-models/download', methods=['POST'])
# def download():
#     data = request.get_json()
#     model_filename = data['model_filename']
#     model_path = data['model_path']
#     response = gpt4all.GPT4All.download_model(model_filename, model_path)
#     return jsonify(response)

@app.route('/v0/language-models/retrieve', methods=['POST'])
def retrieve():
    data = request.get_json()
    model_name = data['model_name']
    model_path = data.get('model_path', None)
    allow_download = data.get('allow_download', True)
    response = GPT4All.retrieve_model(model_name, model_path, allow_download)
    return jsonify(response)

@app.route('/v0/models', methods=['GET'])
def models():
    response = GPT4All.list_models()
    return jsonify(response)

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8888)