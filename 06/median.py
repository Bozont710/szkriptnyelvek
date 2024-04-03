#!/usr/bin/env python3


def median(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        ind = len(nums) // 2
        return (nums[ind-1] + nums[ind]) / 2
    else:
        return nums[len(nums) // 2]
        
#ENDmedian


def main():
    num1 = [1, 2, 3, 4, 5]
    num2 = [3, 1, 2, 5, 3]
    num3 = [1, 300, 2, 200, 1]
    num4 = [3, 6, 20, 99, 10, 15]
    print(median(num1))
    print(median(num2))
    print(median(num3))
    print(median(num4))
#ENDmain
    
    
if __name__ == "__main__":
    main()
#ENDif
