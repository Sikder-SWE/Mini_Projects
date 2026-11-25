from customtkinter import CTk, CTkLabel, CTkEntry,CTkFont

class App (CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("1000x400x")
        
        form_label = CTkLabel(self,
                              text="Land Registration Portal",
                              font=CTkFont(family="Comic Sans", size=40))
        form_label.place(relx = 0.5, rely = 0.5, anchor="center")