a = "amounts"
d = "dollars"
q = "quarters"
ds = "dimes"
n = "nickels"
p = "pennies"

a = float(input("Enter an amount: "))
total_a_in_p = int(a * 100)
d = total_a_in_p // 100
remaining_a_in_p = total_a_in_p % 100
q = remaining_a_in_p // 25
remaining_a_in_p = remaining_a_in_p % 25
ds = remaining_a_in_p // 10
remaining_a_in_p = remaining_a_in_p % 10
n = remaining_a_in_p // 5
p = remaining_a_in_p % 5

print("Your amount", a, "consists of ")
print(d,"dollars")
print (q, "quarters")
print(ds,"dimes")
print(n, "nickels")
print(p, "pennies")
