########################################################### Term 3 Week 7
DATAFILE = "unit-patterns.txt"
def t1q1():
    units = open(DATAFILE)

    # print(units.readline()) prints first line
    # print(units.readline()) prints second line

    for row in range(5):
        print(units.readline())
    units.close()
    
def t1q2():
    units = open(DATAFILE)

    pattern_strings = []
    for line in units:
        pattern_strings.append(line)

    print(pattern_strings[:5])
    ## t2q1
    for row in range(len(pattern_strings)):
        pattern_strings[row] = pattern_strings[row].partition('\t')[0]

    print(pattern_strings[:5])
    units.close()
   
def t2q3():
    units = open(DATAFILE)

    pattern_strings = []
    for line in units:
        pattern_strings.append(line)

    print(pattern_strings[:5])
    ## t2q1
    for row in range(len(pattern_strings)):
        pattern_strings[row] = pattern_strings[row].partition('\t')[0]

    print(pattern_strings[:5])
    
def t2q4():
    units = open(DATAFILE)

    pattern_strings = []
    for line in units:
        pattern_strings.append(line)
    #t2q1
    for row in range(len(pattern_strings)):
        pattern_strings[row] = pattern_strings[row].partition('\t')[0]
    #t2q3
    pattern_lists = []
    for row in range(len(pattern_strings)):
        pattern_lists.append(pattern_strings[row].split('+'))
    #t2q4
    for row in range(len(pattern_lists)): #Every row
        for unit in range(len(pattern_lists[row])):# Every Element
            pattern_lists[row][unit] = pattern_lists[row][unit].strip()
    print(pattern_lists[:5])


def get_patterns(filename):
    pattern_strings = []

    with open(filename, 'r') as file:
        for line in file:
            pattern_strings.append(line.partition('\t')[0])

    pattern_lists = []
    for row in range(len(pattern_strings)):
        pattern_lists.append(pattern_strings[row].split('+'))
        for unit in range(len(pattern_lists[row])):# Every Element
            pattern_lists[row][unit] = pattern_lists[row][unit].strip()
    return(pattern_lists)


def print_patterns (patterns, numlines):
    units = patterns
    for row in range(numlines):
        print(units[row])

def sort_patterns(unit_data):
    final = []
    for row in unit_data:
        final.append(sorted(row))
    sorted_units = sorted(final)
    return sorted_units

def remove_duplicates(patterns):
    unique_list = []
    for unit_pattern in patterns:
        if unit_pattern in unique_list:
            continue
        else:
            unique_list.append(unit_pattern)
    return unique_list

def get_unique_patterns (patterns):
    unique_patterns = remove_duplicates(sort_patterns(patterns))
    num_patterns = len(unique_patterns)
    return unique_patterns, num_patterns


def final(filename):
    return get_unique_patterns(get_patterns(filename))
