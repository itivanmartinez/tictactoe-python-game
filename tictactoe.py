import tkinter as tk
def main():
    
    def showx():
        #--Shows x on labels--
        getPos=int(txtinstructions.get())
        print(getPos)
        labels[getPos].configure(text="X")
    def show0():
        #--Shows 0 on labels--
        getPos=int(txtinstructions.get())
        print(getPos)
        labels[getPos].configure(text="0")
     #--Creates windows--
    windows= tk.Tk()
    windows.title("Tic Tac Toe | By Ivan Martinez")
    windows.geometry("600x400")
    labels=[]
    #--Creates a list of 9 labels--
    for i in range(9):
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

        label.grid(column=ncolumns,row=nrows)
        
        ncolumns=ncolumns+1
  
    windows.mainloop()

        
main()
