#----------------------------------------------------------
#
# Code of Makhambet
#
#__________________________________________________________

mylist = [10, 11, 13, 16, 19, 23, 26, 29, 32, 43, 54, 67]

def binarysearch (mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid - 1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)

iskat = 13
start = 0
stop = len(mylist)

x = binarysearch(mylist, iskat, start, stop)

if x == False:
    print("Item", iskat, "Not Found")
else:
    print("Item", iskat, "Found at Index", x)