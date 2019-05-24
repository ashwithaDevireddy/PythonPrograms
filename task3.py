Task :
Read an integer N. For all non-negative integers i< N , print square(i). See the sample for details.


program:
    if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        while i <=20:
            print(i*i)
            break
