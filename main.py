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
    data_file = []
    data_headings = ['User', 'Pass', 'Description']
    data_values.append([1,2,3])
    data_values.append([2,3,4])
    data_cols_width = [12, 12, 35]
    layout = [
        [sg.Text("PyPass",key="-title-",font=("bold"))],
        [sg.Table(values=data_values, headings=data_headings,
                            display_row_numbers=True,
                            selected_row_colors='white on darkgray',
                            expand_y=True,
                            max_col_width=59,
                            col_widths=data_cols_width,
                            auto_size_columns=False,
                            justification='left',
                            enable_events=True,
                            num_rows=6,
                            key='-table-')],
        [sg.Button("ADD",key="-add-")]
    ]
    window = sg.Window("PyPass",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-add-":
            user_values = add_user_pass()
            data_values.append(user_values)
            data_file = []
            for i in range(0,len(data_values)):
                data_auth = data_values[i][:]
                data_auth[1] = "*****"
                data_file.append(data_auth)
            print(data_file,"secreto")
            print(data_values,"no secreto")
            window["-table-"].update(values=data_file)
            #window.update("")
        if event == "-table-":
            try:
                data_selected = values[event][0]
                print(data_selected,"aqui")
                sg.popup("User: ", data_values[data_selected][0],
                            "Pass: ", data_values[data_selected][1],
                            "Desc: ", data_values[data_selected][2])
            except IndexError:
                pass
    window.close()

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
                #if values["-desc-"] != "":
                #    have_desc = True
                #    break
                #else:
                break
        if event == "-cancel_add_user-":
            break
    if validation:
        window.close()
        return [values["-user-"],values["-pass1-"],values["-desc-"]]
    window.close()

if __name__ == "__main__":
    if menu():
        password_manager()
    