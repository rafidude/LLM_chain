from langchain.llms import OpenAI

import langchain
from langchain.cache import SQLiteCache
langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

r1 = llm("Tell me a joke")
print(r1)
r2 = llm("Tell me a joke")
print(r2)