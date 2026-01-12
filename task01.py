import pandas as pd

data = pd.read_csv(
    r"C:\Users\arthi\Downloads\API_SP.POP.TOTL_DS2_en_csv_v2_34 (1)\API_SP.POP.TOTL_DS2_en_csv_v2_34.csv",
    skiprows=4
)

print(data.head())
print(data.columns)
import matplotlib.pyplot as plt

year = "2022"

top10 = (
    data[["Country Name", year]]
    .dropna()
    .sort_values(by=year, ascending=False)
    .head(10)
)

plt.figure()
plt.bar(top10["Country Name"], top10[year])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Countries by Population (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.show()
