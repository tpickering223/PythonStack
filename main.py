import LinkedStack
import sys


def pushString(value, theStack):
    for i, k in enumerate(value):
        theStack.push(k)


if __name__ == "__main__":
    stack = LinkedStack.Stack()
    # normal = input("Input a string to be reversed: ")
    reverse = ""
    spacing = 0
    if len(sys.argv) != 1:
        if sys.argv[1] == "cmd":
            spacing = 1
            for i in range(2, len(sys.argv)):
                pushString(sys.argv[i], stack)
                if spacing == 1:
                    pushString(" ", stack)
        elif sys.argv[1] != "inter":
            sys.exit("Improper argument placement. Usage: py main.py [cmd/inter] [\"Your message\",]+ ")
            
        else:
            input_str = input("Input a string to be reversed: ")
            pushString(input_str, stack)
            

        while stack.getSize() > 0:
            reverse += stack.pop()
        print("Reversed string: " + reverse)
    else:
        print("Arguments required in format: py main.py [cmd/inter] [\"Your message\",]+ ")
    
        
        
