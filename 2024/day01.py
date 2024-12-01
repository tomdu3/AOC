# get the input from the file
with open("input01.txt") as f:
    in_put = f.read()
left, right = [], []
for i in in_put.split('\n'):
    if i:
        row = i.split()
        left.append(int(row[0]))
        right.append(int(row[1]))
        left.sort()
        right.sort()

# First part -- calculat sum of distances
sum_distances=0
for i, j in zip(left,right):
    distance = abs(i-j)
    sum_distances += distance
print(f'Sum of distances: {sum_distances}')

# Second part - calculate the similarity score
similarity_score = 0
for (i,j) in zip(left,right):
    occurences = right.count(i)
    similarity_score += occurences*i
print(f'Similarity score: {similarity_score}')
