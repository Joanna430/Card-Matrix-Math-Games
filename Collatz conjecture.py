"""
Collatz conjecture.
We'll start with a positive integer. If it's even we'll divide it by 2, but if it's odd we'll multiply by 3 and then add 1.
Then repeat. We stop when we reach 1. The conjecture states that for any starting number, we eventually reach 1 and stop. 
"""
def collatz(num):
    """
    It takes an integer and returns a list with count(counting the number of steps) and result(the initial number).
    """
    count = 0
    result = num 
    #It stores the value of num to "result" so that the following for loop won't change 
    #the value of "result", the initial number.
    a_list = [num] #Create a new list called a_list which is used for iterating the for loop below.
    for num in a_list:   
        if num != 1:
            if num % 2 == 0:
                count += 1
                a_list.append(num / 2)
            elif num % 2 != 0:
                count += 1
                a_list.append(3 * num + 1)
        elif num == 1:
            return [count, result]

def collatz_limit(limit):
    """
    It takes a given number limit and checks whether the steps it uses to get the number one is larger 
    than the limit. By iterating the loop, it returns the smallest integer that is still going when it runs into that limit.
    """
    a_list = [1] #Create a list that only contains number one since one is the smallest number we can start with.
    for num in a_list: 
        result = collatz(num) #Call the previous function collatz(num).
        if result[0] <= limit:
            a_list.append(num + 1)
        elif result[0] > limit:
            return result[1]
#print collatz_limit(10)
