# prints the Reviews
with open('Result_Uber.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 != 0:
            print(line, end = '')