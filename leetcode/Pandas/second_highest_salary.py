"""

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

 

Write a solution to find the second highest distinct salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""
import pandas as pd
employee_dict = {"id":[1,2,3], "salary":[100, 200, 300]}

employee = pd.DataFrame(employee_dict)

#for group by cases
new_df = (employee.groupby('id', as_index=False)['salary']
            .sum()
            .sort_values(by='salary', ascending=False)
            .assign(rownumber=lambda x: range(1,len(x)+1))
            )

#here no group by is required because id is the primary key
new_df2 = (employee.sort_values(by='salary', ascending=False)
           .assign(rownumber=lambda x: range(1,len(x)+ 1)))
new_df2 = (new_df2[new_df2['rownumber']==2].filter(items=['salary'])
           .rename(columns = {'salary':'SecondHighestSalary'}))


#the above solution is rownumber but we need rank
new_df3 = (employee.sort_values(by='salary',ascending=False)
           .assign(rank=lambda x: x['salary'].rank(method='dense', ascending=False)))

new_df3 = (new_df3[new_df3['rank']==2].filter(items = ['salary'])
           .rename(columns = {'salary':'SecondHighestSalary'}))

new_df3 = new_df3.iloc[0:]

if new_df2.empty:
    new_df2 = pd.DataFrame({'SecondHighestSalary':[None]})


print(new_df3.iloc[0])



# grouped = employee.groupby('id', as_index=False)['salary'].sum()


# print(employee.iloc[0])
