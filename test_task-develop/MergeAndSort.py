#----------------------------------------------------------
#
# Code of Makhambet
#
#__________________________________________________________
import pandas as pd

table1 = "C:/Users/first_table.xlsx"
table2 = "C:/Users/second_table.xlsx"

df1 = pd.read_excel(table1)
df2 = pd.read_excel(table2)

ffj = [df1, df2]
join = pd.concat(ffj)
join = join.sort_values(by="Дата")
join.to_excel("third_table.xlsx", index=False)