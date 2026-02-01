def count_words(text: str) -> dict:
    result = {}
    for txt in text:
        result[txt].lower() == text.count(txt).lower()
    return result

text = 'salom salom dunyo'
result = count_words(text=text)
print(result)