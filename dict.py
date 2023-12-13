def is_key_value_pair_in_list(key, value, dictionary_list):
    for dictionary in dictionary_list:
        if key in dictionary and dictionary[key] == value:
            return True
    return False


# example of dictionary
data = [
    {'Mary': 'English'},
    {'John': 'American'},
    {'Thomas': 'French'},
]

if __name__ == "__main__":
    key_dict = input("Enter the key to search: ")
    value_dict = input("Enter the value to search: ")

    print(is_key_value_pair_in_list(key_dict, value_dict, data))