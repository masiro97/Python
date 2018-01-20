def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name,passwd,tries,wins,chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd,tries,wins,chips = members[name]
        line = name + ','+passwd+','+\
               str(tries)+','+str(wins)+','+\
               str(chips)+'\n'
        file.write(line)
    file.close()
