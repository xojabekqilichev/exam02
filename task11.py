def analyze_list(items: list) -> dict:
    result = {'total':0, 'unique': 0, 'duplicate': [], 'most_common':None}
    result['total'] = len(items)
    result['unique'] = len(set(items))
    for i in items:
        if items.count(item) > 1 and item not in result['duplicates']:
            result['duplicates'].append(item)
    result['most_common'] = max(items, key=lambda x: x.count(item), default=None)
    return result
items = []
print(analyze_list(items))