def function_one():
    names = ['jonathan','caitlin','robert','rocio','arya','adrain','desiree']   
    desiree_comprehension = [name for name in names if name=='desiree']
    desiree_list = (name for name in names if name=='desiree')
    print(desiree_comprehension,type(desiree_comprehension))
    print(next(desiree_list),type(desiree_list))
    
    x = str('jon');
    for i in x:
        print(i)

if __name__ == "__main__":
    function_one()