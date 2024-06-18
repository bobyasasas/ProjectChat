import matplotlib
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host='119.188.240.140',
                     port=33077,
                     user='chat',
                     password='EmzPYQEXDwp7S4pd',
                     database='chat')

cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("select username,count(1) as number from ans GROUP BY username ORDER BY count(1) DESC LIMIT 4;")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
cursor.close()
list_name = []
list_data = []
for i in data:
    list_name.append(i[0])
    list_data.append(i[1])

# 关闭数据库连接
db.close()
# 数据
sizes = list_data

# 饼图的标签
labels = list_name

# 饼图的颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 突出显示第二个扇形
explode = (0.1, 0, 0, 0)
matplotlib.use('TkAgg')
# 绘制饼图
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

# 标题
plt.title("User message Statistics")

# 显示图形
plt.show()
