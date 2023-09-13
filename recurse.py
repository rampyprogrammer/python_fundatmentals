def recursive(data):
    total=0
    for ele in data:
        if type(ele)==type([]):
            total=total+recursive(ele)
        else:
            total+=ele
    return total
print(recursive([1,2,[12,34],[11,23],5,6]))
