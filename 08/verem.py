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

    def masol(self):
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

    def kivesz(self, index=-1):
        """Eltávolítja az adott elemet, ha nincs megadva, akkor az utolsót"""
        if index == 0 and self.ures():
            return None
        elif index == 0:
            return self.data.pop(index)
        else:
            return self.data.pop(index)
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
    v = Verem()
    l = []
    v.betesz(5)
    v.betesz(8)
    l.append(5)
    l.append(8)
    print(f"verem: {v}\nlist: {l}")
    v.kiterjeszt([4, 5])
    l.extend([4, 5])
    print(f"verem: {v}\nlist: {l}")
    v.beszur(2, 3)
    l.insert(2, 3)
    print(f"verem: {v}\nlist: {l}")
    v.torol(4)
    l.remove(4)
    print(f"verem: {v}\nlist: {l}")
    print(f"verem 3 sorszáma: {v.sorszam(3)}")
    print(f"list index of 3: {l.index(3)}")
    print(f"verem 5 előfordulasai száma: {v.szamlal(5)}")
    print(f"list count of 5: {l.count(5)}")
    vmasolat = v.masol()
    print(vmasolat)
    lcopy = l.copy()
    print(lcopy)
    v.forditva()
    print(f"verem fordítva: {v}")
    l.reverse()
    print(f"list in reverse: {l}")
    v.sorbarendez()
    print(f"verem sorbarendezve: {v}")
    l.sort()
    print(f"list sort: {l}")
    v.kivesz(3)
    print(f"verem kivesz: {v}")
    l.pop()
    print(f"list pop: {l}")
    print(f"üres a verem? {v.ures()}")
    print(f"verem meret: {v.meret()}")
    
    v.kiurit()
    l.clear()
    print(f"verem: {v}\nlist: {l}")
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
