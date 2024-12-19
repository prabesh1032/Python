import pandas as pd
''''
s = pd.Series([1,2,3,4,6,7])

data={ 
    'A':[1,2,3,4,5],
    'B':[6,7,8,9,10],
    'C':[11,12,13,14,15]}
df=pd.DataFrame(data)
print(s)
print(df)
'''
# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Smith', 'Matt'],
    'Age': [28, 24, 35, 42],
    'City': ['New York', 'Paris', 'London', 'Berlin']
}
df = pd.DataFrame(data)
print(df)
# Using head to get the first three rows
print(df.head(3))

# Using tail to get the last two rows
print(df.tail(2))

'''
s = pd.Series([1,2,3,4,6,7],index=['a','b','c','d','f','g'])
print("/n custome index::/n",s)

#creating a dataframe from dictionary
data={
    'Name':['Alice','Bob','ram','david'],
    'Age':[25,30,40,55],
    'City':['Pkr','Npl','KTM','Ngt']
}
df=pd.DataFrame(data)
print("dataframe from dictionary:\n",df)
print("only age:\n",df['Age'])
print("age and name are:\n",df[['Age','Name']])
'''

#selecting rows by index
data={
    'Name':['Alice','Bob','ram','david'],
    'Age':[25,30,40,55],
    'City':['Pkr','Npl','KTM','Ngt']
}
df=pd.DataFrame(data)
first_row=df.iloc[0]
print("\n first row:\n",first_row)
print("\n first 2 row:\n",df.iloc[0:2])

#add new column
df['salary']=[7000,3000,5000,6000]
print("\n Dataframe with salary Column:\n",df)
filtered_df=(df[df['Age']>30])
print("\n filtered Dataframe (age>30:\n)",filtered_df)
'''
data={
    'Name':['Alice','Bob','ram','david'],
    'Age':[25,30,40,55],
    'City':['Pkr','Npl','KTM','Ngt']
}
df=pd.DataFrame(data)
print("dataframe index:",df.index)
print("dataframe Column:",df.columns)
print("dataframe Columns:",df.dtypes)
print("dataframe shape:",df.shape)
print("dataframe size:",df.size)
print("dataframe Values\n:",df.values)
print("dataframe Transpose:",df.T)
print("dataframe info:")
df.info()

'''
#seriess 

'''
#NaN
data={
    'Name':['Alice','Bob','ram','david'],
    'Age':[25,None,40,55],
    'City':['Pkr','Npl','KTM','Ngt']
}
df=pd.DataFrame(data)
print("is null:\n",df.isnull())

#dropping messing data
df_dropped=df.dropna()
print("Dataframe with dropped row:\n",df_dropped)
'''
'''
#merging and 
df1=pd.DataFrame({
    "id":[1,2,3,4],
    "name":["ram","hari","gita","David"]
})
df2=pd.DataFrame({
    "id":[3,4,5,6],
    "age":[24,32,16,23]
})
inner_join=pd.merge(df1,df2,on="id",how='inner')
print("inner join:",inner_join)
left_join=pd.merge(df1,df2,on="id",how='left')
right_join=pd.merge(df1,df2,on="id",how='right')
outer_join=pd.merge(df1,df2,on="id",how='outer')
print("left join:",left_join)
print("right join:",right_join)
print("outer join:",outer_join)
'''
'''
#joining
df1=pd.DataFrame({
    "id":[1,2,3,4],
    "name":["ram","hari","gita","David"]
},index=[1,2,3,4])
df2=pd.DataFrame({
    "city":["ktm","pkr","india","thiland"]
},index=[3,4,5,6])
# inner_join=df1.join(df2,how='inner')
# print("inner join:",inner_join)
left_join=df1.join(df2,how='left')
right_join=df1.join(df2,how='right')
# outer_join=df1.join(df2,how='outer')
print("left join:",left_join)
print("right join:",right_join)
# print("outer join:",outer_join)

data={
    'Name':['Alice','Bob','ram','david',None,"pranish","jagat"],
    'Age':[25,30,40,55,65,None,45],
    'City':['Pkr','Npl','KTM','Ngt',"A","B","C"]
}
df=pd.DataFrame(data)
#df.to_csv('output.csv',index=False)
df=pd.read_csv('output.csv')
print(df)

print(df.info())
print(df.isnull().sum())

#fill m,issing values in the 'age' column with the mean
Age_mean=df['Age'].mean()
df['Age'].fillna(Age_mean,inplace=True)
print("\n dataframe after filling missing value is 'Age':")
print(df.head())
filtered_df=df[df["Age"]>30]
print("\n filtered Dataframe (Age>30):")
print(filtered_df)
filtered_df.to_csv("filtered_output.csv",index=False)
print("\nfiltered Dataframe written to 'filltered_output.csv")
'''