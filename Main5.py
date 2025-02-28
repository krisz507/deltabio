with open("rosalind_gc.txt", "r") as file:
    data = file.read().strip()

max_gc = 0.0
max_id = ""

entries = data.split('>')[1:]

for entry in entries:
    lines = entry.split('\n')
    current_id = lines[0].strip()
    sequence = ''.join(lines[1:])
    gc = (sequence.count('G') + sequence.count('C'))
    total = len(sequence)
    if total == 0:
        continue
    
    gc_percent = (gc / total) * 100
    if gc_percent > max_gc:
        max_gc = gc_percent
        max_id = current_id

    print(f'{max_id}\n{max_gc}')
