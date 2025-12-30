#Find invalid ids
with open("day2_values", 'r') as f:
    items = list(f.read().split(','))
#print(items)

def make_total(invalid_list):
    invalid_count = 0
    for itr in invalid_list:
        invalid_count += int(itr)
    return invalid_count

### Part 1
def has_equal_parts(n):
    """Check if a number can be split into two equal parts."""
    s = str(n)
    length = len(s)
    
    # Check for even length
    if length % 2 == 0:
        mid = length // 2
        return s[:mid] == s[mid:]  # Compare the two halves
    return False

def find_repeating_numbers_1(start, end):
    """Find and return a list of numbers that repeat by splitting in half."""
    repeating_numbers = [num for num in range(start, end + 1) if has_equal_parts(num)]
    return repeating_numbers

### Part 2
def get_factors(n):
    """Return all factors of a number."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    #print("List of factors: ", factors)
    return factors

def slice_on_factor(num, factor):
    """Check if a number has repeating patterns."""
    unique_digits = set()
    s = str(num) #convert to string for slicing
    length = len(s) 
    #slice into a set
    start_slice = 0
    end_slice = start_slice + factor
    for itr in range(length//factor):
        # add all numbers to set
        sliced = s[start_slice:end_slice]
        unique_digits.add(sliced)
        start_slice = end_slice
        end_slice += factor
    # Check for repeated digits
    #print(unique_digits)
    return len(unique_digits) == 1  # Has repeats if unique is less than length

def is_valid_id(num):
    """Check if an ID is valid based on repeating patterns. Return T/F"""
    print("Testing: ", num)
    length = len(str(num))
    factors = get_factors(length)
    for fac in factors:
        if fac == length: #reached the end of factor list so failed
            return False
        if slice_on_factor(num, fac): #send number and factor to split and check uniqueness of
            print(num, " is invalid!!")
            return True 
    return False
    ### return true if an invalid number

def find_invalid_ids(start, end):
    """Find numbers with invalid IDs in the specified range."""
    invalid_ids = [num for num in range(start, end + 1) if is_valid_id(num)]
    return invalid_ids

### Part 1
invalid_list_1 = list()
for itr in items:
    start = int(itr.split("-")[0])
    end = int(itr.split("-")[1])
    #print("Range:",start,"-",end)
    new_invalids = find_repeating_numbers_1(start, end)
    #print(new_invalids)
    invalid_list_1 = invalid_list_1 + new_invalids
print("part 1 answer: ", make_total(invalid_list_1))

# if make_total(invalid_list_1) == 1227775554:
#     print("Works")
# else:
#     print("failed part 1")

### Part 2
invalid_list_2 = list()
for itr in items:
    start = int(itr.split("-")[0])
    end = int(itr.split("-")[1])
    print("Range:",start,"-",end)
    new_invalids = find_invalid_ids(start, end)
    print(new_invalids)
    invalid_list_2 = invalid_list_2 + new_invalids
print("part 2 answer: ", make_total(invalid_list_2))

# if make_total(invalid_list_2) == 4174379265:
#        print("Works")
# else:
#     print("failed part 2") 