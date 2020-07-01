#                                        *** Module : Interface ***

# --- # --- # --- # --- # --- # IMPORT

from tkinter import *
from PIL import Image
from PIL import ImageTk
from Algo import *
from os import path

# --- # --- # --- # --- # --- # CONSTANTES

RAPPORT = 1.375

            # --> Constantes d'encadrement de la fractale dans le plan complexe :
A_MIN = -2.4
A_MAX = 0.9
B_MIN = -1.2
B_MAX = 1.2

            # --> Constantes définissant la taille du cadre principal.
L_CADRE = 660 
H_CADRE = L_CADRE // RAPPORT

            # --> Constantes définissant le repère du plan complexe :
RAPPORT_POSI_NEGA = abs(A_MIN/A_MAX)# = 2.66666
ORIGINE_V = 480 # A quoi correspond 480
ORIGINE_H = H_CADRE // 2

            # --> Constantes de gestion 
set_bouton_gene = False

# --- # --- # --- # --- # --- # FONCTIONS INTERFACE

def define_motion(event):
    global val_a, val_b
    x_souris = event.x
    y_souris = event.y
    labl_position_pixel.configure(text = "x : " + str(x_souris) +
                                         " ; y : " + str(y_souris))
    labl_position_pixel.pack()
    set_signe = "+"
            # --> Fixe a
    if x_souris > ORIGINE_V :
        surface_non_x = ORIGINE_V
        x_souris = x_souris - surface_non_x
        surface_x = L_CADRE - surface_non_x
        rapport = A_MAX / surface_x 
        val_a = x_souris * rapport
    elif x_souris < ORIGINE_V :
        surface_x = ORIGINE_V
        rapport = abs(A_MIN) / surface_x
        val_a = x_souris * rapport 
        val_a = invert(0, A_MIN, val_a)
    else : 
        val_a = 0.
            # --> Fixe b
    if y_souris < ORIGINE_H :
        surface_y = H_CADRE / 2
        y_souris = y_souris - surface_y
        rapport = - B_MIN / surface_y
        val_b = abs(y_souris * rapport)
    elif y_souris > ORIGINE_H :
        surface_y = H_CADRE / 2
        y_souris = y_souris - surface_y
        rapport = B_MAX / surface_y
        val_b = -(y_souris * rapport)
        set_signe = ""
    else :
        val_b = 0.
    val_a = round(val_a, 2)
    val_b = round(val_b, 2)
    labl_position_coordonnees.configure(text = "c = " + str(val_a) +
                                               set_signe + str(val_b) + "i")
    labl_position_coordonnees.pack()


def invert(maxi, mini, val):
    dist_old_val = abs(maxi - val)
    new_val = abs(mini + dist_old_val)
    return - new_val

rect_tmp = None
def define_clic(event):
    global rect_tmp, set_bouton_gene
    global val_a_clic, val_b_clic
    val_a_clic = val_a
    val_b_clic = val_b
    x_souris_clic = event.x
    y_souris_clic = event.y
    cadre.delete(rect_tmp)
    rect_tmp = cadre.create_rectangle(x_souris_clic - 2, y_souris_clic - 2,
                                      x_souris_clic + 2, y_souris_clic + 2,
                                      fill = "red")
    labl_selection.configure(text = "Selected Position : \nc = " + str(val_a) +
                                " + " + str(val_b) + "i")
    labl_selection.pack()
    if set_bouton_gene == False: 
        bouton_gene = Button(label_frame_info,
                font=("Times", "15"),
                foreground = "black", background = "white", 
                activeforeground = "white", activebackground = "black", 
                text="Generation", command = generation_julia)
        bouton_gene.pack()
        set_bouton_gene = True

def generation_julia():
    julia(val_a_clic, val_b_clic)

# --- # --- # --- # --- # --- # FONCTION GENERATION (MENU)

def gene_alea():
    i = 5

def gene_precise():
    global entry_imaginary, entry_real, top
    top = Toplevel(width=300)
    top.title("Configuration")
    label_frame_config = LabelFrame(top, text="Config", padx=20, pady=20)
    label_frame_config.pack(fill="both", expand="yes")
    labl_real = Label(label_frame_config, text = "real part")
    labl_real.pack()
    entry_real = Entry(label_frame_config)
    entry_real.pack()
    labl_imaginary = Label(label_frame_config, text = "imaginary part")
    labl_imaginary.pack()
    entry_imaginary = Entry(label_frame_config)
    entry_imaginary.pack()
    bouton_gene_prec = Button(label_frame_config,
                    font=("Times", "15"),
                    foreground = "black", background = "white", 
                    activeforeground = "white", activebackground = "black", 
                    text="Generation", command = generation_precise)
    bouton_gene_prec.pack()
    
def generation_precise():
    real_part = entry_real.get()
    imaginary_part = entry_imaginary.get()
    julia(float(real_part), float(imaginary_part))

# --- # --- # --- # --- # --- # GESTION WIDGETS

fen = Tk()
fen.title("Mandelbrot Set Exploration")
cadre = Canvas(fen, width = L_CADRE, height = H_CADRE, background = "white")
cadre.pack(side = LEFT)


mon_menu = Menu(fen)
fen.config(menu=mon_menu)

menu_generation = Menu(mon_menu)
mon_menu.add_cascade(label="Generation", menu=menu_generation)
menu_generation.add_command(label="Aleatoire", command=gene_alea)
menu_generation.add_command(label="Precise", command=gene_precise)


            # --> Génération / récupération de l'image fractale de mandelbrot :
# Si l'image est déja existante, on charge le fichier
# Sinon, on génére l'image.
if path.exists("out_mandel.png") :
    pil_img_mandel = Image.open("out_mandel.png")
else :
    pil_img_mandel = mandelbrot() # Appel au module Algo
    Image.open("out_mandel.png")

tk_img_mandel = ImageTk.PhotoImage(pil_img_mandel)
cadre.create_image(0, 0, anchor=NW, image=tk_img_mandel)

            # --> Création du repère définissant le plan complexe :
cadre.create_line(0, ORIGINE_H, L_CADRE, ORIGINE_H, fill="red")
cadre.create_line(ORIGINE_V, 0, ORIGINE_V, H_CADRE, fill="red")
cadre.create_rectangle(2, 2, L_CADRE, H_CADRE)

            # --> Event
cadre.bind("<Motion>", define_motion)
cadre.bind("<Button-1>", define_clic)

            # --> Label
label_frame_info = LabelFrame(fen, text="Info", padx=20, pady=20)
label_frame_info.pack(fill="both", expand="yes", side = RIGHT)

labl_position_pixel = Label(label_frame_info, text = "x : Undefined ; y : Undefined")
labl_position_pixel.pack()

labl_position_coordonnees = Label(label_frame_info, text = "c = Undefined")
labl_position_coordonnees.pack()

labl_selection = Label(label_frame_info, text = "Selected Position : \nUndefined")
labl_selection.pack()


fen.mainloop()












