n=9
sprints = [9,7,3,1]
sprint_dict = dict(zip(range(1,n+1), [0]*n))

for i in range(len(sprints)-1):
        if sprints[i] < sprints[i+1]:
                for j in range(sprints[i], sprints[i+1]+1):
                        sprint_dict[j]+=1

        elif sprints[i] > sprints[i+1]:
                for j in range(sprints[i+1],sprints[i]+1):
                        sprint_dict[j]+=1

sprints_sorted = dict(sorted(sprint_dict.items(), key=lambda x:x[1]))
print(max(sprints_sorted, key = sprints_sorted.get))
                        
                
