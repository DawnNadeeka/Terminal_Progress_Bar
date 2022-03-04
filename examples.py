from Progress_Bar import ProgressBar

def _example_function(num):
    """
    An example function to help with the driver example. Adds the given amount of numbers, N times, to a list, to give the program enough code to cause a visible stall, so that the change in the progess bar can be easily observed.

    Parameters
    ----------
    num : int
        The number of times to add N items to the list
    """
    example_list = []
    N = 500000

    for i in range(num * N):
        example_list.append(i) #NOTE For example; adds items to an empty list

def driver_example():
    """
    An example driver to show how to use the class
    """

    print("Command Prompt Progress Bar Demo")
    print("   - Read comments in driver_example() for more details):")

    #Creates new progress bar
    bar = ProgressBar()
    bar.show()

    #Runs an example function to demonstrate an action in progress, and then updates the progress by 10%
    _example_function(10)
    bar.add_percent(10)

    #A change of 23%
    _example_function(23)
    bar.add_percent(23)

    #Loops 50 times, running the example function and then updating the progress bar by 1%
    for i in range(50):
        _example_function(1)
        bar.add_percent(1)

    #Decreases the progress bar by using negative numbers
    _example_function(10)
    bar.add_percent(-10)
    _example_function(12)
    bar.add_percent(-12)

    print("Test interruption")

    #Changes the symbol that is used to fill the progress bar
    bar.symbol = "X"
    bar.empty_symbol = "_"
    bar.edge_front = "<"
    bar.edge_back = ">"
    bar.divider = "~"

    for i in range(25):
        _example_function(1)
        bar.add_percent(-1)

    if bar.is_open(): #Checks to make sure the bar can be edited
        #If the progress bar is set above 100%, it will just display 100%
        _example_function(75)
        bar.add_percent(75)
    
    #Closes the bar. The progress bar will no longer be editable, meaning that the functions can no longer be called on it, and an ending display will be drawn
    bar.end()

    print("Closed the progress bar.")

    #A closed bar cannot be edited
    try:
        bar.add_percent(10)
    except PermissionError as e:
        print(f"   - {e}")

driver_example()
print("Finished demonstration.")