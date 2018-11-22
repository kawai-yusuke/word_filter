class WordFilter():
    def __init__(self, target):
        self.target = target

    def censor(self, sentence, converted_word):
        self.sentence = sentence
        self.converted_word = converted_word
        while True:
            ng_word = input("NGワードを入力してください> ")
            if ng_word == "e":
                break
        for i in self.target:
            self.sentence = self.sentence.replace(i, converted_word)
        return self.sentence


def fil():
    fil_list = []
    while True:
        ng_word = input("NGワードを入力してください> ")
        fil_list.append(ng_word)
        if ng_word == "e":
            break
    return fil_list


my_filter = WordFilter(fil())

print(my_filter.censor("昨日のアーセナルの試合アツかった！", "うんこ"))

print(my_filter.censor("昨日のリバプールの試合アツかった！", "うんこ"))
