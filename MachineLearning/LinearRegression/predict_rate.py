"""
线性回归预测房价
"""
import pandas as pd
from sklearn import linear_model
from matplotlib import pyplot as plt


def get_data(file_name):
    """
    读取csv文件并转换返回数据
    """
    data = pd.read_csv(file_name)
    x_parameter = []
    y_parameter = []
    for single_square_feet, single_price in zip(data['square_feet'],
                                                data['price']):
        x_parameter.append([float(single_square_feet)])
        y_parameter.append(float(single_price))
    return x_parameter, y_parameter


def liner_modal_main(x_parameter, y_parameter, predice_value):
    """
    把数据拟合为线性回归模型
    """
    regr = linear_model.LinearRegression()  # 创建线性模型
    regr.fit(x_parameter, y_parameter)  # 训练
    predice_outcome = regr.predict(predice_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predice_outcome
    return predictions


def show_linear_line(x_parameter, y_parameter):
    """
    画线性回归线
    """
    regr = linear_model.LinearRegression()  # 创建线性模型
    regr.fit(x_parameter, y_parameter)  # 训练
    plt.scatter(x_parameter, y_parameter, color='blue')
    plt.plot(x_parameter, regr.predict(x_parameter), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def main():
    """
    主函数
    """
    x, y = get_data('./data/rate.csv')
    show_linear_line(x, y)
    predict_value = 700  # 预测的平方英尺
    result = liner_modal_main(x, y, predict_value)
    print("Intercept value ", result['intercept'])
    print("coefficient", result['coefficient'])
    print("Predicted value: ", result['predicted_value'])


main()
