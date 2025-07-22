a=input("Enter a word")
#print(a[::-1])
reverse =""
for i in a:
    reverse=i+reverse
print(f'The reversal of word is {reverse}')
