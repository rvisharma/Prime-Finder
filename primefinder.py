# using sieve of Eratosthenes to find prime numbers upto N integers

##This Program gives you the prime number upto N ,
##Sieve of Eratosthenes Algorithm is used to determine the
##Prime Number
##
##To find the Prime Number, in the console Shell
##call the prime_finder(N) function, prime number will
##be given upto N integer.

'''
Precondition N > 0

Output of prime_finder is the list of prime ints
'''

import math
import cProfile
# Will be avalaible throughout the program
original_list = []
def prime_finder(n):
    """ (int) -> list

    return the list of prime numbers upto n

    >>> prime_finder(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_finder(31)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    """
    
    global original_list
    original_list = list(range(2,n+1))
  
    index = 0
    prime = 0
    while original_list[index] <= int(math.sqrt(n)):
        prime = original_list[index]

        delete_list = multiples_of_prime(prime, n)

        original_list = remove_delete_list(delete_list)
        
        index += 1

    return original_list

def multiples_of_prime(prime, end):
    """ (int, int) -> int_list

    takes first argument and finds it multiples upto second argument
    and return the list of all multiples

    >>>multiples_of_prime(2, 30)
    [4,6,8,10,...,30]
    >>>multiples_of_prime(3,30)
    [6,9,12,15,...,30]
    """
    temp = []
    for i in list(range(2, end)):
        if prime*i < (end + 1):
            temp.append(prime*i)
    return temp
    

def remove_delete_list(delete):
    
    """ (int_list) -> int_list

    takes the delete list as parameter and removes each element in original list
    that is in delete list

    >>> remove_delete_list([4,6,8,10....30])
    [2,3,5,7,9,11,....,29]
    """
    
    global original_list
    for num in delete:
        if num in original_list:
            original_list.remove(num)
    return original_list


def main():
    '''
    Description of Program:
    '''
    print('''This Program gives you the prime number upto N integer,
Sieve of Eratosthenes Algorithm is used to determine the
Prime Number''')

    n = int(input('\n\nEnter any Number: '))

    # find the prime number below n and return as a list

    print('\nPrime Numbers below ' + str(n) + ' are:\n' + str(prime_finder(n)))

    if len(original_list) > 10000:
        print(original_list[10000])

    input('\n\npress Enter to... ')

# Run the Program
main()


