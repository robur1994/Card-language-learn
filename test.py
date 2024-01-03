import pandas as pd
import random


def random_words():
    data = pd.read_csv("data/french_words.csv")
    data_dict = pd.DataFrame.to_dict(data, orient="records")
    print(data_dict[random.randint(0, 102)]["French"])

random_words()