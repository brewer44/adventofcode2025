with open("day3_values", 'r') as f:
    banks = f.read().split()

def get_total(total_bank):
    total_joltage = 0
    for itr in total_bank:
        total_joltage += int(itr)
    return total_joltage

def best_option(battery_options, count_opts):
    result = ''
    for skip in range(count_opts-1, -1, -1):
        joule_count = battery_options.index(max(battery_options[:len(battery_options)-skip]))
        result += battery_options[joule_count]
        battery_options = battery_options[joule_count+1:]
    return int(result)

def maxj(s, k):
    r = ''
    for skip in range(k-1, -1, -1):
        j = s.index(max(s[:len(s)-skip]))
        r, s = r + s[j], s[j+1:]
    return int(r)

### Part 1 
total_output_bank_1 = []
for battery_bank in banks:
    first_cell = battery_bank[0]
    second_cell = battery_bank[1]
    best_cell = first_cell + second_cell
    for cell in battery_bank[2:]:
        test_1 = first_cell + cell
        test_2 = second_cell + cell
        if int(test_1) >= int(test_2):
            if int(best_cell) < int(test_1):
                second_cell = cell
                best_cell = first_cell + second_cell
        else:
            if int(best_cell) < int(test_2):
                first_cell = second_cell
                second_cell = cell
                best_cell = first_cell + second_cell
    total_output_bank_1.append(int(best_cell))
print("Part 1: ", get_total(total_output_bank_1))

### Part 2
total_output_bank_2 = []
for battery_bank in banks:
    total_output_bank_2.append(best_option(battery_bank,12))
result_2 = sum(tuple(total_output_bank_2))
print("Answer Part 2: ", result_2)