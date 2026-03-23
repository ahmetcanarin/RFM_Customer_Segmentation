# 📊 Customer Segmentation with RFM

---

## 🧩 Business Problem

FLO aims to segment its customers and develop targeted marketing strategies based on these segments.

To achieve this:
- Customer behaviors will be analyzed
- Customers will be grouped into clusters based on these behaviors

This approach enables more effective, data-driven decision-making in marketing activities.

---

## 📁 Dataset Story

The dataset consists of information derived from the past shopping behaviors of customers who made their most recent purchases in **2020–2021** via **OmniChannel** (both online and offline).

---

## 📌 Variables

| Variable | Description |
|----------|-------------|
| **master_id** | Unique customer ID |
| **order_channel** | The channel/platform used for shopping (Android, iOS, Desktop, Mobile, Offline) |
| **last_order_channel** | The channel where the most recent purchase was made |
| **first_order_date** | The date of the customer’s first purchase |
| **last_order_date** | The date of the customer’s most recent purchase |
| **last_order_date_online** | The date of the customer’s most recent online purchase |
| **last_order_date_offline** | The date of the customer’s most recent offline purchase |
| **order_num_total_ever_online** | Total number of online purchases |
| **order_num_total_ever_offline** | Total number of offline purchases |
| **customer_value_total_ever_offline** | Total amount spent on offline purchases |
| **customer_value_total_ever_online** | Total amount spent on online purchases |
| **interested_in_categories_12** | Categories shopped in during the last 12 months |

---

## 🎯 Project Objectives

- Segment customers using **RFM (Recency, Frequency, Monetary)** analysis  
- Identify key customer groups such as:
  - Champions
  - Loyal Customers
  - At Risk
  - New Customers  
- Generate actionable insights for marketing strategies  
- Support personalized campaign targeting  

---

## 🛠️ Methodology

- Data preprocessing and feature engineering  
- RFM metric calculation:
  - **Recency**
  - **Frequency**
  - **Monetary**
- Scoring and segmentation using RFM logic  
- Mapping segments for interpretability  

---

## 🚀 Expected Outcome

- Better understanding of customer behavior  
- Improved targeting in marketing campaigns  
- Increased customer retention and lifetime value  




