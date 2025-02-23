def tiggerfy(s):
    relevant_letters = []
    for i in s:
        if i in "tiger":
            relevant_letters.append(i)
        final_string = "".join(relevant_letters)
    return print(final_string)