def get_num_words(text):
    return len(text.split())

def count_chars(text):
    result = {}
    for char in text.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    result = []
    for key in dict:
        result.append({"char":key, "num":dict[key]})
    result.sort(reverse=True, key=sort_on)
    return result

