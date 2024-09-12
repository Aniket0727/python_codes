import pandas as pd
import numpy as np


dict={
    "name":["Annu","Omakar","Rahul"],
    "Roll_No":[10,20,30],
    "City":["Georai","Jalna","Jalna"]
}
a=pd.DataFrame(dict)
# print(a)
# print(a)


data=pd.read_excel("A:/python/pandas/emp.xlsx")
data2=pd.read_excel("A:/python/pandas/test.xlsx")

# print(data.head(10)) # head default value 5
# print(data.tail(10)) # tail default value 5


#get datatype
# print(data.info())
# print(data.isnull().sum())

# print(data.describe())
# print(data2.duplicated())

# data3=data2.drop_duplicates()

# data3.to_excel('new.xlsx',index=False)
# print(data2)

# print(data3.dropna())

print()
# print(data2.isnull().sum())
# Replace NaN in the 'city' column with 898 if the column exists




# print(data2)
# print(data2['city'].replace(np.nan,10))

# print(data2.fillna(method='bfill'))
# print(data2.fillna(method='ffill'))

# print(data2)


# get columns names

# print(data2.columns)


# create new column with privious column condition
# data2.loc[(data2['age'] < 18),'Eligibility']='Not Eligible'

# data2['new']=data2['age'] * 2

# print(data2)

# data2['full Name']=data2['name']+ ' '+data2['city']
# print(data2)

a=data2.groupby('department').agg({'name':'count'})
# print(a)


df1={
    "name":["Annu","Omakar","Rahul"],
    "Roll_No":[10,20,30],
    "City":["Georai","Jalna","Jalna"]
}

df2={
    "subject":["Java","Python","Django"],
    "Roll_No":[10,50,30],
    "asa":[1,2,3]
}
df1=pd.DataFrame(df1)
df2=pd.DataFrame(df2)

#merge table on the baises of roll number
# print(pd.merge(df1,df2,on='Roll_No'))

#merge same value
# print(pd.merge(df1,df2))

#left join
# print(pd.merge(left=df1,right=df2,on='Roll_No',how='left'))
print()
print()
#right join
# print(pd.merge(left=df1,right=df2,on='Roll_No',how='right'))


# print(df1)
#change value
# df1.loc[0,'name']='aniket'
# print()
# print(df1)

df3={
   "Roll_No":[10,20,300]
}

df4={
     "Roll_No":[10,20,30]
    
}
df3=pd.DataFrame(df3)
df4=pd.DataFrame(df4)

# keep_equal default value false
print(df3.compare(df4))
print()
print()

print(df3.compare(df4,keep_equal=True))
print()
# print(df3.compare(df4,keep_equal=False))
print()

# show qeual value in the form of NaN with diff value
print(df3.compare(df4,keep_shape=True))
print()

# not show qeual value in the form of NaN, also show with diff value
print(df3.compare(df4,keep_shape=False))



