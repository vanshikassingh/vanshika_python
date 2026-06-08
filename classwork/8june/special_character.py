#wap to input a sentence from user and count 
# the no of special char present in sentence 

sentence=str(input("\n Enter the string\n"))
count =0

for ch in sentence:
    if not  ch.isalnum() and ch != " ":
        count=count+1
print("\nTHE NO OF SPECIAL CHARACTERS ARE :\n", count )
