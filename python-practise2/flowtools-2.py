#words = ['cat','window','ajklsd']

#words = [input("type anything you want:")]

#for w in words:
#		print(w,len(w))


# I want to turn it into input mode
# but only 1 input

## goal reached!!

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(users)        # Output: {'Hans': 'active', '景太郎': 'active'}
print(active_users) # Output: {'Hans': 'active', '景太郎': 'active}


# July 23 3:40 留下一些问题吧，实在想不太清楚
# 1 首先这段代码的功能类似excel的过滤功能
# 2 这个代码，看似明白，但是对于操作逻辑，理解不清
# 3 不清楚点如： 
