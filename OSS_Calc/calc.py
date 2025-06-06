import tkinter as tk
import random

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
            ['=', '게임']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = "에러"
        elif char == '게임':
            self.open_game_window()
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def open_game_window(self):
        game_window = tk.Toplevel(self.root)
        game_window.title("계산기 게임")
        game_window.geometry("300x200")

        tk.Label(game_window, text="플레이할 게임을 선택하세요", font=("Arial", 16)).pack(pady=10)
        tk.Button(game_window, text="1. 숫자 야구", font=("Arial", 14), command=lambda: self.play_baseball(game_window)).pack(fill="x", padx=20, pady=5)
        tk.Button(game_window, text="2. 가위바위보", font=("Arial", 14), command=lambda: self.play_rsp(game_window)).pack(fill="x", padx=20, pady=5)

    def play_baseball(self, parent):
        baseball_window = tk.Toplevel(parent)
        baseball_window.title("숫자 야구 게임")
        baseball_window.geometry("300x200")

        secret = random.sample(range(1, 10), 3)
        attempts = 0

        tk.Label(baseball_window, text="1~9 중복 없는 3자리 숫자 입력", font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(baseball_window, font=("Arial", 14))
        entry.pack(pady=5)
        result_label = tk.Label(baseball_window, text="", font=("Arial", 12))
        result_label.pack(pady=5)

        def check_guess():
            nonlocal attempts
            guess = entry.get()
            if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3 or not all(1 <= int(c) <= 9 for c in guess):
                result_label.config(text="잘못된 입력! 1~9 중복 없는 3자리 숫자 입력")
                return

            guess = list(map(int, guess))
            strikes = sum(s == g for s, g in zip(secret, guess))
            balls = sum(g in secret for g in guess) - strikes
            attempts += 1
            result_label.config(text=f"{strikes} 스트라이크, {balls} 볼\n시도 횟수: {attempts}")

            if strikes == 3:
                result_label.config(text=f"정답! 숫자: {''.join(map(str, secret))}\n시도 횟수: {attempts}")
                entry.config(state="disabled")

        tk.Button(baseball_window, text="확인", font=("Arial", 12), command=check_guess).pack(pady=5)

    def play_rsp(self, parent):
        rsp_window = tk.Toplevel(parent)
        rsp_window.title("가위바위보 게임")
        rsp_window.geometry("300x150")

        tk.Label(rsp_window, text="1:가위 2:바위 3:보", font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(rsp_window, font=("Arial", 14))
        entry.pack(pady=5)
        result_label = tk.Label(rsp_window, text="", font=("Arial", 12))
        result_label.pack(pady=5)

        def check_rsp():
            choice = entry.get()
            if not choice in ['1', '2', '3']:
                result_label.config(text="1~3 중 입력하세요!")
                return

            user = int(choice)
            com = random.randint(1, 3)
            rsp = {1: '가위', 2: '바위', 3: '보'}
            result = ""
            if user == com:
                result = "비겼습니다!"
            elif (user == 1 and com == 3) or (user == 2 and com == 1) or (user == 3 and com == 2):
                result = "이겼습니다!"
            else:
                result = "졌습니다!"
            result_label.config(text=f"나: {rsp[user]} vs 컴퓨터: {rsp[com]}\n{result}")

        tk.Button(rsp_window, text="확인", font=("Arial", 12), command=check_rsp).pack(pady=5)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
