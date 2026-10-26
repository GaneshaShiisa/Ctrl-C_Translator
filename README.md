# Ctrl-C_Translator

テキストを選択して `Ctrl + C` を押すだけで、クリップボードの内容をローカルLLM（Ollama）を使って即座に日本語に翻訳し、マウスカーソル付近にポップアップ表示する軽量な翻訳ツールです。

---

## 🌟 特徴

- **ワンアクション翻訳**: テキストをコピー（`Ctrl + C`）するだけで自動的に翻訳が開始されます。
- **スマートなUI**:
  - 翻訳結果はマウスカーソルの位置に最前面ウィンドウ（枠なし）でポップアップ表示。
  - ウィンドウ外をクリックすると自動でポップアップが隠れます。
  - `Esc` キーを押すことでアプリケーションを終了できます。
- **ローカルLLMによる高速・セキュアな翻訳**:
  - [Ollama](https://ollama.com/) と `gemma2` モデルを利用。
  - 外部の翻訳APIキーや通信を必要とせず、プライバシーを保護したままオフラインでも利用可能。

---

## 📋 必要条件（Prerequisites）

1. **Python 3.8+**
2. **Ollama**:
   - [Ollama公式サイト](https://ollama.com/) からインストールしてください。
   - `gemma2` モデルを事前にダウンロード（プル）しておく必要があります:
     ```bash
     ollama run gemma2
     ```
     （または `ollama pull gemma2`）

---

## 🚀 インストール

必要な Python パッケージをインストールします。

```bash
pip install pynput pyperclip ollama
```

> **Note**: GUIツールキットとして `tkinter` を使用しています。Windowsの標準Python環境であれば通常同梱されていますが、Linux等の環境で不足している場合はパッケージマネージャーからインストールしてください。

---

## 💻 使い方

1. **スクリプトの起動**:
   ```bash
   python Ctrl-C_Translator.py
   ```

2. **翻訳の実行**:
   - 任意のブラウザやテキストエディタ等で翻訳したい英文を選択し、`Ctrl + C` を押します。
   - コピーされたテキストが Ollama (`gemma2`) に送信され、日本語に翻訳されます。
   - マウスカーソルの位置に翻訳結果のポップアップウィンドウが表示されます。

3. **ポップアップを閉じる / 終了**:
   - **閉じる（非表示）**: ポップアップ以外の画面外をクリックすると、ウィンドウが非表示（待機状態）になります。
   - **終了**: `Esc` キーを押すとスクリプト全体が終了します。

---

## ⚙️ カスタマイズ

`Ctrl-C_Translator.py` の以下の箇所を変更することで、モデルや翻訳プロンプトをカスタマイズできます。

- **使用するLLMモデルの変更**:
  ```python
  # 22行目
  model = "gemma2"  # 例: "llama3", "mistral", "qwen2.5" などに変更可能
  ```

- **プロンプト / 翻訳先言語の変更**:
  ```python
  # 38-41行目
  response = ollama.generate(
      model=model,
      prompt=f"Please translate '{clipboard_text}' into Japanese. Output only the translated Japanese text."
  )
  ```

---

## 📄 ライセンス

本プロジェクトは [MIT License](LICENSE) のもとで公開されています。
