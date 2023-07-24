fhand = open('./example/py4e.com_code3_mbox-short.txt')

for line in fhand :
    line = line.rstrip()
    #print('Line :', line)
    wds = line.split()

    #print('words : ', wds)
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[1])

