#!/usr/bin/env python3

from typing import List

def sort_data(data: List) -> List:
    for n in data:
        (a, b, c, d) = n
        n = (d, a, b, c)
        data.sort(reverse=True)
        n = (a, b, c, d)
    return data
#ENDsort_data


def sort_users(data: List) -> List:
    data2 = []
    data3 = []
    for n in data:
        (a, b) = n.split(":")
        data2.append(int(a))
    data2.sort(reverse=True)
    for n in data2:
        for m in data:
            (a, b) = m.split(":")
            if n == int(a):
                data3.append(m)
    return data3
#ENDsort_users


def sort_matrix(matrix: List) -> List:
    data = []
    data2 = []
    for n in matrix:
        data.append(n[-1])
        data.sort()
        print(data)
    for n in data:
        for m in matrix:
            if n == m[-1]:
                data2.append(m)
    return data2
#ENDsort_matrix


def main() -> None:
    print("1.")
    print("-"*20)
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (121, 'Wyoming', 'NY', 8722),
    (3, 'Allegany', 'NY', 11986),
    (123, 'Yates', 'NY', 5094)
    ]
    sort_data(data)
    print(data)
    print("-"*20)

    print("\n2.")
    print("-"*20)
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sort_users(users))
    print("-"*20)

    print("\n2.")
    print("-"*20)
    matrix = [ [2, 6], [1, 3], [5, 4] ]
    sort_matrix(matrix)
    print("-"*20)
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
