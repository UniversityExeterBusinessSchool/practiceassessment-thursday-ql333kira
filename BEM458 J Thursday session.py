#######################################################################################################################################################
# 
# Name:Qian Li
# SID:710075091
# Exam Date:27th March 2025 
# Module:Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-ql333kira.git 

#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}
print(key_comments)

my_key_comments = {}

for numbers, comments in key_comments.items():
    if numbers == 7:
        my_key_comments[numbers] = comments

print (my_key_comments)
my_key_comments1 = {}

for numbers, comments in key_comments.items():
    if numbers == 1:
        my_key_comments1[numbers] = comments

print (my_key_comments1)
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""
positions = [
    (customer_feedback.find('satisfactory'), customer_feedback.find('satisfactory') + len('satisfactory')),
    (customer_feedback.find('order'), customer_feedback.find('order') + len('order')),
    (customer_feedback.find('effort'), customer_feedback.find('effort') + len('effort')),
    (customer_feedback.find('issue'), customer_feedback.find('issue') + len('issue')),
    (customer_feedback.find('promptly'), customer_feedback.find('promptly') + len('promptly')),
    (customer_feedback.find('appreciate'), customer_feedback.find('appreciate') + len('appreciate')),
    (customer_feedback.find('experience'), customer_feedback.find('experience') + len('experience')),
    (customer_feedback.find('resolve'), customer_feedback.find('resolve') + len('resolve')),
    (customer_feedback.find('overall'), customer_feedback.find('overall') + len('overall')),
    (customer_feedback.find('minor'), customer_feedback.find('minor') + len('minor')),

]
print("Positions of keywords:", positions)


# Initialize an empty list to store (start, end) positions
my_list = []

##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 71
# Insert last two digits of ID number here: 91

# Write your code for Operating Profit Margin


# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here

def operating_profit_margin (net_operating_profit, revenue):
    return(net_operating_profit / revenue) * 100 

def revenue_per_customer (revenue, number_of_customers):
    return(revenue / number_of_customers)

def customer_churn_rate (numbers_of_customers, net_profit_margin):
    return(numbers_of_customers / net_profit_margin) * 100 

def average_order_value (total_order_value, numbers_of_orders):
    return (total_order_value / numbers_of_orders)

print("Operating Profit Margin:", operating_profit_margin(71,91 ))
print("Revenue per Customer:", revenue_per_customer(71, 91))
print("Customer Churn Rate:", customer_churn_rate(71,91))
print("Average Order Value:", average_order_value(71,91))

##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

Price = np.array([20,25,30,35,40,45,50,55,60,65,70]).reshape(-1,1)
Demand = np.array([300,280,260,240,210,190,160,140,120,100,85])
model = LinearRegression()
model.fit(Price, Demand)

predicted_demand = model.predict(np.array([[52]]))
print(f"Predicted Demand at Price 26: {predicted_demand[0]}")

plt.scatter(Price, Demand, color='blue')
plt.plot(Price, model.predict(Price), color='red')
plt.xlabel('Demand(units)')
plt.ylabel('Price vs Demand')
plt.show()


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart


# Generate 100 random numbers between 1 and student id number
#Student ID: 710075091 

import random
import matplotlib.pyplot as plt

random_numbers = [random.randint(1, 710075091) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='o', linestyle='--', label='Random Numbers', color='blue');
plt.title('Line Chart of 100 Random Numbers')
plt.xlabel('Index')
plt.ylabel=('Random Number')
plt.legend('---')
plt.grid()
plt.show()


