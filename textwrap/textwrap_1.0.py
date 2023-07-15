with open('A.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')
output = []
current_line = ""

for line in lines:
    words = line.split()
    for word in words:
        if len(current_line + " " + word) <= 55:
            current_line += " " + word
        else:
            output.append(current_line.strip())
            current_line = word
    output.append(current_line.strip())
    current_line = ""

with open('B.txt', 'w') as f:
    f.write('\n'.join(output))