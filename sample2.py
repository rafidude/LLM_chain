from langchain.llms import OpenAI

# text-ada-001, gpt-3.5-turbo
llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*3)
print(len(llm_result.generations))
for txt in llm_result.generations:
    print(txt)