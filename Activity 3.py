def count_words(sen):
    words = sen.split(" ")

    dict = {}

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    print("Word count")

    for key, value in dict.items():
        print(f"{key}: {value}")


def main():
    sen = count_words(input("Enter a sentence: ").lower())
    
main()


