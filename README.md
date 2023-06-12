# GPT4All Python API

## Intro

The GPT4All package provides Python bindings and an API to our C/C++ model backend libraries. This README will provide instructions on how to install and use the package, as well as an API reference for the available methods.

The material in this README is based on the documentation found at [GPT4All Python API](https://docs.gpt4all.io/gpt4all_python.html).

## Installation

To install the GPT4All package, run the following command:

```python
pip install gpt4all
```

## Quickstart

In Python, run the following commands to retrieve a GPT4All model and generate a response to a prompt:

```python
import gpt4all

gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
messages = [{"role": "user", "content": "Name 3 colors"}]
gptj.chat_completion(messages)
```

## Flask Server

A Flask server is included with the GPT4All Python API package. The server provides endpoints for chat completion, text generation, model retrieval, and model listing. Below is an example of how to use the Flask server to access the API's endpoints:

```python
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
    app.run(host='0.0.0.0', port=4200)
```

## Supported Models

Python bindings support the following ggml architectures: gptj, llama, mpt. See API reference for more details.

The supported architectures are:

- GPTJ - Based off of the GPT-J architecture with examples found [here](https://docs.gpt4all.io/examples/gptj_examples.html)
- LLAMA - Based off of the LLAMA architecture with examples found [here](https://docs.gpt4all.io/examples/llama_examples.html)
- MPT - Based off of Mosaic ML's MPT architecture with examples found [here](https://docs.gpt4all.io/examples/mpt_examples.html)

## Best Practices

There are two methods to interface with the underlying language model: `chat_completion()` and `generate()`. `chat_completion()` formats a user-provided message dictionary into a prompt template (see API documentation for more details and options). This will usually produce much better results and is the approach we recommend. You may also prompt the model with `generate()` which will just pass the raw input string to the model.

## API Reference

### `gpt4all.GPT4All(model_name, model_path=None, model_type=None, allow_download=True)`

Constructor

Parameters:

- `model_name` (str): Name of GPT4All or custom model. Including ".bin" file extension is optional but encouraged.
- `model_path` (str): Path to directory containing model file or, if file does not exist, where to download model. Default is None, in which case models will be stored in ~/.cache/gpt4all/.
- `model_type` (str): Model architecture. This argument currently does not have any functionality and is just used as descriptive identifier for user. Default is None.
- `allow_download` (bool): Allow API to download models from gpt4all.io. Default is True.

### `gpt4all.GPT4All.chat_completion(messages, default_prompt_header=True, default_prompt_footer=True, verbose=True, streaming=True, **generate_kwargs)`

Format list of message dictionaries into a prompt and call model generate on prompt. Returns a response dictionary with metadata and generated content.

Parameters:

- `messages` (List[Dict]): List of dictionaries. Each dictionary should have a "role" key with value of "system", "assistant", or "user" and a "content" key with a string value. Messages are organized such that "system" messages are at top of prompt, and "user" and "assistant" messages are displayed in order. Assistant messages get formatted as "Response: {content}".
- `default_prompt_header` (bool): If True (default), add default prompt header after any system role messages and before user/assistant role messages.
- `default_prompt_footer` (bool): If True (default), add default footer at end of prompt.
- `verbose` (bool): If True (default), print full prompt and generated response.
- `streaming` (bool): True if want output streamed to stdout.
- `**generate_kwargs`: Optional kwargs to pass to prompt context.

Returns:

- `dict`: Response dictionary with:
  - `"model"`: name of model.
  - `"usage"`: a dictionary with number of full prompt tokens, number of generated tokens in response, and total tokens.
  - `"choices"`: List of message dictionary where "content" is generated response and "role" is set as "assistant". Right now, only one choice is returned by model.

### `gpt4all.GPT4All.generate(prompt, streaming=True, **generate_kwargs)`

Surfaced method of running generate without accessing model object.

Parameters:

- `prompt` (str): Raw string to be passed to model.
- `streaming` (bool): True if want output streamed to stdout.
- `**generate_kwargs`: Optional kwargs to pass to prompt context.

Returns:

- `str`: Raw string of generated model response.

### `gpt4all.GPT4All.generator(prompt, **generate_kwargs)`

Surfaced method of running generate without accessing model object.

Parameters:

- `prompt` (str): Raw string to be passed to model.
- `streaming`: True if want output streamed to stdout.
- `**generate_kwargs`: Optional kwargs to pass to prompt context.

Returns:

- `str`: Raw string of generated model response.

## License

The GPT4All library has the following license:

MIT License

Copyright (c) 2023 Nomic, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Source

This README has been created based on the material found in the following sources:

- [GPT4All Python API](https://docs.gpt4all.io/gpt4all_python.html)
- [GPT4All FAQ](https://docs.gpt4all.io/faq.html)
