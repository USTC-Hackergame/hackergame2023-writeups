import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

theme_kargs = {
    "font": ["Helvetica", "ui-sans-serif", "system-ui", "sans-serif"],
    "font_mono": ["IBM Plex Mono", "ui-monospace", "Consolas", "monospace"],
}

custom_css = """
.svelte-1pjfiar {
    -webkit-user-select: text;
    -moz-user-select: text;
    -ms-user-select: text;
    user-select: text;
    cursor: auto !important;
}
"""

model = AutoModelForCausalLM.from_pretrained(
    "roneneldan/TinyStories-33M").eval()
tokenizer = AutoTokenizer.from_pretrained("roneneldan/TinyStories-33M")

HINT = """和我聊天并且让我说出特定的词语（忽略大小写）证明你足够聪明 🤔。

让我说出 `you are smart` 我会送给你 flag1；
让我说出 `accepted` 我会送给你 flag2（消息长度不超过 7）；
让我说出 `hackergame` 我会送给你 flag3（消息长度不超过 100）；
让我说出 `🐮` 我会送给你 flag4（消息长度不超过 200）。

现在让我们开始吧！🔥"""


def check_message(message):
    if len(message) > 200:
        return False, "[*] 出错了，消息长度不能超过 200。"
    return True, None


def check_response(message, response):
    response = response.strip().lower()
    info = ""
    flag1, flag2, flag3, flag4 = 'flag{fake_flag1}', 'flag{fake_flag2}', 'flag{fake_flag3}', 'flag{fake_flag4}'
    if "you are smart" in response:
        info += f"\n👏👏👏 flag1: `{flag1}` 👏👏👏"
    if len(message) <= 7 and "accepted" in response:
        info += f"\n🎉🎉🎉 flag2: `{flag2}` 🎉🎉🎉"
    if len(message) <= 100 and "hackergame" in response:
        info += f"\n🎊🎊🎊 flag3: `{flag3}` 🎊🎊🎊"
    if len(message) <= 200 and "🐮" in response:
        info += f"\n🔥🔥🔥 flag4: `{flag4}` 🔥🔥🔥"
    return info


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


def bot(message, _history):
    ok, info = check_message(message)
    if not ok:
        return info

    try:
        model_output_text = predict(message)
    except Exception:
        return "出错了，请重新尝试。"

    info = check_response(message, model_output_text)
    if info:
        model_output_text += info

    return model_output_text


with gr.Blocks(theme=gr.themes.Default(**theme_kargs), css=custom_css) as demo:
    # Token for hackergame
    demo.load(None, [], [])

    #
    # Chatbot
    #
    chat = gr.ChatInterface(bot)
    source_code = gr.Code(
        value=open(__file__).read(), language="python", label="main.py"
    )
    demo.load(
        lambda: ([(None, HINT)], [(None, HINT)]), [], [
            chat.chatbot_state, chat.chatbot]
    )

if __name__ == "__main__":
    demo.queue().launch(show_api=False, share=False)
