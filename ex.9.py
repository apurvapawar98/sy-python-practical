marks = [98 , 96 , 88, 85, 99]

marks.append(87)
marks.remove(96)


marks[0]=86

print("updated mark list:",marks)
print("highest mark",max(marks))
print("average marks",sum(marks)/len(marks))