# numbers from 0..255
numbers = list(range(256))
print(len(numbers))

# current position
pos = 0

skip = 0

# puzzle input
lengths = [83, 0, 193, 1, 254, 237, 187, 40, 88, 27, 2, 255, 149, 29, 42, 100]


# test data
# numbers = [0, 1, 2, 3, 4]
# lengths = [3, 4, 1, 5]

for length in lengths:
    if length > 1:
        end_pos = pos + length
        if end_pos > len(numbers):
            second_end_pos = end_pos % len(numbers)
            numbers_subset = numbers[pos:] + numbers[:second_end_pos]
        else:
            numbers_subset = numbers[pos:end_pos]

        reversed_numbers = list(reversed(numbers_subset))

        if end_pos > len(numbers):
            second_end_pos = end_pos % len(numbers)

            numbers = reversed_numbers[-second_end_pos:] + numbers[second_end_pos:pos]  + reversed_numbers[:-second_end_pos]
        else:
            numbers[pos:end_pos] = reversed_numbers

    pos = (pos + length + skip) % len(numbers)

    skip += 1

    # print(numbers)
    # print('pos ', pos)
    # print('skip', skip)
    #
    # print('\n')

print(numbers)
print(numbers[0] * numbers[1])
print(len(numbers))