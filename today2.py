'''Today'''
def main():
    '''input'''
    sum1 = 0
    num1 = int(input())
    if num1 == 0:
        print("No Tape Measure")
    else:
        while True:
            num2 = input()
            if num2 == "No more!":
                if sum1 > 0:
                    print("Sum of Found Number = "+ str(sum1))
                else:
                    print("Not Found Number")
                break
            elif int(num2) <= num1:
                sum1 = sum1+int(num2)
main()
