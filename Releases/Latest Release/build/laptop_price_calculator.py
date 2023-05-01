"""
MIT License

Copyright (c) 2023: Isaac James Lindroos

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

# Explicit imports to satisfy Flake8:
import tkinter
import tkinter.messagebox
import customtkinter
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from tabulate import tabulate
from PIL import Image
from pathlib import Path
import webbrowser
import re
import sys
import os

# Set Local File Mater Pathway:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Set Tabulate Display Settings:
tabulate.PRESERVE_WHITESPACE = True

# Set CustomTkinter Display Settings:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Set Default Pathway to Relative Assets:
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Set Display settings (ALL Pandas dataframes):
def set_pandas_display_options() -> None:
    display = pd.options.display
    display.max_columns = 1000
    display.max_rows = 1000
    display.max_colwidth = 199
    display.width = 1000

set_pandas_display_options()

# Pandas Main Dataframe Configuration (Set Columns):
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb', 'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df = pd.read_csv(ASSETS_PATH / "laptops_dataset_clean_refined.csv", usecols=['os', 'ssd', 'ram_gb', 'display_size', 'touchscreen', 'brand'])

# Pandas Main Dataframe Refinement (Removing all Rows with NaN Values within the Main Dataframe & Updateing the Index axis Accordingly):
df = df.dropna()
df = df.dropna(axis=0)
df = df.dropna().reset_index(drop=True)

# Pandas Results Dataframe Configuration (Set Columns):
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb', 'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df_results = pd.read_csv(ASSETS_PATH / "laptops_dataset_clean_refined_dataref.csv")

# Pandas Results Dataframe Refinement (Removing all Rows with NaN Values within the Main Dataframe & Updateing the Index axis Accordingly):
df_results = df_results.dropna()
df_results = df_results.dropna(axis=0)
df_results = df_results.dropna().reset_index(drop=True)

# Individual Dataframe Configuration:
os_windows_df = df.os == "Windows"
os_mac_df = df.os == "Mac"
os_dos_df = df.os == "Dos"
ssd_128_df = df.ssd == "128 GB"
ssd_256_df = df.ssd == "256 GB"
ssd_512_df = df.ssd == "512 GB"
ssd_1024_df = df.ssd == "1024 GB"
ram_4_df = df.ram_gb == "4 GB"
ram_8_df = df.ram_gb == "8 GB"
ram_16_df = df.ram_gb == "16 GB"
ram_32_df = df.ram_gb == "32 GB"
display_size_13_3_df = df.display_size == "13.3"
display_size_14_df = df.display_size == "14"
display_size_15_6_df = df.display_size == "15.6"
display_size_16_df = df.display_size == "16"
touchscreen_yes_df = df.touchscreen == "Yes"
touchscreen_no_df = df.touchscreen == "No"
brand_apple_df = df.brand == "APPLE"
brand_asus_df = df.brand == "ASUS"
brand_dell_df = df.brand == "DELL"
brand_hp_df = df.brand == "HP"
brand_msi_df = df.brand == "MSI"

# Set Value of User Selection based on Button Function:
def user_select_os_windows():
    df.update(os_windows_df, overwrite=True)

def user_select_os_mac():
    df.update(os_mac_df, overwrite=True)

def user_select_os_dos():
    df.update(os_dos_df, overwrite=True)

def user_select_storage_128():
    df.update(ssd_128_df, overwrite=True)

def user_select_storage_256():
    df.update(ssd_256_df, overwrite=True)

def user_select_storage_512():
    df.update(ssd_512_df, overwrite=True)

def user_select_storage_1024():
    df.update(ssd_1024_df, overwrite=True)

def user_select_ram_4():
    df.update(ram_4_df, overwrite=True)

def user_select_ram_8():
    df.update(ram_8_df, overwrite=True)

def user_select_ram_16():
    df.update(ram_16_df, overwrite=True)

def user_select_ram_32():
    df.update(ram_32_df, overwrite=True)

def user_select_display_size_13_3():
    df.update(display_size_13_3_df, overwrite=False)

def user_select_display_size_14():
    df.update(display_size_14_df, overwrite=False)

def user_select_display_size_15_6():
    df.update(display_size_15_6_df, overwrite=False)

def user_select_display_size_16():
    df.update(display_size_16_df, overwrite=False)

def user_select_touchscreen_yes():
    df.update(touchscreen_yes_df, overwrite=True)

def user_select_touchscreen_no():
    df.update(touchscreen_no_df, overwrite=True)

def user_select_brand_apple():
    df.update(brand_apple_df, overwrite=True)

def user_select_brand_asus():
    df.update(brand_asus_df, overwrite=True)

def user_select_brand_dell():
    df.update(brand_dell_df, overwrite=True)

def user_select_brand_hp():
    df.update(brand_hp_df, overwrite=True)

def user_select_brand_msi():
    df.update(brand_msi_df, overwrite=True)

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        # Configure Results Window
        self.title("Laptop Price Calculator 11.6: Results - FOR DEVELOPMENT USE ONLY!")      # NOTE: Development Version
        self.geometry(f"{1000}x{480}")
        self.wm_iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/window_icon.ico"))
        # self.wm_iconbitmap('window_icon.ico')

        # Configure Results Window Grid Layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame with Internal Widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "laptop_image.png")), size=(200, 200))
        self.sidebar_frame_label = customtkinter.CTkLabel(self.sidebar_frame, text="", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_frame_label.grid(row=4, column=0, padx=20, pady=20)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Laptop Price Calculator", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Instruction Frame with Internal Widgets
        self.instruction_frame = customtkinter.CTkFrame(self, width=140)
        self.instruction_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.instruction_frame.grid_rowconfigure(4, weight=1)
        self.instruction_label = customtkinter.CTkLabel(self.instruction_frame, text=datalabel, anchor="center", justify="left", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.instruction_label.grid(row=0, column=1, padx=20, pady=(20, 10))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

        # Configure Master Window
        self.title("Laptop Price Calculator 11.6 - FOR DEVELOPMENT USE ONLY!")      # NOTE: Development Version
        self.geometry(f"{1000}x{768}")
        self.wm_iconbitmap(os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/window_icon.ico"))
        # self.wm_iconbitmap('window_icon.ico')

        # Configure Master Window Grid Layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame with Internal Widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "laptop_image.png")), size=(200, 200))
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
        self.instruction_label = customtkinter.CTkLabel(self.instruction_frame, text="How to use the Laptop Price Calculator:\n\n1. Once the program has loaded correctly, you will see the main window of the\n     program with several input fields and buttons.\n2. Using the Laptop Specification Selection Tool™, simply select from each\n     dropdown the specification that best suits your needs.\n3. Once you have made all of your selections, click on the 'Submit' button to\n     view your results.\n4. To exit the program at any time, click on the 'Exit' Button.\n\nNote: To update the Master Database to the Latest data, please click the\n'Update Database' Button and upload your preferred CSV file. ", anchor="center", justify="left", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.instruction_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # GitHub Frame with Internal Widgets
        self.github_frame = customtkinter.CTkFrame(self, width=140)
        self.github_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.github_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "github_logo.png")), size=(100, 100))
        self.github_frame_label = customtkinter.CTkLabel(self.github_frame, text="", image=self.logo_image, compound="center", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.github_frame_label.grid(row=4, column=0, padx=20, pady=20)
        self.github_button = customtkinter.CTkButton(self.github_frame, command=self.reset_button)
        self.github_button.grid(row=5, column=0, padx=20, pady=10)

        # Entry Field and Buttons
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Notes & Comments")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(master=self, state="enabled", fg_color="#28A745", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#28A745", text="Submit", command=self.submit_button)
        self.submit_button.grid(row=1, column=3, padx=(20, 20), pady=(38, 0), sticky="nsew")
        self.exit_button = customtkinter.CTkButton(master=self, state="enabled", fg_color="#DC3545", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#DC3545", text="Exit", command=self.exit_button)
        self.exit_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Set All Default Values
        self.reset_button.configure(state="enabled", fg_color="#DC3545", border_width=2, text_color=("gray10", "#DCE4EE"), border_color="#DC3545",text="Reset/Clear Form")
        self.update_button.configure(state="enabled", text="Update Database")
        self.feedback_button.configure(state="disabled", text="Provide Feedback")
        self.github_button.configure(state="enabled", text= "View on GitHub")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # Selection Frame with Internal Widgets
        self.tabview = customtkinter.CTkTabview(self, width=50)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Laptop Specification Selection Tool™")
        self.tabview.tab("Laptop Specification Selection Tool™").grid_columnconfigure(0, weight=1)
        self.label_option_menu_1_brand = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Laptop Brand")
        self.label_option_menu_1_brand.grid(row=0, column=0, padx=0, pady=0)
        self.option_menu_1_brand = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "Apple", "ASUS", "Dell", "HP", "MSI"])
        self.option_menu_1_brand.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_2_operating_system = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Operating System")
        self.label_option_menu_2_operating_system.grid(row=2, column=0, padx=0, pady=0)
        self.option_menu_2_operating_system = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "Windows", "Mac", "DOS"])
        self.option_menu_2_operating_system.grid(row=3, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_3_display_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Display Size (inches)")
        self.label_option_menu_3_display_size.grid(row=4, column=0, padx=0, pady=0)
        self.option_menu_3_display_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "13.3 inches", "14 inches", "15.6 inches", "16 inches"])
        self.option_menu_3_display_size.grid(row=5, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_4_ssd_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="SSD Size (GB)")
        self.label_option_menu_4_ssd_size.grid(row=6, column=0, padx=0, pady=0)
        self.option_menu_4_ssd_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "128 GB", "256 GB", "512 GB", "1024 GB"])
        self.option_menu_4_ssd_size.grid(row=7, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_5_ram_size = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="RAM Size (GB)")
        self.label_option_menu_5_ram_size.grid(row=8, column=0, padx=0, pady=0)
        self.option_menu_5_ram_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "4 GB", "8 GB", "16 GB", "32 GB"])
        self.option_menu_5_ram_size.grid(row=9, column=0, padx=20, pady=(0, 10))
        self.label_option_menu_6_touchscreen = customtkinter.CTkLabel(self.tabview.tab("Laptop Specification Selection Tool™"), text="Touchscreen")
        self.label_option_menu_6_touchscreen.grid(row=10, column=0, padx=0, pady=0)
        self.option_menu_6_touchscreen = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "Yes", "No",])
        self.option_menu_6_touchscreen.grid(row=11, column=0, padx=20, pady=(0, 10))
        
        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

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
            self.open_toplevel()
            
            
    def read_selection(self):
        print("Read Selection")

if __name__ == "__main__":
    app = App()
    app.mainloop()
