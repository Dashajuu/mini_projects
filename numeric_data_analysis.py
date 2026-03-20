num_list = input('Write:').split(',')
num_list = list(map(int, num_list))


def get_list_length(nums_list):
    return len(nums_list)


def get_min_element(nums_list):
    return min(nums_list)


def get_max_element(nums_list):
    return max(nums_list)


def calculate_average(nums_list):
    return sum(nums_list) / len(nums_list)


def count_numbers_frequency(nums_list):
    nums_dict = {}

    for i in nums_list:
        if i in nums_dict:
            nums_dict[i] += 1
        else:
            nums_dict[i] = 1

    return nums_dict


def get_most_frequent_element(freq_dict):
    target_value = max(freq_dict.values())

    for key, value in freq_dict.items():
        if value == target_value:
            return key

    return None


def get_unique_elements(nums_list):
    return set(nums_list)


def has_duplicates(nums_list):
    return True if len(nums_list) != len(set(nums_list)) else False


def sort_numbers(nums_list):
    return sorted(nums_list)


def get_top_3_frequent(freq_dict):
    top_list = []

    for key, value in freq_dict.items():
        top_list.append((key, value))

    top_list.sort(key=lambda x: x[1], reverse=True)

    return top_list[:3]


def main():
    print("Список:", num_list)
    print("Количество:", get_list_length(num_list))
    print("Минимум:", get_min_element(num_list))
    print("Максимум:", get_max_element(num_list))
    print("Среднее:", calculate_average(num_list))

    freq = count_numbers_frequency(num_list)

    print("\nЧастота чисел:", freq)
    print("Самое частое:", get_most_frequent_element(freq))
    print("Уникальные:", get_unique_elements(num_list))
    print("Есть ли дубликаты:", has_duplicates(num_list))
    print("Отсортированный список:", sort_numbers(num_list))
    print("Топ-3 по частоте:", get_top_3_frequent(freq))


if __name__ == "__main__":
    main()


