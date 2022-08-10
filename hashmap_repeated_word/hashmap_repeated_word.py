from hashtable.hashtable import HashTable


def repeated_word(text):
    string = ""
    hash_map = HashTable()

    for char in text:
        char_lower = char.lower()
        if ord(char_lower) in range(ord("a"), ord("z") + 1):
            string += char_lower
        elif len(string):
            if hash_map.contains(string):
                return string
            else:
                hash_map.set(string, None)
                string = ""

    if len(string) and hash_map.contains(string):
        return string
    return None
