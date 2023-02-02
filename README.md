# Text Surfer

An example GPT bot that can quickly read a lot of text or documentation and then answers questions about it.

<img src="https://i.imgur.com/hgBoKUV.png" width="574">

## Usage

First you will need to get an OpenAI API key. You can get one [here](https://beta.openai.com/), and will have $18 of free credits to start with. 
Set the API key as an environment variable

```bash
export OPENAI_API_KEY=sk-...
```

Install dependencies

```bash
pip install -r requirements.txt
```

Now you need to prepare the data. You need a directory with a bunch of text/markdown documents with any extension; it can have any structure, 
the script will scan it recursively. Avoid having binaries and other garbage in there. The script will preprocess the text with OpenAI's cheap Ada model,
it will cost around $0.50 per 1M words. The result will be stored in `data.json` file.

```bash
python read.py <path-to-docs>
```

Now you can run the bot server

```bash
python app.py
```

Visit http://localhost:8080 and ask it some questions