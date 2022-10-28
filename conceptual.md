### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is a high level object oriented language where as JS is a scriptong language
Python is more of a back end language and JS is more front end
JavaScript is browser-native, whereas Python is not. 
When you install Python on your system, you have access to REPL.JavaScript lacks a REPL. Most JS code is browser-based

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
1. Using the get() method. If the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned
2. using the setDefault() method . each time a key is absent, a new key is created with the def_value associated with the key passed in arguments.
 
 
 What is a unit test?
Unit testing is the process of testing the small units of the program.
This is done to make sure that each unit of the program is designed and working properly

- What is an integration test?
Integration testing comes after unit testing. This is the test that test the multiple components together

- What is the role of web application framework, like Flask?
A web application framework enables developers to build and run applications for the web without having to write all the code from scratc


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  you may decide which to use based on the reusability of the param

- How do you collect data from a URL placeholder parameter using Flask?
@app.route('/', methods=['GET'])

- How do you collect data from the query string using Flask?
print(request.query_string)

- How do you collect data from the body of the request using Flask?
print(request.form)

- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data that is used to track user data.
- What is the session object in Flask?
The session object is used to store session data. Session objects work like dictionaries but also can
- What does Flask's `jsonify()` do?
It turns the JSON output into a readable response object
