from tkinter import *
from tkinter import ttk


class Sudoku:
    def __init__(self, filename):
        self.file = open(filename, "r").readlines()
        self.grid = [[" " for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.grid[j][i] = self.file[j][i]

    def display(self):
        file = open(input("Entrez le nom du fichier pour le Sudoku résolu: "), "w")
        root = Tk()
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        for i in range(9):
            if i % 3 == 0 and i > 0:
                file.write("\n")
            for j in range(9):
                if j % 3 == 0 and j > 0:
                    file.write(" ")
                    print(" ", end=' ')
                if self.grid[i][j] == self.file[i][j]:
                    ttk.Label(frm, text=str(self.grid[i][j])).grid(column=j, row=i)
                else:
                    ttk.Label(frm, text=str(self.grid[i][j]), background="red").grid(column=j, row=i)
                file.write(self.grid[i][j])
                print(self.grid[i][j], end=' ')
            print("\n")
            file.write("\n")
        root.mainloop()
        file.close()

    def line_check(self, num, j):
        for i in range(9):
            if self.grid[j][i] == str(num):
                return True
        return False

    def column_check(self, num, i):
        for j in range(9):
            if self.grid[j][i] == str(num):
                return True
        return False

    def area_check(self, num, i, j):
        mod_i = i // 3
        mod_j = j // 3
        for i in [mod_i * 3, mod_i * 3 + 1, mod_i * 3 + 2]:
            for j in [mod_j * 3, mod_j * 3 + 1, mod_j * 3 + 2]:
                if self.grid[j][i] == str(num):
                    return True
        return False

    def possible_position(self, i, j, k):
        if self.column_check(k, i) is False \
                and self.line_check(k, j) is False \
                and self.area_check(k, i, j) is False:
            return True
        return False

    def resolution(self):
        for i in range(9):
            for j in range(9):
                if self.grid[j][i] == '_':
                    for k in range(1, 10):
                        if self.possible_position(i, j, k) is True:
                            self.grid[j][i] = str(k)
                            self.resolution()
                            self.grid[j][i] = '_'
                    return
        self.display()


X = Sudoku("data.txt")
X.resolution()
