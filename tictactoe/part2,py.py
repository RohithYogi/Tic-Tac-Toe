from Tkinter import *


class main:
   
    def _init_(self,master):
        #master frame
        self.frame = Frame(master)
        self.frame.pack(fill="both", expand=True)
        
        #canvas where the game is played on
        self.canvas = Canvas(self.frame, width=300, height=300)
        self.canvas.pack(fill="both", expand=True)
        
        #Shows status of game
        self.label=Label(self.frame, text='Tic Tac Toe Game', height=6, bg='black', fg='blue')
        self.label.pack(fill="both", expand=True)
        
        #frame to contain the buttons
        self.frameb=Frame(self.frame)
        self.frameb.pack(fill="both", expand=True)
        
        #Buttons to initiate the game
        self.Start1=Button(self.frameb, text='Click here to start\ndouble player', height=4, command=self.start1,bg='white', fg='purple')
        self.Start1.pack(fill="both", expand=True, side=RIGHT)
        self.Start2=Button(self.frameb, text='Click here to start\nsingle player', height=4,bg='purple', fg='white')
        self.Start2.pack(fill="both", expand=True, side=LEFT)
        
        #canvas board drawing function call
        self._board()

    def start1(self):
        #Starts double player
        
        #refresh canvas
        self.canvas.delete(ALL)
        self.label['text']=('Tic Tac Toe Game')
        
        #function call on click
        self.canvas.bind("<ButtonPress-1>", self.sgplayer)  
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
        
    def sgplayer(self,event):
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
                self.label['text']=("It's a pass!")
                self.end()


        


                
#initiate the class
root=Tk()
a=main(root)
root.mainloop()
