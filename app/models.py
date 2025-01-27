from transformers import pipeline

# Load text-generation pipeline.
def load_generator():
    generator = pipeline("text-generation", model="gpt2")
    generator.tokenizer.truncation = True 
    return generator