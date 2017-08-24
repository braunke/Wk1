print('Provide and sentence to be changed into camelcase')
#takes the input and cahnges it to lower
sentence = input().lower().title()
#error checking
for char in sentence:
    if not char.isalpha():
        print('Needs to be a letter')
        break
sentence = sentence.replace(' ', '')
#changes the firt character to lower case
sentenceBegin = sentence[1:]
firstLetter = sentence[0].lower()
print (firstLetter + sentenceBegin)
