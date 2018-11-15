from tkinter import *
import backend


class Frontend(object):
    def __init__(self, window):
        self.window = window
        self.bk = backend.Backend()
        myfont = ("Times New Roman", 18)
        # create the widgets

        # start with the labels
        self.lb1 = Label(master=window, text="Title", font=myfont)
        self.lb1.grid(row=0, column=0)

        self.lb2 = Label(master=window, text="Year", font=myfont)
        self.lb2.grid(row=0, column=2)

        self.lb3 = Label(master=window, text="Director", font=myfont)
        self.lb3.grid(row=1, column=0)

        self.lb4 = Label(master=window, text="Actress/Actor", font=myfont)
        self.lb4.grid(row=1, column=2)

        # create the entries
        self.name_text = StringVar()
        self.et1 = Entry(master=window, textvariable=self.name_text, font=myfont)
        self.et1.grid(row=0, column=1)

        self.year_text = StringVar()
        self.et2 = Entry(master=window, textvariable=self.year_text, font=myfont)
        self.et2.grid(row=0, column=3)

        self.dir_text = StringVar()
        self.et3 = Entry(master=window, textvariable=self.dir_text, font=myfont)
        self.et3.grid(row=1, column=1)

        self.act_text = StringVar()
        self.et4 = Entry(master=window, textvariable=self.act_text, font=myfont)
        self.et4.grid(row=1, column=3)

        # create the listbox
        self.listbox = Listbox(master=window, height=10, width=40, font=("Times New Roman", 15))
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2)

        self.listbox.bind('<<ListboxSelect>>', self.get_row)

        self.scroll = Scrollbar(master=window)
        self.scroll.grid(row=2, column=2, rowspan=8, sticky="nsw")

        # link the scrollbar to the listbox
        self.scroll.configure(command=self.listbox.yview)

        # Add the buttons
        self.bt1 = Button(master=window, text="View All", width=10, font=myfont, command=self.view_command)
        self.bt1.grid(row=3, column=3)

        self.bt2 = Button(master=window, text="Add", width=10, font=myfont, command=self.add_command)
        self.bt2.grid(row=4, column=3)

        self.bt3 = Button(master=window, text="Delete", width=10, font=myfont, command=self.delete_command)
        self.bt3.grid(row=5, column=3)

        self.bt4 = Button(master=window, text="Search", width=10, font=myfont, command=self.search_command)
        self.bt4.grid(row=6, column=3)

        self.bt5 = Button(master=window, text="Close", width=10, font=myfont, command=self.close)
        self.bt5.grid(row=7, column=3)

    def view_command(self):
        # display the information into the inbox
        self.listbox.delete(0, END)
        rows = self.bk.view_all()
        for line in rows:
            self.listbox.insert(END, line)

    def add_command(self):
        self.listbox.delete(0, END)
        title = self.name_text.get()
        director = self.dir_text.get()
        year = self.year_text.get()
        lead = self.act_text.get()
        self.bk.add(title=title, director=director, year=year, lead=lead)
        self.listbox.insert(END, (title, director, year, lead))
        self.reset_entries()

    def get_row(self, event=None):
        index = self.listbox.curselection()[0]
        line = self.listbox.get(index)
        self.name_text.set(line[1])
        self.dir_text.set(line[2])
        self.act_text.set(line[3])
        self.year_text.set(line[4])
        return line

    def delete_command(self):
        line = self.get_row()
        self.bk.delete(line[0])
        self.view_command()
        self.reset_entries()

    def search_command(self):
        self.listbox.delete(0, END)
        title = self.name_text.get()
        director = self.dir_text.get()
        year = self.year_text.get()
        lead = self.act_text.get()
        rows = self.bk.search(title=title, director=director, year=year, lead=lead)
        for line in rows:
            self.listbox.insert(END, line)
        self.reset_entries()

    def reset_entries(self):
        self.name_text.set("")
        self.dir_text.set("")
        self.act_text.set("")
        self.year_text.set("")

    def close(self):
        exit(0)


window = Tk()
front = Frontend(window)
window.mainloop()