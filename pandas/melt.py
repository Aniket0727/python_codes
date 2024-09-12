import pandas as pd

# Creating a simple DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 90],
    'Science': [92, 88, 95],
    'Java': [99, 98, 92]
    
})

print("Original DataFrame:")
print(df)
print()

# Melting the DataFrame
melted_df = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')

print("Melted DataFrame:")
print(melted_df)

# melt(): Widens the DataFrame by stacking multiple columns into a single column, making it longer (more rows).
# pivot(): Narrows the DataFrame by spreading rows into multiple columns, making it wider (fewer rows).