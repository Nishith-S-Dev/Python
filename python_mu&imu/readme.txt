this is about the mutable and immutable in the python 

Examples of Mutable Objects:
	•	list
	•	dict
	•	set
	•	bytearray

Example of the immutable Objects:

Examples of Immutable Objects:
	•	int
	•	float
	•	str
	•	tuple
	•	frozenset
	•	bytes


example :


from helloworld import hello

# hello("another Bro ")
my_str  = "hello"
print(id(my_str))
my_str = my_str +"world"
print(my_str)
print(id(my_str))

my_str2  = "helloMeow"
print(my_str2)
my_str2 = "helloDoggy"
print(my_str2)