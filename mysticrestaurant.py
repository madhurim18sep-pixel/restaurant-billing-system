import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {"Chickenbiryani" : 210,
              "Kadaipaneer" : 120,
              "Butterchicken" : 250,
              "Rumaliroti" : 40,
              "Naan" : 60,
              "Momos" : 100,
              "Frenchfries" : 90,
              "Noodles" : 150,
              "Vegburger" : 60,
              "Burrito" : 100}

discount_percentage = 10
gst_percentage = 18

root  = Tk()
root.title(" Mystic Restaurant")

def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    order_id = "MYS_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id

def add():
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + ":" + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

def remove():
    dish_to_remove = displayLabel.cget("text") + ":" + str(prices[displayLabel.cget("text")]) 
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

def displayChickenbiryani():
    ChickenbiryaniDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Chickenbiryani",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = ChickenbiryaniImage,
        compound = "bottom",
        padding = (5, 5, 5, 5))

def displayKadaipaneer():
    KadaipaneerDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Kadaipaneer",
        font = ('Helvetica', 16,"bold"),
        foreground = "white",
        image = KadaipaneerImage,
        compound = "bottom",
        padding=(5, 5, 5, 5))

def displayButterchicken():
    ButterchickenDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")
    
    displayLabel.configure(
        text = "Butterchicken",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = ButterchickenImage,
        compound = "bottom",
        padding=(5, 5, 5, 5))

def displayRumaliroti():
    RumalirotiDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")
    
    displayLabel.configure(
        text = "Rumaliroti",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = RumalirotiImage,
        compound = "bottom",
        padding=(5, 5, 5, 5))

def displayNaan():
    NaanDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")
    
    displayLabel.configure(
        text = "Naan",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = NaanImage,
        compound = "bottom",
        padding=(5, 5, 5, 5))

def displayMomos():
    MomosDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")
    
    displayLabel.configure(
        image = MomosImage,
        text = "Momos",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5) )

def displayFrenchfries():
    FrenchfriesDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Frenchfries",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = FrenchfriesImage,
        compound = "bottom",
        padding = (5, 5, 5, 5))

def displayNoodles():
    NoodlesDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Noodles",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = NoodlesImage,
        compound = "bottom",
        padding = (5, 5, 5, 5))

def displayVegburger():
    VegburgerDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")
    BurritoDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Vegburger",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = VegburgerImage,
        compound = "bottom",
        padding = (5, 5, 5, 5))

def displayBurrito():
    BurritoDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame")
    KadaipaneerDishFrame.configure(style = "DishFrame.TFrame")
    ButterchickenDishFrame.configure(style= "DishFrame.TFrame")
    RumalirotiDishFrame.configure(style = "DishFrame.TFrame")
    NaanDishFrame.configure(style = "DishFrame.TFrame")
    MomosDishFrame.configure(style = "DishFrame.TFrame")
    FrenchfriesDishFrame.configure(style = "DishFrame.TFrame")
    NoodlesDishFrame.configure(style = "DishFrame.TFrame")
    VegburgerDishFrame.configure(style = "DishFrame.TFrame")
    ChickenbiryaniDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        text = "Burrito",
        font=('Helvetica', 16,"bold"),
        foreground="white",
        image = BurritoImage,
        compound = "bottom",
        padding = (5, 5, 5, 5))

    
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()
        
    subtotal = int(orderTotalLabel.cget("text").replace("TOTAL : ", "").replace("$", ""))
    discount = (discount_percentage / 100) * subtotal
    discounted_total = subtotal - discount
    gst = (gst_percentage / 100) * discounted_total
    final_total = discounted_total + gst

    with open(new_receipt, 'w') as file:
        file.write("The Mystic")
        file.write("\n\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        file.write("-----------------------------------------------------------")
        file.write("\n")
        file.write("ITEMS       PRICES")
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "$\n")
        file.write("-----------------------------------------------------------")
        file.write("\n\n")
        file.write(f"Subtotal: ${subtotal: .2f}")
        file.write("\n")
        file.write(f"Discount ({discount_percentage}%): -${discount: .2f}\n")
        file.write(f"GST ({gst_percentage}%): +${gst: .2f}\n")
        file.write(f"Final Total: ${final_total: .2f}\n")
        file.write("\n")
        file.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
                      THANK YOU                                    \n\
                     Visit Again !                                    \n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    orderTotalLabel.configure(text = "TOTAL : $ 0")
    orderIDLabel.configure(text = "ORDER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")
    

s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#3C0008")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#3C0008", relief = "raised")
s.configure('SelectedDish.TFrame', background = "white")
s.configure('MenuLabel.TLabel',
            background = "#f2bc94",
            font = ("Arial", 15, "italic"),
            foreground = "black",
            padding = (5, 5, 5, 5),
            width = 26)
s.configure('orderTotalLabel.TLabel',
            background = "#f2bc94",
            font = ("Arial", 14, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w")
s.configure('orderTransaction.TLabel',
            background = "#3C0008",
            font = ('Helvetica', 15),
            foreground = "white",
            wraplength = 190,
            anchor = "nw",
            padding = (3, 3, 3, 3))

LogoImageObject = Image.open("../cs/logo.jpg").resize((220, 150))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("../cs/topbanner.jpg").resize((1300, 150))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

displayDefaultImageObject = Image.open("../cs/displaydefault.jpg").resize((580,570))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

ChickenbiryaniImageObject = Image.open("../cs/chickenbiryani.jpg").resize((580,540))
ChickenbiryaniImage = ImageTk.PhotoImage(ChickenbiryaniImageObject)

KadaipaneerImageObject = Image.open("../cs/kadaipaneer.jpg").resize((580,540))
KadaipaneerImage = ImageTk.PhotoImage(KadaipaneerImageObject)

ButterchickenImageObject = Image.open("../cs/butterchicken.jpg").resize((580,540))
ButterchickenImage = ImageTk.PhotoImage(ButterchickenImageObject)

RumalirotiImageObject = Image.open("../cs/rumaliroti.jpg").resize((580,540))
RumalirotiImage = ImageTk.PhotoImage(RumalirotiImageObject)

NaanImageObject = Image.open("../cs/naan.jpg").resize((580,540))
NaanImage = ImageTk.PhotoImage(NaanImageObject)

MomosImageObject = Image.open("../cs/momos.jpg").resize((580,540))
MomosImage = ImageTk.PhotoImage(MomosImageObject)

FrenchfriesImageObject = Image.open("../cs/frenchfries.jpg").resize((580,540))
FrenchfriesImage = ImageTk.PhotoImage(FrenchfriesImageObject)

NoodlesImageObject = Image.open("../cs/noodles.jpg").resize((580,540))
NoodlesImage = ImageTk.PhotoImage(NoodlesImageObject)

VegburgerImageObject = Image.open("../cs/vegburger.jpg").resize((580,540))
VegburgerImage = ImageTk.PhotoImage(VegburgerImageObject)

BurritoImageObject = Image.open("../cs/burrito.jpg").resize((580,540))
BurritoImage = ImageTk.PhotoImage(BurritoImageObject)


mainFrame = ttk.Frame(root, width = 1300, height = 880, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 6)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 1, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

ChickenbiryaniDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
ChickenbiryaniDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

KadaipaneerDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
KadaipaneerDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

ButterchickenDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
ButterchickenDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

RumalirotiDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
RumalirotiDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

NaanDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
NaanDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

MomosDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
MomosDishFrame.grid(row = 6, column = 0, sticky ="NSEW")

FrenchfriesDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
FrenchfriesDishFrame.grid(row = 7, column = 0, sticky ="NSEW")

NoodlesDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
NoodlesDishFrame.grid(row = 8, column = 0, sticky ="NSEW")

VegburgerDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
VegburgerDishFrame.grid(row = 9, column = 0, sticky ="NSEW")

BurritoDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
BurritoDishFrame.grid(row = 10, column = 0, sticky ="NSEW")


LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(anchor = "center",font = ("Helvetica", 15, "bold"))

ChickenbiryaniDishLabel = ttk.Label(ChickenbiryaniDishFrame, text ="Chicken biryani :   $210", style ="MenuLabel.TLabel")
ChickenbiryaniDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

KadaipaneerDishLabel = ttk.Label(KadaipaneerDishFrame, text ="Kadai paneer :       $120", style ="MenuLabel.TLabel")
KadaipaneerDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

ButterchickenDishLabel = ttk.Label(ButterchickenDishFrame, text ="Butter chicken :     $250", style ="MenuLabel.TLabel")
ButterchickenDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

RumalirotiDishLabel = ttk.Label(RumalirotiDishFrame, text ="Rumali roti :          $40", style ="MenuLabel.TLabel")
RumalirotiDishLabel.grid(row = 0, column = 0, padx =30, pady = 10, sticky = "W")

NaanDishLabel = ttk.Label(NaanDishFrame, text ="Naan :                  $60", style ="MenuLabel.TLabel")
NaanDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

MomosDishLabel = ttk.Label(MomosDishFrame, text ="Momos :              $100", style ="MenuLabel.TLabel")
MomosDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

FrenchfriesDishLabel = ttk.Label(FrenchfriesDishFrame, text ="French fries :       $90", style ="MenuLabel.TLabel")
FrenchfriesDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

NoodlesDishLabel = ttk.Label(NoodlesDishFrame, text ="Noodles :            $150", style ="MenuLabel.TLabel")
NoodlesDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

VegburgerDishLabel = ttk.Label(VegburgerDishFrame, text ="Veg burger :        $60", style ="MenuLabel.TLabel")
VegburgerDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

BurritoDishLabel = ttk.Label(BurritoDishFrame, text ="Burrito :              $100", style ="MenuLabel.TLabel")
BurritoDishLabel.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")


ChickenbiryaniDisplayButton = ttk.Button(ChickenbiryaniDishFrame, text ="Display", command = displayChickenbiryani)
ChickenbiryaniDisplayButton.grid(row = 0, column = 1, padx = 20)

KadaipaneerDisplayButton = ttk.Button(KadaipaneerDishFrame, text ="Display", command = displayKadaipaneer)
KadaipaneerDisplayButton.grid(row = 0, column = 1, padx = 20)

ButterchickenDisplayButton = ttk.Button(ButterchickenDishFrame, text ="Display", command = displayButterchicken)
ButterchickenDisplayButton.grid(row = 0, column = 1, padx = 20)

RumalirotiDisplayButton = ttk.Button(RumalirotiDishFrame, text ="Display", command = displayRumaliroti)
RumalirotiDisplayButton.grid(row = 0, column = 1, padx = 20)

NaanDisplayButton = ttk.Button(NaanDishFrame, text ="Display", command = displayNaan)
NaanDisplayButton.grid(row = 0, column = 1, padx = 20)

MomosDisplayButton = ttk.Button(MomosDishFrame, text ="Display", command = displayMomos)
MomosDisplayButton.grid(row = 0, column = 1, padx = 20)

FrenchfriesDisplayButton = ttk.Button(FrenchfriesDishFrame, text ="Display", command = displayFrenchfries)
FrenchfriesDisplayButton.grid(row = 0, column = 1, padx = 20)

NoodlesDisplayButton = ttk.Button(NoodlesDishFrame, text ="Display", command = displayNoodles)
NoodlesDisplayButton.grid(row = 0, column = 1, padx = 20)

VegburgerDisplayButton = ttk.Button(VegburgerDishFrame, text ="Display", command = displayVegburger)
VegburgerDisplayButton.grid(row = 0, column = 1, padx = 20)

BurritoDisplayButton = ttk.Button(BurritoDishFrame, text ="Display", command = displayBurrito)
BurritoDisplayButton.grid(row = 0, column = 1, padx = 20)


orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="black", background="tan",
    font=("Helvetica", 15, "bold"), anchor = "center",
    padding = (10, 10, 10, 10))
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "tan",
    foreground = "black",
    font = ("Helvetica", 13, "italic"),
    anchor = "center")
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 5)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL :   $0", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add )
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove )
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)

menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
menuFrame.rowconfigure(7, weight = 1)
menuFrame.rowconfigure(8, weight = 1)
menuFrame.rowconfigure(9, weight = 1)
menuFrame.rowconfigure(10, weight = 1)

orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)


root.mainloop()
