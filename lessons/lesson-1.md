# Native data types and structures #

## Table of Contents ##
* [Integer](#integer)
* [String](#string)
* [Boolean](#boolean)
* [None](#none)
* [List](#list)
* [Dictionary](#dictionary)
* [Tuple](#tuple)
* [More about data structures](#more-about-data-structures)
* [Float](#float)
* [String formatting](#string-formatting)

This lesson is split into several small stages for your guidance.
The later stages are based on the previous ones, 
so for the best experience it is recommended to do them in order.

Open your REPL!

## Integer ##

Let's start by assigning a numeric value of 100 to a variable `a`:

`a = 100`

Now input `a` and press enter to see the assigned value.
Always do that if you want to see the actual value of a variable or expression.

## String ##

Let's do the same for a string, assign the famous 'hello, world!':

`b = "hello, world!"`

Python supports single and double quotation marks. Let's rewrite the statement:

`b = 'hello, world!'`

Python also supports multi line strings:

`
b = """hello
, 
world!"""
`

P.S.: After you input a multi line string you must press enter 
to send your input to the REPL. You will learn the *why* in the next lesson.

Now assign the original value with double quotation marks again.
You can navigate through previously executed inputs in the REPL
by using the up and down arrow keys on your keyboard.

## Boolean ##

Python is case sensitive and booleans start with an uppercase letter:

`c = True`

what's the opposite of True? Find out by executing the following:

`not True`

## None ##

Null? Nil? No, None! Again, the uppercase letter is important:

`d = None`

## List ##

Let's put all variables in a list:

`e = [a,b,c,d]`

A list can contain elements of any type, even other lists.
Expected value of `e`:  `[100, 'hello, world!', True, None]`
* You can replace the square brackets by curly brackets to use a set instead of a list.
* You can declare an empty list by assigning `[]`.
* You cannot assign `{}` to create an empty set, instead assign `set()`.
Why? You will see in a moment. But first let's have another look at lists.

`string = 'Fantasticsearch'`

Strings are basically lists (of characters). Input the following commands and observe the output:

`string[1:4]`

`string[:4]`

`string[4:]`

`string[1:-1]`

`string[-4:-1]`

`string[:]`

You can easily extract a sub list from a list this way: `[1,2,3,4][1:-1] == [2,3]`  

## Dictionary ##

Let's create a dictionary. This is also called an associative array or a map in other languages:

`f = {a:b, c:d}`

Expected value of `f`: `{100: 'hello, world!', True: None}`

Now guess what `{}` creates? Right, an empty dictionary.

Accessing dictionaries is very *pythonic*. Can you guess how to extract `'hello, world!'` from `f`?

Yes, it's `f[100]`, or alternatively `f[a]`.

## Tuple ##

Another native type in Python is a tuple. Tuples are immutable:

`g = (a,b,c,d)`

Expected value of g: `(100: 'hello, world!', True: None)`

Tuples can be *unpacked*:

`d,c,b,a = g`

Did you see what we just did? `a` and `d`, 
as well as `b` and `c` switched values.
We can do that with just a single command like `a, b = b, a`.

## More about data structures ##

Okay to avoid confusion let's have a quick look what's in these variables now.
Input the following: `a, b, c, d, e, f, g`
The output should be: 
```
(None, True, 'hello, world!', 100, [100, 'hello, world!', True, None], 
{100: 'hello, world!', True: None}, (100, 'hello, world!', True, None))
```

Let's review the output. The output is wrapped in parentheses
because the input is interpreted as a tuple.
This tuple contains `a`, `b`, `c` and `d` followed by a list 
followed by a dictionary followed by a tuple where list, dictionary and tuple 
all have `d`, `c`, `b` and `a` 
in this same order in their textual representation.

Keys in a dictionary must be unique but can we use `None` as a key? Yes we can:

`f = {a:b, c:d}`

What about lists and dictionaries? Well they can't be used as keys 
but it's perfectly fine to use them as values. Try the following:

`f = {a:e, b:f}`

So what's in `f`? Well if you thought about self reference or an endless loop,
don't worry. It just contains a list and another dictionary which is not
the same as `f` anymore since `f` has simply been reassigned.

Expected value of `f`: 
`{None: [100, 'hello, world!', True, None], True: {None: True, 'hello, world!': 100}}`

Now let's see if you paid attention. What's this? `{(): [], (): {}}`

If you type it into the REPL the output will be `{(): {}}`

What happened? You created a dictionary with two elements:
* an empty tuple as key and an empty list as value
* an empty tuple as key and an empty dictionary as value

Keys in a dictionary are unique so the latter entry replaces the former
and thus you have created a dictionary with one entry 
consisting of an empty tuple and an empty dictionary.  

Paid attention? Then you've noticed an advantage tuples have over lists:
They can be used as dictionary keys. So if you want to use an immutable list
as a dictionary key, simply convert it to a tuple. 😉

By the way you can *typecast* between tuples and lists:
`tuple([1,2,3])` creates a tuple from a list,
`list((1,2,3))` creates a list from a tuple.

Oh right and you can nest tuples however you want. Perfectly valid assignment:
`z = ((),((),((),())),())`

## Float ##

Well before we conclude this lesson, let's mention floats.
You could probably assign a float value without my help by now
since there's no big surprise, and they suffer from the same arithmetic problems
they do in other languages.

What's the output of `(1+2)==3`? Yes, the output is `True`.
Now how about `(0.1+0.2)==0.3`? Exactly, it's `False`. 
Like in other languages if you care about floating-point precision
you are better off using a library designed for that instead of using simple floats.
In Python, you could use the decimal module, but let's talk about modules in another lesson.

Okay, let's create a float:

`h = 98/99`

## String formatting ##

What have we learnt in this lesson?

Input the following into your REPL:
```
"""
%s It is %s that I learnt a lot about Python today. 
I learnt %d things and I regret %s of them. 
I'm %.02f%% sure that I will master the language in no time!
""" % (c.upper(), str(b).lower(), d, a, h*100)
```

This should result in the following output:

```
HELLO, WORLD! It is true that I learnt a lot about Python today.
I learnt 100 things and I regret None of them.
I'm 98.99% sure that I will master the language in no time!
```

Let's analyze what's happened:
* Python has native string formatting
* String variables can be embedded in a string using `%s`
* Integer variables can be embedded using `%d`
* Float variables can be embedded using `%f`
* Numbers can be further formatted: `%.02f` will print a float representation with two decimal places
* To escape % in a string double it: `%%`
* a built-in method to convert anything to a string is `str()`
* strings can be converted to upper- or lowercase with the respective methods `upper()` and `lower()`
* the syntax to format variable a in to a string is `"%s" % a` (assuming a is "stringable")
* multiple variables must be wrapped in a tuple so they can be unpacked into the string `"%s%s" % (a,b)`

Now let's erase everything we've assigned. You could leave the REPL by entering `exit()` and reopen it
or you could assign all variables to None: `a=b=c=d=e=f=g=h=z=None`

This concludes the lesson.

## Navigation ##
* [back to course overview](../README.md)
* [continue with lesson 2](lesson-2.md)
