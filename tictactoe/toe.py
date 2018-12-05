from tkinter import *

from tkinter import messagebox
class main:
    def __init__(self, master):
        self.master = master 
        self.master.title("TIC TAC TOE")
        self.label = Label(self.master, text = "Choose the Number of Players", font=("Helvetica", 20), bg = "black", fg = "white")
        self.label.pack(side = TOP, fill = X) 
        self.sin = Button(self.master, text = "Single Player",font=("Helvetica", 16),padx=32,pady=32, bg = "white", fg = "blue", command = self.sgp)
        self.sin.pack(side = LEFT)
        self.mul = Button(self.master, text = "Multi Player",font=("Helvetica", 16), padx=32,pady=32,bg = "blue", fg = "white", command = self.mul)
        self.mul.pack(side = LEFT) 
        self.exit = Button(self.master, text = "Exit",font=("Helvetica", 16),padx=32,pady=32, command = self.quit).pack(side = LEFT)



    def quit(self):
        self.master.destroy()


    def sgp(self):
        root1 = Toplevel(self.master)
        my_window = single_player(root1)

    def mul(self):
        root2 = Toplevel(self.master)
        my_window = multi_player(root2)

#single player start



class single_player:
    board = [ "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    
    def __init__(self, root):
        self.root=root
        self.frame = Frame(root)
        self.frame.pack()

        self.button1 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button1.bind("<ButtonRelease-1>", self.task)
        self.button1.grid(row=0,column=0)

        self.button2 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button2.bind("<ButtonRelease-1>", self.task)
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button3.bind("<ButtonRelease-1>", self.task)
        self.button3.grid(row=0, column=2)

        self.button4 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button4.bind("<ButtonRelease-1>", self.task)
        self.button4.grid(row=1,column=0)

        self.button5 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button5.bind("<ButtonRelease-1>", self.task)
        self.button5.grid(row=1, column=1)

        self.button6 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button6.bind("<ButtonRelease-1>", self.task)
        self.button6.grid(row=1, column=2)

        self.button7 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button7.bind("<ButtonRelease-1>", self.task)
        self.button7.grid(row=2,column=0)

        self.button8 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button8.bind("<ButtonRelease-1>", self.task)
        self.button8.grid(row=2,column=1)

        self.button9 = Button(self.frame,padx=32,pady=32,fg="black")
        self.button9.bind("<ButtonRelease-1>", self.task)
        self.button9.grid(row=2,column=2)

        self.button10=Button(self.frame,padx=32,pady=32,fg="black",bg="blue",command=self.endProgram)
        self.button10.grid(row=3,column=2)
        self.B = Button(self.frame,padx=32,pady=32,fg="blue",bg="black")
        self.B.grid(row=3,column=0,columnspan=2)
        self.view()
        
    def view(self):
        self.button1.config( text = self.board[0],font=('Arial 30 bold'),height=1,width=2)
        self.button2.config( text = self.board[1],font=('Arial 30 bold'),height=1,width=2)
        self.button3.config( text = self.board[2],font=('Arial 30 bold'),height=1,width=2)
        self.button4.config( text = self.board[3],font=('Arial 30 bold'),height=1,width=2)
        self.button5.config( text = self.board[4],font=('Arial 30 bold'),height=1,width=2)
        self.button6.config( text = self.board[5],font=('Arial 30 bold'),height=1,width=2)
        self.button7.config( text = self.board[6],font=('Arial 30 bold'),height=1,width=2)
        self.button8.config( text = self.board[7],font=('Arial 30 bold'),height=1,width=2)
        self.button9.config( text = self.board[8],font=('Arial 30 bold'),height=1,width=2)
        self.button10.config(text="BACK",font=('Arial 30 bold'),height=1,width=2)
        self.B.config(text="RESET",font=('Arial 30 bold '),height=1,width=8)
    def task(self, event):
        if event.widget == self.button1:
            self.playersj(0)
        if event.widget == self.button2 :
            self.playersj(1)
        if event.widget == self.button3 :
            self.playersj(2)
        if event.widget == self.button4 :
            self.playersj(3)
        if event.widget == self.button5:
            self.playersj(4)
        if event.widget == self.button6 :
            self.playersj(5)
        if event.widget == self.button7 :
            self.playersj(6)
        if event.widget == self.button8 :
            self.playersj(7)
        if event.widget == self.button9 :
            self.playersj(8)

    def playersj(self, pos):
        if self.board[pos] == "   ":
            
            self.board[pos] = "X"
            self.view()
            i=self.checkwin()
            if (i!=1):
               self.computersturn()
               self.view()
               self.checkwin()
            

        else:   
            messagebox.showwarning("Invalid j",
                                    "j is not valid!")

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
         return 1
       if(self.board[0] == self.board[1]=="O" and self.board[1] == self.board[2]=="O"
                or self.board[3] == self.board[4] =="O" and self.board[4] == self.board[5]=="O"
                or self.board[6] == self.board[7]=="O" and self.board[7] == self.board[8]=="O"
                or self.board[0] == self.board[3]=="O" and self.board[3] == self.board[6]=="O"
                or self.board[1] == self.board[4]=="O" and self.board[4] == self.board[7]=="O"
                or self.board[2] == self.board[5]=="O" and self.board[5] == self.board[8]=="O"
                or self.board[0] == self.board[4]=="O" and self.board[4] == self.board[8]=="O"
                or self.board[2] == self.board[4]=="O" and self.board[4] == self.board[6]=="O"):
         messagebox.showwarning("RESULT","computer wins")

       if(self.board[0] != "   " and self.board[1] != "   "
                  and self.board[2] != "   " and self.board[3] != "   " 
                  and self.board[4] != "   " and self.board[5] != "   "
                  and self.board[6] != "   " and self.board[7] != "   " 
                  and self.board[8] != "   "):
         messagebox.showwarning("RESULT","game draw")
         return 1
    def computersturn(self):
        if(self.board[6]=="X" and self.board[4]=="X"):
           self.board[1]="O"
        elif(self.board[0]=="O" and self.board[1]=="O"):
           self.board[2]="O"
        elif(self.board[0]=="O" and self.board[2]=="O"):
           self.board[1]="O"
        elif(self.board[2]=="O" and self.board[1]=="O"):
           self.board[0]="O"
        elif(self.board[3]=="O" and self.board[4]=="O"):
           self.board[5]="O"
        elif(self.board[3]=="O" and self.board[5]=="O"):
           self.board[4]="O"
        elif(self.board[4]=="O" and self.board[5]=="O"):
           self.board[3]="O"
        elif(self.board[6]=="O" and self.board[7]=="O"):
           self.board[8]="O"
        elif(self.board[6]=="O" and self.board[8]=="O"):
           self.board[7]="O"
        elif(self.board[7]=="O" and self.board[8]=="O"):
           self.board[6]="O"
        elif(self.board[0]=="O" and self.board[3]=="O"):
           self.board[6]="O"
        elif(self.board[0]=="O" and self.board[6]=="O"):
           self.board[3]="O"
        elif(self.board[3]=="O" and self.board[6]=="O"):
           self.board[0]="O"
        elif(self.board[1]=="O" and self.board[4]=="O"):
           self.board[7]="O"
        elif(self.board[1]=="O" and self.board[7]=="O"):
           self.board[4]="O"
        elif(self.board[7]=="O" and self.board[4]=="O"):
           self.board[1]="O"
        elif(self.board[2]=="O" and self.board[8]=="O"):
           self.board[5]="O"
        elif(self.board[2]=="O" and self.board[5]=="O"):
           self.board[8]="O"
        elif(self.board[5]=="O" and self.board[8]=="O"):
           self.board[2]="O"
        elif(self.board[0]=="O" and self.board[8]=="O"):
           self.board[4]="O"
        elif(self.board[0]=="O" and self.board[4]=="O"):
           self.board[8]="O"
        elif(self.board[8]=="O" and self.board[4]=="O"):
           self.board[0]="O"
        elif(self.board[6]=="O" and self.board[2]=="O"):
           self.board[4]="O"
        elif(self.board[6]=="O" and self.board[4]=="O"):
           self.board[2]="O"
        elif(self.board[2]=="O" and self.board[4]=="O"):
           self.board[6]="O"
        elif(self.board[0]=="X" and self.board[1]=="X"):
           self.board[2]="O"
        elif(self.board[0]=="X" and self.board[2]=="X"):
           self.board[1]="O"
        elif(self.board[2]=="X" and self.board[1]=="X"):
           self.board[0]="O"
        elif(self.board[3]=="X" and self.board[4]=="X"):
           self.board[5]="O"
        elif(self.board[3]=="X" and self.board[5]=="X"):
           self.board[4]="O"
        elif(self.board[4]=="X" and self.board[5]=="X"):
           self.board[3]="O"
        elif(self.board[6]=="X" and self.board[7]=="X"):
           self.board[8]="O"
        elif(self.board[6]=="X" and self.board[8]=="X"):
           self.board[7]="O"
        elif(self.board[7]=="X" and self.board[8]=="X"):
           self.board[6]="O"
        elif(self.board[0]=="X" and self.board[3]=="X"):
           self.board[6]="O"
        elif(self.board[0]=="X" and self.board[6]=="X"):
           self.board[3]="O"
        elif(self.board[3]=="X" and self.board[6]=="X"):
           self.board[0]="O"
        elif(self.board[1]=="X" and self.board[4]=="X"):
           self.board[7]="O"
        elif(self.board[1]=="X" and self.board[7]=="X"):
           self.board[4]="O"
        elif(self.board[7]=="X" and self.board[4]=="X"):
           self.board[1]="O"
        elif(self.board[2]=="X" and self.board[8]=="X"):
           self.board[5]="O"
        elif(self.board[2]=="X" and self.board[5]=="X"):
           self.board[8]="O"
        elif(self.board[5]=="X" and self.board[8]=="X"):
           self.board[2]="O"
        elif(self.board[0]=="X" and self.board[8]=="X"):
           self.board[4]="O"
        elif(self.board[0]=="X" and self.board[4]=="X"):
           self.board[8]="O"
        elif(self.board[8]=="X" and self.board[4]=="X"):
           self.board[0]="O"
        elif(self.board[6]=="X" and self.board[2]=="X"):
           self.board[4]="O"
        elif(self.board[6]=="X" and self.board[4]=="X"):
           self.board[2]="O"
        elif(self.board[2]=="X" and self.board[4]=="X"):
           self.board[6]="O"
        
        
        elif(self.board[4]!="X"):
           self.board[4]="O"
        elif(self.board[4]=="X"):
           self.board[2]="O"
        else:
          for j in [4, 0, 8, 2, 6, 1, 3, 8, 5]:
               if self.board[j] == "   ":
                   self.board[j] = "O"
                   return
    def endProgram(self):
        self.root.destroy()
        

#multi player start

class multi_player:
   
    def __init__(self,master):
        #master frame
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack(fill="both", expand=True)
        
        #canvas where the game is played on
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        
        #Shows status of game
        self.label=Label(self.frame, text='Tic Tac Toe Game',font=("Helvetica", 16), height=4, bg='black', fg='white')
        self.label.pack(fill="both", expand=True)
        
        #frame to contain the buttons
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        
        #Buttons to initiate the game
        self.Start1=Button(self.frameb, text='Click here to start\ndouble player',padx=25,pady=20,font=("Helvetica", 12), height=4, command=self.start1,bg='purple', fg='white')
        self.Start1.pack(fill="both", expand=True, side=LEFT)
        self.back = Button(self.frameb, text = '   Back   ',font=("Helvetica", 12),padx=25,pady=20, command = self.back).pack(fill = "both", side = LEFT)
        
        #canvas board drawing function call
        self._board()

    def back(self):
        self.master.destroy()


    def start1(self):
        #Starts double player
        
        #refresh canvas
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game')
        
        #function call on click
        self.canvas.bind("<ButtonPress-1>", self.dublayer)  
        self._board()
        
        #Starts the matrix to do calculations
        #of the positions of circles and crosses.
        self.TTT=[[0,0,0],[0,0,0],[0,0,0]]
        
        #counter of turns
        self.i=0
        
        #trigger to end game
        self.j=False

   

    def end(self):
        #Ends the game
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True
        
    
    def _board(self):
        #Creates the board
        self.canvas.create_rectangle(0,0,300,300, outline="black")
        self.canvas.create_rectangle(100,300,200,0, outline="black")
        self.canvas.create_rectangle(0,100,300,200, outline="black")
        
    def dublayer(self,event):
        #Double player game loop
        for k in range(0,300,100):
            for j in range(0,300,100):
                #checks if the mouse input is in a bounding box
                if event.x in range(k,k+100) and event.y in range(j,j+100):
                    #checks if there is nothing in the bounding box
                    if self.canvas.find_enclosed(k,j,k+100,j+100)==():
                        #Player plays first
                        if self.i%2==0:
                            #draws circle
                            #no need to create a new function since there is just two cases where this code is used
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas.create_oval( X+25, Y+25, X-25, Y-25, width=4, outline="black")
                            self.TTT[Y1][X1]+=1
                            self.i+=1
                        else:
                            #creates the cross.
                            #I don't use the self.cross function here because k and j are not compatible
                            X=(2*k+100)/2
                            Y=(2*j+100)/2
                            X1=int(k/100)
                            Y1=int(j/100)
                            self.canvas. create_line( X+20, Y+20, X-20, Y-20, width=4, fill="black")
                            self.canvas. create_line( X-20, Y+20, X+20, Y-20, width=4, fill="black")
                            self.TTT[Y1][X1]+=9
                            self.i+=1
        self.check()

    
                        
                        
    def check(self):
        #horizontal check
        for i in range(0,3):
            if sum(self.TTT[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.TTT[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
        #vertical check
        #for vertical rows
        self.ttt=[[row[i] for row in self.TTT] for i in range(3)]
        for i in range(0,3):            
            if sum(self.ttt[i])==27:
                self.label['text']=('2nd player wins!')
                self.end()
            if sum(self.ttt[i])==3:
                self.label['text']=('1st player wins!')
                self.end()
        #check for diagonal wins
        if self.TTT[1][1]==9:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('2nd player wins!')
                self.end()
        if self.TTT[1][1]==1:
            if self.TTT[0][0]==self.TTT[1][1] and self.TTT[2][2]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
            if self.TTT[0][2]==self.TTT[1][1] and self.TTT[2][0]==self.TTT[1][1] :
                self.label['text']=('1st player wins!')
                self.end()
        #check for draws
        if self.j==False:
            a=0
            for i in range(0,3):
                a+= sum(self.TTT[i])
            #As the player starts with a circle(value=1),
            #There will be a total of 5(1) and 4(9)=41
            if a==41:
                self.label['text']=("It's a draw!")
                self.end()

#multi player end

root = Tk()
d= main(root)

root.mainloop()
