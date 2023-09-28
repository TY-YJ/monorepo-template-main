# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- MObject is not an abstarct. It is indeed a concrete class. In order to create abstract class in Python, you would need a ABC module, along with the abstract method decorator. 
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- According to the document provided, the __del__ method is called a finalizer or destructor and a special method in Python classes that gets called when an instance of the class is about to be destroyed or garbage collected.
1. What class does Texture inherit from?
	- the Texture class inherits from the Image class
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- 'Texture' inherits all methods and attributes from the 'Image' class. 
  - Methods: init method, getWidth, getHeight, getPixelColorR, getPixels, and setPixelsToRandomValue
  - Attributes: m_width, m_height, m_colorChannels, and m_Pixels
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- In order for a texture to have a 'has-a' function, Texture class would contain an instance of the Image class as one of its members. 
  - If it was a 'has-a' relationship, the code would look like
    ```python
      class Texture:
        def __init__(self, w,h):
          self.obj = Image(w,h) 
    ```
  - In this case, Texture extends Image by Texture(Image). Texture is a type of Image. Therefore, "is-a" relationship (inheritance) seems more appropriate

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Python will provide a default constructors for us if no constructor is defined.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
- In single threaded environment, it will be safe, however
in multi-threaded environment, explicit synchronization is required to maintain the singleton pattern and ensure that only one instance is created regardless of concurrent access attempts from multiple threads. 
  
