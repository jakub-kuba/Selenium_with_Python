from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter import messagebox as msb
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Application(Frame):
    """ Application for linking """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Creates all necessary widgets"""
        self.txt_edit = tk.Text(root, background="floral white", fg="RoyalBlue4", font="sans 11 bold", state="disabled")
        fr_buttons = tk.Frame(root, background="RoyalBlue4", bd=8)
        self.btn_upload = tk.Button(fr_buttons, bg="white", fg="RoyalBlue4", text="Upload file", command = self.upload_file, font="sans 8 bold")
        self.btn_start = tk.Button(fr_buttons, bg="white", fg="RoyalBlue4", text="START", command = self.do_the_job, font="sans 8 bold")
        self.btn_upload.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.btn_start.grid(row=1, column=0, sticky="ew", padx=20)
        fr_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")
        message = "\n\n1. Upload the codes (txt)\n"
        message += "\n2. Press START"
        self.edit_text(message)

    def upload_file(self):
        """Uploads the txt file and shows the number of codes in it"""
        file = askopenfile(mode = "r", filetypes =[("Text Documents", "*.txt")])
        if file is not None:
            new_codes = file.read()
            file.close()
            with open('codes left.txt', 'w') as codes_left:
                codes_left.writelines(new_codes)
            with open('codes left.txt', 'r') as lines:
                self.lines = lines.read().splitlines()
            self.numball = len(self.lines)
            print("Codes to check: ", self.lines)
            message = "\n\nThe file has been imported.\n"
            message += "The number of codes is: "
            message += str(self.numball)
            self.edit_text(message)

    def edit_text(self, message):
        """Edits the textbox"""
        self.txt_edit.tag_configure("center", justify='center')
        self.txt_edit.configure(state="normal")
        self.txt_edit.delete(0.0, END)
        self.txt_edit.insert(0.0, message, "center")
        self.txt_edit.configure(state="disabled")

    def do_the_job(self):
        """Main part of the program"""
        #finds the required HTML element
        def get_element(browser, seconds, link, kind):
            count = 0
            while count < seconds:
                try:
                    return browser.find_element(kind, link)
                except:
                    count += 1
                    time.sleep(1)
            else:
                msb.showerror(title="Error", message="Element not found")
                raise NoSuchElementException("Element not found: ", link)

        website = 'https://data.jakub-kuba.com/table'
        elem_1_link = '/html/body/div[1]/div[2]/input'
                
        try:
            self.lines
        except AttributeError:
            return msb.showerror(title="Error", message="No file uploaded!")
        with open('codes left.txt', 'r') as rs:
            new_codes_left = rs.readlines()
        if not new_codes_left:
            print("Left is empty")
            msb.showerror(title="Error", message="Upload the file again!")
        else:
            print("Starting...")
            #driver = webdriver.Chrome("/usr/bin/chromedriver") #linux
            driver = webdriver.Chrome() #windows
            driver.get(website)
            element = get_element(driver, 10, elem_1_link, By.XPATH)
            box_elem = "input[type=checkbox]"
            boxes = driver.find_elements(By.CSS_SELECTOR, box_elem)

            for line in self.lines:
                print(line)
                element.click()
                element.send_keys(line)
                for box in boxes:
                    if box.is_displayed():
                        if not box.is_selected():
                            box.click()
                        time.sleep(1)
                        break
                del new_codes_left[0]
                print("Codes left:", len(new_codes_left))
                with open('codes left.txt', 'w') as left:
                    left.writelines(new_codes_left)
                element.clear()
                time.sleep(1)
                if not new_codes_left:
                    print("Job complete")
                    msb.showinfo(title="Info", message="Job complete!")
                    message = "\n\n\nJob complete!"
                    self.edit_text(message)
                    break

            element.send_keys(Keys.DELETE)

root = tk.Tk()
root.title("Check the Box")
root.geometry("350x125")
root.resizable(False, False)
app = Application(root)
root.rowconfigure(0, minsize=75, weight=1)
root.columnconfigure(1, minsize=50, weight=3)
root.mainloop()