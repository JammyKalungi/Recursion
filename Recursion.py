def compute_sum(list1):
    if not isinstance(list1, list):
        return 'Invalid argument type. This should be a list'
    mysum=0
    for i in list1:
        if isinstance(i,int):
            mysum+=i

        elif isinstance(i,list):
            mysum+=compute_sum(i)
        
    return mysum

if __name__ == '__main__':
    print(compute_sum(['a',3,[5,6]]))