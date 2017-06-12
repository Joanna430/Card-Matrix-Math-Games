def diag_matrix(diag_nums):
    """
    It takes a list of numbers and returns a diagonal square matrix having those numbers along the diagonal.
    """
    result = []
    sublist = []
    for dummy_num in range(len(diag_nums)):
        sublist.append(0)
    #The precedures above set an initial sublist whose items are all zero.
    count = -1 
    #The count starts from -1 because when we are running the for loop below, it automatically adds one to count.
    #So in fact, the first "count" we use to index the list "copy" is 0.
    for item in diag_nums:
        count += 1
        copy = list(sublist) #Copy the sublist again so that the for loop won't change the initial sublist.
        copy[count] = item
        result.append(copy)
    return result

print diag_matrix([1,2,3])
