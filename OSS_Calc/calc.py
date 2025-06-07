import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("320x420")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(10,0), ipadx=8, ipady=15, sticky="nsew")

        # 커서 위치 표시 라벨
        self.cursor_label = tk.Label(root, text="커서 위치: 0", font=("Arial", 12), anchor="w")
        self.cursor_label.grid(row=1, column=0, columnspan=4, padx=10, pady=(0,10), sticky="w")

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '←', '→']
        ]

        # 버튼 생성 및 grid 배치
        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                if char == '':
                    continue  # 빈칸은 버튼 생성하지 않음
                btn = tk.Button(
                    root,
                    text=char,
                    font=("Arial", 18),
                    width=5,
                    height=2,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.grid(row=i+2, column=j, padx=3, pady=3, sticky="nsew")

        # grid row/column weight로 크기 자동 조절
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        # 입력창 커서 이동/입력 시 커서 위치 업데이트
        self.entry.bind('<KeyRelease>', lambda e: self.update_cursor_label())
        self.entry.bind('<ButtonRelease-1>', lambda e: self.update_cursor_label())

        # 최초 표시
        self.update_cursor_label()

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                self.expression = str(eval(self.entry.get()))
            except Exception:
                self.expression = "에러"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
        elif char == '←':
            pos = self.entry.index(tk.INSERT)
            if pos > 0:
                self.entry.icursor(pos - 1)
        elif char == '→':
            pos = self.entry.index(tk.INSERT)
            if pos < len(self.entry.get()):
                self.entry.icursor(pos + 1)
        else:
            pos = self.entry.index(tk.INSERT)
            self.entry.insert(pos, char)
            self.expression = self.entry.get()
        self.update_cursor_label()

    def update_cursor_label(self):
        pos = self.entry.index(tk.INSERT)
        self.cursor_label.config(text=f"커서 위치: {pos}")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
