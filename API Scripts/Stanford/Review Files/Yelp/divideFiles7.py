ds1 = "Amazon_Reviews"
ds2 = "IMDB_Reviews"
ds4 = "Uber_Ride_Reviews"
ds5 = "Yelp_Reviews"

# prints the Reviews
with open(ds5 + '.txt', 'r') as f:
    count = 0
    n = 0
    for line in f:
        count+=1
        if count > 601 and count <= 701:
            print(line, end='')
