# %%

from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

# %%

model = AutoModelForCausalLM.from_pretrained(
    "roneneldan/TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-33M")

# %%


def predict(message):
    model_inputs = tokenizer.encode(message, return_tensors="pt")
    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(model_inputs[0]):]
    model_output_text = tokenizer.decode(
        model_outputs, skip_special_tokens=True)
    return model_output_text


for word, token_id in tqdm(tokenizer.get_vocab().items()):
    if 'accepted' in predict(word).lower():
        print(word, token_id)
