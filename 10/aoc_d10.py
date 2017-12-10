# numbers from 0..255
numbers = range(256)

# current position
pos = 0

skip = 0

# puzzle input
lengths = [83, 0, 193, 1, 254, 237, 187, 40, 88, 27, 2, 255, 149, 29, 42, 100]


# test data
numbers = [0, 1, 2, 3, 4]
lengths = [3, 4, 1, 5]

for length in lengths:
    numbers_subset = numbers[pos:pos+length]

    reversed_numbers = list(reversed(numbers_subset))

    numbers = reversed_numbers + numbers[pos+length:]

    pos = (pos + length + skip) % len(numbers)

    skip += 1

    print(numbers)

