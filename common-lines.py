import sys

#If no file are given, your program must print some help,
#then exit with a return code greater than zero.
if len(sys.argv) < 2: sys.exit("no files given")
common_lines = open(sys.argv[1]).read().splitlines()
common_lines_found = False

for file in sys.argv[2:]:
    new_file = open(file).read().splitlines()

    compare_sets = set(common_lines) & set(new_file)

    if len(list(compare_sets)) > 0:
        common_lines_found = True
        common_lines = compare_sets
    else:
        common_lines_found = False
    

#If no lines are common between the given files, 
#your program must exit with an error code greater than zero.
if common_lines_found == False: sys.exit("no common lines found")
else:
    common_lines_found = False
    for line in common_lines:
        if len(line) > 0: 
            print(line)
            common_lines_found = True

if common_lines_found == False: sys.exit("no common lines found")
        # verify if empty line exit with a message
# you split on lines or individual words?
# https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
# splitlines()