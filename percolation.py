from matplotlib.figure import figaspect
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

np.random.seed(0)

size=200
x=size**2
sys.setrecursionlimit(x)
main=np.zeros((size,size)) #where everything happens, every index in main is a point on the plane
connections_horizontal=np.random.rand(size-1,size)  #horizontal connections between every points in main
connections_vertical=np.random.rand(size,size-1)  #vertical connections between every points in main
p=0.5 #parameter of percolation

def group(array,index,grp_nbr,p): #index of point for which we want to find the group, the group number (to distinguish the groups), parameter p (percolation)

    array[index]=grp_nbr
    # 1: find if the neighbouring connection is active
    # 2. if the connection is active, put the neighbouring point in the same group
    # 3. for every new point, repeat the procedure until either no connections, or every neighbour is in the same group

    if index[0]<size-1: #checking connections to the right
        if connections_horizontal[index]>p: #if connection is active
            if array[index[0]+1,index[1]]!=grp_nbr: #and neighbour is not in the same group
                array[index[0]+1,index[1]]=grp_nbr #adding the point to the group
                group(array,(index[0]+1,index[1]),grp_nbr,p) #repeat procedure for new point (recursion)
    if index[1]<size-1: #checking the connections up
        if connections_vertical[index]>p:
            if array[index[0],index[1]+1]!=grp_nbr:
                array[index[0],index[1]+1]=grp_nbr
                group(array,(index[0],index[1]+1),grp_nbr,p)
    if index[0]>0: #checking the connections to the left
        if connections_horizontal[index[0]-1,index[1]]>p:
            if array[index[0]-1,index[1]]!=grp_nbr:
                array[index[0]-1,index[1]]=grp_nbr
                group(array,(index[0]-1,index[1]),grp_nbr,p)
    if index[1]>0: #checking the connections down
        if connections_vertical[index[0],index[1]-1]>p:
            if array[index[0],index[1]-1]!=grp_nbr:
                array[index[0],index[1]-1]=grp_nbr
                group(array,(index[0],index[1]-1),grp_nbr,p)

p=0.4
for i in range(size): #finding a group for every point on the plane
    for j in range(size):
        if main[i,j]==0:
            group(main,(i,j),np.random.rand(1),p)

plt.imshow(main,cmap='rainbow',interpolation='none')
plt.savefig('test.png')
plt.show()

# fig=plt.figure()
# im=plt.imshow(main,cmap='rainbow',interpolation='none')
# txt=plt.text(0,0,'p')

# main1=main

# def animate(i):
#     p=0.531-0.0001*i
#     main=np.zeros((size,size))
#     for i in range(size): #finding a group for every point on the plane
#         for j in range(size):
#             if main[i,j]==0:
#                 group(main,(i,j),main1[i,j],p)
#     im.set_array(main)
#     txt.set_text(p)
#     return [im]

# anim = animation.FuncAnimation(fig, animate, frames=500)
# anim.save('test_anim3.mp4',fps=30)
# plt.show()