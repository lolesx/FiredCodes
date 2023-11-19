def calculer_moyenne(liste_nombres):
    if not liste_nombres:
        return None
    return sum(liste_nombres) / len(liste_nombres)

def calculer_somme(liste_nombres):
    return sum(liste_nombres)

def calculer_mediane(liste_nombres):
    if not liste_nombres:
        return None
    liste_triee = sorted(liste_nombres)
    n = len(liste_triee)
    if n % 2 == 0:
        mediane = (liste_triee[n//2 - 1] + liste_triee[n//2]) / 2
    else:
        mediane = liste_triee[n//2]
    return mediane

if __name__ == "__main__":
    entrees_utilisateur = input("Entrez une liste de nombres séparés par des espaces : ")
    liste_nombres = [float(nombre) for nombre in entrees_utilisateur.split()]

    moyenne = calculer_moyenne(liste_nombres)
    somme = calculer_somme(liste_nombres)
    mediane = calculer_mediane(liste_nombres)

    print(f"Moyenne : {moyenne}")
    print(f"Somme : {somme}")
    print(f"Médiane : {mediane}")
