with open('file.txt', 'rt', encoding='UTF8') as f:
    lines = f.readlines()
    lines.encode('utf-8').strip()

new_lines = []
for line in lines:
    if line.strip():
        new_lines.append(line)

with open('temp.txt', 'wt', encoding='UTF8') as f:
    f.encode('utf-8').strip()
    f.writelines(new_lines)