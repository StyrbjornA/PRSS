num_list = [1, 5, 4, 2, 7, 4, 8, 5]
iterations = 5


def expand(original_list):
    last_digit = original_list.pop()
    end_index = 0
    for index in range(0, len(original_list)):
        if original_list[index] < last_digit:
            end_index = index
    return original_list + original_list[end_index:] * 2


for i in range(0, iterations):
    num_list = expand(num_list)

print(num_list)

