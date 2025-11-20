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

text = "python"
print(text[-1]) 
print(text[-4:-1])

 #0    1   2   3   4   5 (Positive)
  # p    y   t   h   o   n
  #-6    5   4   3  -2  -1(negative)

print(text[-4:-1:1])
print(text[-4:-1:-1])#empty
print(text[-4:-6:-1])#ty
print(text[1:4:-1])
#Reversing string
print(text[::-1])

text="python"
reversed_text=""
for char in text:
    reversed_text= char + reversed_text
    print("Reversed text", reversed_text)

#Reassinging
text = "Hello"
print(text)

text = "hi"
print(text)

#StringImmutability

text = "hello"
print(text)

#modify hello to Hello
#text[0]="H"
#print(text)#TypeError: 'str' object does not support item assignment

#String Concatenation
s1="Hello"
s2="Good Morining"
print(s1+s2)

#String Formatting
name = "Ravi"
age = 30
print("My Age is ",age)
print(f"My Age is {age}")
print("My Age is ", +age)
print("My Age is " +str(age))

#String Repetation
text = "Ha"
Laugh = "HAHAHAHA"
print(Laugh)

Laugh_hard = text * 10
print(Laugh_hard)

#String Methods

text = "Ha"
print(dir(text))

#Simulate mail functionality using strings
user_given_email = input("Enter Your Email ID: ")
format_email = user_given_email.lower() + "@gmail.com"
print("user given ID: "+user_given_email)
print("Gmail Auto Format ID: "+format_email)

#simulate pan correction -> https://www.pan.utiitsl.com/panonline_ipg/forms/csfPan.html/csfPreForm
