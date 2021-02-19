def fibiter(n): # This is the iteration function
    prenum = 0 # we are making 0 as previous number
    currentNum = 1 # We are making 1 as current number
    for i in range(1, n): # this is a for loop which will run from 1 to n
        preprenum = prenum # we are assigning a pre-previous number as 0
        prenum = currentNum # now we are assigning 0 as 1
        currentNum = prenum + preprenum # Now we are making the current number = previous number + pre-previous number
    return currentNum


def fibrecur(n):# This is the recursion process
    if n==0:# if 0 then it will return 0
        return 0
    elif n==1:# if 1 it will return 1
        return 1

    else:# if given another number it will add (n - 1) with (n - 2)
        return fibrecur(n - 1) + fibrecur(n - 2)

def main():# This is main loop
    num = int(input("Enter a index number which will tell the number in that index\n(This program is python based and \nhere indexing starts from 0\n) : "))
    # here we will take input from user which will give the index of the fibonacci series
    print(f"The number at index {num} in fibonacci series by recursion is {fibrecur(num)}")
    print(f"The number at index {num} in fibonacci series by iteration is {fibiter(num)}")

main()