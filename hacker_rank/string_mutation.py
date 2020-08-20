"""Task
Read a given string, change the character at a given index and then print the modified string.
Input Format
The first line contains a string,S.
The next line contains an integer i, denoting the index location and a character c separated by a space.
Output Format
Using any of the methods explained above, replace the character at index i with character c."""

S = input()
i = int(input())
char = input()
def mutation(string,position,character):
    a = string
    b = list(a)
    b[position] = character
    c = ''.join(b)
    return c

print(mutation(S,i,char))