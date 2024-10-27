
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


if 3 in set1:
  print("3 is in set1")




set3 = set1 | set2  
print("Union:", set3)


set4 = set1 & set2  
print("Intersection:", set4)


set5 = set1 - set2 
print("Difference:", set5)


set1.add(5)
print("Set1 after adding 5:", set1)

set1.remove(2)
print("Set1 after removing 2:", set1)




print("Is set2 a subset of set1?", set2.issubset(set1))
print("Is set1 a superset of set2?", set1.issuperset(set2))


print("Are set1 and set2 disjoint?", set1.isdisjoint(set2))

set1.clear()
print("Set1 after clearing:", set1)