def find_vowels(char):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    if char in vowels:
        return True
    return False
       
Random=str(input("Am I Vowel? :"))
find_vowels(Random)
size=len(Random)

print("My length is %d" %size)

if find_vowels(Random)==True:
    print("True: You are a Vowel character -->(%s)" %Random)

if find_vowels(Random)==False:
    print("False: You are Not a Vowel character --> (%s)" %Random)