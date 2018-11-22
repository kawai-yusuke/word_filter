class WordFilter:
    def __init__(self, filter):
        self.my_filter = filter

    def censor(self, my_filter):
        word_area = my_filter
        return word_area.replace(self.ng_word(), self.ng_word_hit())

    def ng_word(self):
        word = input("｢NGワードを入力してください｣　入力:")
        return word

    def ng_word_hit(self):
        word_hit = input("｢NGワードにヒットしたときの表示文字を設定してください｣　入力:")
        return word_hit


ng_list = []
my_filter = WordFilter(filter)
print(my_filter.censor("昨日のアーセナルの試合アツかった！"))
print(my_filter.censor("昨日のリバプールの試合アツかった！"))
