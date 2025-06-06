import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '시속-마일']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.button_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = "에러"
        elif char == '시속-마일':
            self.convert_kph_to_mph()
        else:
            self.expression += str(char)

        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def convert_kph_to_mph(self):
        try:
            # 입력창의 값을 읽어서 km/h로 간주
            kph = float(self.expression)
            mph = kph * 0.621371
            self.expression = f"{mph:.2f} mph"
            self.update_entry()
        except:
            self.expression = "입력 오류"
            self.update_entry()

root = tk.Tk()
app = Calculator(root)
root.mainloop()
