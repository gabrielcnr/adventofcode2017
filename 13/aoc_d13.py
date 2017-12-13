import collections

up = lambda x: x - 1
down = lambda x: x + 1

class Layer(object):
    def __init__(self, depth, range_, scanner):
        self.depth = depth
        self.range_ = range_
        self.scanner = scanner
        self.severity = depth * range_
        self.direction = up

    def move_scanner(self, packet_pos):
        """
        Moves the scanner and checks if it catches the packet.
        Returns True if it does, False otherwise.
        """
        caught = packet_pos == self.depth and self.scanner == 0

        # check if we need to flip the direction
        if self.scanner == (self.range_ - 1):
            self.direction = up
        elif self.scanner == 0:
            self.direction = down

        self.scanner = self.direction(self.scanner)
        return caught

    def __str__(self):
        return 'Layer<%s: %s>' % (self.depth, self.range_)

    __repr__ = __str__


def test_part1():
    input = '''
    0: 3
    1: 2
    4: 4
    6: 4
    '''

    total_severity = part1(input)

    assert 24 == total_severity


def part1(input):
    layers = collections.OrderedDict()
    for line in input.strip().split('\n'):
        line = line.strip()

        if not line:
            continue

        depth, range_ = [int(n) for n in line.split(': ')]

        layers[depth] = Layer(depth=depth, range_=range_, scanner=0)
    packet_pos = -1
    final_layer = max(layers)
    layers_caught = []
    while packet_pos < final_layer:
        packet_pos += 1

        for layer_depth, layer in layers.items():
            if layer.move_scanner(packet_pos):
                layers_caught.append(layer)
    total_severity = sum(layer.severity for layer in layers_caught)
    return total_severity


if __name__ == '__main__':
    with open('input.txt') as f:
        contents = f.read()
    print('part1', part1(contents))





