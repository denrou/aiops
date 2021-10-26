from prophet import Prophet


def predict(data):
    m = (
        Prophet(
            weekly_seasonality=False, yearly_seasonality=False, daily_seasonality=False
        )
        .add_seasonality(name="minutely", period=1 / (24 * 60), fourier_order=5)
        .fit(data)
    )
    future = m.make_future_dataframe(periods=600, freq="S", include_history=False)
    forecast = m.predict(future)
    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
