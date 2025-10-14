class Voiture:
    def __init__(self,code,marque,kilometrage):
        self.code = code
        self.marque = marque
        self.kilometrage = kilometrage
    
    def mod_kilo(self,new_kilo):
        self.kilometrage = self.kilometrage + new_kilo
    
    def afficher(self):
        print(f"le code: {self.code}, la marque: {self.marque}, le kilometrage: {self.kilometrage}")


v1 = Voiture("MS156","Mazda",12000)
v2 = Voiture("KD152","Toyota",155230)
v3 = Voiture("jd153","Dacia",100510)


v1.afficher()
v2.afficher()
v3.afficher()

