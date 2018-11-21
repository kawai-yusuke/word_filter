class WordFilter():
    def __init__(self, target):
        self.target = target

    def detect(self, sentence):
        return self.target in sentence

    def censor(self, sentence):
        self.sentence = sentence
        conversion = self.sentence.replace(self.target, "<consored>")
        return conversion



my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！

# NGワードが含まれている場合
my_filter.censor("昨日のアーセナルの試合アツかった！")  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.censor("昨日のリバプールの試合アツかった！")  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！
