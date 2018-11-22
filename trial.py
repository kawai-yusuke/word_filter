class WordFilter:
    def __init__(self, target):
        self.target = target

    def censor(self, sentence, converted_word):
        for i in self.target:
            if i in sentence:
                sentence = sentence.replace(i, converted_word)
        return sentence


print("NGワードを設定してください")
print("NGワードを入力し終わったら、半角でeを入力してください")

fil = []


def ng_word_list():
    counter = 1
    while True:
        ng_word = input(f"NGワード{counter} :")
        if ng_word == "e":
            break
        fil.append(ng_word)
        counter += 1
    return fil


def sentence():
    my_sentence = input("フィルタリングしたい文章を入力してください> ")
    return my_sentence


def convert():
    conv_word = input("変換後のワードを入力してください> ")
    return conv_word


repeat = "y"
while repeat.lower() == "y":
    my_filter = WordFilter(ng_word_list())
    print(my_filter.censor(sentence(), convert()))
    repeat = input("フィルタリングをし直しますか?(y/n)")
    if repeat.lower() == "n":
        break
