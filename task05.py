def count_words(text: str) -> dict:
    result = {}
    words = text.split()
    for i in words:
        result[i] = words.count(i)
    return result
text = 'salom salom dunyo'
print(count_words(text=text))