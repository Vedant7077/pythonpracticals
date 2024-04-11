source_file = input("Enter source file name:")
dest_file = input("Enter destination file name:")

with open(source_file,'r') as source:
    with open(dest_file,'w') as dest:
        dest.write(source.read())
print("Contents copied")