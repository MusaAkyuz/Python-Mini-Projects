import tkinter
import random
from tkinter import ttk as widget
from tkinter.messagebox import showinfo
from ctypes import windll

# initialize
lower = "qwertyuopasdfghjklizxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
special = "/*-+,.\"\'\\(){}&%$#!"


def auto_generate(check_lower, check_upper, check_special, check_number, character_number):
    full_list = ""

    if (check_lower or check_upper or check_number or check_special) == 0:
        signal("You must choose one check box")
    if character_number == 0:
        signal("You can not zero character password")
    if check_lower:
        full_list += lower
    if check_upper:
        full_list += upper
    if check_special:
        full_list += special
    if check_number:
        full_list += number

    result = ""
    for _ in range(character_number):
        result += random.choice(full_list)

    result_auto.set(result)
    return True


def specific_generate(char_string, char_number):

    if char_string == "":
        signal("You must enter any character!")
    if char_number == 0:
        signal("You can not zero character password")
    result = ""
    for _ in range(char_number):
        result += random.choice(char_string)

    result_specific.set(result)
    return True


def signal(message):
    tkinter.messagebox.showinfo(title="Warning", message=message)
    return -1


try:
    # to window blur problem
    windll.shcore.SetProcessDpiAwareness(1)

    # creating window
    window = tkinter.Tk()

    # giving window name
    window.title("Password Generator")

    # icon on window
    window.iconbitmap('./icons/icon.ico')

    # not resizeable
    window.resizable(False, False)
    '''
    giving window size
    (first)x(second)+(third)+(forth)
    first is a x length
    second is a y length
    third is a distance from the left edge of the screen
    forth is a distance from the up edge of the screen
    '''
    # --- CENTERING THE SCREEN ---
    window_width = 600
    window_height = 450
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 2 - window_width / 2)
    positionDown = int(window.winfo_screenheight() / 2 - window_height / 2)
    # Positions the window in the center of the page.
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, positionRight, positionDown))

    # label frame automatically generate
    label_auto = widget.LabelFrame(window, text='Automatically generate')
    label_auto.place(x=20, y=20, width=560, height=200)

    lower_check = tkinter.IntVar()
    checkbox_lower = widget.Checkbutton(label_auto,
                                        text="Includes lower characters [a-z]",
                                        variable=lower_check,
                                        onvalue=1,
                                        offvalue=0)

    checkbox_lower.place(x=20, y=10)
    upper_check = tkinter.IntVar()
    checkbox_upper = widget.Checkbutton(label_auto,
                                        text="Includes upper characters [A-Z]",
                                        variable=upper_check,
                                        onvalue=1,
                                        offvalue=0)

    checkbox_upper.place(x=20, y=30)
    special_check = tkinter.IntVar()
    checkbox_special = widget.Checkbutton(label_auto,
                                          text="Includes special characters [/*-+,.\"\'\\(){}&%$#!]",
                                          variable=special_check,
                                          onvalue=1,
                                          offvalue=0)
    checkbox_special.place(x=20, y=50)

    number_check = tkinter.IntVar()
    checkbox_number = widget.Checkbutton(label_auto,
                                         text="Includes numbers characters [0-9]",
                                         variable=number_check,
                                         onvalue=1,
                                         offvalue=0)
    checkbox_number.place(x=20, y=70)

    label_info_a = widget.Label(label_auto, text="How much character : ")
    label_info_a.place(x=20, y=100)

    num_of_char_a = tkinter.IntVar()
    entry_number_a = widget.Entry(label_auto, textvariable=num_of_char_a)
    entry_number_a.place(x=180, y=100)

    button_generate_auto = widget.Button(label_auto, text="Generate", command=lambda: auto_generate(lower_check.get(),
                                                                                                    upper_check.get(),
                                                                                                    special_check.get(),
                                                                                                    number_check.get(),
                                                                                                    num_of_char_a.get()))
    button_generate_auto.place(x=20, y=130)

    result_auto = tkinter.StringVar()
    result_auto.set("Result will appear here")
    result_entry_a = widget.Entry(label_auto, textvariable=result_auto, state="readonly", justify="center")
    result_entry_a.place(x=130, y=133, width=300)

    # label frame specific
    label_specific = widget.LabelFrame(window, text='Specific generate')
    label_specific.place(x=20, y=240, width=560, height=200)

    label_info2 = widget.Label(label_specific, text="Write your characters : ")
    label_info2.place(x=20, y=10)

    character_list = tkinter.StringVar
    entry_list = widget.Entry(label_specific, textvariable=character_list)
    entry_list.place(x=180, y=10)

    logo = tkinter.PhotoImage(file="./icons/info.gif")
    label_logo = widget.Label(label_specific, image=logo)
    label_logo.place(x=20, y=40)

    label_info3 = widget.Label(label_specific, text="If write more than one same character, you increase\n"
                                                    "the probability of the character appearing")
    label_info3.place(x=85, y=45)

    label_info4 = widget.Label(label_specific, text="How much character : ")
    label_info4.place(x=20, y=95)

    num_of_char_s = tkinter.IntVar()
    entry_number_s = widget.Entry(label_specific, textvariable=num_of_char_s)
    entry_number_s.place(x=180, y=95)

    button_generate_specific = widget.Button(label_specific, text="Generate",
                                             command=lambda: specific_generate(entry_list.get(),
                                                                               num_of_char_s.get()))
    button_generate_specific.place(x=20, y=125)

    result_specific = tkinter.StringVar()
    result_specific.set("Result will appear here")
    result_entry_s = widget.Entry(label_specific, textvariable=result_specific, state="readonly", justify="center")
    result_entry_s.place(x=130, y=127, width=300)

except:
    signal()
finally:
    window.mainloop()
