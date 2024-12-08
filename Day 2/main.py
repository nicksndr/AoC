with open('example.txt', 'r') as file:
    lines = file.readlines()
    
# Function to check if a row is strictly increasing or decreasing
def is_monotonic_and_safe(row):
    increasing = all(row[i] <= row[i + 1] for i in range(len(row) - 1))
    decreasing = all(row[i] >= row[i + 1] for i in range(len(row) - 1))
    
    if increasing or decreasing:
        safe = all(1 <= abs(row[i + 1] - row[i]) <= 3 for i in range(len(row) - 1))
        return safe
    else:
        return False

# def is_safe(row, direction):
#     if(direction = increasing):
        

results = []
for line in lines:
    row = list(map(int, line.split()))
    results.append(is_monotonic_and_safe(row))
    
print(results.count(True))