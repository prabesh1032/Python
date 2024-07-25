import matplotlib.pyplot as plt
'''
x=[1,12,3,4,5]
y=[2,3,5,7,0]
# plt.plot(x,y,marker='o',linestyle='-',color='b',label='Circle marker')
# plt.plot(x,[i-1 for i in y],marker='D',linestyle='--',color='g',label='Triangle marker')
plt.plot(x,y,marker='o',linestyle='-',color='blue',label='Circle marker')
plt.plot(x,[i-1 for i in y],marker='D',linestyle='--',color='#ff7f0e',label='Triangle marker')
plt.title("Plot with different markers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.grid(True)
# plt.grid(True,which='both',linestyle='--',linewidth=2,color='pink')
plt.grid(True,axis='x',linestyle='--',linewidth=1,color='pink')
plt.grid(True,axis='y',linestyle='--',linewidth=1,color='pink')
plt.legend()
plt.show()
'''
'''
x=[1,5,3,0,5]
y1=[9,3,2,7,0]
y2=[1,5,0,8,10]
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,y1,marker='o',linestyle='--',color='blue')
plt.title('Subplot 1')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(1,2,2)
plt.plot(x,y2,marker='o',linestyle='--',color='red')
plt.title('Subplot 2')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.tight_layout()
plt.show()
'''
'''
#scatterplot
x=[1,12,3,4,5]
y=[2,3,5,7,0]
size=[200,50,100,200,300]
colors=["r","g","b",'orange','purple']
plt.scatter(x,y,s=size,c=colors,alpha=0.5,edgecolors='w',label='Data Points')
plt.title('customized Scatter Plot')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.legend()
plt.show()
'''
'''
#subplots
x=[1,2,3,4,5]
y1=[11,3,0,4,6]
y2=[0,8,3,9,1]
y3=[3,5,1,11,0]
y4=[0,4,5,6,1]
fig,axs=plt.subplots(2,2,figsize=(10,8))
#1st plot
axs[0,0].plot(x,y1,marker='o',linestyle='-',color='b')
axs[0,0].set_title('Subplot 1')
axs[0,0].set_xlabel("x-axis")
axs[0,0].set_ylabel("y-axis")
#2nd plot
axs[0,1].plot(x,y2,marker='^',linestyle='--',color='r')
axs[0,1].set_title('Subplot 2')
axs[0,1].set_xlabel("x-axis")
axs[0,1].set_ylabel("y-axis")
#3rd plot
axs[1,0].plot(x,y3,marker='^',linestyle='--',color='g')
axs[1,0].set_title('Subplot 3')
axs[1,0].set_xlabel("x-axis")
axs[1,0].set_ylabel("y-axis")
#4th plot
axs[1,1].plot(x,y4,marker='o',linestyle='--',color='purple')
axs[1,1].set_title('Subplot 4')
axs[1,1].set_xlabel("x-axis")
axs[1,1].set_ylabel("y-axis")
plt.legend()
plt.show()

'''
'''
categories=['A','B','C','D','E']
values=[3,5,2,11,3]
plt.barh(categories,values,color="cyan",edgecolor='red',linewidth=1)
plt.title("Basic Bar Graph")
plt.xlabel("categories")
plt.ylabel("values")
plt.grid(True,axis='y',linestyle='--',linewidth=0.7)
plt.legend()
plt.show()
'''
'''
semesters=['2nd','4th','5th']
boys=[20,30,25]
girls=[15,20,22]
x=range(len(semesters))
plt.bar(x,boys,width=0.4,label="Boys",color="purple",align="center")
plt.bar(x,girls,width=0.4,label="Girls",color="pink",align="edge")
plt.title("Basic Bar Graph")
plt.xlabel("Semester")
plt.ylabel("No of students")
plt.legend()
plt.show()
'''
'''
data=[2,3,4,2,3,1,2,2,1,4,5,6,5,6,3,5,3,2,4,2,3,6,5]
plt.hist(data,bins=5,color='blue',edgecolor='black')
plt.title("Basic Histogram")
plt.xlabel("Data values")
plt.ylabel("Frequency")
plt.grid(True,axis='y',linestyle='--',linewidth=0.7)
plt.legend()
plt.show()
'''
'''
data1=[1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7,7]
data2=[2,3,3,4,4,4,5,5,5,5,6,6,6,6,7]
plt.hist([data1,data2],bins=5,color=['blue','cyan'],edgecolor='black',label=['Dataset 1','Dataset 2'],alpha=0.7)
plt.legend()
plt.show()
'''
#normalization
'''
data1=[1,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7]
plt.hist(data1,bins=5,color='blue',edgecolor='black',alpha=0.7,density=True)
plt.legend()
plt.show()
'''
'''
labels=['2nd','4th','5th']
sizes=[25,35,45]
colors=['cyan','gold','lime']
explode=(0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%', shadow=True,startangle=140)
plt.legend()
plt.show()
'''
#boxplot
'''data1=[1,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7]
plt.boxplot(data1)
plt.legend()
plt.show()'''
#multipleplot
data1=[1,2,2,20,3,3,4,10,4,5,5,5,6,6,11,7]
data2=[1,2,20,3,3,7,1,5,11,5,5,5,6,6,7,7]
data3=[1,2,2,3,6,1,4,4,4,5,20,5,17,6,10,7]
plt.boxplot([data1,data2,data3],labels=['data1','data2','data3'])
plt.xlabel("DATASET")
plt.ylabel("values")
plt.legend()
plt.show()
