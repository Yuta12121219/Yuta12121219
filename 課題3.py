from matplotlib import pyplot as plt
import numpy as np
import japanize_matplotlib
 
# ランダムな点を生成する
#x1 =[2014,2015,2016,2017,2018,2019]
#x2 =[2014,2015,2016,2017,2018,2019]
y1 = [1452, 1796,1894,2584,2735,3447]
y2 = [3231,3747,3726,5853,8866,10913]
xscale = np.arange(0, 3500, 500)
yscale = np.arange(0, 14000, 2000)
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# x1, y1を青色でプロット
ax.scatter(y1, y2,  c='r')
 
# x2, y2を青色でプロット

 
# 汎用要素を表示

ax.set_ylabel('志\n願\n者',fontsize=10, rotation=0)  # x軸ラベル
ax.set_xlabel('オープンキャンパス参加者数')  # y軸ラベル

 
plt.show()