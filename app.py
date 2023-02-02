
from langchain import OpenAI
from flask import Flask, request
from gpt_index import GPTSimpleVectorIndex, LLMPredictor

app = Flask(__name__, static_folder='.')
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=1024))
index = GPTSimpleVectorIndex.load_from_disk('data.json', llm_predictor=llm_predictor)

# If you don't care about long answers, you can initialize the index with default 256 token limit simply by:
# index = GPTSimpleVectorIndex.load_from_disk('data.json')

@app.route('/answer', methods=['GET'])
def question():
    question = request.args.get('question')
    prompt = f'You are a helpful support agent. You are asked: "{question}". Try to use only the information provided. Format your answer nicely as a Markdown page.'
    response = index.query(prompt).response.strip()
    return app.response_class(response, mimetype='text/markdown')

@app.route('/')
def main():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=8080, threaded=True)