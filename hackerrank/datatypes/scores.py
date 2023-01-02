if __name__ == '__main__':
    d={}
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        d[name]=score
    x=set(d.values())
    a=sorted(x)#[1]#Second smallest
    l=[]
    for key,value in d.items():
        if value == a[1]:
            l.append(key)
    l.sort()
    for i in l:
        print(i)
