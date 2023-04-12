"""
 Copyright 2022 Isaac Lindroos IPP

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """

# WARNING: THE REQUIRED DEPENDENCY FILES MUST BE INSTALLED FROM requirements.txt BEFORE RUNNING THIS PROGRAM. PLEASE SEE README.MD FOR MORE INFORMATION!
# coding: utf8

# Set PATH LIB:
from pathlib import Path

# From tkinter import:
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk, filedialog, Frame, scrolledtext, Label
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import askyesno
from tkinter.ttk import Progressbar
from tkinter.scrolledtext import ScrolledText
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from tabulate import tabulate
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import webbrowser
import re
import sys
import os
import pydotplus


# Set local PATH:
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Set Tabulate Display settings:
tabulate.PRESERVE_WHITESPACE = True

# Set default PATH TO ASSETS:
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Pandas Main Dataframe Configuration: (Set Columns)
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb',
           'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df = pd.read_csv(ASSETS_PATH / "laptops_dataset_clean_refined.csv",
                 usecols=['os', 'ssd', 'ram_gb', 'display_size', 'touchscreen', 'brand'])


# Pandas Main Dataframe refinement: (Removing all Rows with NaN Values within the Main Dataframe & Updateing the Index axis Accordingly)
df = df.dropna()
df = df.dropna(axis=0)
df = df.dropna().reset_index(drop=True)


# Pandas Results Dataframe Configuration: (Set Columns)
columns = ['brand', 'model', 'processor_brand', 'processor_name', 'processor_gnrtn', 'ram_gb', 'ram_type', 'ssd', 'hdd', 'os', 'os_bit', 'graphic_card_gb',
           'weight', 'display-size', 'warranty', 'touchscreen', 'msoffice', 'latest_price', 'old_price', 'discount', 'star_rating', 'ratings', 'reviews']
df_results = pd.read_csv(
    ASSETS_PATH / "laptops_dataset_clean_refined_dataref.csv")


# Pandas Results Dataframe refinement: (Removing all Rows with NaN Values within the Main Dataframe & Updateing the Index axis Accordingly)
df_results = df_results.dropna()
df_results = df_results.dropna(axis=0)
df_results = df_results.dropna().reset_index(drop=True)


# Function: "Display settings (ALL Pandas dataframes)"
def set_pandas_display_options() -> None:
    display = pd.options.display
    display.max_columns = 1000
    display.max_rows = 1000
    display.max_colwidth = 199
    display.width = 1000


set_pandas_display_options()


# Individual dataframe Configuration:
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


# User Selection based on button function definitions:
def user_select_purpose_school():
    print("User has selected the PURPOSE of the device to be SCHOOL")


def user_select_purpose_work():
    print("User has selected the PURPOSE of the device to be WORK")


def user_select_purpose_home():
    print("User has selected the PURPOSE of the device to be HOME")


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


# Results GUI class to connect the Results GUI and the Main Window's GUI:
class ResultsWindowGUI:
    def showresultswindow(self):
        # Dataframe Refinement: + "Count", Selection of the top 10 values in "Count", Index Refrence to resultant dataframe:
        df['count'] = df[['os', 'ssd', 'ram_gb',
                          'touchscreen', 'brand']].sum(axis=1)
        rslt_df = df.nlargest(10, 'count')
        data_index = rslt_df.index

        # Datalabel readout Configuration:
        dataprintout = df_results.loc[df_results.index[data_index]]
        df_reset = dataprintout.set_index('Brand')
        datalabel = tabulate(df_reset, headers='keys', tablefmt='plain')

        # Results window GUI:
        results = tk.Toplevel()
        results.geometry("1500x1000")
        results.title("Laptop Price Calculator 10.3 - Results")
        results.configure(bg="#FFFFFF")
        results.iconphoto(False, tk.PhotoImage(
            file=relative_to_assets("usd-circle.png")))

        canvas = tk.Canvas(results, bg="#FFFFFF", height=1000,
                           width=1500, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        image_image_1 = PhotoImage(file=relative_to_assets("image_1_a.png"))
        image_1 = canvas.create_image(749.0, 894.0, image=image_image_1)

        image_image_2 = PhotoImage(file=relative_to_assets("image_2_a.png"))
        image_2 = canvas.create_image(1264.0, 851.0, image=image_image_2)

        canvas.create_text(435.0, 19.0, anchor="nw", text="Top 10 Laptop recommendations based on your Selection: ",
                           fill="#000000", font=("RobotoRoman ExtraBold", 24 * -1))
        canvas.create_text(372.0, 752.0, anchor="nw", text="To download your results as a PDF file, Click The DOWNLOAD Button. To close this window, Click EXIT at any time.",
                           fill="#000000", font=("RobotoRoman Regular", 15 * -1))
        canvas.create_text(30.0, 701.0, anchor="nw", text="\n\n\n\nPlease note: The displayed prices are\n",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(30.0, 801.0, anchor="nw", text="program was released.",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(30.0, 785.0, anchor="nw", text="correct as of the time & date that this",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(30.0, 854.0, anchor="nw", text="\nTo update prices to the latest figures &",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(30.0, 903.0, anchor="nw", text="or contact our Developer Team.",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(30.0, 887.0, anchor="nw", text="values, Please visit the GitHub Repository ",
                           fill="#000000", font=("RobotoItalic Regular", 15 * -1))
        canvas.create_text(576.0, 717.0, anchor="nw", text="Thank you for choosing Laptop Price Calculator! ",
                           fill="#007BFF", font=("RobotoRoman Bold", 16 * -1))
        canvas.create_text(643.0, 786.0, anchor="nw", text="Follow this Project on GitHub:",
                           fill="#868E96", font=("RobotoRoman Bold", 16 * -1))

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1_a.png"))
        entry_bg_1 = canvas.create_image(750.0, 323.0, image=entry_image_1)
        label = tk.Label(results, text=datalabel, relief="flat", font=(
            "RobotoRoman Regular", 10), anchor="n", padx=0, pady=5, wraplength=1450)
        label.place(x=33.0, y=68.0, width=1434.0, height=508.0)

        canvas.create_rectangle(0.0, 695.0, 1500.0, 701.0,
                                fill="#D9D9D9", outline="")

        button_image_1 = PhotoImage(file=relative_to_assets("button_1_a.png"))
        button_1 = Button(results, image=button_image_1, borderwidth=0,
                          highlightthickness=0, command=lambda: save_file(), relief="flat")
        button_1.place(x=690.0, y=599.0, width=120.0, height=36.44775390625)

        button_image_2 = PhotoImage(file=relative_to_assets("button_2_a.png"))
        button_2 = Button(results, image=button_image_2, borderwidth=0,
                          highlightthickness=0, command=confirm, relief="flat")
        button_2.place(x=714.0, y=656.0, width=72.0, height=18.44775390625)

        results.resizable(False, False)
        results.mainloop()


ResultsWindow = ResultsWindowGUI()


# Function "Refresh Window":
def refresh():
    window.update()


# Function "Quit Window + Confirmation":
def confirm():
    answer = askyesno(title='Exit Confirmation',
                      message='Are you sure that you want to quit?', icon='warning')
    if answer:
        closewindow()


# Function "Generation + Confirmation":
def confirmgen():
    answer = askyesno(title='Confirm Price Generation',
                      message='Are you sure that you want to Generate results?')
    if answer:
        ResultsWindow.showresultswindow()


# Function "Destroy Window - <window>":
def closewindow():
    window.destroy()


# Function "Hide Window - <window>":
def hidewindow():
    window.withdraw()


# Function "Save File":
def save_file():
    f = asksaveasfile(initialfile='My Results.pdf',
                      defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])


# Function "Set Label text":
def get_input():
    label.config(text="")


# Tkinter GUI: Initial Window settings (Main):
window = tk.Tk()
window.geometry("1000x600")
window.configure(bg="#FFFFFF")
window.title("Laptop Price Calculator 10.3")
logo = tk.PhotoImage(file=ASSETS_PATH / "usd-circle.png")
window.call('wm', 'iconphoto', window._w, logo)


# Tkinter GUI: Window GUI Outline (CANVAS):
canvas = Canvas(window, bg="#FFFFFF", height=600, width=1000,
                bd=0, highlightthickness=0, relief="ridge")


# Tkinter GUI: Window GUI Outline (CANVAS COMPONENTS >):
canvas.place(x=0, y=0)
canvas.create_rectangle(0.0, 0.0, 418.0, 600.0, fill="#007BFF", outline="")
canvas.create_rectangle(0.0, 60.0, 418.0, 507.0, fill="#6C757D", outline="")
canvas.create_rectangle(0.0, 57.0, 418.0, 63.0, fill="#FFFFFF", outline="")


image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(208.0, 284.0, image=image_image_1)


canvas.create_text(148.0, 451.0, anchor="nw", text=" Easy, Simple!",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 20 * -1))
canvas.create_text(84.0, 12.0, anchor="nw", text="Laptop Price Calculator",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 24 * -1))
canvas.create_text(25.0, 80.0, anchor="nw", text="The best way to find the right laptop that works for you!",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 15 * -1))
canvas.create_text(103.0, 545.0, anchor="nw", text="Click Generate to calculate Laptop Cost",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 12 * -1))
canvas.create_text(113.0, 576.0, anchor="nw", text="Exit at any time to close the window",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 12 * -1))
canvas.create_text(68.0, 514.0, anchor="nw", text="Select an option in each row according to your needs ",
                   fill="#FFFFFF", font=("RobotoRoman Regular", 12 * -1))
canvas.create_text(603.0, 12.0, anchor="nw", text="Find a laptop for you!",
                   fill="#000000", font=("RobotoRoman Regular", 24 * -1))
canvas.create_text(615.0, 65.0, anchor="nw", text="What will be the main purpose of the Laptop?",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(555.0, 579.0, anchor="nw", text="Please wait until results have been Generated before exiting this window",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(524.0, 472.0, anchor="nw", text="Results will be shown in a seperate window ",
                   fill="#000000", font=("RobotoRoman Regular", 20 * -1))
canvas.create_text(676.0, 114.0, anchor="nw", text="Operating System",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(677.0, 163.0, anchor="nw", text="Storage Capacity",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(671.0, 212.0, anchor="nw", text="RAM (Memory) Size",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(688.0, 261.0, anchor="nw", text="Display Size",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(687.0, 310.0, anchor="nw", text="Touchscreen",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(677.0, 359.0, anchor="nw", text="Brand Preference",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))
canvas.create_text(700.0, 408.0, anchor="nw", text="Notes:",
                   fill="#000000", font=("RobotoRoman Regular", 10 * -1))


entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(715.0, 441.5, image=entry_image_1)


entry_1 = Entry(bd=0, bg="#F5F5F5", highlightthickness=0)
entry_1.place(x=511.0, y=422.0, width=408.0, height=37.0)


canvas.create_rectangle(0.0, 57.0, 1000.0, 63.0, fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 106.0, 1000.0, 112.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 155.0, 1000.0, 161.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 204.0, 1000.0, 210.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 253.0, 1000.0, 259.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 302.0, 1000.0, 308.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 351.0, 1000.0, 357.0,
                        fill="#D9D9D9", outline="")
canvas.create_rectangle(418.0, 400.0, 1000.0, 406.0,
                        fill="#D9D9D9", outline="")


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=confirmgen,
    relief="flat"
)
button_1.place(
    x=656.0,
    y=507.0,
    width=120.0,
    height=36.44775390625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_purpose_work,
    relief="flat"
)
button_2.place(
    x=679.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_purpose_school,
    relief="flat"
)
button_3.place(
    x=558.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_purpose_home,
    relief="flat"
)
button_4.place(
    x=800.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_os_mac,
    relief="flat"
)
button_5.place(
    x=679.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_os_windows,
    relief="flat"
)
button_6.place(
    x=558.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_os_dos,
    relief="flat"
)
button_7.place(
    x=800.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_storage_512,
    relief="flat"
)
button_8.place(
    x=739.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_storage_256,
    relief="flat"
)
button_9.place(
    x=619.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_storage_128,
    relief="flat"
)
button_10.place(
    x=499.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_storage_1024,
    relief="flat"
)
button_11.place(
    x=859.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_ram_16,
    relief="flat"
)
button_12.place(
    x=739.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_ram_8,
    relief="flat"
)
button_13.place(
    x=619.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_ram_4,
    relief="flat"
)
button_14.place(
    x=499.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_ram_32,
    relief="flat"
)
button_15.place(
    x=859.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_display_size_15_6,
    relief="flat"
)
button_16.place(
    x=739.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_display_size_14,
    relief="flat"
)
button_17.place(
    x=619.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_touchscreen_no,
    relief="flat"
)
button_18.place(
    x=739.0,
    y=326.0,
    width=74.0,
    height=21.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_touchscreen_yes,
    relief="flat"
)
button_19.place(
    x=619.0,
    y=326.0,
    width=74.0,
    height=21.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_display_size_13_3,
    relief="flat"
)
button_20.place(
    x=499.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_display_size_16,
    relief="flat"
)
button_21.place(
    x=860.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_brand_dell,
    relief="flat"
)
button_22.place(
    x=672.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_brand_hp,
    relief="flat"
)
button_23.place(
    x=793.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_brand_msi,
    relief="flat"
)
button_24.place(
    x=914.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_brand_asus,
    relief="flat"
)
button_25.place(
    x=551.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=user_select_brand_apple,
    relief="flat"
)
button_26.place(
    x=430.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=confirm,
    relief="flat"
)
button_27.place(
    x=680.0,
    y=549.0,
    width=72.0,
    height=18.44775390625
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=refresh,
    relief="flat"
)
button_28.place(
    x=915.0,
    y=549.0,
    width=72.0,
    height=18.44775390625
)

window.resizable(False, False)
window.mainloop()

# End
