import time
import pyautogui
import tkinter as tk
import threading

# Flag to stop spamming
stop_spam = False

def stop_spamming():
    global stop_spam
    stop_spam = True
    print("Spamming stopped by user")

def start_spamming():
    global stop_spam
    stop_spam = False

    # Welcome message in ASCII art
    text = """
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗██╗   ██╗██████╗     ██████╗  ██████╗ ████████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██║   ██║██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██║ █╗ ██║███████║███████║   ██║   ███████╗██║   ██║██████╔╝    ██████╔╝██║   ██║   ██║   
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██║   ██║██╔═══╝     ██╔══██╗██║   ██║   ██║   
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝    ╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║╚██████╔╝██║         ██████╔╝╚██████╔╝   ██║   
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝      ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝         ╚═════╝  ╚═════╝    ╚═╝   
    """
    print(text)

    print("The bot will type all the lines in the txt file very fast")
    print("when u want to stop the bot just put ur mouse in the top left corner")
    
    # Start spamming after a delay
    time.sleep(3)

    with open('spam.txt', 'r') as f:
        for line in f:
            if stop_spam:
                break
            pyautogui.typewrite(line)
            pyautogui.press('enter')

    print("Script ended.")

# Create a simple Tkinter window with a Stop button
def create_gui():
    root = tk.Tk()
    root.title("Spam Bot Control")

    stop_button = tk.Button(root, text="Stop Spamming", command=stop_spamming)
    stop_button.pack(pady=20)

    # Start the spam bot in a new thread to avoid blocking the GUI
    spam_thread = threading.Thread(target=start_spamming)
    spam_thread.daemon = True  # Ensure the thread closes when the main program exits
    spam_thread.start()

    root.mainloop()

# Run the GUI
create_gui()
