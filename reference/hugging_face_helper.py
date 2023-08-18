import os


from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

from langchain.agents import load_tools, initialize_agent


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


profile_link = "https://www.linkedin.com/in/richard-chen-082b868a/"

template = """Linked Profile: {profile_link}

Is this linked-in profile technical or non technical ?"""

prompt = PromptTemplate(template=template, input_variables=["profile_link"])

# repo_id = "facebook/bart-large-mnli"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options

repo_id = "meta-llama/Llama-2-7b"

llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.run(profile_link))




