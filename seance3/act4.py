class Personne:
    def __init__(self,nom,adresse):
        self.nom = nom
        self.adresse = adresse
    def afficher(self):
        print(f"non: {self.nom}, adresse:{self.adresse}")

class Employe(Personne):
    def __init__(self,cnss,nom,adresse):
        self.cnss = cnss
        Personne.__init__(self,nom,adresse)
    
    def afficher(self):
        print(f"cnss: {self.cnss}")
        Personne.afficher(self)

class Enseignant(Personne):
    def __init__(self,cnops,nom,adresse):
        self.cnops = cnops
        Personne.__init__(self,nom,adresse)
    
    def afficher(self):
        print(f"cnops: {self.cnops}")
        Personne.afficher(self)

class Etudiant(Personne):
    def __init__(self,cne,nom,adresse):
        self.cne = cne
        Personne.__init__(self,nom,adresse)
    
    def afficher(self):
        print(f"cne: {self.cne}")
        Personne.afficher(self)


e = Etudiant("CNE123", "Adam", "Casablanca")
e.afficher()
Personne.afficher(e)