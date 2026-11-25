from customtkinter import CTk, CTkLabel, CTkEntry,CTkFont, CTkFrame

class App (CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("900x900")
        
        form_label = CTkLabel(self,
                              text="Land Registration Portal",
                              font=CTkFont(family="Comic Sans", size=30))
        form_label.place(relx = 0.5, rely = 0.15, anchor="center")
        
        
        # Creating Another Extra frame to place login forms
        
        login_frame = CTkFrame(self,
                               corner_radius=25,
                               border_width=3,
                               border_color="white"
                               )
        login_frame.place(relx=0.5, rely=0.45, anchor="center", relwidth = 0.7, relheight=0.45)