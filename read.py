import sys
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

if (len(sys.argv) < 2):
    print("Usage: python read.py <path>")
    sys.exit(1)
documents = SimpleDirectoryReader(sys.argv[1], recursive=True).load_data()
index = GPTSimpleVectorIndex(documents)
index.save_to_disk('data.json')