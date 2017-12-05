def part1():
    with open('input_05.txt') as f:
        contents = [int(s.strip()) for s in f]

    pos = 0
    it = 0

    while True:

        try:
            value = contents[pos]
        except IndexError as ex:
            return it

        contents[pos] = value + 1

        pos += value

        it += 1


if __name__ == '__main__':
    print(part1())
