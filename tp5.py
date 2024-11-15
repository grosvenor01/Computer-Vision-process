import cv2
import numpy as np 
import math
# 1. calculer l gradient on utilison ce tahrach 
#2. change la fonction gauss pour retourner la matrice de convolution ( nhssbou el mask w nbdlouh bel mask li raho  fel kernel)

var = img = cv2.imread("image.png" , cv2.IMREAD_GRAYSCALE)

def gauss(x, y, sigma):
    sigma2 = sigma**2  
    part1 = 1 / (2 * math.pi * sigma2)
    part2 = -(x**2 + y**2) / (2 * sigma2)
    return part1 * math.exp(part2) 


def print_gauss(sigma=1.4, vois_mat=3):
    if vois_mat % 2 == 0:
        raise ValueError("vois_mat doit être un nombre impair.")
    vois = vois_mat // 2
    matrice = []
    somme_totale = 0.0
    for i in range(-vois, vois + 1):
        ligne = []
        for j in range(-vois, vois + 1):
            val = gauss(i, j, sigma)
            ligne.append(val)
            somme_totale += val
        matrice.append(ligne)
    matrice_normalisee = [[val / somme_totale for val in ligne] for ligne in matrice]
    for ligne in matrice_normalisee:
        for val in ligne:
            print("{:0.4f}".format(val), '\t', end=" ")
        print()
    print("Somme des valeurs normalisées :", sum(sum(ligne) for ligne in matrice_normalisee))
    return matrice_normalisee


kernel = np.array(print_gauss())
imgRes = cv2.filter2D(img,-1 , kernel)
cv2.normalize(imgRes,imgRes,0,255,cv2.NORM_MINMAX)
cv2.imshow("img" , img)
cv2.imshow("result",imgRes)
cv2.waitKey()
cv2.destroyAllWindows()