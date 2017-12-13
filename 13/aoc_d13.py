import collections

class Layer(object):
    def __init__(self, depth, range_, scanner):
        self.depth = depth
        self.range_ = range_
        self.scanner = scanner
        self.severity = depth * range_

    def move_scanner(self, packet_pos):
        """
        Moves the scanner and checks if it catches the packet.
        Returns True if it does, False otherwise.
        """
        self.scanner = (self.scanner + 1) % self.range_
        return packet_pos == self.depth and self.scanner == 0

    def __str__(self):
        return 'Layer<%s: %s>' % (self.depth, self.range_)

    __repr__ = __str__


def test_part1():
    input = '''
    0: 3
    1: 2
    4: 4
    6: 6
    '''

    layers = collections.OrderedDict()

    for line in input.strip().split('\n'):
        line = line.strip()

        if not line:
            continue

        depth, range_ = [int(n) for n in line.split(': ')]

        layers[depth] = Layer(depth=depth, range_=range_, scanner=0)

    packet_pos = 0

    final_layer = max(layers)

    layers_caught = []

    while packet_pos < final_layer:
        for layer_depth, layer in layers.items():
            if layer.move_scanner(packet_pos):
                layers_caught.append(layer)

        packet_pos += 1

    total_severity = sum(layer.severity for layer in layers_caught)

    # import pdb; pdb.set_trace()

    assert 24 == total_severity







