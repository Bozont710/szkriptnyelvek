#!/usr/bin/env python3


def main():
    #list of the top 10 speedcubers taken from https://www.worldcubeassociation.org/results/rankings/333/single
    ranking_info = [("Max Park", 3.13, "United States", "Pride in Ling Beach 2023"),
                    ("Luke Garett", 3.44, "United States", "Flag City Summer 2023"),
                    ("Yiheng Wang", 3.47, "China", "MYHM Singapore Championship 2024"),
                    ("Yusheng Du", 3.47, "China", "Wuhu Open 2018"),
                    ("Tymon Kolasiński", 3.66, "Poland", "Flatåsen Open 2024"),
                    ("Jode Brewster", 3.88, "Australia", "Tassie Summer 2023"),
                    ("Asher Kim-Magierek", 3.89, "United States", "Rose City 2022"),
                    ("Ruihang Xu", 4.01, "China", "Vietnam Championship 2023"),
                    ("Natthaphat Mahtani", 4.02, "Thailand", "Bangkok Cube Day Winter 2024"),
                    ("Max Siauw", 4.03, "United States", "BC Cubing Springback A 2022")]
    
    #set the spaces between each word and assign a value
    print("{0:21} {1:11} {2:16} {3:24}".format("Name", "Result(s)", "Representing", "Competition"))
    print("-"*90)
    for element in ranking_info:
        #set the spaces again and also align and format the time
        print("{0:22} {1:<10.2f} {2:16} {3:24}".format(element[0], element[1], element[2], element[3]))
    
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
