def parse(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    return data


def solve(data):
    sum=0
    for i in data:
        if data[i+2] > data[i+1]:
            sum+=1
    
    print(sum)
    return str(sum)



print(solve(parse('input.txt')))