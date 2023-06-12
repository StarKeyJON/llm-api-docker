
# GPT4All Flask Server

:TOC:

- [GPT4All Flask Server](#gpt4all-flask-server)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Supported Models](#supported-models)
  - [Getting the most of your local LLM](#getting-the-most-of-your-local-llm)
  - [Best Practices](#best-practices)
  - [API Endpoints](#api-endpoints)
    - [`/v0/language-models/chat-completions` (POST)](#v0language-modelschat-completions-post)
    - [`/v0/language-models/generate` (POST)](#v0language-modelsgenerate-post)
    - [`/v0/language-models/retrieve` (POST)](#v0language-modelsretrieve-post)
    - [`/v0/models` (GET)](#v0models-get)
  - [API References](#api-references)
    - [`gpt4all.GPT4All(model_name, model_path=None, model_type=None, allow_download=True)`](#gpt4allgpt4allmodel_name-model_pathnone-model_typenone-allow_downloadtrue)
    - [`gpt4all.GPT4All.chat_completion(messages, default_prompt_header=True, default_prompt_footer=True, verbose=True, streaming=True, **generate_kwargs)`](#gpt4allgpt4allchat_completionmessages-default_prompt_headertrue-default_prompt_footertrue-verbosetrue-streamingtrue-generate_kwargs)
    - [`gpt4all.GPT4All.generate(prompt, streaming=True, **generate_kwargs)`](#gpt4allgpt4allgenerateprompt-streamingtrue-generate_kwargs)
    - [`gpt4all.GPT4All.generator(prompt, **generate_kwargs)`](#gpt4allgpt4allgeneratorprompt-generate_kwargs)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

This repository contains the source code for a Flask server that provides endpoints for interacting with the GPT4All language models.
It includes a Dockerfile that allows for effortless containerization of the local LLM server, enhancing its portability and reproducibility across different platforms, as well as offering unrivaled privacy. Running a local LLM within a Docker container not only simplifies your setup process but also isolates the application and its dependencies, minimizing conflicts and ensuring a uniform operational environment.

The server supports chat completions, text generation, model retrieval, and model listing. It uses the GPT4All python bindings to interface with the models.

## Prerequisites

- Python 3.9
- Docker

## Getting Started

To run the server, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/StarKeyJON/llm-api-docker.git
   ```

2. Change to the project directory:

   ```shell
   cd llm-api-docker
   ```

    Make sure you have Docker downloaded and running.

3. Build the Docker image:

   ```shell
   yarn run docker_build
   ```

4. Run the Docker container:

   ```shell
   yarn run docker_run
   ```

   The server will start running on `http://localhost:8888`.

## Supported Models

Python bindings support the following ggml architectures: gptj, llama, mpt. See API reference for more details.

The supported architectures are:

- GPTJ - Based off of the GPT-J architecture with examples found [here](https://docs.gpt4all.io/examples/gptj_examples.html)
- LLAMA - Based off of the LLAMA architecture with examples found [here](https://docs.gpt4all.io/examples/llama_examples.html)
- MPT - Based off of Mosaic ML's MPT architecture with examples found [here](https://docs.gpt4all.io/examples/mpt_examples.html)

<details>
<summary>Currently listed models retrieved from the /v0/models endpoint</summary>

```javascript
[
 {
  "bestGPTJ": "true",
  "description": "GPT-J 6B finetuned by Nomic AI on the latest GPT4All dataset.<br>- Licensed for commercial use.<br>- Fast responses.",
  "filename": "ggml-gpt4all-j-v1.3-groovy.bin",
  "filesize": "3785248281",
  "isDefault": "true",
  "md5sum": "81a09a0ddf89690372fc296ff7f625af"
 },
 {
  "bestLlama": "true",
  "description": "LLaMA 13B finetuned by Nomic AI on the latest GPT4All dataset.<br>- Cannot be used commercially.<br>- Slower responses but higher quality.",
  "filename": "ggml-gpt4all-l13b-snoozy.bin",
  "filesize": "8136770688",
  "md5sum": "91f886b68fbce697e9a3cd501951e455"
 },
 {
  "bestMPT": "true",
  "description": "MPT 7B chat model trained by Mosaic ML.<br>- Cannot be used commercially.<br>- Fast responses.",
  "filename": "ggml-mpt-7b-chat.bin",
  "filesize": "4854401050",
  "isDefault": "true",
  "md5sum": "756249d3d6abe23bde3b1ae272628640",
  "requires": "2.4.1"
 },
 {
  "description": "LLaMa 13B finetuned on over 300,000 curated and uncensored instructions instructions.<br>- Cannot be used commercially.<br>- Best finetuned LLaMA model.<br>- This model was fine-tuned by Nous Research, with Teknium and Karan4D leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors. The result is an enhanced Llama 13b model that rivals GPT-3.5-turbo in performance across a variety of tasks. This model stands out for its long responses, low hallucination rate, and absence of OpenAI censorship mechanisms.",
  "filename": "ggml-v3-13b-hermes-q5_1.bin",
  "filesize": "8136777088",
  "md5sum": "f26b99c320ff358f4223a973217eb31e",
  "requires": "2.4.5",
  "url": "https://huggingface.co/eachadea/ggml-nous-hermes-13b/resolve/main/ggml-v3-13b-hermes-q5_1.bin"
 },
 {
  "description": "LLaMA 7B finetuned by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.<br>- Cannot be used commercially.",
  "filename": "ggml-vicuna-7b-1.1-q4_2.bin",
  "filesize": "4212859520",
  "md5sum": "29119f8fa11712704c6b22ac5ab792ea"
 },
 {
  "description": "LLaMA 13B and trained by teams from UC Berkeley, CMU, Stanford, MBZUAI, and UC San Diego.<br>- Cannot be used commercially.",
  "filename": "ggml-vicuna-13b-1.1-q4_2.bin",
  "filesize": "8136770688",
  "md5sum": "95999b7b0699e2070af63bf5d34101a8"
 },
 {
  "description": "LLaMA 7B finetuned by Microsoft and Peking University.<br>- Cannot be used commercially.",
  "filename": "ggml-wizardLM-7B.q4_2.bin",
  "filesize": "4212864640",
  "md5sum": "99e6d129745a3f1fb1121abed747b05a"
 },
 {
  "description": "LLaMa 13B finetuned with RLHF by Stability AI.<br>- Cannot be used commercially.",
  "filename": "ggml-stable-vicuna-13B.q4_2.bin",
  "filesize": "8136777088",
  "md5sum": "6cb4ee297537c9133bddab9692879de0"
 },
 {
  "description": "MPT 7B pre-trained by Mosaic ML. Trained for text completion with no assistant finetuning.<br>- Licensed for commercial use.",
  "filename": "ggml-mpt-7b-base.bin",
  "filesize": "4854401028",
  "md5sum": "120c32a51d020066288df045ef5d52b9",
  "requires": "2.4.1"
 },
 {
  "description": "LLaMa 13B fine-tuned on ~180,000 instructions by Nous Research.<br>- Cannot be used commercially.",
  "filename": "ggml-nous-gpt4-vicuna-13b.bin",
  "filesize": "8136777088",
  "md5sum": "d5eafd5b0bd0d615cfd5fd763f642dfe"
 },
 {
  "description": "MPT 7B instruction finetuned by Mosaic ML.<br>- Licensed for commercial use.",
  "filename": "ggml-mpt-7b-instruct.bin",
  "filesize": "4854401028",
  "md5sum": "1cfa4958f489f0a0d1ffdf6b37322809",
  "requires": "2.4.1"
 },
 {
  "description": "LLaMa 13B finetuned on the uncensored assistant and instruction data.<br>- Cannot be used commercially.",
  "filename": "ggml-wizard-13b-uncensored.bin",
  "filesize": "8136777088",
  "md5sum": "679fc463f01388ea2d339664af0a0836"
 },
 {
  "description": "Replit 3B code model trained on subset of the Stack. Licensed for commercial use.",
  "filename": "ggml-replit-code-v1-3b.bin",
  "filesize": "5202046853",
  "md5sum": "615890cb571fcaa0f70b2f8d15ef809e",
  "requires": "2.4.7",
  "url": "https://huggingface.co/nomic-ai/ggml-replit-code-v1-3b/resolve/main/ggml-replit-code-v1-3b.bin"
 }
]
```

</details>
## Getting the most of your local LLM

Inference Speed Inference speed of a local LLM depends on two factors: model size and the number of tokens given as input. It is not advised to prompt local LLMs with large chunks of context as their inference speed will heavily degrade. You will likely want to run GPT4All models on GPU if you would like to utilize context windows larger than 750 tokens. Native GPU support for GPT4All models is planned.

Inference Performance Which model is best? That question depends on your use-case. The ability of an LLM to faithfully follow instructions is conditioned on the quantity and diversity of the pre-training data it trained on and the diversity, quality and factuality of the data the LLM was fine-tuned on. A goal of GPT4All is to bring the most powerful local assistant model to your desktop and Nomic AI is actively working on efforts to improve their performance and quality.

## Best Practices

There are two methods to interface with the underlying language model: `chat_completion()` and `generate()`. `chat_completion()` formats a user-provided message dictionary into a prompt template (see API documentation for more details and options). This will usually produce much better results and is the approach we recommend. You may also prompt the model with `generate()` which will just pass the raw input string to the model.

## API Endpoints

The server provides the following API endpoints:

### `/v0/language-models/chat-completions` (POST)

This endpoint performs chat completions using the GPT4All model. It expects a JSON payload with a `messages` field containing an array of message objects. Each message object should have a `role` ("system", "user", or "assistant") and `content` (the message text).

Example request payload:

```json
{
  "messages": [
    {"role": "user", "content": "Tell me a joke"},
    {"role": "assistant", "content": "Why don't scientists trust atoms?"},
    {"role": "user", "content": "I don't know, why?"},
    {"role": "assistant", "content": "Because they make up everything!"}
  ]
}
```

Example response:

```json
{
  "id": "chat-completions-1623419351.123456",
  "replies": [
    {"role": "assistant", "content": "Because they make up everything!"}
  ]
}
```

### `/v0/language-models/generate` (POST)

This endpoint generates text based on a given prompt using the GPT4All model. It expects a JSON payload with a `prompt` field containing the text prompt.

Example request payload:

```json
{
  "prompt": "Once upon a time"
}
```

Example response:

```json
{
  "id": "generate-1623419351.123456",
  "text": "Once upon a time, in a land far away..."
}
```

### `/v0/language-models/retrieve` (POST)

This endpoint retrieves a pre-trained model for use with the GPT4All ecosystem. It expects a JSON payload with a `model_name` field specifying the model to retrieve. Optionally, you can provide a `model_path` to specify the directory to save the model, and an `allow_download` flag to control whether the model can be downloaded.

Example request payload:

```json
{
  "model_name": "gptj",
  "model_path": "/path/to/save/model",
  "allow_download": true
}
```

Example response:

```json
{
  "success": true,
  "message": "Model retrieved successfully."
}
```

### `/v0/models` (GET)

This endpoint lists the available models in the GPT4All ecosystem.

Example response:

```json
{
  "models": ["gptj", "llama", "mpt"]
}
```

## API References

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

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This project leverages the GPT4All python bindings and the ggml library. For more information about the supported model architectures and their differences, refer to the [GPT4All FAQ](https://github.com/nomic-ai/gpt4all#faq).

For any questions or issues, please refer to the [GPT4All repository](https://github.com/nomic-ai/gpt4all) or contact the GPT4All team.
