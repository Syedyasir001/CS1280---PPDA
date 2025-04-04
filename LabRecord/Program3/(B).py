def merge_dictionaries():
    dict1 = eval(input("Enter first dictionary: "))
    dict2 = eval(input("Enter second dictionary: "))

    merged_dict = {**dict1, **dict2}

    print(f"\nMerged Dictionary: {merged_dict}")

merge_dictionaries()
