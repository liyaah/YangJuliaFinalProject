"""
Program: YangJuliaFinalProject
Author: Yang Julia
Last date Modified: Mar/14/2022
This program allows user order different flavors listed of Mochi for $1.50 and Boba Tea for $3.99 each.
The application will capture the user’s order and calculate charges, including a sales tax of 7%, and generate a total bill.
"""
# importing the packages

import tkinter as tk

from tkinter import *

from tkinter import messagebox

from PIL import ImageTk, Image

# creating the root window

root = tk.Tk()

root.minsize(700, 500)  # setting the size of the

# main window

root.title("So ThirsTea")  # title of the window

# opening 1st image file

image1 = Image.open("mochi.jpg")

# resizing the image

image1 = image1.resize((150, 150), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)

# opening 2nd image file

image2 = Image.open("boba.jpg")

# resizing the image

image2 = image2.resize((150, 150), Image.ANTIALIAS)

test2 = ImageTk.PhotoImage(image2)

# setting 1st image in label l3

l3 = tk.Label(root, image=test)

l3.place(x=50, y=10)  # position the label

# setting 2nd image in label l4

l4 = tk.Label(root, image=test2)

l4.place(x=350, y=10)  # position the label

# displaying a menu/flavors for mochi using a label with font and size of text

l5 = tk.Label(root, text="Mochi flavors ($1.50 each): Strawberry, Green Tea, Mango", font=("Arial", 15))

l5.place(x=50, y=200)

# displaying a menu/flavor for boba

l6 = tk.Label(root, text="Boba Tea flavors ($3.99 each): Passion Fruit, Lychee, Taro", font=("Arial", 15))

l6.place(x=50, y=230)

l1 = tk.Label(root, text="Enter Mochi flavor(s) (using comma)", font=("Arial", 15))

l1.place(x=50, y=280)

# entry box with font and size

t1 = tk.Entry(root, font=("Arial", 15))

t1.place(x=420, y=280)  # position of entry box

l2 = tk.Label(root, text="Enter Boba Tea flavor(s) (using comma)", font=("Arial", 15))

l2.place(x=50, y=310)

t2 = tk.Entry(root, font=("Arial", 15))

t2.place(x=420, y=310)


# function to calculate price of mochi and boba separately

def calc():

    s1 = t1.get()  # taking all the contents from 1st entry

    s2 = t2.get()  # taking all the contents from 2nd entry

    mochi = s1.split(sep=', ')  # separating each item from s1

    boba = s2.split(sep=', ')  # separating each item from s1

    # Create finalized lists of mochi and boba
    mochifinal = []

    bobafinal = []

    # Checks the inputs in the mochi list. If there are key words that match with the flavor list, add it to the finalized list which will be used for calculation
    for flavor in range(len(mochi)):
        print(flavor)
        if mochi[flavor] == "Strawberry" or mochi[flavor] == "Mango" or mochi[flavor] == "Green Tea":
            mochifinal.append(mochi[flavor])

    # Checks the inputs in the mochi list. If there are key words that match with the flavor list, add it to the finalized list which will be used for calculation
    for flavor in range(len(boba)):
        print(flavor)
        if boba[flavor] == "Passion Fruit" or boba[flavor] == "Lychee" or boba[flavor] == "Taro":
            bobafinal.append(boba[flavor])

    len1 = len(mochifinal)  # finding the length(number of items or mochi)

    len2 = len(bobafinal)  # finding the length(number of items or boba)

    if len1 == 0:
        priceOfmochi = 1 * 1.50
    else:
        priceOfmochi = len1 * 1.50  # multiplying number of mochi with price of 1

    if len2 == 0:
        priceOfboba = 1 * 3.99
    else:
        priceOfboba = len2 * 3.99  # multiplying number of boba with price of 1

    # displaying in a message box

    s = 'Price of each Mochi selected : {} Price of each Boba Tea selected : {}'.format(priceOfmochi, priceOfboba)

    messagebox.showinfo('Price of each Mochi and Boba Tea selected', s)

    # returning price of mochi ,boba ,list of mochi flavors and boba flavors

    return priceOfmochi, priceOfboba, mochifinal, bobafinal

def total():
    # collecting price of mochi and boba and flavors of mochi and boba

    pr_mochi, pr_boba, mochifinal, bobafinal = calc()

    # Checks to see if there are any flavors in the finalized lists. If the contents in the lists are not valid, then show message. If not, continue with calculation.
    if len(mochifinal) == 0 and len(bobafinal) == 0:
        messagebox.showinfo('Wait!', 'Please add a valid flavor!')
    elif len(mochifinal) == 0:
        messagebox.showinfo('Wait!', 'Please add a valid Mochi flavor!')
    elif len(bobafinal) == 0:
        messagebox.showinfo('Wait!', 'Please add a valid Boba Tea flavor!')
    else:

        total = pr_mochi + pr_boba  # finding total price

        s = 'Total + 7% tax : {:5.2f}'.format(total)

        child_w = Toplevel(root)  # creating another window

        child_w.geometry("350x350")  # size of child window

        child_w.grid_location(x=300, y=300)  # location of child window

        child_w.title("Receipt")  # title of the window

        # creating label widgets

        label_child = Label(child_w, text=s, font=('Helvetica 15'))

        label_child.place(x=20, y=50)  # positioning the label

        l2 = Label(child_w, text="You have ordered:", font=('Helvetica 15'))

        l2.place(x=20, y=100)  # positioning the label

        s2 = "Mochi: " + ' '.join(mochifinal) + " , " + " Boba Tea: " + ' '.join(bobafinal)

        l3 = Label(child_w, text=s2, font=('Helvetica 15'))

        l3.place(x=20, y=150)  # positioning the label

# creating the buttons

# click this button to calculate price of mochi and boba tea separately
b1 = tk.Button(root, text="Price of Mochi and Boba Tea selected", command=calc, font=("Arial", 15))
b1.place(x=100, y=380)

# click this button to calculate total price of mochi and boba tea
b2 = tk.Button(root, text="Overall Order Total", command=total, font=("Arial", 15))
b2.place(x=100, y=420)

# click this button to exit from the program
b3 = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 15))
b3.place(x=100, y=460)

# starting the main window
root.mainloop()