import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("ghg.csv")
# print(df.head(10))
df_clean=df.dropna(subset=["Supply Chain Emission Factors with Margins"])
df_clean=df_clean.drop_duplicates()
df_clean.to_csv("ghgclean.csv",index=False)
top=(
    df_clean.groupby("Industry Name")["Supply Chain Emission Factors with Margins"].sum().sort_values(ascending=False).head(10)
)
plt.figure(figsize=(12,6))
sns.barplot(x=top.values,y=top.index,palette="Reds_r")
plt.xlabel("Total Emissions(with Margins)")
plt.ylabel("Top 10 Industries with Highest Emissions")
plt.tight_layout()
plt.show()
plt.savefig("top_10_industries.png")
plt.close()
plt.figure(figsize=(10,6))
sns.histplot(df_clean["Supply Chain Emission Factors with Margins"],bins=30,kde=True,color='skyblue')
plt.xlabel("Emissions Factor (with Margin)")
plt.title("Distribution of supply Chain Emissions")
plt.tight_layout()
plt.savefig("emission_distibution.png")
plt.close()

print("Analysis complete. Graphs Saved as PNG..")