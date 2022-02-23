fruit_list = ["banana", "apple", "orange", "grape", "strawberry"]
new_fruit_list = [fruit for fruit in fruit_list if fruit != "orange"]
print(new_fruit_list)
new_fruit_list = [fruit for fruit in fruit_list]
print(new_fruit_list)
new_fruit_list = [fruit for fruit in fruit_list]
new_fruit_list.append("orange")
print(new_fruit_list)

