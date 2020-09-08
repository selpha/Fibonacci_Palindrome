class Test:
    def first100_fibonacci_numbers(self,nterms):
        #The first and the second
        n1, n2 = 1, 1
        #initialize count
        count = 0
        #loop through while incrementing as we print the fib
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

    def find_the_longest_palindromic_substring(self,word) -> str:
        # This string will store our palindrome
        palindrome = ''
        # loop through the input
        for x in range(len(word)):
            # backwards loop
            for y in range(len(word), x, -1):
                # Break
                if len(palindrome) >= y - x:
                    break
                # Update if matches
                elif word[x:y] == word[x:y][::-1]:
                    palindrome = word[x:y]
                    break
        print(palindrome)
        return palindrome



object = Test()
# object.first100_fibonacci_numbers(100)
object.find_the_longest_palindromic_substring('cbbd')
