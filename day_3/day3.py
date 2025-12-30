with open("day3_values", 'r') as f:
    banks = f.readlines()
print(banks)

def get_total(total_bank):
    total_joltage = 0
    for itr in total_bank:
        total_joltage += int(itr)
    return total_joltage

### Part 1 
total_output_bank_1 = []
for battery_bank in banks:
    first_cell = battery_bank[0]
    second_cell = battery_bank[1]
    best_cell = first_cell + second_cell
    print("Starting with: ", best_cell) 
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