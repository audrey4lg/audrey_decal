#1. The Terminal + Command Line + Git
    #1 To find out what your working directory is type "pwd", print working directory
    #2 The command to list all the files in your current working directory is "ls"
    #3 To pull the corrected homework.py from brianna.repo there are a few steps to take. First "cd .." will bring us back to the python_decal directory, and then we "cd brianna_repo" to change into the brianna_repo directory, finally we "git pull" to pull the new updates from git.
    #4 To more this new homework.py to your personal repository it is "mv ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/homework.py"
    #5 To see the contents of the homework.py in your terminal "cat homework.py" in order to print what is written in that file.
    #6 To edit the contents of homework.py while in terminal "nano homework.py" will open it to edit in terminal.
    #7 To save the changes and push to your remote repository first while in the correct directory type "git add homework.py" and then "git commit -m "finished hw" and finally "git push origin master". It will then ask you to type in your ssh and it will not show up while typing. 
    #8 It seems Judy is trying to push a file that does not have all the updates someone else has made. Someone else has made changes and pushed them into the remote repository that Judy does not yet have. To fix this Judy should first pull the updates "git pull homework.py" and then check her changes and re add, commit, and push.
    #9 "cd ~/Recent"

#2. Data Types + Functions + Conditionals + Loops
    #2.1 Data Types
def checkDataType(x):
    return(type(x).__name__)
print (checkDataType(3.14))
print (checkDataType(True))
    #2.2 Conditionals
def evenOrOdd(x):
    if x % 2 ==0:
        return 'even'
    else:
        return 'odd'
print (evenOrOdd(7))
print (evenOrOdd(10))

#3. Loops
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
print (sumWithLoop(numbers))

#4. Lists
#4.1 Lists
def duplicateList(lst):
    newList = []
    for item in lst:
        newList.append(item)
        newList.append(item)
    return newList
print (duplicateList(['a', 'b', 'c']))
#4.2 Debugging
    # def square(num)
    #     return num*num
    #error as there is a missing colon after the def line
def square(num):
    return num * num
print (square(4))
