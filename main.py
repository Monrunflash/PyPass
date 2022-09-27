import PySimpleGUI as sg
import encrypter as enc
import os.path

def menu():
    title = [
        [sg.Text(" ____        ____               ")],
        [sg.Text("|  _ \ _   _|  _ \ __ _ ___ ___ ")],
        [sg.Text("| |_) | | | | |_) / _` / __/ __|")],
        [sg.Text("|  __/| |_| |  __/ (_| \__ \__ \\")],
        [sg.Text("|_|    \__, |_|   \__,_|___/___/")],
        [sg.Text("       |___/                    ")],
    ]
    start_button = [[sg.Button("Start",key="-start-")]]
    layout = [
                [sg.Column(title)],
                [sg.Column(start_button)]
            ]
    window = sg.Window("PyPass",layout,font=("Andale Mono", 12),element_justification="c")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-start-" and sg.popup_yes_no("Do you have a file?") == "Yes":
            enc_file = sg.popup_get_file("Enter file name")
            if os.path.exists(enc_file):
                passwd = sg.popup_get_text("Password", password_char="*")
                enc.decrypt(enc_file, passwd)
            else:
                sg.popup_error("File doesn't exists!")
        else:
            window.close()
            return True
    window.close()

def password_manager():
    data_values = []
    data_headings = ['User', 'Pass', 'Description']
    data_values.append([1,2,3])
    data_values.append([1,2,3])
    data_cols_width = [5, 8, 35]
    layout = [
        [sg.Text("PyPass",key="-title-",font=("bold"))],
        [sg.Table(values=data_values, headings=data_headings,
                            max_col_width=48,
                            col_widths=data_cols_width,
                            auto_size_columns=False,
                            justification='left',
                            enable_events=True,
                            num_rows=6,
                            key='_filestable_')],
        [sg.Button("ADD",key="-add-")]
    ]
    window = sg.Window("PyPass",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-add-":
            user_values = add_user_pass()
            print(user_values)
            data_values.append(user_values)
            window["_filestable_"].update(data_values.append(for user_values[i] in range(0,len(user_values)))
            #window.update("")

def add_user_pass():
    layout = [
        [[sg.Text("User")]],
        [[sg.Input(key="-user-")]],
        [[sg.Text("Pass")]],
        [[sg.Input(key="-pass1-",password_char="*")]],
        [[sg.Text("Confirm Pass")]],
        [[sg.Input(key="-pass2-",password_char="*")]],
        [[sg.Text("Desc.")]],
        [[sg.Input(key="-desc-")]],
        [sg.Button("Add",key="-add_user-"),sg.Button("Cancel",key="-cancel_add_user-")],

    ]
    window = sg.Window("PyPass",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-add_user-":
            validation = True
            have_desc = False
            user = values["-user-"]
            if values["-user-"] == "":
                sg.popup_error("No user!")
                validation = False
            if values["-pass1-"] != values["-pass2-"]:
                sg.popup_error("The password aren't the same!")
                validation = False
            if  validation:
                print("Validacion")
                if values["-desc-"] != "":
                    have_desc = True
                    break
                else:
                    break
        if event == "-cancel_add_user-":
            break
    if validation and have_desc:
        window.close()
        return values["-user-"],values["-pass1-"],values["-desc-"]
    window.close()

if __name__ == "__main__":
    if menu():
        password_manager()
    