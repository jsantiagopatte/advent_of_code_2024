
# Import rules
file_rules = open('input_day5_rules.txt', 'r')
rules_list = []
for line in file_rules:
    rules_list.append(line.strip().split('|'))

# Import prints
file_prints = open('input_day5_prints.txt', 'r')
prints_list = []
for line in file_prints:
    prints_list.append(line.strip().split(','))
# Create rules dict
pass
# Loop through prints