class WordFilter():
    def __init__(self, target):
        self.target = target

    def detect(self, sentence):
        return self.target in sentence


my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！
