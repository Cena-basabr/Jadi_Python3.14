input_1 = list(map(int, input().split()))
input_2 = list(map(int, input().split()))
merged_list = []
i = 0
j = 0

while i < len(input_1) and j < len(input_2):
    if input_1[i] < input_2[j]:
        merged_list.append(input_1[i])
        i = i + 1
    else:
        merged_list.append(input_2[j])
        j = j + 1
if i < len(input_1):
    merged_list.extend(input_1[i:])
if j < len(input_2):
    merged_list.extend(input_2[j:])

print("لیست نهایی :", merged_list)