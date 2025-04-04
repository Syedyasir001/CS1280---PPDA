def merge_dictionaries():
    dict1 = eval(input("Enter first dictionary: "))
    dict2 = eval(input("Enter second dictionary: "))

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    print(f"\nMerged Dictionary: {merged_dict}")

merge_dictionaries()
