import tkinter as tk
def main():
    def checkRange(numInt):
        #checks if given number is in range 1-9
        Range=range(1,10)
        numInt=int(numInt)
        if numInt in Range:
            return numInt
        else:
            txtinstructions.delete(0,'end')
            txtinstructions.insert(0,"Type in a number between 1-9")
        
    def checkWinner(player):
        #checks if player is winner

        #Checking Horizontally
        if labels[0].cget("text")==player and labels[1].cget("text")==player and labels[2].cget("text")==player:return True
        if labels[3].cget("text")==player and labels[4].cget("text")==player and labels[4].cget("text")==player:return True
        if labels[6].cget("text")==player and labels[8].cget("text")==player and labels[9].cget("text")==player:return True
        #Checking Vertically
        if labels[0].cget("text")==player and labels[3].cget("text")==player and labels[6].cget("text")==player:return True
        if labels[1].cget("text")==player and labels[4].cget("text")==player and labels[7].cget("text")==player:return True
        if labels[2].cget("text")==player and labels[5].cget("text")==player and labels[8].cget("text")==player:return True
        #Checking Diagonally
        if labels[0].cget("text")==player and labels[4].cget("text")==player and labels[8].cget("text")==player:return True
        if labels[2].cget("text")==player and labels[4].cget("text")==player and labels[7].cget("text")==player:return True
    
    def showx():
        #--Shows x on labels--
        getPos=checkRange(txtinstructions.get())
        if getPos:
            labels[getPos-1].configure(text="X")
            txtinstructions.delete(0,'end')
            txtinstructions.focus_set()   
        if checkWinner("X"):
            txtinstructions.delete(0,'end')
            txtinstructions.insert(0,"X is the winner") 
    def show0():
        #--Shows 0 on labels--
        getPos=checkRange(txtinstructions.get())
        if getPos:
            labels[getPos-1].configure(text="0")
            txtinstructions.delete(0)
            txtinstructions.focus_set()
        if checkWinner("0"):
            txtinstructions.delete(0)
            txtinstructions.insert(0,"0 is the winner") 
    def resetLabel():
        #Resets Board to original values
        i=1
        for label in labels:
            label.configure(text=str(i))
            i=i+1
        txtinstructions.delete(0, 'end')
        txtinstructions.focus_set()

        
     #--Creates windows--
    windows= tk.Tk()
    windows.title("Tic Tac Toe | By Ivan Martinez")
    windows.geometry("600x400")
    labels=[]
        #--Creates a list of 9 labels--
    for i in range(1,10):
        labels.append(tk.Label(windows,text=str(i), bg="red", height=8, width=8))
        nrows=1
        ncolumns=1

    #--Displays a list of labels--   
    for label in labels:
        if ncolumns>3:
           ncolumns=1
           nrows=nrows+1
        if ncolumns==3 and nrows==1:
            lblinstructions=tk.Label(text="Enter number to place X")
            lblinstructions.grid(column=4,row=1)
            txtinstructions=tk.Entry()
            txtinstructions.grid(column=5,row=1)
            btnplay=tk.Button(text="Place X",command=showx)
            btnplay.grid(column=6,row=1)
            btnplay=tk.Button(text="Place 0",command=show0)
            btnplay.grid(column=8,row=1)
            btnplay=tk.Button(text="Reset",command=resetLabel)
            btnplay.grid(column=10,row=1)
        label.grid(column=ncolumns,row=nrows)
        ncolumns=ncolumns+1

  
    windows.mainloop()

        
main()
