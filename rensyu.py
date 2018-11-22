class WordFilter():
    # def __init__(self, target):
    #     self.target = target

    def censor(self, sentence, converted_word):
        self.sentence = sentence
        self.converted_word = converted_word
        while True:
            ng_word = input("NGワードを入力してください> ")
            if ng_word == "e":
                break
            self.sentence = self.sentence.replace(ng_word, converted_word)
        return self.sentence


# def fil():
#     fil_list = []
#     while True:
#         ng_word = input("NGワードを入力してください> ")
#         fil_list.append(ng_word)
#         if ng_word == "e":
#             break
#     return fil_list

repeat = "y"
while repeat.lower() == "y":
    my_filter = WordFilter()
    print(my_filter.censor("昨日のアーセナルの試合は熱かった", "ピー"))
    # print(my_filter.censor("昨日のリバプールの試合は熱かった", "ピー"))
    repeat = input("フィルタリングをし直しますか?(y/n)")
    if repeat.lower() == "n":
        break
