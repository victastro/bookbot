def get_num_words(text):
    count = len(text.split())
    return count

def get_symbol_counts(text):
    counts = {}
    for c in text.lower():
        try:
            cc = counts[c]
            counts[c] = cc + 1
        except:
            counts[c] = 1
    return counts


def get_count(element):
    return element["count"]

def get_counts_list(symbol_counts):
    counts_list = [{ "symbol" : s, "count" : symbol_counts[s]} for s in symbol_counts]
    counts_list.sort(key=get_count, reverse=True)
    return counts_list

