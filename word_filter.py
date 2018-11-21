class WordFilter():
    def __init__(self, target):
        self.target = target

    def detect(self, sentence):
        return self.target in sentence

    def censor(self, sentence, converted_word):
        self.sentence = sentence
        self.converted_word = converted_word
        conversion = self.sentence.replace(self.target, self.converted_word)
        return conversion



my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！

# NGワードが含まれている場合
my_filter.censor("昨日のアーセナルの試合アツかった！", "<bad word>")  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.censor("昨日のリバプールの試合アツかった！", "<negative word>")  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！
