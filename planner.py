from transformers import pipeline

# Load model locally
generator = pipeline('text-generation', model='distilgpt2')

def generate_todo(context):
    prompt = f"Based on this weather and news:\n{context}\nSuggest a simple to-do list for the day:"
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']
