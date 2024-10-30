import numpy as np


#1
A = np.array([[4, 6, -2, 3], [2, -1, 0,1], [-7,0,1,12]])
#2
print(f"Dimensions : {A.shape}") 
print(f"Data type : {A.dtype}")
#3

print("2ème ligne :", A[2])
#les deux-points : signifient "toutes les lignes"
print("2ème colonne :", A[:, 1])  

print("Élément (1,2) :", A[2, 3])
#4

#Avec numpy, la notation [:2, :] sélectionne les deux premières lignes (les lignes d'indice 0 et 1) 
# et toutes les colonnes (grâce aux :), puis on applique la multiplication directement avec *= 2.

 # A[:2, :] *= 2
#print("Matrice après modification :", AM)

#5
B = np.array([[4, 5, 6], [5, 10, 15], [1,1,1]])

#6
C=A[:,:3]
print("Matrice c:", C)

#7
D = np.dot(B, A)
E = np.dot(B, C)

#8


SOME = np.sum(E)
vecteur = np.sum(D,axis=0)

#9

A[A<0] =0
print("Matrice A:", A)



