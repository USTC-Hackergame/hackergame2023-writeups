import json
import pathlib

import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

root_dir = pathlib.Path('TinyStories-33M')
model = AutoModelForCausalLM.from_pretrained(root_dir).eval()
tokenizer = AutoTokenizer.from_pretrained(root_dir)


def predict(message):
    model_inputs = tokenizer.encode(message, return_tensors="pt")
    model_outputs = model.generate(
        model_inputs,
        max_new_tokens=30,
        num_beams=1,
        pad_token_id=tokenizer.eos_token_id,
    )
    model_outputs = model_outputs[0, len(model_inputs[0]) :]
    model_output_text = tokenizer.decode(model_outputs, skip_special_tokens=True)
    return model_output_text


def main() -> None:
    with open(root_dir / 'vocab.json', 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)
        for word in vocabulary:
            if len(word) > 7:
                continue
            output = predict(word)
            if 'accepted' in output:
                print(word, output)
                exit()


if __name__ == "__main__":
    main()
