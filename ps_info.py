import commands

program = input("Enter the name of the program to check: ")

#perform a ps, assign results to a list

proginfo = []
output = commands.getoutput("ps -f|grep " + program)
proginfo = output.split()

#display results

print(f"\n Full path:\t\t {proginfo[5]}") 
print(f"\n Owner:\t\t {proginfo[0]}") 
print(f"\n Process ID:\t\t {proginfo[1]}") 
print(f"\n Parent process:\t\t {proginfo[2]}") 
print(f"\n Start Time:\t\t {proginfo[4]}") 
