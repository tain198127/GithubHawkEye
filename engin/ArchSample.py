try:
    import seaborn
except ImportError:
    pass
import datetime as dt

st = dt.datetime(1990, 1, 1)
en = dt.datetime(2015, 6, 30)
data = DataAPI.MktEqudGet(secID=u"", ticker=u"000001", tradeDate=u"", beginDate=u"", endDate=u"",
                          field=u"ticker,secShortName,tradeDate,closePrice,PE", pandas="1")
# data.index = data.tradeDate
returns = 100 * data['closePrice'].pct_change().dropna()
figure = returns.plot(figsize=(20, 6))
