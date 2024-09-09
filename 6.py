import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文本编辑器")

        # 创建菜单栏
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # 创建文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="另存为", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="关闭", command=self.close_file)

        # 创建文本区域
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill="both")

        # 绑定事件来更新行数
        self.text_area.bind("<<Modified>>", self.update_line_count)

        # 创建状态栏
        self.status_bar = tk.Label(root, text="行数: 1", anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.root.title(f"文本编辑器 - {file_path}")
            self.update_line_count(None)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"文本编辑器 - {file_path}")

    def close_file(self):
        if messagebox.askokcancel("关闭", "确定要关闭文件吗?"):
            self.text_area.delete(1.0, tk.END)
            self.root.title("文本编辑器")
            self.update_line_count(None)

    def update_line_count(self, event):
        # 获取文本的总行数
        total_lines = int(self.text_area.index('end-1c').split('.')[0])
        # 更新状态栏显示
        self.status_bar.config(text=f"行数: {total_lines}")
        # 重置文本修改状态
        self.text_area.edit_modified(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

