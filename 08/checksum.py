#!/usr/bin/env python3



def checksum(line):
    nums = line.split()
    print(nums)
    largest = float("-inf")
    smallest = float("inf")
    for n in nums:
        if int(n) < smallest:
            smallest = int(n)
        if int(n) > largest:
            largest = int(n)
    return largest - smallest
#ENDchecksum


def main():
    nums = []
    with open("test", 'r') as INPUT:
        for line in INPUT:
            nums.append(checksum(line))
    print(sum(nums))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
