from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style


users = ['1', '2', '3']
titles = ["title1", "title2", "title3"]


def get_user():
    user_id = entry.get()
    if len(user_id) != 0 and user_id in users:
        print('welcome')
        notebook.add(add_tab, text="Add")
        notebook.add(remove_tab, text="Remove")
        notebook.add(lastread_tab, text="Last Read")
        notebook.pack(expand=True, side='bottom', fill="both")

        add_canvas.pack()
        remove_canvas.pack()
        last_canvas.pack()
        add_canvas.create_image(0, 0, image=back_img1, anchor=NW)
        remove_canvas.create_image(0, 0, image=back_img2, anchor=NW)
        last_canvas.create_image(0, 0, image=back_img3, anchor=NW)

        add_canvas.create_window(20, 50, window=search_entry, anchor=W)
        found_titles.place(x=0, y=100)

        search_button.place(x=400, y=30)
        add_button.place(x=200, y=400)
        remove_button.place(x=200, y=400)

        entry.pack_forget()
        submit_button.pack_forget()
    else:
        print('user not found')


def add_title():
    print("title added")


def search_title():
    print("searching...")
    # titles.clear()
    found_titles.delete(0, found_titles.size())
    for i in range(len(titles)):
        found_titles.insert(i, titles[i])
    found_titles.config(height=found_titles.size())


def remove_title():
    print("title removed")


window = Tk()
'''
# Establish connection with mySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1@nc310t",
    database="notification"
)

my_cursor = mydb.cursor()
'''
style_config = Style()
style_config.theme_use('default')

style_config.configure('TNotebook',
                       background='dark',
                       borderwidth=0)
style_config.configure('TNotebook.Tab',
                       font=('Courier', '20', 'bold'),
                       background='#1c1c1b',
                       foreground='white',
                       padding=[10, 2],
                       borderwidth=.5)
style_config.map('TNotebook.Tab', background=[('selected', '#4bbf45')])

entry = Entry(window, font=('Courier', '20'))
submit_button = Button(window, text="Submit", command=get_user)
entry.pack()
submit_button.pack()

notebook = ttk.Notebook(window)
add_tab = Frame(notebook)
remove_tab = Frame(notebook)
lastread_tab = Frame(notebook)

add_canvas = Canvas(add_tab, width=512, height=512)
back_img1 = PhotoImage(file='yellow.png')
remove_canvas = Canvas(remove_tab, width=512, height=512)
back_img2 = PhotoImage(file='red.png')
last_canvas = Canvas(lastread_tab, width=512, height=512)
back_img3 = PhotoImage(file='blue.png')

search_entry = Entry(add_canvas, font=('Courier', '20'), background='#f2d055')
search_button = Button(add_canvas,
                       text="Search",
                       font=('Courier', '15', 'bold'),
                       fg='black',
                       bg='#f2d055',
                       activeforeground='black',
                       activebackground='#f29f3f',
                       command=search_title)

add_button = Button(add_canvas,
                    text="Add Manga",
                    font=('Courier', '15', 'bold'),
                    fg='black',
                    bg='#f2d055',
                    activeforeground='black',
                    activebackground='#f29f3f',
                    command=add_title)
remove_button = Button(remove_canvas, text="Remove Manga",
                       font=('Courier', '15', 'bold'),
                       fg='black',
                       bg='#f58e53',
                       activeforeground='black',
                       activebackground='#fa5a41',
                       command=remove_title)
found_titles = Listbox(add_canvas,
                       font=('Courier', '15', 'bold'),
                       background='#f2d055',
                       selectbackground='#f29f3f',
                       width=100)
window.resizable(False, False)
window.mainloop()
