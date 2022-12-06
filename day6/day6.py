
with open('day6/input.txt', 'r') as f:
    data = f.read()

n = 14
marker = ['0'] * n
for i in range(len(data)):
    marker[i % n] = data[i]
    if len(set(marker)) == n and ''.join(marker).isalpha():
        print(set(marker))
        print(i+1)
        break
