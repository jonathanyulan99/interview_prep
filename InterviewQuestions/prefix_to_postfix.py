def prefix_to_postfix(pre_expr):
    print(f"Before Post Function: {pre_expr}")
    ##reverse the pre_expression in place
    ##this sorts but not based on the last position can implement w/helper function or just return a new_expr reversed
    ##pre_expr.sort(reverse=True)
    pre_expr = pre_expr[::-1]
    print(f"After Post Function: {pre_expr}")
    ##need a stack, implement w/ pop and a list 
    stack = [] 
    
    ##user-variable to distinguish all the operators 
    operators = "*/-+"
    
    ##iterate through the backwards pre-infix expression
    for element in pre_expr:
        ##symbol is an operand, push on stack
        if element not in operators:
            ##.append() to the end of the list or top of the stack which is the tail
            stack.append(element)
        ##symbol is an operator
        else:
            #operand1 and operand2 
            operand_one = stack.pop()
            operand_two = stack.pop()
            
            #temp string 
            ##this operand_one + element + operand_two is what distinguishes the pre->infix and infix->post
            ##temp_string = operand_one + element + operand_two
            temp_string = operand_one + operand_two + element 
            
            #push the temp string on the stack 
            stack.append(temp_string)
    
    return(stack.pop())

def prefix_to_infix(pre_expr):
    print(f"Before Infix Function: {pre_expr}")
    ##reverse the pre_expression in place
    ##this sorts but not based on the last position can implement w/helper function or just return a new_expr reversed
    ##pre_expr.sort(reverse=True)
    pre_expr = pre_expr[::-1]
    print(f"After Infix Function: {pre_expr}")
    ##need a stack, implement w/ pop and a list 
    stack = [] 
    
    ##user-variable to distinguish all the operators 
    operators = "*/-+"
    
    ##iterate through the backwards pre-infix expression
    for element in pre_expr:
        ##symbol is an operand, push on stack
        if element not in operators:
            ##.append() to the end of the list or top of the stack which is the tail
            stack.append(element)
        ##symbol is an operator
        else:
            #operand1 and operand2 
            operand_one = stack.pop()
            operand_two = stack.pop()
            
            #temp string 
            ##this operand_one + element + operand_two is what distinguishes the pre->infix and infix->post
            temp_string = operand_one + element + operand_two
            
            #push the temp string on the stack 
            stack.append(temp_string)
    
    return(stack.pop())
            
print(f'PRE-> *-A/BC-/AKL \nINFIX-> {prefix_to_infix(list("*-A/BC-/AKL"))} \nPOST-> {prefix_to_postfix(list("++A*BCD"))}')