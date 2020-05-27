import matplotlib.pyplot as plt
import random

# 设置画布
fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(20,8),dpi=100)

# 设置x，y
x = range(60)
y = [random.randint(10, 20) for i in x]
z = [random.randint(1, 6) for i in x]

# 绘制
axes[0].plot(x,y,label='A',color='r')
axes[1].plot(x,z,label='B')


# x,y轴需要显示的东西
tem=range(100)
xticks_labe=['teim.{}'.format(i) for i in x]

# 先设置坐标轴
axes[0].set_xticks(x[::5])
axes[0].set_yticks(tem[::5])

# x轴是字符串，需要替换
axes[0].set_xticklabels(xticks_labe[::5],fontsize=15,rotation=-60)
axes[0].set_yticklabels(tem[::5],fontsize=15)
# 先设置坐标轴
axes[1].set_xticks(x[::5])
axes[1].set_yticks(tem[::5])

# x轴是字符串，需要替换
axes[1].set_xticklabels(xticks_labe[::5])

plt.savefig('f2.eps')
plt.show()




