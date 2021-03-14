# Functions, objects and control structures #

## Table of Contents ##
* [Blocks of code in Python](#blocks-of-code-in-python)
* [Writing functions](#writing-functions)
* [Using for loops](#using-for-loops)
* [Process a list in a function](#process-a-list-in-a-function)
* [More list processing](#more-list-processing)
* [Writing a closure](#writing-a-closure)
* [Creating a class](#creating-a-class)
* [Creating an object](#creating-an-object)
* [Modifying an object at runtime](#modifying-an-object-at-runtime)
* [More about classes](#more-about-classes)

Python is multi-paradigmatic. It has multiple inheritance, interfaces, 
first class functions, and you can even change objects at runtime.
We will only scratch the surface in this lesson, 
but it will give you a good starting point to continue.

## Blocks of code in Python ##

A word about blocks of code in Python before we begin.

Python is a space sensitive language.
Languages like *Java* use curly braces for blocks.
Languages like *Pascal* use keywords like begin and end instead.
Python uses tabs or spaces, similar to *YAML* format.

This is in my humble opinion the most common reason not to like Python,
but I can assure you other features of the Python language
more than compensate for this controversial design decision.

It does not matter too much if you use Python mainly for small
scripts but if the codebase gets bigger, or you work with several
other developers in the same codebase it's probably wise to use an IDE
that immediately converts all tabs to spaces, or the other way around
(while of course all developers should use the same tab size).
It could also happen that you copy some code from the internet
and while it looks like the code is indented correctly
it will not execute as expected because you have spaces mixed with tabs.

## Functions ##

Back on topic.

Let's start by writing a *fibonacci* function:

```def fib(n): return 1 if n in {0, 1} else fib(n-1) + fib(n-2)```

How to input this into the REPL? You REPL should prefix any input with ```>>>```.
If you started a block however the prefix should change to ```...```.
While the prefix is like this, the REPL expects more input
before it will try to make something useful out of it.
Since theoretically you could have entered more code for this function
in a second line, the REPL requires you to finalize your input by pressing enter.

The REPL will then process the input and return to the ```>>>``` prefix.

Let's rewrite this code as an anonymous function and assign it to a variable:

```fib2 = lambda n: 1 if n in {0, 1} else fib2(n-1) + fib2(n-2)```

Anonymous functions have the advantage that they can be passed directly into functions,
they do not need to be assigned to variables like we're doing now.

Let's rewrite our code as a multi line function, which is more suitable for beginners:

```
def fib3(n):
     if n in {0, 1}:
             return 1
     else:
             return fib3(n - 1) + fib3(n - 2)
```

I would advise using tabs instead of spaces when working in the REPL,
so in the above code make sure to put one tab each before the ```if```
and the ```else``` line and put two tabs before the two ```return``` lines each.

```{0, 1}``` is a set containing 0 and 1.
You learnt that in the previous lesson, but only very briefly.

Now let's analyse what has happened so far:
* functions are declared like this: ```def functionname(parameters):```
* for assignments and return values you can use ternary expressions like this: 
  ```firstoption if condition else secondoption```
* anonymous functions consist of one statement only and are written like this: 
  ```lambda parameters: statement```
* lambdas can receive multiple parameters, e.g. this lambda returns 
  the sum of ```a``` and ```b```: ```lambda a, b: a + b```
* unlike function parameters, function return values are not part of the function signature

We have declared three functions ```fib```, ```fib2``` and ```fib3```,
and we can use all of them in the REPL from now on.

## Loops ##

Let's test if the fibonacci functions work:
             
```a = [(y, x(y)) for x in [fib, fib2, fib3] for y in range(0, 10 + 1)]```

As you've noticed by now, Python code can be made quite compact. Let's rewrite this line
as a more beginner-friendly function:

```
def give_me_a():
     a = []
     for fibo in [fib, fib2, fib3]:
             for n in range(0, 10 + 1):
                     a.append((n, fibo(n)))
     return a
```

Now let's assign the function return value to a variable ```b```:

```b = give_me_a()```

Okay time to analyse what has happened:
* Python's for loop can be used like this ```for element in list```
* You can write nested for loops as one-liners, but it can be difficult to read
* ```range``` is a built-in function returning a list of numbers: 
  ```range(0,5)``` will return ```[0,1,2,3,4]```
* as we learnt in the lesson's intro, functions are first-class citizens: 
  you can assign functions to variables and then invoke them

The above code iterates over all three fibonacci functions.
It iterates over the numbers 0 to 10 in a nested loop
and invokes all three fibonacci methods with these numbers 0 to 10.
The results are appended to a list as a tuple consisting 
of 1) the number and 2) the return value of the fibonacci invocation 
with this number passed as argument.

## Process a list in a function  ##

Now let's check if both lists ```a``` and ```b``` are the same. 
Of course, we could just execute ```a==b``` but that's boring.

Let's do two things:
* count all distinct elements in the lists and see 
  if all of them appear exactly 3 times in the list
* remove all duplicates from the lists and check if they look the same then:

```def reduce(l): return list(dict.fromkeys(l))```

This was sort of a hack. ```dict.fromkeys()``` creates a dictionary from a list 
passed as an argument. ```list()``` creates a list from the dictionary keys. 
As dictionary keys must be unique, all duplicates are automatically removed.

Now input ```reduce(a)``` and then ```reduce(b)``` to see if both results look the same.

Note that we didn't change ```a``` and ```b```, 
but simply returned another list by calling the ```reduce``` function.

## Imports ##

Now let's check if all elements in the lists ```a``` and ```b``` are evenly distributed.
We could use the ```count(element)``` method of the list for every value in it
but that is not a good idea for big lists performance wise 
so let's use a standard library for that.

Input the following into your REPL: ```from collections import Counter as c```

Oh something new. :-) We imported the ```Counter``` class from the ```collections``` module
and refer to it as ```c``` (because programmers are lazy).

If we entered ```import collections``` we would have to refer
to ```Counter``` as ```collections.Counter``` in our code 
(and we would have imported the whole module instead of only the ```Counter``` class).

Need to know if a module is installed? Just try to import it in the REPL!

*Pip* is the most popular Python Package Installer. You will not learn about it
in this course but you should definitely visit the 
[Python Package Index](https://pypi.org) online! 
Don't worry, it's very to install Python packages.

Unlike in many other languages, in Python you can import anything on the fly.
You can even import stuff in loops or branches. You could even write code
that writes source code files and then imports them! Everything is possible in Python. 😄

Now input the following and observe the output: ```c(a), c(b), c(a)==c(b)```

The output should look like this:
```(Counter({(0, 1): 3, (1, 1): 3, (2, 2): 3, (3, 3): 3, (4, 5): 3, (5, 8): 3, (6, 13): 3, (7, 21): 3, (8, 34): 3, (9, 55): 3, (10, 89): 3}), Counter({(0, 1): 3, (1, 1): 3, (2, 2): 3, (3, 3): 3, (4, 5): 3, (5, 8): 3, (6, 13): 3, (7, 21): 3, (8, 34): 3, (9, 55): 3, (10, 89): 3}), True)```

The output is a tuple with three elements:
* an instance of ```Counter```
* another instance of ```Counter```
* ```True```

```Counter``` creates a dictionary containing all distinct entries of the passed list 
and how many times they appeared in the list.

As every element appears 3 times in the original list 
I would say all the fibonacci functions do the same.
Also ```a``` and ```b``` are the same. Let's move forward to something else.

## Closure ##

Let's write a fibonacci closure to demonstrate Python supports closures:

```
def fib4():
    prv = 0
    nxt = 1
    def nextfib():
        nonlocal prv
        nonlocal nxt
        nxt = prv + nxt
        prv = nxt - prv
        return nxt
    return nextfib
```

Now let's assign that function and invoke it in a loop:

```
myfib = fib4()
while (x:=myfib()) < 100: print(x)
```

Expected output:

```
1
2
3
5
8
13
21
34
55
89
```

Looks legit. Let's analyse what happened:
* Python supports closures (the state of ```prv``` and ```nxt``` 
  is retained across multiple invocations)
* to manipulate variables of a higher level function declare them as ```nonlocal```
* the while loop can be used like this: ```while condition:```
* Python allows assignments in conditions (since Python 3.8)
* In the while loop's condition, ```x``` is assigned to the result of ```myfib()```
  and then compared to ```100```
* ```print``` is a built-in function to pass text to ```stdout``` - 
  if we weren't in the REPL you would have learnt that earlier!

## Class ##

Now let's create a class:

```class Empty: pass```

For those coming from languages like *Java* or *C#*: 
Yeah, there is no *one class per file rule*, 
and a class doesn't need to be big and bloated either.

Let's analyse what happened:
* we created a new class named ```Empty```
* blocks in Python cannot be empty due to the space/tab based syntax, 
  instead we can use the keyword ```pass``` to create an empty block, this works for if/else branches and loops too
  
## Object ##

Let's assign an instance of ```Empty``` to a variable ```a```:

```a = Empty()```

The output of a should look something like this:

```
>>> a
<__main__.Empty object at 0x7fd102913f70>
```

We can use the built-in ```dir``` function to inspect an object:

```
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

## Modifying an object at runtime ##

Let's make ```a``` more lively:

```
>>> a.fib = myfib
>>> a.fib()
233
```

Yes, we've just created a new instance method ```fib()``` in instance ```a``` of class ```Empty```,
and it still retains the state of ```nxt``` and ```prv``` of the closure we made earlier.

Let's see if class ```Empty``` is aware of this new property:

```
>>> dir(a)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fib']
>>> dir(Empty)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

As we can see the ```fib``` property is exclusive to instance ```a```
and the class ```Empty``` doesn't know about it. This behaviour is similar
to the *prototype* model used in *JavaScript*.

## More about classes ##

Let's create another class:

```
class Sum:
  def __init__(self, a,b):
    self.a = a
    self.b = b
    
  def __str__(self):
    return "The sum of %d and %d is %d!" % (self.a, self.b, self.a + self.b)

```

Now enter the following into the REPL:

```str(Sum(3,5))```

The output should be:

```'The sum of 3 and 5 is 8!'```

Let's analyse what happened:
* class methods must declare ```self``` as the first parameter
* ```self``` is like ```this``` in many other languages: it refers to the instance
* instance fields (variables) don't need to be declared,
but if they're referred to before assigning them, it will result in an error
* methods enclosed in double underscores are considered private,
  but actually they can still be called from outside the class
* ```__init__``` is a standard method functioning as a constructor
* ```__str__``` is a standard method invoked by the built-in ```str()``` function 
  to return a string representation of an object
* omitting ```self``` when declaring instance methods is a very common mistake, 
  and as a casual Python user, it happens to me all the time! If you see an error
  like ```method() takes 0 positional arguments but 1 was given```, it probably
  means you forgot to declare ```self```.

This concludes the lesson.

## Navigation ##
* [back to course overview](../README.md)
* [continue with lesson 3](lesson-3/0.md)
* [revise lesson 1](lesson-1.md)
