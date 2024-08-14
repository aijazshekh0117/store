from transformers import pipeline
summarizer = pipeline(
    'summarization',
    'pszemraj/long-t5-tglobal-base-16384-book-summary',
    )
long_text = "Here is a lot of text I don't want to read. Replace me"
result = summarizer(long_text)
print(result[0]['summary_text'])


import transformers
import torch

model_id = "meta-llama/Meta-Llama-3-8B"

pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
)
pipeline("Hey how are you doing today?")
