import requests #accessing internet
import bs4 #parsing a webpage

# Use the `requests` library to initialize a `Response` object called
# `response` for this webpage
url = "https://greenteapress.com/thinkpython2/html/thinkpython2002.html"
response = None###YOUR CODE HERE###

# Use the `bs4` library to initialize a `BeautifulSoup` object called `soup`
# for the html in `response.text`
soup = None###YOUR CODE HERE###

# Use the `prettify()` method to make a string version of the soup object
pretty_html_string = None###YOUR CODE HERE###

# Using the `with` syntax (so that the file gets closed properly), make a file
# object called `f` for a new text file called "think_python_chapter1.html"
###YOUR CODE HERE###

    # Inside the indented block for `with` (so that the file isn't closed yet
    # when you use it) use the `write()` method to write `pretty_html_string`
    # to the file
    ###YOUR CODE HERE###

# Open the file "think_python.html" using your computer's file explorer
###TRY IT!###

