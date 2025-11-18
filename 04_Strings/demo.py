#strings
s1 = "data"
s2 = "data"
s3 = '''data'''
s4 = """data"""
print(s1)
print(s2)
print(s3)
print(s4)

print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))

#Multiline strings
mls = """this is a very 
big line of string
more lines
more lines"""
print(mls)

# ' inside a string

Question = "How are you?"
#answer = 'i'm fine' #SyntaxError: unterminated string literal (detected at line 26)
answer = "i'm fine"
#answer = "doing "great"" #SyntaxError: invalid syntax
answer ='doing "great"'
print(answer)
answer = '''i'm fine doing great'''

print(answer)
answer = """i'm fine doing great"""
print(answer)


#indexing : Accessing characters from string

text = "Python"
print(text)
print(text[4])#Positive
print(text[0])#Positive
print(text[-1])#negative
print(text[-2])#negative
#print(text[10])#IndexError: string index out of range

#String Accessing
text = "Python"
print ("MAnually")
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])

print ("using loops")

#USing Loops to access
for character in text:
    
    print(character)

#Len()->returns the number od items in a object
text = "Python" #space is also a acharacter
print("length is", len(text))

#example using list
list_data = ["dell","lenevo","hp","acer"]
print("Brand count is", len(list_data))

#len()- >doenot work with numbers
#num = 100
#print(dir(len))
#print("length is", len(num))# TypeError: object of type 'int' has no len()

#slicing in python
text = "python"
print(text[0]) #access using index

#[start:stop:step]
print(text[0:3])#start:stop
print(text[0:])#start:end
print(text[:])#start:stop
print(text[2:5])#start:stop->tho

print(text[:4])#start(0):stop(4)->pyth

