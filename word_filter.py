class WordFilter:
    def __init__(self, target):
        self.target = target

    def censor(self, sentence, converted_word):
        for i in range(0, len(self.target)):
            # if self.target[i] in sentence:   ←なくてもよさげ?
            sentence = sentence.replace(self.target[i], converted_word)
        return sentence


print("NGワードを設定してください")
print("NGワードを入力し終わったら、半角でeを入力してください")


def ng_word_list():
    fil = []
    counter = 1
    while True:
        ng_word = input(f"NGワード{counter} :")
        if ng_word == "e":
            break
        fil.append(ng_word)
        counter += 1
    return fil


repeat = "y"
while repeat.lower() == "y":
    my_filter = WordFilter(ng_word_list())
    print(my_filter.censor("昨日のアーセナルの試合は熱かった", "ピー"))
    print(my_filter.censor("昨日のリバプールの試合は熱かった", "ピー"))
    repeat = input("フィルタリングをし直しますか?(y/n)")
    if repeat.lower() == "n":
        break
