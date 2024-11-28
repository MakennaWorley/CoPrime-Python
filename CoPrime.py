'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    Makenna Worley
'''

import sys

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = ['^'] * (n + 1)
        
    '''
    output the contents of result
    '''
    """for x in result:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            print(y + ' ', end="")
            
        print() """

    '''
        YOUR WORK WILL GO HERE
    '''

    for i in reversed(range(0,m+1)):
        for j in range(0,n+1):
            if i == 0 or j == 0:  # 0 cannot be co-prime with anything
                print('  ', end="")
            elif i == 1 or j == 1: # 1 will always be co-prime with any other number
                print('* ', end="")
            else:
                common_denominator = 2
                has_common_denominator = False

                while common_denominator <= i or common_denominator < j:
                    if i%common_denominator == 0 and j%common_denominator == 0:
                        has_common_denominator = True
                        break #stop the loop since one has been found
                    common_denominator += 1
                if has_common_denominator:
                    print('  ', end="")
                else:
                    print('* ', end="")

        print()

# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
