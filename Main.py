from Add import Add

t1 = ['▷', 0, 1, 1, 1, '☐']
t2 = ['▷', 0, 1, 0, 1, '☐']
work = ['▷', '☐', '☐']
out =  ['▷', '☐', '☐', '☐', '☐', '☐']

a = Add(t1, t2, work, out)
a.add()