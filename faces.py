# Get input
emoticon_to_emoji = {
    ":-)": "🙂", ": )": "🙂", ":)": "🙂", ":-(": "🙁", ":(": "🙁", ": (": "🙁"}

user_input = input()

# Correct emoticon to emoji
for emoticon in sorted(emoticon_to_emoji):
    user_input = user_input.replace(emoticon, emoticon_to_emoji[emoticon])

print(user_input)
