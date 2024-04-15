#!/usr/bin/env python3

from collections import deque

class Sor:
    def __init__(self):
        self.data = deque([])
    #END__init__

    def betesz(self, elem):
        """Egy elemet jobb oldalra betesz"""
        self.data.append(elem)
    #ENDbetesz

    def beteszbal(self, elem):
        """Egy elemet bal oldalra tesz be"""
        self.data.appendleft(elem)
    #ENDbeteszbal

    def kiurit(self):
        """Kiüríti a sort teljesen"""
        self.data.clear()
    #ENDkiurit

    def masol(self, name):
        """Egy másolatot készít a sorról"""
        name = self.data.copy()
        return name
    #ENDmasol

    def szamlal(self, elem):
        """Megszámlálja az adott elem előfordulásait"""
        return self.data.count(elem)
    #ENDszamlal

    def kiterjeszt(self, iter):
        """Kiterjeszti jobbra a sort az adott elemekkel"""
        self.data.extend(iter)
    #ENDkiterjeszt

    def kiterjesztbal(self, iter):
        """Kiterjeszti ballra a sort az adott elemekkel"""
        self.data.extendleft(iter)
    #ENDkiterjesztbal

    def sorszam(self, elem):
        """Visszaadja az elem sorszámát"""
        return self.data.index(elem)
    #ENDsorszam

    def beszur(self, index, elem):
        """Beszúrja az adott indexre az elemet"""
        self.data.insert(index, elem)
    #ENDbeszur

    def kivesz(self):
        """Kivesz és visszaad egy elemet a jobb oldalról"""
        if self.ures():
            return None
        else:
            return self.data.pop()
    #ENDkivesz

    def kiveszbal(self):
        """Kivesz és visszaad egy elemet a bal oldalról"""
        if self.ures():
            return None
        else:
            return self.data.popleft()
    #ENDkiveszbal

    def torol(self, elem):
        """Kitöröli az adott elemet"""
        self.data.remove(elem)
    #ENDtorol

    def forditva(self):
        """Helyben fordítja meg az elemeket"""
        self.data.reverse()
    #ENDforditva

    def forgat(self, n=1):
        """Forgatja az elemeket n lépéssel
           ha n negatív akkor ballra forgat"""
        self.data.rotate(n)
    #ENDforgat

    def maxhossz(self):
        return self.data.maxlen()
    #ENDmaxhossz

    def meret(self):
        return len(self.data)
    #ENDmeret
    
    def ures(self):
        if self.meret() == 0:
            return True
        else:
            return False
    #ENDures

    def __str__(self):
        return str(self.data)
#ENDSor


def main():
    s = Sor()      # üres verem létrehozása
    print(s)         # [
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # [1 4 5
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(f"x == {x}")         # 5
    print(s)         # [1 4
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
