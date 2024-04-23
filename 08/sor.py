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

    def masol(self):
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
        return self.data.maxlen
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
    s = Sor()
    q = deque([])
    s.betesz(5)
    s.betesz(8)
    q.append(5)
    q.append(8)
    print(s)
    print(q)
    s.beteszbal(7)
    q.appendleft(7)
    print(s)
    print(q)
    
    smasol = s.masol()
    print(smasol)
    qcopy = q.copy()
    print(qcopy)
    s.betesz(5)
    q.append(5)
    print(s.szamlal(5))
    print(q.count(5))

    s.kiterjeszt([3, 5])
    q.extend([3, 5])
    print(s)
    print(q)
    s.kiterjesztbal([2, 2])
    q.extendleft([2, 2])
    print(s)
    print(q)

    print(s.sorszam(8))
    print(q.index(8))
    s.beszur(1, 9)
    q.insert(1, 9)
    print(s)
    print(q)
    s.kivesz()
    q.pop()
    print(s)
    print(q)
    s.kiveszbal()
    q.popleft()
    print(s)
    print(q)
    
    s.torol(3)
    q.remove(3)
    print(s)
    print(q)
    s.forditva()
    q.reverse()
    print(s)
    print(q)
    s.forgat(2)
    q.rotate(2)
    print(s)
    print(q)

    print(s.maxhossz())
    print(q.maxlen)    
    print(s.meret())
    print(len(q))
    print(s.ures())
    s.kiurit()
    print(s)
    print(s.ures())
    q.clear()
    print(q)
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
