def check(inp):
    stack_=[]
    for i in inp:  
        if i==')' and stack_[-1]=='(':
            stack_.pop()
        elif i=='}' and stack_[-1]=='{':
            stack_.pop()
        elif i==']' and stack_[-1]=='[':
            stack_.pop()
        elif i == '(' or i=='{' or i=='[':
            stack_.append(i)
    print(stack_)     
    if stack_:
        return False
    return True

print(check("([)]"))