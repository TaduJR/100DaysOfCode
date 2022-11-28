def set_list(list):
  list = ["A", "B", "C"]
  return list

def add(list):
	list.append("D")
	return list

my_list = ["E"]

print(my_list)
print(set_list(my_list))


print(my_list)
print(add(my_list))
print(my_list)
