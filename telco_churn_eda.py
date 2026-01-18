# 1️⃣ استدعاء المكتبات
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2️⃣ قراءة البيانات (تأكدي أن الملف في نفس المجلد)
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# 3️⃣ معلومات عامة عن البيانات
print("شكل البيانات قبل التنظيف:", data.shape)
print(data.info())
print("عدد القيم الفارغة لكل عمود:\n", data.isnull().sum())

# 4️⃣ تنظيف عمود TotalCharges
data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors='coerce')
data["TotalCharges"].fillna(data["TotalCharges"].mean(), inplace=True)

# 5️⃣ إزالة الصفوف المكررة
data.drop_duplicates(inplace=True)

# 6️⃣ حذف الأعمدة غير المهمة
data.drop("customerID", axis=1, inplace=True)

# 7️⃣ التحقق بعد التنظيف
print("شكل البيانات بعد التنظيف:", data.shape)
print("عدد القيم الفارغة بعد التنظيف:\n", data.isnull().sum())
print(data.head())

# -------------------------
# 8️⃣ التحليل الاستكشافي للبيانات (EDA)

# توزيع فئة Churn
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=data)
plt.title("توزيع العملاء: Churn vs Not Churn")
plt.show()

# 9️⃣ مدة الاشتراك (tenure) وعلاقة Churn
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="tenure", data=data)
plt.title("مدة الاشتراك vs ترك العميل")
plt.show()

# 10️⃣ إجمالي الفاتورة (TotalCharges) وعلاقة Churn
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="TotalCharges", data=data)
plt.title("إجمالي الفاتورة vs ترك العميل")
plt.show()

# 11️⃣ إحصائيات عامة
print(data.describe())

# 12️⃣ فحص توازن الفئات (Class Imbalance)
print(data["Churn"].value_counts())
print(data["Churn"].value_counts(normalize=True))  # بالنسبة المئوية
