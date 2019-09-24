###########################
###       Lab 2         ###
###########################

# Part 1
def select_bubbleSort(L,k):
    #run until length of the list is reached
    if k > len(L)-1:
        return
    else:
        #iterate for length of list
        for num in range(len(L)-1):
            #if current number is greater than the next num...
            if L[num] > L[num + 1]:
                #swappity swap!
                tmp = L[num]
                L[num] = L[num + 1]
                L[num + 1] = tmp
        return select_bubbleSort(L,k + 1)
    
def select_quickSort(L, left, right):
    if left < right:
        #p is now at its 'right' place
        p = quick_Split(L, left, right)
        
        #sorting the elements to the left of the
        #rightfully placed element
        select_quickSort(L,left,p - 1)
        #sorting the elements to the right of the
        #rigthfully placed element
        select_quickSort(L,p + 1, right)

def quick_Split(L,left, right):
    #Pivot will be used to compare with the other elements in order to
    #place it in its rightfull place
    pivot = L[right] #pivot will start off as the last element
    i = left - 1 #keeps track of the element(s) before L[j]
    curr = left #begins at L[0]
    
    #run from left to right not including len(L) but len(L)-1    
    for curr in range(left,right):
        #comparing current with pivot
        #if current is less than pivot, swap
        if L[curr] < pivot:
            i = i + 1
            #swappity swap!
            tmp = L[i]
            L[i] = L[curr]
            L[curr] = tmp
            
    #Swappity swap again
    tmp = L[i+1]
    L[i+1] = L[right]
    L[right] = tmp
    
    return i+1

#Does this count?
def select_modifiedQuick(L, small, large):
    while small < large: #to traverse through the list
        p = quick_Split(L, small, large) #partition
        if (p - small) < (large - p):
            select_modifiedQuick(L, small, p - 1) #sort elems to the left
            small = p + 1 
        else:
            select_modifiedQuick(L, p + 1, large) #sorts elems to the right
            large = p - 1

# Part 2
# Incomplete

#class QuickStack:
#    #constructor
#    def _init_(self, left, right):
#        self.left = left
#        self.right = right

#def select_ModQuick(L, left, right):
#    stack = []
#    while left < right:
#        p = quick_Split(L, left, right) #partition
#        if (p - left) < (right - p):
#            stack.append(QuickStack(L, left, p - 1)) #sort elems to the left
#            left = p + 1 
#        else:
#            stack.append(QuickStack(L, p + 1, right)) #sorts elems to the right
#            right = p - 1
    
#Running method
    
def main():
    set1 = [10, 9, 4, 88, 100, 3]
    set2 = [5, 40, -10, 100, 0, 1]
    set3 = [101, 45, 2, 5, 15, 90]
    
    print("PART 1\n")
    print("Without sorting:", set1)
    select_bubbleSort(set1, 0)    
    print("Bubble Sort:", set1)
    print("\n")
    print("Without sorting:", set2)
    select_quickSort(set2, 0, len(set2)-1)
    print("Quick Sort:", set2)
    print("\n")
    print("Without sorting:", set3)    
    select_modifiedQuick(set3, 0, len(set3)-1)
    print("Modified Quick:",set3)
    
#    set4 = [81, 9, 18, 21, 64, 32]
#    print("PART 2\n")
#    select_ModQuick(set4,0, len(set4)-1)
#    print(set4)
    
main()