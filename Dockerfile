FROM python:3.9-slim

RUN apt-get update && apt-get install -y build-essential cmake git

RUN git clone --recurse-submodules https://github.com/nomic-ai/gpt4all
RUN cd gpt4all/gpt4all-backend/ && mkdir build && cd build && cmake .. && cmake --build . --parallel

RUN cd /gpt4all/gpt4all-bindings/python && pip install -e .

RUN pip install flask

COPY server.py /app/server.py

WORKDIR /app

CMD ["python", "server.py"]