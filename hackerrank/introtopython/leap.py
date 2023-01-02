def is_leap(year):
    leap = False
    
    bad_years ={
        1800 : 1800,
        1900 : 1900,
        2100 : 2100,
        2300 : 2300,
        2500 : 2500
    }
    # Write your logic here
    
    return True if (year%4 == 0 and (year not in bad_years)) else False

year = int(input())
print(is_leap(year))
