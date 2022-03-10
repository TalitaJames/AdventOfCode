def parse(file):
    with open(file, 'r') as f:
        data = [line for line in f.read().splitlines()]
    return data


def solve(data):
    sum = 0

    #FIXME: Prints as 1389, but the answer is 1390, logic error somewhere in the loop
    for i in range(1,len(data)):
        if data[i] > data[i-1]:
            sum+=1

 
    return sum



print(solve(parse('input.txt')))
print("------------------------ Solution")