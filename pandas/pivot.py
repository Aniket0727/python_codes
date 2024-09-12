import pandas as pd


df1={"city":['Jacksonville','Jacksonville','Jacksonville','Jacksonville','Jacksonville','ElPaso','ElPaso','ElPaso','ElPaso','ElPaso'],
     "month":['January','February','March','April','May','January','February','March','April','May'],
     "temperature":[13,23,38,5,34,20,6,26,2,43]
     }

df1=pd.DataFrame(df1)
print(df1)
print()
# print(df11.pivot("city","month","temperature"))
pivot_df = df1.pivot(index="city", columns="month", values="temperature")

print(pivot_df)




# The pivot() method in Pandas is used to reshape a DataFrame by reorganizing its data based on specified columns.