# Boilerplate code


def parse(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    return data


def solve(data):
    return data


if __name__ == '__main__':
    print(solve(parse('input.in')))