#15.2.1修改标签文字和线条的粗细
import matplotlib.pyplot as plt
s=[1,4,9,16,25,36]
plt.plot(s,linewidth=5)
plt.title("s numbers",fontsize=24)#指定标题
plt.xlabel("value",fontsize=24)#X轴显示
plt.ylabel("abs value",fontsize=24)#Y轴显示
plt.tick_params(axis='both',labelsize=14)
plt.show()
