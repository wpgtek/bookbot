def count_words(source:str) -> int:
    words = source.split()
    return len(words)

def count_letters(source:str) -> dict[str, int]:
    char_counts: dict[str, int] = {}
    for ch in source:
        lc = ch.lower()
        char_counts[lc] = char_counts.get(lc,0) + 1
    return char_counts

def _num_value(entry: dict[str,int]) -> int:
    return entry["num"]

def sort_dictionary(source: dict[str,int]) -> list[dict[str,int]]:
    sorted_list = [{"char":ch, "num":cnt} for ch,cnt in source.items()]
    sorted_list.sort(key=_num_value,reverse=True)

    return sorted_list