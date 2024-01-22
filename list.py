# family = ["Sanni", "Ajose", "Idowu", "Babafemi", "Adele"]
# family[0] = "Latteef"
#
# print(family[1:3])
# print(family)
#
luccky_numbers = [4,2,12,56,89,43]
family = ["Sanni", "Ajose", "Idowu", "Babafemi", "Adele"]
family.extend(luccky_numbers) # join 2 list
family.append("Obadina") # add an item
family.insert(1,"test") # add element in a specific index
family.remove("test") # remove element
# family.clear() # empty the array

print(family)