# Fantasticsearch - a small search engine written in Python #

The aim of this lesson is to write a software in Python consisting of multiple source files.

Fantasticsearch is a small program that makes JEPs - 
Java Enhancement Proposals, the Java equivalent to Python's PEPs - searchable.

For that purpose Fantasticsearch parses the online JEP index and downloads all listed JEPs.
In a next step all relevant text will be extracted from JEPs, split into tokens,
serialized and saved as a file which will allow Fantasticsearch to launch significantly faster
in subsequent sessions.

Fantasticsearch is accompanied by Jepana, a web frontend that allows users to input a search string
and list all JEPs relevant for this search string. JEPs are linked to their web pages so
the user can jump directly from Jepana to the respective JEP hosted at the OpenJDK website.

Writing Fantasticsearch and Jepana is broken down into several small lessons.
