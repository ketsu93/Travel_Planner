
from string import digits

selection = input("Please select an option: \n -A- Plan Travel Route \n -B- Check list \n")
i = 1

if selection == "a":

    count = input("\nHow many locations do you want to add?\n")

    Des1 = input("\nEnter your First destination with distance (KM): \n")
    Des2 = input("\nEnter your Second destination with distance (KM): \n")        
    Des3 = input("\nEnter your Third destination with distance (KM): \n")
    Des4 = input("\nEnter your Fourth destination with distance (KM): \n")


    def DestinationPlanner(array, size):
        
        for ind in range(size):
            min_index = ind
    
            for j in range(ind + 1, size):
                # select the minimum element in every iteration
                if array[j] < array[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (array[ind], array[min_index]) = (array[min_index], array[ind])
    
    arr = [Des1, Des2, Des3, Des4]
    size = len(arr)
    DestinationPlanner(arr, size)


    print('\nThe shortest route is:')
    print(arr)

    print("\n------------------------------------------\n")

    selection2 = input("Do you want to view your Destination checklist \n Y/N \n")

'''Check list program below, purpose is to delete locations that the user has already visited'''

    

if (selection2 == "yes" or selection == "b"):

    remove_digits = str.maketrans('', '', digits)
    res1 = Des1.translate(remove_digits)

    remove_digits = str.maketrans('', '', digits)
    res2 = Des2.translate(remove_digits)

    remove_digits = str.maketrans('', '', digits)
    res3 = Des3.translate(remove_digits)

    remove_digits = str.maketrans('', '', digits)
    res4 = Des4.translate(remove_digits)
 
    # Initializing a queue

    queue = []
    
    # Adding elements to the queue
    queue.append(res1)
    queue.append(res2)
    queue.append(res3)
    queue.append(res4)
    
    print("Planned destinations\n")
    print(queue)


    answer = input('have you visited your previous location yet?\n (Y/N) \n')
    if answer == 'yes':
         # Removing elements from the queue
        '''print("\nLocation dequeued from queue\n")'''
        queue.pop(0)
          
          
        print("\nChecklist after removing Location\n")
    print(queue)

    if answer == "no":
        print("\n No locations have been checked out.\n")

    i = 0


if selection2 == "no" or i == 0:
    print("\nProcess Ended")

    


  
