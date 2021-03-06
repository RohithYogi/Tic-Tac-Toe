from tkinter import *

class computer():
    board = [ "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    
    def __init__(self, root):
        self.root=root
        frame = Frame(root)
        frame.pack()

        self.B1 = Button(frame,padx=32,pady=32,fg="black")
        self.B1.bind("<ButtonRelease-1>", self.clicked)
        self.B1.grid(row=0,column=0)

        self.B2 = Button(frame,padx=32,pady=32,fg="black")
        self.B2.bind("<ButtonRelease-1>", self.clicked)
        self.B2.grid(row=0, column=1)

        self.B3 = Button(frame,padx=32,pady=32,fg="black")
        self.B3.bind("<ButtonRelease-1>", self.clicked)
        self.B3.grid(row=0, column=2)

        self.B4 = Button(frame,padx=32,pady=32,fg="black")
        self.B4.bind("<ButtonRelease-1>", self.clicked)
        self.B4.grid(row=1,column=0)

        self.B5 = Button(frame,padx=32,pady=32,fg="black")
        self.B5.bind("<ButtonRelease-1>", self.clicked)
        self.B5.grid(row=1, column=1)

        self.B6 = Button(frame,padx=32,pady=32,fg="black")
        self.B6.bind("<ButtonRelease-1>", self.clicked)
        self.B6.grid(row=1, column=2)

        self.B7 = Button(frame,padx=32,pady=32,fg="black")
        self.B7.bind("<ButtonRelease-1>", self.clicked)
        self.B7.grid(row=2,column=0)

        self.B8 = Button(frame,padx=32,pady=32,fg="black")
        self.B8.bind("<ButtonRelease-1>", self.clicked)
        self.B8.grid(row=2,column=1)

        self.B9 = Button(frame,padx=32,pady=32,fg="black")
        self.B9.bind("<ButtonRelease-1>", self.clicked)
        self.B9.grid(row=2,column=2)
        self.B10=Button(frame,padx=32,pady=32,fg="black",bg="red",command=self.endProgram)
        self.B10.grid(row=3,column=0,columnspan=3)
  
        self.view()
        
    def view(self):
        self.B1.config( text = self.board[0],font=('Arial 30 bold'),height=1,width=2)
        self.B2.config( text = self.board[1],font=('Arial 30 bold'),height=1,width=2)
        self.B3.config( text = self.board[2],font=('Arial 30 bold'),height=1,width=2)
        self.B4.config( text = self.board[3],font=('Arial 30 bold'),height=1,width=2)
        self.B5.config( text = self.board[4],font=('Arial 30 bold'),height=1,width=2)
        self.B6.config( text = self.board[5],font=('Arial 30 bold'),height=1,width=2)
        self.B7.config( text = self.board[6],font=('Arial 30 bold'),height=1,width=2)
        self.B8.config( text = self.board[7],font=('Arial 30 bold'),height=1,width=2)
        self.B9.config( text = self.board[8],font=('Arial 30 bold'),height=1,width=2)
        self.B10.config(text="EXIT",font=('Arial 30 bold'),height=1,width=2)
    def endProgram(self):
        self.root.destroy()
    def clicked(self, event):
        if event.widget == self.B1:
            self.userMove(0)
        if event.widget == self.B2 :
            self.userMove(1)
        if event.widget == self.B3 :
            self.userMove(2)
        if event.widget == self.B4 :
            self.userMove(3)
        if event.widget == self.B5:
            self.userMove(4)
        if event.widget == self.B6 :
            self.userMove(5)
        if event.widget == self.B7 :
            self.userMove(6)
        if event.widget == self.B8 :
            self.userMove(7)
        if event.widget == self.B9 :
            self.userMove(8)

    def userMove(self, pos):

        #Is this a valid move?
        if self.board[pos] == "   ":
            
            self.board[pos] = "X"
            self.view()
            self.checkwin()
            self.computerMove()
            self.view()
            self.checkwin()

        else:   
            messagebox.showwarning("Invalid Move",
                                    "I'm sorry, that move is not valid!")

    def checkwin(self):
       if (self.board[0] == self.board[1]=="X" and self.board[1] == self.board[2]=="X"
                or self.board[3] == self.board[4] =="X" and self.board[4] == self.board[5]=="X"
                or self.board[6] == self.board[7]=="X" and self.board[7] == self.board[8]=="X"
                or self.board[0] == self.board[3]=="X" and self.board[3] == self.board[6]=="X"
                or self.board[1] == self.board[4]=="X" and self.board[4] == self.board[7]=="X"
                or self.board[2] == self.board[5]=="X" and self.board[5] == self.board[8]=="X"
                or self.board[0] == self.board[4]=="X" and self.board[4] == self.board[8]=="X"
                or self.board[2] == self.board[4]=="X" and self.board[4] == self.board[6]=="X"):
         messagebox.showwarning("RESULT","player wins")
         
       elif(self.board[0] == self.board[1]=="O" and self.board[1] == self.board[2]=="O"
                or self.board[3] == self.board[4] =="O" and self.board[4] == self.board[5]=="O"
                or self.board[6] == self.board[7]=="O" and self.board[7] == self.board[8]=="O"
                or self.board[0] == self.board[3]=="O" and self.board[3] == self.board[6]=="O"
                or self.board[1] == self.board[4]=="O" and self.board[4] == self.board[7]=="O"
                or self.board[2] == self.board[5]=="O" and self.board[5] == self.board[8]=="O"
                or self.board[0] == self.board[4]=="O" and self.board[4] == self.board[8]=="O"
                or self.board[2] == self.board[4]=="O" and self.board[4] == self.board[6]=="O"):
         messagebox.showwarning("RESULT","computer wins")
         
       elif(self.board[0] != "   " and self.board[1] != "   "
                  and self.board[2] != "   " and self.board[3] != "   " 
                  and self.board[4] != "   " and self.board[5] != "   "
                  and self.board[6] != "   " and self.board[7] != "   " 
                  and self.board[8] != "   "):
         messagebox.showwarning("RESULT","game draw")
         
    def computerMove(self):
       for move in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
           if self.board[move] == "   ":
               self.board[move] = "O"
               return


        
root= Tk()
t = computer(root)
root.mainloop()
