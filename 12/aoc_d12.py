def part1(pipes):
    programs = {}

    zero = set([0])

    for pipe in pipes:
        left, right = pipe.strip().split(' <-> ')

        prog_left = int(left)
        programs_right = [int(p) for p in right.split(', ')]
        programs[prog_left] = programs_right

        # if the program on the left is already on the set of programs connected to zero
        # then automatically we promote all the programs on the right hand side
        # to the set of programs connect to zero
        if prog_left in zero:
            zero = zero.union(programs_right)

        visited = set()

        def visit(p):
            zero.add(p)
            if p in programs:
                visited.add(p)
                for p in programs[p]:
                    if p not in visited:
                        visit(p)

        # now for each program on the right hand side we visit it recursively
        # if it belongs to the set of programs connected to zero
        for p in programs_right:
            if p in zero:
                visit(p)

    return programs, zero


def test_input():
    contents = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

    programs, zero = part1(contents.strip().split('\n'))

    assert 6 == len(zero)

    assert [1] == [p for p in programs if p not in zero]


if __name__ == '__main__':
    _, zero = part1(open('input.txt').readlines())
    print(len(zero))
