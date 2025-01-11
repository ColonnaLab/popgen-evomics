import sys

# Check if a filename is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <replacement_pairs_file>")
    sys.exit(1)

replacement_pairs_file = sys.argv[1]

# Read replacement pairs from the provided file
replacement_pairs = {}
with open(replacement_pairs_file) as file:
    for line in file:
        source, target = line.strip().split('\t')
        replacement_pairs[source] = target

# Process the input stream
for line in sys.stdin:
    for source, target in replacement_pairs.items():
        line = line.replace(source, target)
    print(line, end='')