import pandas as pd

# Creating a long-format DataFrame
df_long = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Score': [85, 78, 90, 92, 88, 95]
})

print("Original Long-Format DataFrame:")
print(df_long)

# Pivoting the DataFrame
pivoted_df = df_long.pivot(index='Name', columns='Subject', values='Score')

print("Pivoted DataFrame (Wide Format):")
print(pivoted_df)




# melt(): Widens the DataFrame by stacking multiple columns into a single column, making it longer (more rows).
# pivot(): Narrows the DataFrame by spreading rows into multiple columns, making it wider (fewer rows).