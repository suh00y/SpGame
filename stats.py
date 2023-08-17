class Stats():
    #отслеживание статистики

    def __init__(self):
        self.reset_stats()
        self.run_game=True
        with open("highscore.txt",'r') as f:
            self.hight_score=int(f.readline())


    def reset_stats(self):
        #статистика имзменяющая во время игры
        self.guns_left=3
        self.score=0

