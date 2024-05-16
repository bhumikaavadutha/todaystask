import argparse
parser = argparse.ArgumentParser(description='process some integers')

parser.add_argument('current_number', type=int)
parser.add_argument('previous_number', type=int)
args = parser.parse_args()
current_num = args.current_number
previous_num = args.previous_number

for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i
