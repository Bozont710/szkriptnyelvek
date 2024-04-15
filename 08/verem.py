#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.data = []
    #END__init__


    def betesz(self, elem):
        """Beteszi a verem végébe az adott elemet"""
        self.data.append(elem)
    #ENDbetesz

    def kiterjeszt(self, iter):
        """Kiterjeszti jobbra a vermet az adott elemekkel"""
        self.data.extend(iter)
    #ENDkiterjeszt

    def beszur(self, index, elem):
        """Beszúrja az adott indexre az elemet"""
        self.data.insert(index, elem)
    #ENDbeszur

    def torol(self, elem):
        """Kitörli az adott elemet"""
        self.data.remove(elem)
    #ENDtorol

    def kiurit(self):
        """Kiüríti a vermet teljesen"""
        self.data.clear()
    #ENDkiurit

    def sorszam(self, elem):
        """Visszaadja az elem sorszámát"""
        return self.data.index(elem)
    #ENDsorszam

    def szamlal(self, elem):
        """Megszámlálja az adott elem előfordulásait"""
        return self.data.count(elem)
    #ENDszamlal

    def masol(self, name):
        """Egy másolatot készít a veremről"""
        name = self.data.copy()
        return name
    #ENDmasol

    def forditva(self):
        """Helyben fordítja meg az elemeket"""
        self.data.reverse()
    #ENDforditva

    def sorbarendez(self):
        """Helyben sorbarendezi az elemeket"""
        self.data.sort()
    #ENDsorbarendez

    def kivesz(self, elem=0):
        """Eltávolítja az adott elemet, ha nincs megadva, akkor az utolsót"""
        if elem == 0 and self.ures():
            return None
        elif elem == 0:
            return self.data.pop(self.meret()-1)
        else:
            return self.data.pop(elem)
    #ENDkivesz

    def ures(self):
        """Visszaadja bool-ként hogy üres e a verem"""
        if self.meret() == 0:
            return True
        else:
            return False

    def meret(self):
        """Visszatér a verem méretével"""
        return len(self.data)
    #ENDmeret

    def __str__(self):
        return str(self.data)
    #END__str__
#ENDVerem


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(f"x == {x}")         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
