def main(text):
    ignoring_next = False
    inside_garbage = False

    group_stack = []

    total = 0
    for c in text:
        if ignoring_next:
            ignoring_next = False
        elif c == "!":
            ignoring_next = True
        elif inside_garbage:
            if c == '>':
                inside_garbage = False
        elif c == '<':
            inside_garbage = True
        elif c == '{':
            group_stack.append(1)
        elif c == '}':
            total += len(group_stack)
            group_stack.pop()
        elif c == ',':
            pass
        else:
            import pdb;
            pdb.set_trace()

    return total


def test_it():
    assert main('{}') == 1
    assert main('{{{}}}') == 6
    assert main('{{},{}}') == 5
    assert main('{{{},{},{{}}}}') == 16
    assert main('{<a>,<a>,<a>,<a>}') == 1
    assert main('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert main('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert main('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


if __name__ == '__main__':
    print(main(open('input.txt').read().strip()))
