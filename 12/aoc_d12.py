"""
--- Day 12: Digital Plumber ---
Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

You need to figure out how many programs are in the group that contains program ID 0.

For example, suppose you go door-to-door like a travelling salesman and record the following list:

0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
In this example, the following programs are in the group that contains program ID 0:

Program 0 by definition.
Program 2, directly connected to program 0.
Program 3 via program 2.
Program 4 via program 2.
Program 5 via programs 6, then 4, then 2.
Program 6 via programs 4, then 2.
Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

How many programs are in the group that contains program ID 0?

Your puzzle answer was 134.

--- Part Two ---
There are more programs than just the ones in the group containing program ID 0. The rest of them have no way of reaching that group, and still might have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either directly or indirectly. The programs you identified just a moment ago are all part of the same group. Now, they would like you to determine the total number of groups.

In the example above, there were 2 groups: one consisting of programs 0,2,3,4,5,6, and the other consisting solely of program 1.

How many groups are there in total?

Your puzzle answer was 193.

Both parts of this puzzle are complete! They provide two gold stars: **
"""
import pytest


def part1(pipes):
    programs = parse(pipes)

    group = make_group(programs, group=set([0]))

    return programs, group


def make_group(programs, group):
    for prog_left, programs_right in programs.items():
        # if the program on the left is already on the set of programs connected to group
        # then automatically we promote all the programs on the right hand side
        # to the set of programs connect to group
        if prog_left in group:
            group = group.union(programs_right)

        visited = set()

        def visit(p):
            group.add(p)
            if p in programs:
                visited.add(p)
                for p in programs[p]:
                    if p not in visited:
                        visit(p)

        # now for each program on the right hand side we visit it recursively
        # if it belongs to the set of programs connected to group
        for p in programs_right:
            if p in group:
                visit(p)
    return group


def parse(pipes):
    programs = {}

    for pipe in pipes:
        left, right = pipe.strip().split(' <-> ')

        prog_left = int(left)
        programs_right = [int(p) for p in right.split(', ')]
        programs[prog_left] = programs_right

    return programs


def part2(pipes):
    programs = parse(pipes)

    groups = []
    while programs:
        first_program = sorted(programs)[0]
        group_in = set([first_program])
        group_out = make_group(programs, group=group_in)
        groups.append(group_out)

        for p in group_out:
            del programs[p]

    return groups


@pytest.fixture
def contents():
    return """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".strip().split('\n')


def test_part1(contents):
    programs, zero = part1(contents)

    assert 6 == len(zero)

    assert [1] == [p for p in programs if p not in zero]


def test_part2(contents):
    assert 2 == len(part2(contents))


if __name__ == '__main__':
    _, zero = part1(open('input.txt').readlines())
    print(len(zero))

    groups = part2(open('input.txt').readlines())
    print(len(groups))
