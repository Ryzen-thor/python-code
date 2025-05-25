def check(inp):
    stack_=[]
    for i in inp:
        if stack_:    
            if i==')' and stack_[-1]=='(':
                stack_.pop()
            elif i=='}' and stack_[-1]=='{':
                stack_.pop()
            elif i==']' and stack_[-1]=='[':
                stack_.pop()
        elif i == '(' or i=='{' or i=='[':
            stack_.append(i)
            
    if stack_:
        return False
    return True

print(check("([)]"))