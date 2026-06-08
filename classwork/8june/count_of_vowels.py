#wap to input the sentence an ddisplay th efrequency of
#  vowels which are present in the given sentence 

string=input("Enyter the string")
count= 0
for ch in string:
    if ch in "AEIOUaeiou":
       count = count + 1
print("frequency of vowels:", count)
