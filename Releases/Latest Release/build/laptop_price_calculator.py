"""
MIT License

Copyright (c) [2023] [Isaac James Lindroos]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        # Configure Master Window
        self.title("Laptop Price Calculator 11.2 - FOR DEVELOPMENT USE ONLY!")      # NOTE: Development Version
        self.geometry(f"{1000}x{768}")
        self.wm_iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/window_icon.ico"))
        # self.wm_iconbitmap('window_icon.ico')

        # Configure Master Grid Layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame with Internal Widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "laptop_image_a.png")), size=(200, 200))
        self.sidebar_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text="", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_frame_label.grid(row=4, column=0, padx=20, pady=20)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Laptop Price Calculator", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.reset_button = customtkinter.CTkButton(self.sidebar_frame, command=self.reset_button)
        self.reset_button.grid(row=1, column=0, padx=20, pady=10)
        self.update_button = customtkinter.CTkButton(self.sidebar_frame, command=self.update_button)
        self.update_button.grid(row=2, column=0, padx=20, pady=10)
        self.feedback_button = customtkinter.CTkButton(self.sidebar_frame, command=self.feedback_button)
        self.feedback_button.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        # Instruction Frame with Internal Widgets
        self.instruction_frame = customtkinter.CTkFrame(self, width=140)
        self.instruction_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.instruction_frame.grid_rowconfigure(4, weight=1)
        self.instruction_label = customtkinter.CTkLabel(self.instruction_frame, text="How to use the Laptop Price Calculator:\n1. Once the program has loaded correctly, you will see the main window of the program with several input fields and buttons.\n2.", anchor="center", justify="left", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.instruction_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Credit Frame with Internal Widgets
        self.credit_frame = customtkinter.CTkFrame(self, width=140)
        self.credit_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.credit_frame.grid_rowconfigure(4, weight=1)

        # Entry Field and Buttons
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Notes & Comments")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(master=self, fg_color="#28A745", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#28A745", text="Submit", command=self.submit_button)
        self.submit_button.grid(row=1, column=3, padx=(20, 20), pady=(38, 0), sticky="nsew")
        self.exit_button = customtkinter.CTkButton(master=self, fg_color="#DC3545", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#DC3545", text="Exit", command=self.exit_button)
        self.exit_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Set All Default Values
        self.reset_button.configure(state="enabled", fg_color="#DC3545", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#DC3545",text="Reset/Clear Form")
        self.update_button.configure(state="enabled", text="Update Database")
        self.feedback_button.configure(state="disabled", text="Provide Feedback")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # Selection Frame with Internal Widgets
        self.tabview = customtkinter.CTkTabview(self, width=50)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Laptop Specification Selection Tool™")
        self.tabview.tab("Laptop Specification Selection Tool™").grid_columnconfigure(0, weight=1)
        self.label_option_menu_1_brand = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Laptop Brand")
        self.label_option_menu_1_brand.grid(row=0, column=0, padx=0, pady=0)
        self.option_menu_1_brand = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["Apple", "ASUS", "Dell", "HP", "MSI"])
        self.option_menu_1_brand.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_2_operating_system = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Operating System")
        self.label_option_menu_2_operating_system.grid(row=2, column=0, padx=0, pady=0)
        self.option_menu_2_operating_system = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["Windows", "Mac", "DOS"])
        self.option_menu_2_operating_system.grid(row=3, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_3_display_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Display Size (inches)")
        self.label_option_menu_3_display_size.grid(row=4, column=0, padx=0, pady=0)
        self.option_menu_3_display_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["13.3 inches", "14 inches", "15.6 inches", "16 inches"])
        self.option_menu_3_display_size.grid(row=5, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_4_ssd_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="SSD Size (GB)")
        self.label_option_menu_4_ssd_size.grid(row=6, column=0, padx=0, pady=0)
        self.option_menu_4_ssd_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["128 GB", "256 GB", "512 GB", "1024 GB"])
        self.option_menu_4_ssd_size.grid(row=7, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_5_ram_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="RAM Size (GB)")
        self.label_option_menu_5_ram_size.grid(row=8, column=0, padx=0, pady=0)
        self.option_menu_5_ram_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["4 GB", "8 GB", "16 GB", "32 GB"])
        self.option_menu_5_ram_size.grid(row=9, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_6_touchscreen = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Touchscreen")
        self.label_option_menu_6_touchscreen.grid(row=10, column=0, padx=0, pady=0)
        self.option_menu_6_touchscreen = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["Yes", "No",])
        self.option_menu_6_touchscreen.grid(row=11, column=0, padx=20, pady=(0, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def reset_button(self):
        reset_yes = tkinter.messagebox.askyesnocancel(title="reset_button", message="Are you sure that you want to Reset/Clear the Form?", icon='warning')
        print("Reset/Clear Form Button Pressed")
        
        if reset_yes:
            print("Form Reset/Cleared")
    
    def update_button(self):
        update_yes = tkinter.messagebox.askyesnocancel(title="update_button", message="Are you sure that you want to Update the Database?", icon='warning')
        print("Update Database Button Pressed")
        
        if update_yes:
            print("Database Updated")
    
    def feedback_button(self):
        print("Provide Feedback Button Pressed")
        
    def exit_button(self):
        exit_yes = tkinter.messagebox.askyesnocancel(title="exit_button", message="Are you sure that you want to Exit the Application?", icon='warning')
        print("Application Exit Button Pressed")
        
        if exit_yes:
            self.quit()

    def submit_button(self):
        submit_yes = tkinter.messagebox.askyesnocancel(title="submit_button", message="Are you sure that you want to submit your entries?", icon='warning')
        print("Submit Results Button Pressed")

        if submit_yes:
            print("Results Submitted")

if __name__ == "__main__":
    app = App()
    app.mainloop()
