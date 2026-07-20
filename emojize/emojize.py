import emoji
user_input = input("Input: ")
output_text = emoji.emojize(user_input, language="alias")
print(f"Output: {output_text}")


