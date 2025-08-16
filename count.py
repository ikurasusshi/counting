import tkinter as tk

def count_characters():
    # テキストボックスの内容を取得(最後の改行を除く)
    text = entry.get("1.0", "end-1c")
    count = len(text)
    result_label.config(text=f"文字数: {count}")

# ウィンドウを作成
root = tk.Tk()
root.title("文字数カウントアプリ")
root.geometry("400x300")

# テキスト入力欄
entry = tk.Text(root, height=8, width=40)
entry.pack(pady=10)

# カウントボタン
count_button = tk.Button(root, text="カウント", command=count_characters)
count_button.pack(pady=5)

# 結果表示ラベル
result_label = tk.Label(root, text="文字数: 0", font=("Arial", 14))
result_label.pack(pady=10)

# アプリを実行
root.mainloop()