class HTMLDocument:
    """Typing doc for class"""
    content = "HTML/CSS"
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

#since python is dynamic langage 

