import pandas as pd

employees_lst = [
    {"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1},
    {"id": 2, "name": "Henry", "salary": 80000, "departmentId": 2},
    {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2},
    {"id": 4, "name": "Max", "salary": 90000, "departmentId": 1},
    {"id": 5, "name": "Janet", "salary": 69000, "departmentId": 1},
    {"id": 6, "name": "Randy", "salary": 85000, "departmentId": 1},
    {"id": 7, "name": "Will", "salary": 70000, "departmentId": 1},
]

employee = pd.DataFrame(employees_lst)
department_lst = [{"id":1, "name":"IT"}, {"id":2, "name":"Sales"}]
department = pd.DataFrame(department_lst)

def top_three_salaries(employee, department):
    rename_dept_cols = {"name":"Department"}
    rename_emp_cols = {"name":"Employee","salary":"Salary"}
    department = department.rename(columns = rename_dept_cols)
    employee = employee.rename(columns = rename_emp_cols)
    merged_df = pd.merge(department, employee, left_on='id', right_on='departmentId', how='inner')
    merged_df = merged_df[['Department','Employee','Salary']]
    #merged_df = (merged_df.groupby(['Department','Employee','Salary']))
    # merged_df = (merged_df.sort_values(by=['Department','Salary'], ascending=False)
    #              .assign(rank = lambda x: x[['Department','Salary']]
    #                      .rank(method='dense', ascending=False)))
    merged_df = (merged_df.assign(rank = lambda x: 
                                 x.groupby(['Department'])['Salary']
                                 .rank(method = 'dense', ascending = False))
                                 .sort_values(by = ['Department','rank'], ascending=True)
                                 .query("rank <= 3"))
    return merged_df[['Department','Employee','Salary']]

new_df = top_three_salaries(employee, department)
print(new_df)

