import pandas as pd
data = { 
    "Name" : ['me','KK','Aa'],
    "Score" : [50,100,200]
}

student_df  = pd.DataFrame(data)
print(student_df)
for (index,row) in student_df.iterrows():
    if row.Name == 'me':
        print(row.Score)
    print(row.Score)