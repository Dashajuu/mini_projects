text = "This is a simple example text. It is used to demonstrate how word frequency analysis works. The text contains repeated words, and some words appear more often than others."


def remove_punctuation(txt):
    punctuation_list = [',', '.', ':', ';', '-']

    words = txt.lower().split(' ')
    cleaned_text = []

    for word in words:
        for p in punctuation_list:
            word = word.replace(p, '')
        cleaned_text.append(word)

    return cleaned_text


def count_words(txt):
    words_dict = {}

    for i in txt:
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1

    return words_dict


def sort_dict_count_words(dct):
    return sorted(dct.items(), key=lambda x: x[1], reverse=True)


def count_general_words(txt_list):
    return len(txt_list)


def get_top_3_frequent(freq_dict):
    top_list = []

    for key, value in freq_dict.items():
        top_list.append((key, value))

    top_list.sort(key=lambda x: x[1], reverse=True)

    return top_list[:3]


def main():
    text_list = remove_punctuation(text)

    print('Всего слов:', count_general_words(text_list))

    text_dict = count_words(text_list)

    print('Частота слов:', sort_dict_count_words(text_dict))
    print('Топ-3 слова:', get_top_3_frequent(text_dict))


if __name__ == '__main__':
    main()