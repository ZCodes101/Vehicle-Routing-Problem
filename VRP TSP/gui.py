# import tkinter as tk
# import tkinter.font as tkFont
#
# class App:
#     def __init__(self, root):
#         #setting title
#         root.title("WGUPS Package Routing Program")
#         #setting window size
#         width=600
#         height=500
#         screenwidth = root.winfo_screenwidth()
#         screenheight = root.winfo_screenheight()
#         alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
#         root.geometry(alignstr)
#         root.resizable(width=False, height=False)
#
#         GLabel_641=tk.Label(root)
#         GLabel_641["anchor"] = "center"
#         ft = tkFont.Font(family='Times',size=10)
#         GLabel_641["font"] = ft
#         GLabel_641["fg"] = "#333333"
#         GLabel_641["justify"] = "center"
#         GLabel_641["text"] = "WGUPS Package Routing Program"
#         GLabel_641.place(x=120,y=10,width=252,height=35)
#
#         GListBox_222=tk.Listbox(root)
#         GListBox_222["borderwidth"] = "1px"
#         ft = tkFont.Font(family='Times',size=10)
#         GListBox_222["font"] = ft
#         GListBox_222["fg"] = "#333333"
#         GListBox_222["justify"] = "center"
#         GListBox_222.place(x=20,y=50,width=412,height=367)
#
#         GButton_782=tk.Button(root)
#         GButton_782["bg"] = "#efefef"
#         ft = tkFont.Font(family='Times',size=10)
#         GButton_782["font"] = ft
#         GButton_782["fg"] = "#000000"
#         GButton_782["justify"] = "center"
#         GButton_782["text"] = "Button"
#         GButton_782.place(x=20,y=430,width=311,height=44)
#         GButton_782["command"] = self.GButton_782_command
#
#         GLineEdit_781=tk.Entry(root)
#         GLineEdit_781["borderwidth"] = "1px"
#         ft = tkFont.Font(family='Times',size=10)
#         GLineEdit_781["font"] = ft
#         GLineEdit_781["fg"] = "#333333"
#         GLineEdit_781["justify"] = "center"
#         GLineEdit_781["text"] = "Entry"
#         GLineEdit_781.place(x=450,y=100,width=129,height=30)
#
#         GLabel_178=tk.Label(root)
#         ft = tkFont.Font(family='Times',size=10)
#         GLabel_178["font"] = ft
#         GLabel_178["fg"] = "#333333"
#         GLabel_178["justify"] = "center"
#         GLabel_178["text"] = "label"
#         GLabel_178.place(x=340,y=440,width=94,height=30)
#
#         GButton_316=tk.Button(root)
#         GButton_316["bg"] = "#efefef"
#         ft = tkFont.Font(family='Times',size=10)
#         GButton_316["font"] = ft
#         GButton_316["fg"] = "#000000"
#         GButton_316["justify"] = "center"
#         GButton_316["text"] = "Button"
#         GButton_316.place(x=500,y=450,width=70,height=25)
#         GButton_316["command"] = self.GButton_316_command
#
#         GButton_897=tk.Button(root)
#         GButton_897["bg"] = "#efefef"
#         ft = tkFont.Font(family='Times',size=10)
#         GButton_897["font"] = ft
#         GButton_897["fg"] = "#000000"
#         GButton_897["justify"] = "center"
#         GButton_897["text"] = "Button"
#         GButton_897.place(x=480,y=150,width=70,height=25)
#         GButton_897["command"] = self.GButton_897_command
#
#         GLabel_257=tk.Label(root)
#         ft = tkFont.Font(family='Times',size=10)
#         GLabel_257["font"] = ft
#         GLabel_257["fg"] = "#333333"
#         GLabel_257["justify"] = "center"
#         GLabel_257["text"] = "label"
#         GLabel_257.place(x=430,y=60,width=145,height=30)
#
#         GRadio_442=tk.Radiobutton(root)
#         ft = tkFont.Font(family='Times',size=10)
#         GRadio_442["font"] = ft
#         GRadio_442["fg"] = "#333333"
#         GRadio_442["justify"] = "center"
#         GRadio_442["text"] = "RadioButton"
#         GRadio_442.place(x=460,y=220,width=85,height=25)
#         GRadio_442["command"] = self.GRadio_442_command
#
#         GRadio_756=tk.Radiobutton(root)
#         ft = tkFont.Font(family='Times',size=10)
#         GRadio_756["font"] = ft
#         GRadio_756["fg"] = "#333333"
#         GRadio_756["justify"] = "center"
#         GRadio_756["text"] = "RadioButton"
#         GRadio_756.place(x=460,y=260,width=85,height=25)
#         GRadio_756["command"] = self.GRadio_756_command
#
#     def GButton_782_command(self):
#         print("command")
#
#
#     def GButton_316_command(self):
#         print("command")
#
#
#     def GButton_897_command(self):
#         print("command")
#
#
#     def GRadio_442_command(self):
#         print("command")
#
#
#     def GRadio_756_command(self):
#         print("command")
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
