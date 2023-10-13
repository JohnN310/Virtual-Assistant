def epl(lst):
    i=0
    max_points=0
    max_goal=0
    total=1
    goal_def=0
    index=0
    while i<len(lst):
        total=3*lst[i]['wins']+lst[i]['draws']
        goal_def=lst[i]['scored']-lst[i]['conceded']
        if (total>max_points):
            max_points=total
            index=i
            if (goal_def>max_goal):
                max_goal=goal_def
        if total==max_points:
            if goal_def>max_goal:
                index=i
        i+=1
    return lst[index]['name']
print(epl([
    {
      "name": "Chelsea",
      "wins": 35,
      "loss": 3,
      "draws": 0,
      "scored": 102,
      "conceded": 20,
    },
    {
      "name": "Liverpool",
      "wins": 24,
      "loss": 6,
      "draws": 8,
      "scored": 118,
      "conceded": 29,
    },
    {
      "name": "Arsenal",
      "wins": 28,
      "loss": 2,
      "draws": 8,
      "scored": 87,
      "conceded": 39,
    },
  ]))