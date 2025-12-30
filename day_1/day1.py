#with open("day1_sample_values.txt", 'r') as f:
with open("day1_values", 'r') as f:
    instructions = f.readlines()
    #dial = list(map(int, f.read().replace('R', '').replace('L', '-').split()))
#print(instructions)
#print(dial)

### Part 1
curr_loc = 50
zero_count = 0
for ops in instructions:
    if ops[0] == "L":
        curr_loc -= int(ops[1:])
    else:
        curr_loc += int(ops[1:])
    if curr_loc % 100 == 0:
        zero_count += 1
print()
print("Count of zero lands is: ", zero_count)

## Part 2
curr_loc = 50
zero_count = 0 
#print("starting")
for ops in instructions:
    if ops[0] == "L":
        curr_loc -= int(ops[1:])
    else:
        curr_loc += int(ops[1:])
    #print("Location: ", curr_loc)
    #if curr_loc == 0:
        #zero_count += 1
    zero_count = zero_count + abs(curr_loc // 100)
    #print(zero_count)
    curr_loc = curr_loc % 100 
    #print("fixed: ", curr_loc)
print("Count of zero lands is: ", zero_count)