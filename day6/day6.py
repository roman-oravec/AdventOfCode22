
with open('day6/input.txt', 'r') as f:
    data = f.read()


marker = ['0'] * 4
for i in range(len(data)):
    marker[i % 4] = data[i]
    if len(set(marker)) == 4 and ''.join(marker).isalpha():
        print(set(marker))
        print(i+1)
        break
