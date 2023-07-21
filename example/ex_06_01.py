fhand = open('./example/py4e.com_code3_mbox-short.txt')

for line in fhand :
    line = line.rstrip()
    if line.startswith('This') :
        print(line)
