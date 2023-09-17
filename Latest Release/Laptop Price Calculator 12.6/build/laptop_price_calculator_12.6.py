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
import webbrowser
import uuid
from tabulate import tabulate
from PIL import Image
from pathlib import Path
from tkinter import filedialog
from fpdf import fpdf
from tkinter import filedialog as fd

# Set Local File Mater Pathway:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Set Tabulate Display Settings:
tabulate.PRESERVE_WHITESPACE = False

# Set CustomTkinter Display Settings:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Set Default Pathway to Relative Assets:
def ewrelative_to_assets(path: str) -> Path:
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
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb',
           'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df = pd.read_csv(ASSETS_PATH / "laptops_dataset_clean_refined.csv",
                 usecols=['os', 'ssd', 'ram_gb', 'display_size', 'touchscreen', 'brand'])

# Pandas Main Dataframe Refinement (Removing all Rows with NaN Values within the Main Dataframe & Updateing the Index axis Accordingly):
df = df.dropna()
df = df.dropna(axis=0)
df = df.dropna().reset_index(drop=True)

# Pandas Results Dataframe Configuration (Set Columns):
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb',
           'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df_results = pd.read_csv(
    ASSETS_PATH / "laptops_dataset_clean_refined_dataref.csv")

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

# UUID Configuration:
unique_id = uuid.uuid4()
unique_id_str = str(unique_id)

# Set Default customtkinter window values:
button_border_width = 2
global_frame_width = 140
x_axis_padding_0 = 0
x_axis_padding_10 = 10
x_axis_padding_20 = 20
y_axis_padding_0 = 0
y_axis_padding_10 = 10
y_axis_padding_20 = 20


class ToplevelWindow(customtkinter.CTkToplevel):
    '''Results window is created as part of the CTK Package.'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "assets")

        df['count'] = df[['os', 'ssd', 'ram_gb',
                          'touchscreen', 'brand']].sum(axis=1)
        df['count'] = pd.to_numeric(df['count'], errors='coerce')
        rslt_df = df.nlargest(10, 'count')
        data_index = rslt_df.index

        # Datalabel readout Configuration:
        dataprintout = df_results.loc[df_results.index[data_index]]
        self.df_reset = dataprintout.set_index('Brand')

        # Configure Results Window:
        self.title(
            "Laptop Price Calculator 12.6: Results")
        self.geometry(f"{1020}x{320}")

        # Configure Results Window Grid Layout (4x4):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=global_frame_width, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "laptop_image.png")), size=(200, 200))
        self.sidebar_frame_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_frame_label.grid(row=4, column=0, padx=x_axis_padding_20, pady=y_axis_padding_20)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Laptop Price Calculator\nResults", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=x_axis_padding_20, pady=(20, 10))

        # Instruction Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.instruction_frame = customtkinter.CTkFrame(self, width=global_frame_width)
        self.instruction_frame.grid(row=0, column=1, padx=(
            20, 20), pady=(20, 0), sticky="nsew")
        self.instruction_frame.grid_rowconfigure(2, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.instruction_frame, text="                   Thank you for using the Laptop Price Calculator 2023!", anchor="center", compound="center", justify="center", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=4, padx=x_axis_padding_20, pady=(20, 20))
        self.exit_button = customtkinter.CTkButton(master=self, state="enabled", fg_color="#DC3545", border_width=button_border_width, text_color=(
            "gray10", "#DCE4EE"), border_color="#DC3545", text="Exit", command=self.exit_button_2)
        self.exit_button.grid(row=3, column=1, padx=(
            20, 20), pady=(20, 20), sticky="nsew")
        self.go_back_button = customtkinter.CTkButton(
            master=self, command=self.go_back)
        self.go_back_button.grid(row=2, column=1, padx=(
            20, 20), pady=(20, 0), sticky="nsew")
        self.save_button = customtkinter.CTkButton(
            master=self, command=self.save_file)
        self.save_button.grid(row=1, column=1, padx=(
            20, 20), pady=(20, 0), sticky="nsew")

        # Set All Default Values:
        '''Default values are set.'''
        self.go_back_button.configure(state="enabled", text="Change your Specifications")
        self.save_button.configure(state="enabled", fg_color="#28A745", text="Save your Results as a PDF file")

    def exit_button_2(self):
        exit_yes = tkinter.messagebox.askyesnocancel(
            title="exit_button", message="Are you sure that you want to Exit the Application?", icon='warning')

        if exit_yes:
            self.quit()

    def go_back(self):
        tkinter.messagebox.showinfo("Warning", "Please clear your selection before changing any Specifications!")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf")

        if file_path:
            pdf = fpdf.FPDF(orientation='L', format='letter')
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(40, 10, "Laptop Price Calculator 2023: Results")
            pdf.ln()
            pdf.set_font('Arial', '', 9)
            pdf.multi_cell(0, 10, tabulate(
                self.df_reset, headers='keys', colalign='center', tablefmt='plain'), align='C')
            pdf.ln()
            pdf.set_font('Arial', 'I', 9)
            pdf.multi_cell(0, 3, "All content and materials available on this platform, including but not limited to text, graphics, logos, images, audio clips, video clips, and data compilations, are the property of the respective owner, protected by copyright laws and international treaties. Unauthorized copying, reproduction, modification, distribution, transmission, display, or usage of any copyrighted material without prior written consent from the owner may result in legal action and infringement claims. Visitors and users of this platform are granted a limited, non-exclusive, and non-transferable license to access and use the content and materials for personal and non-commercial purposes. This license does not grant the right to reproduce, distribute, modify, display, or create derivative works of the copyrighted materials. Any use of the copyrighted material for commercial purposes, including but not limited to reproduction, distribution, display, or creation of derivative works, requires prior written permission from the owner. Requests for permission should be addressed to the owner and include detailed information about the intended use. All trademarks, service marks, logos, and trade names displayed on this platform are the property of their respective owners and may not be used without prior written permission. This copyright statement applies to all content and materials available on this platform, whether displayed or accessed through various devices or mediums, including but not limited to websites, applications, social media, and other digital or analog formats. We reserve the right to modify, update, or remove any content or materials on this platform without prior notice. The unauthorized use of any copyrighted material, trademarks, service marks, or logos may result in civil and/or criminal penalties. By accessing or using this platform, you acknowledge and agree to abide by this copyright statement and any applicable laws or regulations regarding copyright and intellectual property rights. This copyright statement is effective as of Friday the 26th of May 2023 and may be updated or revised at any time without prior notice.")
            pdf.ln()
            pdf.ln()
            pdf.set_font('Arial', 'B', 9)
            pdf.cell(40, 10, "Result UUID:")
            pdf.set_font('Courier', '', 9)
            pdf.multi_cell(0, 10, unique_id_str)
            pdf.output(file_path, 'F')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "assets")

        # Configure Master Window:
        self.title("Laptop Price Calculator 12.6")
        self.geometry(f"{1000}x{768}")

        # Configure Master Window Grid Layout (4x4):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # Sidebar Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=global_frame_width, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "laptop_image.png")), size=(200, 200))
        self.sidebar_frame_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_frame_label.grid(row=4, column=0, padx=x_axis_padding_20, pady=y_axis_padding_20)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Laptop Price Calculator", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=x_axis_padding_20, pady=(20, 10))
        self.reset_button = customtkinter.CTkButton(
            self.sidebar_frame, command=self.reset_button)
        self.reset_button.grid(row=1, column=0, padx=x_axis_padding_20, pady=y_axis_padding_10)
        self.update_button = customtkinter.CTkButton(
            self.sidebar_frame, command=self.update_button)
        self.update_button.grid(row=2, column=0, padx=x_axis_padding_20, pady=y_axis_padding_10)
        self.feedback_button = customtkinter.CTkButton(
            self.sidebar_frame, command=self.feedback_button)
        self.feedback_button.grid(row=3, column=0, padx=x_axis_padding_20, pady=y_axis_padding_10)
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=x_axis_padding_20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[
                                                                       "Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=6, column=0, padx=x_axis_padding_20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=x_axis_padding_20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[
                                                               "80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=x_axis_padding_20, pady=(10, 20))

        # Instruction Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.instruction_frame = customtkinter.CTkFrame(self, width=global_frame_width)
        self.instruction_frame.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.instruction_frame.grid_rowconfigure(4, weight=1)
        self.instruction_label = customtkinter.CTkLabel(self.instruction_frame, text="How to use the Laptop Price Calculator:\n\n1. Once the program has loaded correctly, you will see the main window of the\n     program with several input fields and buttons.\n2. Using the Laptop Specification Selection Tool™, simply select from each\n     dropdown the specification that best suits your needs.\n3. Once you have made all of your selections, click on the 'Submit' button to\n     view your results.\n4. To exit the program at any time, click on the 'Exit' Button.\n\nNote: To update the Master Database to the Latest data, please click the\n'Update Database' Button and upload your preferred CSV file. ", anchor="center", justify="left", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.instruction_label.grid(row=0, column=0, padx=x_axis_padding_20, pady=(20, 10))

        # GitHub Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.github_frame = customtkinter.CTkFrame(self, width=global_frame_width)
        self.github_frame.grid(row=0, column=3, padx=(
            20, 20), pady=(20, 0), sticky="nsew")
        self.github_frame.grid_rowconfigure(4, weight=1)
        self.logo_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "github_logo.png")), size=(100, 100))
        self.github_frame_label = customtkinter.CTkLabel(
            self.github_frame, text="", image=self.logo_image, compound="center", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.github_frame_label.grid(row=4, column=0, padx=x_axis_padding_20, pady=y_axis_padding_20)
        self.github_button = customtkinter.CTkButton(
            self.github_frame, command=self.open_github_link)
        self.github_button.grid(row=5, column=0, padx=x_axis_padding_20, pady=y_axis_padding_10)

        # Entry Field and Buttons:
        '''Frame widget is created as part the CTKFrame.'''
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Please enter Result UUID:")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="nsew")
        self.submit_button = customtkinter.CTkButton(master=self, state="enabled", fg_color="#28A745", border_width=button_border_width, text_color=(
            "gray10", "#DCE4EE"), border_color="#28A745", text="Submit", command=self.submit_button)
        self.submit_button.grid(row=1, column=3, padx=(
            20, 20), pady=(38, 0), sticky="nsew")
        self.exit_button = customtkinter.CTkButton(master=self, state="enabled", fg_color="#DC3545", border_width=button_border_width, text_color=(
            "gray10", "#DCE4EE"), border_color="#DC3545", text="Exit", command=self.exit_button_1)
        self.exit_button.grid(row=3, column=3, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        # Set All Default Values:
        '''Default values are set.'''
        self.reset_button.configure(state="enabled", fg_color="#DC3545", border_width=button_border_width, text_color=(
            "gray10", "#DCE4EE"), border_color="#DC3545", text="Reset/Clear Form")
        self.update_button.configure(state="enabled", text="Update Database")
        self.feedback_button.configure(
            state="enabled", text="Provide Feedback")
        self.github_button.configure(state="enabled", text="View on GitHub")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        # Selection Frame with Internal Widgets:
        '''Frame widget is created as part the CTKFrame.'''
        self.tabview = customtkinter.CTkTabview(self, width=50)
        self.tabview.grid(row=1, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Laptop Specification Selection Tool™")
        self.tabview.tab(
            "Laptop Specification Selection Tool™").grid_columnconfigure(0, weight=1)
        self.label_option_menu_1_brand = customtkinter.CTkLabel(
            self.tabview.tab("Laptop Specification Selection Tool™"), text="Laptop Brand")
        self.label_option_menu_1_brand.grid(row=0, column=0, padx=x_axis_padding_0, pady=y_axis_padding_0)
        self.option_menu_1_brand = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=[
                                                               "-", "Apple", "ASUS", "Dell", "HP", "MSI"], command=self.option_menu_1_brand_callback)
        self.option_menu_1_brand.grid(row=1, column=0, padx=x_axis_padding_20, pady=(0, 10))
        self.label_option_menu_2_operating_system = customtkinter.CTkLabel(
            self.tabview.tab("Laptop Specification Selection Tool™"), text="Operating System")
        self.label_option_menu_2_operating_system.grid(
            row=2, column=0, padx=x_axis_padding_0, pady=y_axis_padding_0)
        self.option_menu_2_operating_system = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=[
                                                                          "-", "Windows", "Mac", "DOS"], command=self.option_menu_2_operating_system_callback)
        self.option_menu_2_operating_system.grid(
            row=3, column=0, padx=x_axis_padding_20, pady=(0, 10))
        self.label_option_menu_3_display_size = customtkinter.CTkLabel(self.tabview.tab(
            "Laptop Specification Selection Tool™"), text="Display Size (inches)")
        self.label_option_menu_3_display_size.grid(
            row=4, column=0, padx=x_axis_padding_0, pady=y_axis_padding_0)
        self.option_menu_3_display_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=[
                                                                      "-", "13.3 inches", "14 inches", "15.6 inches", "16 inches"], command=self.option_menu_3_display_size_callback)
        self.option_menu_3_display_size.grid(
            row=5, column=0, padx=x_axis_padding_20, pady=(0, 10))
        self.label_option_menu_4_ssd_size = customtkinter.CTkLabel(
            self.tabview.tab("Laptop Specification Selection Tool™"), text="SSD Size (GB)")
        self.label_option_menu_4_ssd_size.grid(row=6, column=0, padx=x_axis_padding_0, pady=y_axis_padding_0)
        self.option_menu_4_ssd_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=[
                                                                  "-", "128 GB", "256 GB", "512 GB", "1024 GB"], command=self.option_menu_4_ssd_size_callback)
        self.option_menu_4_ssd_size.grid(
            row=7, column=0, padx=x_axis_padding_20, pady=(0, 10))
        self.label_option_menu_5_ram_size = customtkinter.CTkLabel(
            self.tabview.tab("Laptop Specification Selection Tool™"), text="RAM Size (GB)")
        self.label_option_menu_5_ram_size.grid(row=8, column=0, padx=0, pady=y_axis_padding_0)
        self.option_menu_5_ram_size = customtkinter.CTkOptionMenu(self.tabview.tab("Laptop Specification Selection Tool™"), dynamic_resizing=False, values=[
                                                                  "-", "4 GB", "8 GB", "16 GB", "32 GB"], command=self.option_menu_5_ram_size_callback)
        self.option_menu_5_ram_size.grid(
            row=9, column=0, padx=x_axis_padding_20, pady=(0, 10))
        self.label_option_menu_6_touchscreen = customtkinter.CTkLabel(
            self.tabview.tab("Laptop Specification Selection Tool™"), text="Touchscreen")
        self.label_option_menu_6_touchscreen.grid(
            row=10, column=0, padx=x_axis_padding_0, pady=y_axis_padding_0)
        self.option_menu_6_touchscreen = customtkinter.CTkOptionMenu(self.tabview.tab(
            "Laptop Specification Selection Tool™"), dynamic_resizing=False, values=["-", "Yes", "No"], command=self.option_menu_6_touchscreen_callback)
        self.option_menu_6_touchscreen.grid(
            row=11, column=0, padx=x_axis_padding_20, pady=(0, 10))

        self.toplevel_window = None

    brand_data_frames = {
        "-": None,
        "Apple": brand_apple_df,
        "ASUS": brand_asus_df,
        "Dell": brand_dell_df,
        "HP": brand_hp_df,
        "MSI": brand_msi_df
    }

    def option_menu_1_brand_callback(self, value):
        selected_brand_df = self.brand_data_frames.get(value)

        if selected_brand_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_brand_df, overwrite=True)

    os_data_frames = {
        "-": None,
        "Windows": os_windows_df,
        "Mac": os_mac_df,
        "DOS": os_dos_df
    }

    def option_menu_2_operating_system_callback(self, value):
        selected_os_df = self.os_data_frames.get(value)

        if selected_os_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_os_df, overwrite=True)

    display_size_data_frames = {
        "-": None,
        "13.3 inches": display_size_13_3_df,
        "14 inches": display_size_14_df,
        "15.6 inches": display_size_15_6_df,
        "16 inches": display_size_16_df
    }

    def option_menu_3_display_size_callback(self, value):
        selected_display_size_df = self.display_size_data_frames.get(value)

        if selected_display_size_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_display_size_df, overwrite=False)

    ssd_size_data_frames = {
        "-": None,
        "128 GB": ssd_128_df,
        "256 GB": ssd_256_df,
        "512 GB": ssd_512_df,
        "1024 GB": ssd_1024_df
    }

    def option_menu_4_ssd_size_callback(self, value):
        selected_ssd_size_df = self.ssd_size_data_frames.get(value)

        if selected_ssd_size_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_ssd_size_df, overwrite=True)

    ram_size_data_frames = {
        "-": None,
        "4 GB": ram_4_df,
        "8 GB": ram_8_df,
        "16 GB": ram_16_df,
        "32 GB": ram_32_df
    }

    def option_menu_5_ram_size_callback(self, value):
        selected_ram_size_df = self.ram_size_data_frames.get(value)

        if selected_ram_size_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_ram_size_df, overwrite=True)

    touchscreen_data_frames = {
        "-": None,
        "Yes": touchscreen_yes_df,
        "No": touchscreen_no_df
    }

    def option_menu_6_touchscreen_callback(self, value):
        selected_touchscreen_df = self.touchscreen_data_frames.get(value)

        if selected_touchscreen_df is None:
            tkinter.messagebox.showinfo("Warning", "Invalid Selection")
        else:
            df.update(selected_touchscreen_df, overwrite=True)

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

    def open_github_link(self):
        webbrowser.open("https://github.com/ISAACLINDROOS/NCEA-Level-3-2023")

    def reset_button(self):
        reset_yes = tkinter.messagebox.askyesnocancel(
            title="reset_button", message="Are you sure that you want to Reset/Clear the Form?", icon='warning')

        if reset_yes:
            tkinter.messagebox.showinfo("Information", "Form Reset/Cleared")

    def update_button(self):
        update_yes = tkinter.messagebox.askyesnocancel(
            title="update_button", message="Are you sure that you want to Update the Database?\n\nPlease Note:\nAll updated dataset files must be in a .csv format!", icon='warning')

        if update_yes:
            filename = fd.askopenfilename()

    def feedback_button(self):
        webbrowser.open(
            "https://github.com/ISAACLINDROOS/NCEA-Level-3-2023/issues")

    def exit_button_1(self):
        exit_yes = tkinter.messagebox.askyesnocancel(
            title="exit_button", message="Are you sure that you want to Exit the Application?", icon='warning')

        if exit_yes:
            self.quit()

    def submit_button(self):
        submit_yes = tkinter.messagebox.askyesnocancel(
            title="submit_button", message="Are you sure that you want to submit your entries?\n\nPlease Note:\nYou must have made a Selection for each Specification Option before Submitting!", icon='warning')

        if submit_yes:
            self.open_toplevel()
            self.print_final_dataset()
    
    # Loop Function for Testing:
    def print_final_dataset(self, dataframe=None):
        if dataframe is None:
            dataframe = df

    # Iterate through rows of the DataFrame.
        for index, row in dataframe.iterrows():
            print(f"Row {str(index + 1)}:")
            for column, value in row.items():
                print(f"{column}: {str(value)}")
            print("\n")

        if app.toplevel_window is not None:
            df_reset = app.toplevel_window.df_reset
            self.print_final_dataset(df_reset)
        else:
            print("ToplevelWindow is not open.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
