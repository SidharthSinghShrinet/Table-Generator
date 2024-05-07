#Table Generator
n=int(input("Enter the number:"))
upto=int(input("How long the table should be:"))

for i in range(1,upto):
    table=n*i
    print(table)
