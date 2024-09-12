# import time 

# # # start=time.time()
# # # for i in range(1000000):
# # #     print(i)
    
# # # print(time.time()-start)


# # # import pandas as pd

# # # # Sample dataset
# # # data = {
# # #     'Transaction_ID': [1, 2, 3, 4, 5],
# # #     'Product': ['A', 'B', 'A', 'C', 'B'],
# # #     'Quantity': [10, 5, 2, 8, 7],
# # #     'Price_per_Unit': [100, 200, 100, 300, 200]
# # # }

# # # # Create a pandas DataFrame
# # # df = pd.DataFrame(data)

# # # # Function to calculate the average revenue per transaction
# # # def calculate_average_revenue(df):
# # #     df['Revenue'] = df['Quantity'] * df['Price_per_Unit']
# # #     average_revenue = df['Revenue'].mean()
# # #     return average_revenue

# # # # Calculate and print average revenue per transaction
# # # average_revenue = calculate_average_revenue(df)
# # # print(average_revenue)


# # import pandas as pd

# # # Sample dataset
# # data = {
# #     'Transaction_ID': [1, 2, 3],
# #     'Date': ['2023-08-01', '2023-08-02', '2023-08-03'],
# #     'Product': ['Product A', 'Product B', 'Product C'],
# #     'Quantity': [5, 10, 2],
# #     'Price_per_Unit': [100, 50, 200]
# # }

# # # Create a pandas DataFrame
# # df = pd.DataFrame(data)

# # # Define the function to calculate total revenue
# # def calculate_total_revenue(df):
# #     df['Total_Price'] = df['Quantity'] * df['Price_per_Unit']
# #     total_revenue = df['Total_Price'].sum()
# #     return total_revenue

# # # Calculate the total revenue
# # total_revenue = calculate_total_revenue(df)
# # print(f"The total revenue is: {total_revenue}")

# start=time.time()
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Example usage
# number = 5
# print(f"The factorial of {number} is {factorial(number)}")

# print(time.time()-start)



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print(func)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()