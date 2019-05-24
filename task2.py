Task :
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You do not need to perform any rounding or formatting operations.


program:
    if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = a//b
    d = a/b
    print(int(c))
    print(float(d))
