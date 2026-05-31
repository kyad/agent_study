# agent_study

LangChainによるAgentやMCPの勉強用リポジトリ

## 使い方

```
ollama pull gemma4
uv run langchain_sample.py
uv run func_calling.py
uv run mcp_cli.py
```

## Streamlit アプリ

このリポジトリには、直接 `ollama` を呼び出して `gemma4` モデルを使う Streamlit アプリ `streamlit_app.py` が含まれています。

### セットアップ

1. 依存関係をインストールします。

```bash
uv run pip install streamlit
```

2. `gemma4` モデルをダウンロードします。

```bash
ollama pull gemma4
```

### アプリ起動

```bash
streamlit run streamlit_app.py
```

### 使い方

- 起動後、ブラウザに表示されたテキスト入力欄に質問や指示を入力します。
- `送信` ボタンを押すと、Ollama に問い合わせが送信されて応答が表示されます。
- 会話履歴は画面に保存され、過去のやりとりを確認できます。

### 注意点

- `ollama` コマンドがシステムの PATH に設定されている必要があります。
- `gemma4` モデルがダウンロード済みであることを確認してください。
