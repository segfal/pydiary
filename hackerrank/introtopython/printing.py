if __name__ == '__main__':
    n = int(input())
    res = ""
    table = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
    }
    
    for i in range(1,n+1):
        if i in table:
            res += table[i]
        else:
            x = i
            temp = ""
            while(x != 0):
                temp += table[x%10]
                x = int(x/10)
            res += temp[::-1]
    print(res)
