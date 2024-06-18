from datetime import datetime, timedelta

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pymysql

db = pymysql.connect(host='119.188.240.140',
                     port=33077,
                     user='chat',
                     password='EmzPYQEXDwp7S4pd',
                     database='chat')

cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询


list_sum = []
today = datetime.now()
for i in range(7):
    # 计算当前天的日期
    current_date = today - timedelta(days=i)
    cursor.execute("select COUNT(*) as number from ans WHERE YEAR = %s AND MONTH=%s AND DAY=%s;",
                   (current_date.year, current_date.month, current_date.day))
    result = cursor.fetchone()
    list_sum.append(result[0])

cursor.close()
custom_style = {
    'axes.prop_cycle': plt.cycler('color', ['red', 'blue', 'green']),
    'lines.linewidth': 2,
    'font.size': 12,
    'axes.facecolor': 'lightgray',
    'axes.edgecolor': 'black',
    'axes.linewidth': 1,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10
}

matplotlib.use('TkAgg')
plt.style.use(custom_style)
x = np.arange(7)  # start,stop,step
y = np.arange(7)
for i in range(7):
    y[i] = list_sum[i]
plt.title('Messages Statistics')
plt.xlabel('DAY')
plt.ylabel('MESSAGES')
plt.plot(x, y)
plt.show()
