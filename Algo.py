#                                        *** Module : Algo ***

# --- # --- # --- # --- # --- # IMPORT

from PIL import Image


# --- # --- # --- # --- # --- # IMPORT (PROVISOIRE)


RAPPORT = 1.375

            # --> Constantes d'encadrement de la fractale dans le plan complexe :
A_MIN = -2.4
A_MAX = 0.9
B_MIN = -1.2
B_MAX = 1.2

            # --> Constantes définissant la taille du cadre principal.
L_CADRE = 660 
H_CADRE = 480

            # --> Constantes définissant le repère du plan complexe :
RAPPORT_POSI_NEGA = abs(A_MIN/A_MAX)# = 2.66666
ORIGINE_V = 480 # A quoi correspond 480
ORIGINE_H = H_CADRE // 2

def invert(maxi, mini, val):
    dist_old_val = abs(maxi - val)
    new_val = abs(mini + dist_old_val)
    return - new_val


# --- # --- # --- # --- # --- # ALGO GENERATION


PRECISION = 50

# --- # --- # --- # --- # --- # --- # --- # MANDELBROT

def mandelbrot():
                        # --> Gestion de dimension
    dim = 1
    largeur = L_CADRE * dim
    hauteur = H_CADRE * dim
    local_ORIGINE_V = ORIGINE_V * dim
    local_ORIGINE_H = ORIGINE_H * dim
                        # --> Calcul position
    img = Image.new("RGB", (largeur, hauteur), "white")
    for i1 in range (largeur):
        for i2 in range (hauteur):
            tmp_i1 = i1
            tmp_i2 = i2
                        # --> Fixe a
            if i1 > local_ORIGINE_V :
                surface_non_x = local_ORIGINE_V
                surface_x = largeur - local_ORIGINE_V
                tmp_i1 = tmp_i1 - surface_non_x
                rapport = A_MAX / surface_x 
                pos_a = tmp_i1 * rapport
            elif i1 < local_ORIGINE_V :
                surface_x = local_ORIGINE_V
                rapport = abs(A_MIN) / surface_x
                pos_a = tmp_i1  * rapport 
                pos_a = invert(0, A_MIN, pos_a)
            else : 
                pos_a = 0.
                        # --> Fixe b
            if i2 < local_ORIGINE_H :
                surface_y = hauteur / 2
                tmp_i2 = tmp_i2 - surface_y
                rapport = abs(B_MIN) / surface_y
                pos_b = abs(tmp_i2 * rapport)
            elif i2 > local_ORIGINE_H :
                surface_y = hauteur / 2
                tmp_i2 = tmp_i2 - surface_y
                rapport = B_MAX / surface_y
                pos_b = -(tmp_i2 * rapport)
            else :
                pos_b = 0
                        # --> Fixe c
            pos_a = round(pos_a, 3)
            pos_b = round(pos_b, 3)
            z = complex(0, 0)
            c = complex(pos_a, pos_b)
                        # --> Itération
            for i in range (PRECISION):
                z = z*z + c
            if abs(z) < 2 :
                img.putpixel((i1, i2), (0, 0, 0))
    img.save('out_mandel.png')
    return img


# --- # --- # --- # --- # --- # --- # --- # JULIA

                        # --> Nouvelle encadrement Julia
A_MIN_J = -1.7
A_MAX_J = 1.6
B_MIN_J = -1.2
B_MAX_J = 1.2

ORIGINE_V_J = 320



def julia(rea, ima):
    c = complex(rea, ima)
                        # --> Gestion de dimension
    dim = 1
    largeur = L_CADRE * dim
    hauteur = H_CADRE * dim
    local_ORIGINE_V = ORIGINE_V_J * dim
    local_ORIGINE_H = ORIGINE_H * dim
                        # --> Calcul position
    img = Image.new("RGB", (largeur, hauteur), "white")
    for i1 in range (largeur):
        for i2 in range (hauteur):
            tmp_i1 = i1
            tmp_i2 = i2
                        # --> Fixe a
            if i1 > local_ORIGINE_V :
                surface_non_x = local_ORIGINE_V
                surface_x = largeur - local_ORIGINE_V
                tmp_i1 = tmp_i1 - surface_non_x
                rapport = A_MAX_J / surface_x 
                pos_a = tmp_i1 * rapport
            elif i1 < local_ORIGINE_V :
                surface_x = local_ORIGINE_V
                rapport = abs(A_MIN_J) / surface_x
                pos_a = tmp_i1  * rapport 
                pos_a = invert(0, A_MIN_J, pos_a)
            else : 
                pos_a = 0.
                        # --> Fixe b
            if i2 < local_ORIGINE_H :
                surface_y = hauteur / 2
                tmp_i2 = tmp_i2 - surface_y
                rapport = abs(B_MIN_J) / surface_y
                pos_b = abs(tmp_i2 * rapport)
            elif i2 > local_ORIGINE_H :
                surface_y = hauteur / 2
                tmp_i2 = tmp_i2 - surface_y
                rapport = B_MAX_J / surface_y
                pos_b = -(tmp_i2 * rapport)
            else :
                pos_b = 0
                        # --> Fixe z
            pos_a = round(pos_a, 3)
            pos_b = round(pos_b, 3)
            z = complex(pos_a, pos_b)
            for i in range (PRECISION):
                z = z*z + c
            if abs(z) < 2 :
                img.putpixel((i1, i2), (0, 0, 0))
    img.save('Collection/' + str(rea) + '+' + str(ima) + '.png')
    img.save('out_julia.png')
    img.show()


# test du "Lapin de Douady" : julia(-0.123, 0.745)



























