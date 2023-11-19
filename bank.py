class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant
        print(f"{montant}€ déposés. Nouveau solde : {self.solde}€")

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print(f"{montant}€ retirés. Nouveau solde : {self.solde}€")
        else:
            print("Solde insuffisant.")

    def afficher_solde(self):
        print(f"Solde actuel pour {self.titulaire} : {self.solde}€")


class SimulateurBanque:
    def __init__(self):
        self.clients = {}

    def ajouter_client(self, nom):
        compte = CompteBancaire(nom)
        self.clients[nom] = compte

    def simuler(self):
        while True:
            print("\nSimulateur Bancaire:")
            print("1. Ajouter un client")
            print("2. Afficher le solde d'un client")
            print("3. Effectuer un dépôt")
            print("4. Effectuer un retrait")
            print("5. Quitter")

            choix = input("Choisissez une option (1/2/3/4/5): ")

            if choix == '1':
                nom_client = input("Entrez le nom du client : ")
                self.ajouter_client(nom_client)
                print(f"Client {nom_client} ajouté avec succès.")
            elif choix == '2':
                nom_client = input("Entrez le nom du client : ")
                if nom_client in self.clients:
                    self.clients[nom_client].afficher_solde()
                else:
                    print("Client non trouvé.")
            elif choix == '3':
                nom_client = input("Entrez le nom du client : ")
                montant = float(input("Entrez le montant à déposer : "))
                if nom_client in self.clients:
                    self.clients[nom_client].deposer(montant)
                else:
                    print("Client non trouvé.")
            elif choix == '4':
                nom_client = input("Entrez le nom du client : ")
                montant = float(input("Entrez le montant à retirer : "))
                if nom_client in self.clients:
                    self.clients[nom_client].retirer(montant)
                else:
                    print("Client non trouvé.")
            elif choix == '5':
                print("Au revoir!")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    simulateur = SimulateurBanque()
    simulateur.simuler()
