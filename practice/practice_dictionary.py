score = {'english' : 99, 'math' : 100, 'chinese' : 95}
print(score)

pack = dict()
pack['class'] = 5
pack['language'] = 4
pack['class'] += 1
print(pack)
'class' in pack

counts = dict()
names = ['hyejin', 'sungsoo', 'hyejin', 'sejun', 'yonghao', 'sungsoo', 'hyejin']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# get() 메서드
