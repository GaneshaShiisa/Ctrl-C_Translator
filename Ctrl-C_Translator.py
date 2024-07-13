# Ctrl-C Translator
# 選択した文章を翻訳する。

from pynput import keyboard, mouse
import pyperclip
import threading
import tkinter
import ollama

root = tkinter.Tk()
root.overrideredirect(True)
root.configure(bg="lightblue")

# ウィンドウを最前面に設定
root.attributes("-topmost", True)

root.withdraw()

label = tkinter.Label(root, text="Hello, tkinter!")
label.pack()

model = "gemma2"

# マウスコントローラを作成
mouse_controller = mouse.Controller()


def ctrl(letter):
    return chr(ord(letter.upper())-64)


def on_release(key):
    try:
        if key.char == ctrl("c"):
            x, y = mouse_controller.position
            clipboard_text = pyperclip.paste()
            print(f"クリップボードの内容: {clipboard_text}")
            response = ollama.generate(
                model=model,
                prompt=f"Please translate '{clipboard_text}' into Japanese. Output only the translated Japanese text."
            )
            print(response['response'])
            label.config(text=response['response'])
            print(f'Key {key.char} pressed at mouse position: ({x}, {y})')

            root.geometry(f"+{x}+{y}")
            root.deiconify()
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        root.destroy()


def start_keyboard_listener():
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()


# キーボードリスナーを別のスレッドで実行
listener_thread = threading.Thread(target=start_keyboard_listener)
listener_thread.daemon = True
listener_thread.start()


def on_click(x, y, button, pressed):
    if pressed:
        # ウィンドウの位置とサイズを取得
        window_x = root.winfo_x()
        window_y = root.winfo_y()
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        # クリックがウィンドウの外側かをチェック
        if not (window_x <= x <= window_x + window_width and window_y <= y <= window_y + window_height):
            print("Clicked outside the window")
            # root.destroy()
            root.withdraw()


# マウスリスナーを別のスレッドで実行
listener = mouse.Listener(on_click=on_click)
listener_thread = threading.Thread(target=listener.start)
listener_thread.daemon = True
listener_thread.start()


def close_on_esc(event):
    root.destroy()


# ESCキーのバインディング
root.bind('<Escape>', close_on_esc)

root.mainloop()
