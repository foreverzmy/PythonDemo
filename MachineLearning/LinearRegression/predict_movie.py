"""
线性回归预测美剧观众
"""
import pandas as pd
from sklearn import linear_model

# from matplotlib import pyplot as plt


def get_data(file_name):
    """
    读取csv文件并转换返回数据
    """
    data = pd.read_csv(file_name)
    flash_viewers = []
    arrow_viewers = []
    idxs = []
    for idx, flash, arrow in zip(data.index, data['flash'], data['arrow']):
        idxs.append([float(idx)])
        flash_viewers.append(float(flash))
        arrow_viewers.append(float(arrow))
    return idxs, flash_viewers, arrow_viewers


def movie_viewers(idxs, views):
    regr = linear_model.LinearRegression()
    regr.fit(idxs, views)
    predicted_value = regr.predict(9)
    return predicted_value


def main():
    idxs, flash, arrow = get_data('./data/movies.csv')
    flash_viewers = movie_viewers(idxs, flash)
    arrow_viewers = movie_viewers(idxs, arrow)
    if flash_viewers > arrow_viewers:
        print("The Flash Tv Show will have more viewers for next week")
    else:
        print("Arrow Tv Show will have more viewers for next week")


main()
