# PART A
"""
Q1
"""
def fib_rec(n, i=0, first = 'a',last = 'bc' ):
    """
    Recursive Function thats return a fibonacci series of char
    :param n: the number of the Fibonacci sequence
    :param i: counter
    :param first: the first char in the fibonacci
    :param last:  the second char in the fibonacci
    :return: the fibonacci characters series as a string
    """
    tmp = "" #temp string
    if i == n-1: #if statment to stop the recursion
        return last #return resualt
    tmp = last
    last += first
    first = tmp
    return fib_rec(n, i+1, first, last) #call back the function with counter increased

def fibonacci_chars(n, k):
    """
    Function that call a recursive Fibonacci chars function and return the 'k' char
    :param n:the number of the Fibonacci sequence
    :param k:the 'k' char wanted
    :return:the 'k' char wanted
    """
    if n == 2:
        return 'abc'[k]
    if n == 0:
        return 'a'[k]
    return fib_rec(n)[k] #return the 'k' char in the string

def dr_mem(ev, ls, i=0):
    """
    Recursive function that gets a list of numbers and return the indexes of any number inbetween two bigger numbers.
    :param ev: list of elevations histogram
    :param ls: list of indexs to save to
    :param i: counter
    :return: list of indexs
    """
    if i == len(ev) - 1: #if statment to stop the recursion
        if ev[i] < ev[i-1]:
            ls.append(i)
        return ls #final return
    if i == 0: #check for first num
        if ev[0] < ev[1]:
            ls.append(i)
            return dr_mem(ev, ls, i + 1) #call the function again with counter increased
        else:
            return dr_mem(ev, ls, i + 1) #call the function again with counter increased
    if (ev[i] < ev[i+1]) and (ev[i] < ev[i-1]): #check for any number if its in between two bigger numbers
        ls.append(i)
    return dr_mem(ev, ls, i+1) #call back the function with counter increased

def drainage_basins(ridge_elavation):
    """
    Function that call the recursive function and return result
    :param elevation_histogram: list of elevations histogram
    :return: list of the indexs
    """
    ls = [] #list that saves indexs
    return dr_mem(ridge_elavation, ls) #call back the recursive function


import copy
def isValidCell(i1, j1, grid, current_weight):
    """
    Function that check if the next step is valid
    :param i1: the y of the cell
    :param j1: the x of the cell
    :param grid: the grid
    :param current_weight: total current weight
    :return: boolean
    """
    return not (i1 < 0 or j1 < 0 or i1 >= len(grid) or j1 >= len(grid[0]))


def countPaths(grid, i1, j1, i2, j2, current_weight, visited, count):
    """
    Function that check recursive all the ways to solve the path and count how many ways.
    :param grid: the "maze" (list of lists)
    :param i1: starting y
    :param j1: starting x
    :param i2: goal y
    :param j2: goal x
    :param current_weight: starting weight
    :param visited: copy of the grid to mark visited cells
    :param count: counter
    :return: counter
    """
    if i1 == i2 and j1 == j2 and isValidCell(i1, j1, grid, current_weight):
        if grid[i1][j1] * 2 > current_weight:
            return count + 1
    temp_cell = grid[i1][j1]
    current_weight += grid[i1][j1]
    visited[i1][j1] = - 1 #mark current cell as visited

    # if current cell is a valid and valid in weight
    if isValidCell(i1, j1, grid, current_weight) and grid[i1][j1] * 2 > current_weight or not current_weight:

        # go up (i1, j1) --> (x, y+1)
        if i1 + 1 < len(grid) and visited[i1 + 1][j1] != -1 and temp_cell != grid[i1 + 1][j1]:
            count = countPaths(grid, i1 + 1, j1 ,i2 ,j2 , current_weight , visited, count)

        # go down (i1, j1) --> (x, y-1)
        if i1 - 1 >= 0 and visited[i1 - 1][j1] != -1 and temp_cell != grid[i1 - 1][j1]:
            count = countPaths(grid, i1 - 1,j1 ,i2 , j2, current_weight, visited, count)

        # go right (i1, j1) --> (x+1, y)
        if j1 + 1 < len(grid[0]) and visited[i1][j1 + 1] != -1 and temp_cell != grid[i1][j1+1]:
            count = countPaths(grid, i1, j1 + 1,i2 ,j2, current_weight, visited, count)

        # go left (i1, j1) --> (x-1, y)
        if j1 - 1 >= 0 and visited[i1][j1 - 1] != -1 and temp_cell != grid[i1][j1 - 1]:
            count = countPaths(grid, i1, j1 - 1,i2 ,j2, current_weight, visited, count)


    visited[i1][j1] = False #backtrack from the cell and delete the visited state
    return count #return counter

def is_legit_track(grid, i1, j1, i2, j2, current_weight):
    """
    check if move from cell to another is valid
    :param grid: the "maze" (list of lists)
    :param i1: starting y
    :param j1: starting x
    :param i2: goal y
    :param j2: goal x
    :param current_weight: current weight
    :return: return boolean true if valid else return false
    """
    if i1 + 1 == i2 and j1 == j2: #check if up valid
        if (current_weight + grid[i2][j2]) < 2 * grid[i2][j2]:
            return True
    elif i1 - 1 == i2 and j1 == j2:#check if down valid
        if (current_weight + grid[i2][j2]) < 2 * grid[i2][j2]:
            return True
    elif i1 == i2 and j1 + 1 == j2:#check if right valid
        if (current_weight + grid[i2][j2]) < 2 * grid[i2][j2]:
            return True
    elif i1 == i2 and j1 - 1 == j2:#check if left valid
        if (current_weight + grid[i2][j2]) < 2 * grid[i2][j2]:
            return True
    return False
"""
Q2
"""
def get_number_legit_tracks(grid, i1, j1):
    """
    Function that call the recursive function to get the number of valid tracks
    :param grid: grid (list of lists)
    :param i1: starting y
    :param j1: starting x
    :return: the number of valid tracks
    """
    i2 = len(grid) - 1 #set ending y
    j2 = len(grid[0]) - 1 #set ending x
    visited = copy.deepcopy(grid) #copy grid for visited
    current_weight = 0 #set weight
    count = 0 #set counter
    return countPaths(grid, i1, j1, i2, j2, current_weight, visited, count) #call recursive function

# PART C
"""
Q1
"""
# flower = 'Name' 'LVL' 'Price'
def flower_helper(flowers, budget, list_of_best, counter = 0, max = 0):
    """
    Recursive Helper Function to find best flower arrangement possible from budget
    :param flowers: list of flowers with name, beauty value and price
    :param budget: budget for the arrangement
    :param list_of_best: list of the best arrangement found
    :param counter: counter for the index of the list
    :param max: maximum beauty value
    :return: return tuple object of max beauty value and budget left
    """
    if budget < 0 or counter == len(flowers):
        if budget < 0:
            return
        elif not list_of_best: #if not in list than add to list
            list_of_best.append((max, budget))
        elif (max, budget) > list_of_best[0]: #if in list than check if smaller than th current to save maximum value
            list_of_best.pop(0) #delete old one
            list_of_best.append((max, budget)) #add new one
        return
    flower_helper(flowers, budget - flowers[counter][2], list_of_best, counter + 1, max + flowers[counter][1]) #call back the function taking next value
    flower_helper(flowers, budget, list_of_best, counter + 1, max) #call back the function ignoring next value
    return list_of_best[0] #return the tuple

def optimize_flowers_selection(flowers, budget):
    """
    Function that call the recursive function
    :param flowers: list of flowers with name, beauty value and price
    :param budget: budget for the arrangement
    :return: return tuple object of max beauty value and budget left
    """
    if budget == 0:
        return (0, 0)
    if not flowers:
        return (0, budget)
    ls = []
    return flower_helper(flowers, budget, ls)
"""
Q2
"""
#[['lilach',1,3],['roni',5,1],['itamar',6,2]]
def flower_helper_faster(flowers, budget, list_of_best,dic , counter = 0, max = 0, temp="" ,temp_max = 0, temp_budget = 0):
    """
    Recursive Helper Function to find best flower arrangement possible from budget, with memorization to prevent double calculations
    :param flowers: list of flowers with name, beauty value and price
    :param budget: budget for the arrangement
    :param list_of_best: list of the best arrangement found
    :param dic: dictionary of combinations available
    :param counter: counter for the index of the list
    :param max: maximum beauty value
    :param temp: temp string that save the combinations names
    :param temp_max: temp maximum beauty value that save the combinations beauty value
    :param temp_budget: temp budget that save the combinations price
    :return: return tuple object of max beauty value and budget left
    """
    if budget < 0 or counter == len(flowers):
        if budget < 0:
            return
        elif not list_of_best:
            list_of_best.append((max, budget))
        elif (max, budget) > list_of_best[0]: #if in list than check if smaller than th current to save maximum value
            list_of_best.pop(0) #delete old one
            list_of_best.append((max, budget)) #add new one
        return
    temp += str(flowers[counter][0]) #save the names to string
    temp_max += flowers[counter][1] #sum the beauty values
    temp_budget += flowers[counter][2] #sum the prices
    if temp not in dic: #check if not in dictionary
        dic[temp] = (temp_max, temp_budget)
    elif temp in dic: #if in dictionary use the calculates we already did
        flower_helper_faster(flowers, budget - dic[temp][1], list_of_best,dic , counter + 1, dic[temp][0], temp, temp_max, temp_budget)
        flower_helper_faster(flowers, budget, list_of_best,dic , counter + 1, max, temp, temp_max, temp_budget)
    flower_helper_faster(flowers, budget - flowers[counter][2], list_of_best,dic, counter + 1, max + flowers[counter][1], temp, temp_max, temp_budget) #call back the function ignoring next value
    flower_helper_faster(flowers, budget, list_of_best,dic, counter + 1, max, temp, temp_max, temp_budget) #call back the function ignoring next value
    return list_of_best[0] #return tuple

def get_plants_to_buy_faster(flowers, budget):
    """
    Function that call the recursive function
    :param flowers: list of flowers with name, beauty value and price
    :param budget: budget for the arrangement
    :return: return tuple object of max beauty value and budget left
    """
    if budget == 0:
        return (0, 0)
    if not flowers:
        return (0, budget)
    ls = []
    dic = {}
    return flower_helper_faster(flowers, budget, ls, dic)