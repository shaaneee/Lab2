def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67)")

def calc_average(temp_list):
    if not temp_list:
        return 0.0
    return sum(temp_list) / len(temp_list)

def get_user_input():
    x = input()
    x = x.split(x, ",")
    x = sorted(x)
    return x
def find_min_max(temp_list):
    if not temp_list:
        return [None, None]
    return [min(temp_list), max(temp_list)]

def sort_temperature(temp_list):
    return sorted(temp_list)

def calc_median_temperature(temp_list):
    n = len(temp_list)
    if n == 0:
        return None
    sorted_list = sorted(temp_list)
    mid = n // 2
    if n % 2 == 0:
        # even length
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        # odd length
        return sorted_list[mid]