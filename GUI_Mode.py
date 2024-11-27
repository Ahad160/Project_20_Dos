import tkinter as tk
from tkinter import ttk
from yt_dlp import YoutubeDL


def YouTube_Download_Module(Url):
    Video_Settings= {
        'format': f'bestvideo[height<={selected_option.get()}]+bestaudio/best[height<=2160]',

        # 'format': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',

        'outtmpl': r'4K-V.%(ext)s',
    }
    with YoutubeDL(Video_Settings) as ydl:
        ydl.download([Url])


def Download_Event():
    
    User_URL=entry.get()
    YouTube_Download_Module(User_URL)
    # Main label with extra bottom padding
    label = ttk.Label(root, text="Patience, The Video is Downloading...",foreground="#ff8000")
    label.grid(row=0, column=0,padx=0, pady=(0,0))  # Reduces bottom padding on the label
    #Padx left-Right
    #pady up-down

    # Main label with extra bottom padding
    label = ttk.Label(root, text="Download Completed!",foreground="#006400")
    label.grid(row=0, column=0,padx=0, pady=(0,0))  # Reduces bottom padding on the label


#               ---GUI MODE---
# Initialize the main application window
root = tk.Tk()
root.title("4K Videos")
root.geometry("350x500")

# Load the Azure theme
try:
    root.tk.call("source", r"E:\Codeing\Python Language\Projects\Project_20_YouTube_4K_Tool\Theme\azure.tcl")  # Replace with the correct path to azure.tcl
    root.tk.call("set_theme", "light")  # Use "dark" for dark mode
except tk.TclError:
    print("Azure theme file not found. Please check the path to 'azure.tcl'.")

# ⭕ URL Entry Box
# Main label
label = ttk.Label(root, text="YouTube 4K Video Downloader")
label.grid(row=0, column=0,padx=0, pady=0)
# Main label with extra bottom padding
label = ttk.Label(root, text="Enter YouTube Video link")
label.grid(row=1, column=0,padx=0, pady=(0, 0))  # Reduces bottom padding on the label
# Add a ttk entry box with top padding to add more spacing below the label
entry = ttk.Entry(root, width=30)
entry.grid(row=2, column=0,padx=0, pady=(0, 0))  # Adds top padding on the entry box

# ⭕ OptionMenu
# Define a frame for the OptionMenu
frame = ttk.Frame(root, padding=(0, 0))
frame.grid(row=3, column=0, padx=(0,0), pady=(0,0), sticky="nsew")
# Create a list of options
option_menu_list = ["", "2160p (4K)", "1440p (2K)", "1080P","720p", "480p", "360p","240p","144p"]
# Create a StringVar to hold the selected value
selected_option = tk.StringVar(value=option_menu_list[1])
# Create the OptionMenu widget
optionmenu = ttk.OptionMenu(frame, selected_option, *option_menu_list)
optionmenu.grid(row=3, column=0, padx=(0,0), pady=0, sticky="nsew")


#---------------------------------------------------------------------
def checkbutton_callback(var):
    if var.get():
        # Checkbutton is checked
        label.config(text="Checkbutton is checked")
    else:
        # Checkbutton is unchecked
        label.config(text="Checkbutton is unchecked")

# Create BooleanVars to track the state of each Checkbutton
var_0 = tk.BooleanVar(value=False)
var_1 = tk.BooleanVar(value=True)

# Create Checkbuttons
check_1 = ttk.Checkbutton(frame, text="Audio", variable=var_1, command=lambda: checkbutton_callback(var_0))
check_1.grid(row=3, column=3, padx=(0,0), pady=0, sticky="nsew")

# Create a label to display the status
label = ttk.Label(frame, text="")
label.grid(row=3, column=4, padx=0, pady=0, sticky="nsew")



# Apply the style to the button
accent_button = ttk.Button(root, text="Download", style='Accent.TButton',command=Download_Event)
accent_button.grid(row=4, column=0,padx=0, pady=(0, 0))



# Run the application
root.mainloop()