import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 0 and n > 20:
        print("Not Weird")
    if n%2 ==0 and n>=2 and n<= 5:
        print("Not Weird")
    if n>= 6 and n<=20:
        print("Weird")
    if n%2 == 1:
        print("Weird")
