import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageFlipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像展示和翻转")

        # 创建按钮和标签
        self.btn_select_image = tk.Button(root, text="选择图像", command=self.select_image)
        self.btn_select_image.pack(side=tk.TOP, pady=10)

        self.btn_run = tk.Button(root, text="Run", command=self.flip_image, state=tk.DISABLED)
        self.btn_run.pack(side=tk.TOP, pady=10)

        # 创建左侧和右侧标签来展示图像
        self.image_label = tk.Label(root)
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.flipped_image_label = tk.Label(root)
        self.flipped_image_label.pack(side=tk.RIGHT, padx=10, pady=10)

        # 初始化图像变量
        self.image = None
        self.flipped_image = None

    def select_image(self):
        # 打开文件选择对话框并选择图像
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")]
        )
        if file_path:
            # 使用 PIL 打开图像
            self.image = Image.open(file_path)
            # 显示原始图像
            self.display_image(self.image, self.image_label)
            # 激活 Run 按钮
            self.btn_run.config(state=tk.NORMAL)

    def display_image(self, image, label):
        # 调整图像大小以适应 GUI 并在标签中显示
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # 保存对 image 对象的引用

    def flip_image(self):
        if self.image:
            # 对图像进行上下翻转
            self.flipped_image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            # 在右侧标签中显示翻转后的图像
            self.display_image(self.flipped_image, self.flipped_image_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFlipperApp(root)
    root.mainloop()

