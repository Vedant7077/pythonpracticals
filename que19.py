rows = 5

# Upper half of the pattern
for i in range(1,rows+1,2):
    print("*"*i)
# Lower half of the pattern
for i in range(rows-2,0,-2):
    print("*"*i)