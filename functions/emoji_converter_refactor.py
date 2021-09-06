def get_emoji(raw_emoji):
    emojis= {
        ":)": "😊",
        ":(": "😕"
    }
    return emojis.get(raw_emoji, raw_emoji)


words = input()
converted = ""
for w in words.split(' '):
    converted = converted + get_emoji(w) + " "

print(converted)