# Read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initialize two lists for the columns
column1 = []
column2 = []

# Split the lines and append to the respective lists
for line in lines:
    parts = line.split()
    column1.append(int(parts[0]))
    column2.append(int(parts[1]))
    
    
def calculate_difference(column1, column2):
    sum_of_diff = 0
    for a, b in zip(sorted(column1), sorted(column2)):
        sum_of_diff += abs(a - b)
    return sum_of_diff

sum_of_diff = calculate_difference(column1, column2)

print(sum_of_diff)

########

def calculate_similarity(column1, column2):
    similarity_sum = 0
    for num in column1:
        count_in_col2 = column2.count(num) 
        similarity_sum += num * count_in_col2 
    return similarity_sum

similarity = calculate_similarity(column1, column2)
print(similarity)
    
    
