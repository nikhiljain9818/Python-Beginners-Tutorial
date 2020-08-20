# define is_palindrome func that take one word in string as input
# and return True if it is palindrome else return False

# palindrome - word that reads same backwards as forwards

#ex ----> is_palindrome("madam") -----> True
#         is_palindrome("horse") -----> False

word_1 = input("Enter the word: ")
word_2 = word_1[::-1]

def is_palindrome(word_1,word_2):
    if (word_1 == word_2):
        print(f"{word_1} is a palindrome word")
    else:
        print(f"{word_1} is not a palindrome word")
is_palindrome(word_1,word_2)

##def is_palindrome(word_1):                                #SHORTCUT
##    if (word_1 == word_1[::-1]):                          # taking input in func call
##        print(f"{word_1} is a palindrome word")
##    else:
##        print(f"{word_1} is not a palindrome word")
##is_palindrome(input("Enter the word: "))
 




