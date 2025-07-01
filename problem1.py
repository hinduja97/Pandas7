import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    new_delivery=delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    new_perc=(len(new_delivery)/len(delivery) *100)
    print(round(new_perc,2))
    return pd.DataFrame({'immediate_percentage':[round(new_perc,2)]})