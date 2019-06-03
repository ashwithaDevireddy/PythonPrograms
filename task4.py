Task 
You are given the year, and you have to write a function to check if the year is leap or not


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False
    
    
        
    
        
        
    
       

    
    return leap
   
year = int(input())
