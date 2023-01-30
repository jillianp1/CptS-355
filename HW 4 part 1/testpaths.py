
dict = {A:{}}
node = 'A'
listOfLists = [['A']]


def main_function(dict):
    # as if just given dictionary and not a key node
    listOfLists = []
    #get the first key 
    for key in dict.keys():
        print(key)
        listOfLists.append(key)
        print(listOfLists)

    #need to add a while the delimeter is not included 
    deliminator = []
    for key,paths in dict.keys():
        if paths == {}:
             key = deliminator

    # send list to helper function 
    helper_function(listOfLists, dict)

    #once list of list is returned need to check it deliminator is in list 
    


    return None


def helper_function(listOfLists, dict):
    #make a copy of the list 
    copiedList = listOfLists.copy()
    #getting the paths (the things that A can touch)
    for nodes, paths in dict.items():
        print(nodes)
        print (paths)
        if len(paths) == 1:
            #theres only one thing the node can go to so append
            copiedList.append(paths)
        elif len(paths) > 1:
            # there is multiple things it can go to so need to make a copy and append
            copiedList.append(paths)


    return copiedList





