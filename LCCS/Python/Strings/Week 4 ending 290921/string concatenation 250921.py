word1= ('4')
word2= ('3 ')


subject = word1 + word2 
print (subject)

#the results will be 43 as python sees 4 and 3 as string not numbers

word1= int('4')
word2= int('3')


subject = word1 + word2 
print (subject)

# if you take away the quotation marks it automatically sees the numbers not the string
# another technique is called casting (see below)

word1= float(4)
word2= float(3)

subject = word1 + word2
print(subject)