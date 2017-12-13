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


def get_scanner_pos(counter, depth):
    """Get the index of scanner, given the counter time and layer depth."""
    remainder = counter / 2 * (depth - 1)
    if remainder > depth:
        return 2 * depth - remainder
    return remainder



def part2(input):
    """
    The scanner will be in pos0 every range*2 picoseconds, and the pkg will be 
    at layer[depth] after exactly [depth] picoseconds. Thus we can find out the smallest delay such that
    for each layer, delay + depth != n * (range-1) * 2, where n can be any number.

    This works for the given example. If delay = 0, delay + depth of layer 0 = 0 + 0 = n * (3-1) * 2 = 0 -> we hit first layer. 
    If delay = 1, we hit the scanner in layer at depth 1. (1 + 1 = n * (2-1) * 2)
    If delay = 2, we hit layer d=4  (2 + 4 = n * (4 - 1) * 2)
    If delay = 3, we hit .... this goes on trust me.
    The first number we reach that doesn't have any constraints is 10.

    Mathematically
    let x to be our desired number, let k = number of layers - 1 
    and let a0, a1, ... be respectively, 2*(layer d0.range - 1), 2*(layer d1.range -1) ...,
    
    Then we have

    x + 0 not a multiple of a0
    x + 1 not a multiple of a1
    ...
    x + k not a multiple ak
    """
    counter = 0
    pkg_pos = -1
    layers = {}

    for line in input.strip().split('\n'):
        
        if not line:
            continue
        
        depth, range_ = [int(n) for n in line.split(': ')]
        layers[depth] = 2 * (range_ - 1)

    found = False
    delay = 0
    while not found:
        # Check the delay for the constraints
        found = True
        for depth, check in layers.items():
            if (delay + depth) % check == 0:
                # Wrong delay, hit this layer
                found = False
                delay += 1
                break
    return delay    
            

if __name__ == '__main__':
    with open('input.txt') as f:
        contents = f.read()
    print('part1', part1(contents))
    print('part2', part2(contents))




