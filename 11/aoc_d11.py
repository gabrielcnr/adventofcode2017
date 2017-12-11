from collections import defaultdict

two_makes_zero = {
    'n': 's',
    's': 'n',

    'nw': 'se',
    'se': 'nw',

    'sw': 'ne',
    'ne': 'sw',
}

two_makes_one = {
    'n': {
        'sw': 'nw',
        'se': 'ne',
    },

    'ne': {
        'nw': 'n',
        's': 'se',
    },

    'se': {
        'n': 'ne',
        'sw': 's',
    },

    's': {
        'nw': 'sw',
        'ne': 'se',
    },

    'sw': {
        'n': 'nw',
        'se': 's',
    },

    'nw': {
        'ne': 'n',
        's': 'sw',
    }
}


def part1(steps):
    fewest_steps, furthest = _day11(steps)
    return fewest_steps


def part2(steps):
    fewest_steps, furthest = _day11(steps)
    return furthest


def _day11(steps):
    d = defaultdict(int)
    furthest = 0
    for step in steps:

        # First we try to null one existing step
        anti_step = two_makes_zero[step]
        if d[anti_step]:
            d[anti_step] -= 1

        else:

            d[step] += 1
            # Else we try to combine 2 steps into one
            for k in two_makes_one[step]:
                if d[k]:
                    d[step] -= 1
                    d[k] -= 1
                    d[two_makes_one[step][k]] += 1
                    break

        furthest = max(furthest, sum(d.values()))

    return sum(d.values()), furthest


def test_part1():
    assert 3 == part1(['ne', 'ne', 'ne'])

    assert 0 == part1(['ne', 'ne', 'sw', 'sw'])

    assert 2 == part1(['ne', 'ne', 's', 's'])

    assert 3 == part1(['se', 'sw', 'se', 'sw', 'sw'])


if __name__ == '__main__':
    with open('input.txt') as f:
        steps = [s.strip() for s in f.read().strip().split(',')]
        print(part1(steps))
        print(part2(steps))
