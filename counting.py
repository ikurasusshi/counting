import tkinter as tk

def count_characters():
    text = entry.get("1.0", "end-1c")
    count = len(text)
    result_label.config(text=f"文字数: {count}")


def reset_characters():
    entry.delete("1.0", "end")
    result_label.config(text="文字数: 0")

root = tk.Tk()
root.title("文字数カウントアプリ")
root.geometry("400x300")

entry = tk.Text(root, width=40, height=8)
entry.pack(pady=10)

count_button = tk.Button(root, text="カウント", command=count_characters)
count_button.pack(pady=5)

reset_button = tk.Button(root, text="クリア", command=reset_characters)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="文字数: 0", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()