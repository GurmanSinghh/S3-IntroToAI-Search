#!/usr/bin/env python
# coding: utf-8

# In[2]:


from GraphData import graph
queue = [] 
visited = []
path = []
def BFS_gurman(graph, start, goal):
  visited.append(start)
  queue.append(start)
  if start == goal:
      print("He is meeting to him only")
  if goal not in graph:
      print("Goal state not in graph")
  if start not in graph:
      print("Start state not in graph")
  while len(queue)>0:
    f = queue.pop(0)
    path.append(f)
    if(f == goal):
        break
    for neighbour in graph[f]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
  
  if start in graph and goal in graph[start]:
    print("He can meet directly to the goal node")       
  if goal not in path:
       print("Relationship can't be established")
  else:
      for p in path:
          print(p)
      
BFS_gurman(graph, 'Dolly', 'Gurman')
print("\n------------------")
BFS_gurman(graph, 'George','Bob')


# In[ ]:




