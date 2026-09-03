
from rich import print

def hello(name: str) -> None : 
    print(f"Hello {name} ! ")
    
print("Hello World ! ")
print(f"Script name : {__name__}")


if __name__ == "__main__" :
 hello("Jeune Trublion")

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
