import tkinter as tk

class TicTacToe:
    def _init_(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.turn = "X"
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", width=10, height=5, command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)

    def play(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.turn
            self.turn = "X" if self.turn == "O" else "O"
            self.update_widgets()

    def update_widgets(self):
        for i in range(3):
            for j in range(3):
                self.master.children["!button"][i * 3 + j].config(text=self.board[i][j])

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()