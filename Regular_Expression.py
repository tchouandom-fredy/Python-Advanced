import re
#finding a word in a string and returns it as a list
string1 = "Hello my name is Fredy Fredy"
print(re.findall(r"Fredy",string1))

#finding all digits in a string 
string2 = "I have 2 phones and 3 airpods with 13 books"
print(re.findall(r"\d",string2))

#Usimg msodifiers to remedy to number spliting
print(re.findall(r"\d+", string2))

#search fxn
text = "Fredy is so awesome"
if re.search("awesome", text):
	print("yes he is awesome")

#Using the split fxn to separate a string by the occurence of a given pathern
result = re.split(r"o","tchouandom")
print(result)

