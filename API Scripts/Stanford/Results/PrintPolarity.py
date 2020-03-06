# prints the Reviews
with open('Result_Restaurant.txt', 'r') as f:
    count = 0
    for line in f:
        count+=1
        if count % 2 != 0:
            with open ('Result_Restaurant_Polarity.txt', 'a') as f:
                f.write(line)
