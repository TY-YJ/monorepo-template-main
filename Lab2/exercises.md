# Exercises

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.


    - I think the names of the member functions correlate to what they do. Using 'popAndGet' might add clarity about the dual nature of the action, but it could also introduce verbosity. The names of functions and member functions in the Python Standard Library are seemed carefully chosen to align with Pythonic principles, providing descriptive and intuitive names that effectively convey the actions they perform.*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

  - Dictionary:
    - It is unordered data collection
    - It stores data as key:value pairs
    - Underlying data structure is a hash table-based implementation 

  - List: 
    - It is ordered collections. The order of elements is preserved.
    - Elements can be accessed with indices
    - Use a dynamic array-based implementation for underlying data structure*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

  - List allows for a random access. Elements within the list are stored in contiguous memory locations, which enables efficient access to any elements by its indices

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

  - Pros:
    - Simplicity and reusability: developers can use and reuse the same set of functions and data structures regardless of the data types they are working with. 
    - Flexibility: Not only they can accommodate built-in types like integers and floats, but also custom data types created by developers.

  - Cons:
    - Type safety: Debugging might become more complex when data types are not well-defined.
    - Optimization: Generic libraries may not be optimized for specific data types.


## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

  - I think the function names in the Requests module generally align well with their intended actions.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

  - Class constructor has many parameters, however as far as the functions in Request module are concerned, the functions in the requests module usually have a moderate number of arguments, which is a good practice to maintain usability and avoid complexity

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

 - ** kwargs is used in some functions of the requests module to allow for flexibility in passing keyworded arguments, variable-length argument list. It allows users to provide additional arguments beyond the defined ones, which can be useful for customization. However, excessive reliance on ** kwargs can potentially make the usage less intuitive and harder to understand.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


 - Parameters are often set to None to indicate that if no value is provided for the parameter when calling the function or method, None will be used as the default value
 - Parameters can be set to any valid value based on the desired default behavior, like if you would like the default value to be empty string, it can be set to '[]'
 - Advantage of setting a default value is that is reduces the complexity of function calls and simplifies the API. Users can choose to override default values only when necessary and minimizes error due to missing or improperly specified arguments.
