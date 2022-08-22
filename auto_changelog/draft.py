def is_part_in_list(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return True
    return False

ignore = ["merge", "attempt", "OMG"]
s = "Merge d"
print(is_part_in_list(s, ignore))
