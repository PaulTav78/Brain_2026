from C_menu_libs import show_menu, store_number
from A_init_heavy import *


NB_ITEMS = 10
selected = show_menu(nb_items=NB_ITEMS)
x = 800

# bien penser a desactiver le giro dans le A_init_heavy

if selected == "1":
    speed(100)
    straight(x, True)

if selected == "2":
    speed(200)
    straight(x, True)

if selected == "3":
    speed(300)
    straight(x, True)

if selected == "4":
    speed(400)
    straight(x, True)

if selected == "5":
    speed(500)
    straight(x, True)

if selected == "6":
    speed(600)
    straight(x, True)

if selected == "7":
    speed(700)
    straight(x, True)

if selected == "8":
    speed(800)
    straight(x, True)

if selected == "9":
    speed(900)
    straight(x, True)

if selected == "10":
    speed(1000)
    straight(x, True)

store_number(int(selected) % NB_ITEMS) # code du menu, ne pas enlever
