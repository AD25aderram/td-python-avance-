from datetime import date


class Employe:
    def __init__(self):
        self.__Identifiant = input("Entrez l'identifiant de l'employé : ")
        self.__Nom = input("Entrez le nom de l'employé : ")
        self.__Prenom = input("Entrez le prénom de l'employé : ")
        self.__DateNaissance = int(input("Entrez l'année de naissance : "))
        self.__DateEmbauche = int(input("Entrez l'année d'embauche : "))
        self.__Salaire = float(input("Entrez le salaire : "))

    def get_Identifiant(self):
        return self.__Identifiant
    def get_Nom(self):
        return self.__Nom
    def get_Prenom(self):
        return self.__Prenom
    def get_DateNaissance(self):
        return self.__DateNaissance
    def get_DateEmbauche(self):
        return self.__DateEmbauche
    def get_Salaire(self):
        return self.__Salaire


    def set_Identifiant(self, id):
        self.__Identifiant=id
    def set_Nom(self,nom):
        self.__Nom=nom
    def set_Prenom(self,prenom):
        self.__Prenom=prenom
    def set_DateNaissance(self,datenaissance):
        self.__DateNaissance=datenaissance
    def set_DateEmbauche(self,dateembauche):
        self.__DateEmbauche=dateembauche
    def set_Salaire(self,salaire):
        self.__Salaire=salaire


    def Age(self):
        todays_year = date.today().year
        birthyear = self.__DateNaissance
        return todays_year - birthyear
    
    def Anciennete(self):
        todays_year = date.today().year
        EmbaucheYear = self.__DateEmbauche
        return todays_year - EmbaucheYear
    
    def afficher(self):
        """Affiche toutes les informations de l'employé."""
        print("\n--- Informations de l'employé ---")
        print(f"Identifiant : {self.__Identifiant}")
        print(f"Nom complet : {self.__Prenom} {self.__Nom}")
        print(f"Âge : {self.Age()} ans")
        print(f"Ancienneté : {self.Anciennete()} ans")
        print(f"Salaire : {self.__Salaire} DH")

e = Employe()
e.afficher()
