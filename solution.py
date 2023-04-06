import pandas as pd
import numpy as np


chat_id = 729362937 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = (x+25)/10
    return x.mean() - 1
