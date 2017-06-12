"""
Think of shuffling a deck of cards. Split the deck in half, or roughly so. Then we interleave the cards from the two groups. 
This game takes two lists and creates a new list, alternating cards from the two lists.
The resulting list starts with the first card from the longer list (or the first list, in the case of equal lengths).
Any "extra" elements of the longer list are put at the end of the new list.
Example:  interleave(['a', 'b'], [1, 2, 3, 4]) should result in [1, 'a', 2, 'b', 3, 4].
"""

def interleave(list1, list2):
    """
    It takes two lists and creates a new list, alternating cards from the two lists.
    It returns a resulting list starts with the first card from the longer list.
    Extra cards are put at the end of the resulting list.
    """
    result = [] #Create an empty list which later we use it to add our result in it.
    extra = [] #Create an empty list which later we use it to sort out the extra cards.
    if len(list2) > len(list1):
        new_list = zip(list2, list1)
        for idx in range(len(list1),len(list2)):
            extra.append(list2[idx])
    else:
        new_list = zip(list1, list2)
        for idx in range(len(list2),len(list1)):
            extra.append(list1[idx])
    for item1, item2 in new_list:
        result.append(item1)
        result.append(item2)
    for item in extra:
        result.append(item)
    return result
            
        
#print interleave(['a', 'b', 'c'], [1, 2, 3, 4])   
    

