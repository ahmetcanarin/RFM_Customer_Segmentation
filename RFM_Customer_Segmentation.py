#####################################
# Data Preparation and Understanding
#####################################

import numpy as np
import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_csv("flo_data_20k.csv")
df = df_.copy()

df.head(10)
df.columns
df.shape
df.describe().T
df.isnull().sum()
df.info()


df["total_order_num"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]


df.info()

date_columns = df.columns[df.columns.str.contains("date")]
df[date_columns] = df[date_columns].apply(pd.to_datetime)


df.groupby("order_channel").agg({"master_id": lambda x: x.nunique(),
                                 "total_order_num": lambda x: x.sum(),
                                 "total_customer_value": lambda x: x.sum()})


df["total_customer_value"].sort_values(ascending=False).head(10)
df["total_order_num"].sort_values(ascending=False).head(10)


################################
# Calculating the RFM metrics
################################

df["last_order_date"].max()

type(df["last_order_date"].max())

today_date = df["last_order_date"].max() + dt.timedelta(days=2)


# Creating a new rfm dataframe with customer_id, recency, frequency and monetary

rfm = df.groupby("master_id").agg({"last_order_date": lambda x: (today_date - x.max()).days,
                                   "total_order_num": lambda x: x.nunique(),
                                   "total_customer_value": lambda x: x.sum()}).reset_index()

rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

rfm.isnull().sum()


#####################################
# Calculating RF and RFM Scores
#####################################

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])

rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])

rfm.info()

rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))


###############################################################
# Describing RF Scores as Segments
###############################################################

# Creation of segment definitions to make the generated RFM scores more interpretable, and converting the RF_SCORE into segments using the defined seg_map.

seg_map = {r"[1-2][1-2]": "hibernating",
           r"[1-2][3-4]": "at_risk",
           r"[1-2]5": "cant_loose",
           r"3[1-2]": "about_to_sleep",
           r"33": "need_attention",
           r"[3-4][4-5]": "loyal_customers",
           r"41": "promising",
           r"51": "new_customers",
           r"[4-5][2-3]": "potential_loyalists",
           r"5[4-5]": "champions"}

rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)


rfm[["segment","recency", "frequency", "monetary"]].groupby("segment").agg("mean")



# CASE 1:
# FLO is adding a new women’s shoe brand to its portfolio. The product prices of this brand are above general customer preferences.
# Therefore, it is intended to communicate specifically with customers who have a profile likely to be interested in the brand for promotion and product sales.
# These customers are planned to be loyal and to have shopped in the women’s category. Save the customer ID numbers to a CSV file as new_brand_target_customer_id.csv.

df1 = rfm[rfm["segment"].isin(["loyal_customers", "champions"])]["customer_id"]
df_ids = df[(df["master_id"].isin(df1)) & (df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]

df_ids.to_csv("new_brand_target_customer_id.csv", index=False)


# CASE 2:
# A discount of nearly 40% is planned for men’s and children’s products.
# With this discount, it is intended to specifically target customers who are interested in these categories,
# were previously good customers but have not made purchases for a long time, as well as newly acquired customers.
# Save the IDs of customers with the appropriate profile to a CSV file as discount_target_customer_id.csv.

segment_ids = rfm[rfm["segment"].isin(["at_risk", "cant_loose", "new_customers"])]["customer_id"]
customer_ids = df[(df["master_id"].isin(segment_ids)) & (df["interested_in_categories_12"].str.contains("ERKEK | COCUK"))]["master_id"]

customer_ids.to_csv("discount_target_customer_id.csv", index=False)








