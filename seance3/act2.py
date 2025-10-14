class Etudiant:
    def __init__(self,matricule,Nom,prenon,note):
        self.matricule = matricule
        self.Nom = Nom
        self.prenon = prenon
        self.note = note

    def afficher(self):
        print(f"matricule: {self.matricule}, non: {self.Nom}, prenon: {self.prenon}, note: {self.note}")
    
etud1 = Etudiant("D12354","adam","aderram",15)
etud2 = Etudiant("Defe","ahmed","chaib",16)

etud1.afficher()
etud2.afficher()

somme = etud1.note + etud2.note


moyenne = somme / 2






