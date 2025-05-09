from pprint import pprint

class HTMLDocument:
    """Typing doc for class"""
    content = "HTML/CSS"
    version = 5
    def __init__(self, version):
        self.version = version

    def __str__(self):
        print("HTMLDocument instance is created with version {self.version}")


print(type(HTMLDocument))
print(HTMLDocument.__name__)
print(HTMLDocument.__dict__)
print(HTMLDocument.__dir__)
print(HTMLDocument.__doc__)
print(HTMLDocument)

#we can access class varaible using dot notation
print(HTMLDocument.content)
#or with getattr() function
print(getattr(HTMLDocument,'content'))

#to set a value of class variable/attribute
HTMLDocument.content = "HTML5"
print(HTMLDocument.content)
#or can use setattr() function
setattr(HTMLDocument, 'content', 'HTML5+')
print(HTMLDocument.content)

#since python is dynamic langage we can add class variable during runtime
HTMLDocument.media_type= 'text/html'
print(HTMLDocument.media_type)

#to delete class variable 
delattr(HTMLDocument, 'content')
print(HTMLDocument.__dict__)

# or can do 
del HTMLDocument.version


# callable class attribute
"""class attribute can be any objects such as functions
When we add function to a class the function becomes a class attribute.
Since function is callable the class attribute is callable attribute"""

def render():
    print("Rendering HTML doc")

HTMLDocument.render = render
pprint(HTMLDocument.__dict__)  # now you will see one more key render with function address
print(HTMLDocument.render())
