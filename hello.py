import sys
def greet(name:str) ->str:
    return f"hello {name},python version{sys.version_info.major}.{sys.version_info.minor}"

def add(a: int ,b: int)->int:
    return a+b
if __name__=="__main__":
    print(greet("nexerro"))
    print(f"3+5= {add(3,5)}")
