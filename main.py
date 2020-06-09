import tkinter, random
class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid()

        self.entry = tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')

        
        self.result = tkinter.Entry(self)
        self.result.grid(column=0,row=1,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        
        self.gen_button = tkinter.Button(self,text=u"Generate password of len 8 from the characters above",command=self.generate_pswd)
        self.gen_button.grid(column=1,row=0)
    
    def generate_pswd(self):
        self.alphabet = self.entry.get()
        self.result.delete(1, last='end')
        password = ''.join(random.choice(self.alphabet) for i in range(8))
        self.result.insert(0,password)


# saving a 500mb 3dsmax file do be kinda taking a long time doe
    
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Password Generator')
    app.mainloop()