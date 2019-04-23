# coding: utf-8

import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like
import numpy as np

import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs
# from arch import arch_model

import matplotlib.pyplot as plt


# %matplotlib inline
# print('Machine:{} {}\n'.format(os.uname().sysname,os.uname().machine))
# print(sys.version)
# start = '2010-01-01'
# end = '2017-02-25'
# get_px = lambda x: web.get_data_yahoo(x, start=start, end=end)['Adj Close']
#
# symbols = ['SPY', 'TLT', 'MSFT']
#
# data = pd.DataFrame({sym:get_px(sym) for sym in symbols})
#
# Irets = np.log(data/data.shift(1)).dropna()

def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):  # 定义局部样式
        fig = plt.figure(figsize=figsize)
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))

        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)  # 自相关系数ACF图
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)  # 偏相关系数PACF图
        sm.qqplot(y, line='s', ax=qq_ax)  # QQ图检验是否是正太分布
        qq_ax.set_title('QQ Plot')
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
    return


np.random.seed(1)
randser = np.random.normal(size=1000)  # 高斯概率分布
tsplot(randser, lags=30)
