from ollama import generate
import streamlit as st

MODEL_NAME = "gemma4"
SYSTEM_PROMPT = """You are a helpful assistant. Answer politely and clearly in Japanese when the user writes Japanese."""


def generate_prompt(history, user_input: str) -> str:
    prompt_lines = [SYSTEM_PROMPT, ""]
    for turn in history:
        prompt_lines.append(f"ユーザー: {turn['user']}")
        prompt_lines.append(f"アシスタント: {turn['assistant']}")
        prompt_lines.append("")
    prompt_lines.append(f"ユーザー: {user_input}")
    prompt_lines.append("アシスタント:")
    return "\n".join(prompt_lines)


def call_ollama(prompt: str) -> str:
    response = generate(
        model=MODEL_NAME,
        prompt=prompt,
    )
    return response["response"]


def init_session() -> None:
    if "history" not in st.session_state:
        st.session_state.history = []


def add_message(user_input: str, assistant_response: str) -> None:
    st.session_state.history.append(
        {"user": user_input, "assistant": assistant_response}
    )


def main() -> None:
    st.set_page_config(page_title="Ollama Agent", page_icon="🤖")
    st.title("Ollama Agent App")
    st.write(
        "Ollama の `gemma4` を直接呼び出して動かす基本的なエージェントUIです。"
    )

    init_session()

    with st.sidebar:
        st.header("セットアップ")
        st.write("事前に `ollama pull gemma4` を実行してください。")
        st.write(f"モデル: `{MODEL_NAME}`")
        st.write("`ollama` がインストールされていない場合は https://ollama.ai を確認してください。")

    user_input = st.text_area("メッセージを入力", height=140)
    submit = st.button("送信")

    if submit and user_input.strip():
        prompt = generate_prompt(st.session_state.history, user_input.strip())
        assistant_response = call_ollama(prompt)
        add_message(user_input.strip(), assistant_response)

    if st.session_state.history:
        st.markdown("## 会話履歴")
        for turn in st.session_state.history:
            st.markdown(f"**ユーザー:** {turn['user']}")
            st.markdown(f"**アシスタント:** {turn['assistant']}")
            st.write("---")

    st.markdown("### 使い方")
    st.write("上のテキストボックスに入力して `送信` を押すと、Ollama に問い合わせを送ります。")


if __name__ == "__main__":
    main()
