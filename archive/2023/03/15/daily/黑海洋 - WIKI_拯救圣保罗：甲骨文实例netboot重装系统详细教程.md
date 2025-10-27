---
title: 拯救圣保罗：甲骨文实例netboot重装系统详细教程
url: https://blog.upx8.com/3276
source: 黑海洋 - WIKI
date: 2023-03-15
fetch_date: 2025-10-04T09:36:02.489165
---

# 拯救圣保罗：甲骨文实例netboot重装系统详细教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 拯救圣保罗：甲骨文实例netboot重装系统详细教程

发布时间:
2023-03-14

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
18381

# 场景

可能是你用不到，但是我遇到了这样一个问题，就是我想详细了解我的竞争对手的网站（电商类）销售情况和新品上架情况，但是我总不至于像盯盘一样，在电脑或者手机上一直看着这个站吧！

于是我想到用一个脚本来检测，脚本的功能是如果发现对手出售了商品，就发送我售出商品的名称，价格；如果是新上线了商品，就要邮件告诉我新品的名称，价格，这对于我分析对手的销量和趋势，然后在我的店铺中择优上货是有一定帮助作用的。

另外，这个脚本作用不仅仅如此，你也可以修改一下，包括但不限于监控自己的抖音粉丝上升趋势、其他事件新闻进展、甚至是当前热点等等。

# 现成的产品

当然，我前面的想法在现实中每个公司、店铺都用得到，而且有人专门开发程序为此而服务，比方说比较好的网页监控工具：Visualping、Distill Web Monitor、Wachete等，他们都是做这个的也都很专业，但是要想深度使用，就要收费了；

国内也有类似的产品，我尝试过。不过也有限制，每天1个网页变化只给10封邮件，申请再多也要收费！

所以吧，自己写来自己用吧！

# 代码

```
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# 网站 URL
url = "https://"

# 发送邮件的参数
sender = '你的发件人邮箱'
receiver = '你的收件人邮箱'
smtp_server = 'smtp.xxx.com' # 发件人邮箱的 SMTP 服务器地址
smtp_port = 465 # 发件人邮箱的 SMTP 端口
username = '你的发件人邮箱'
password = '你的发件人邮箱密码'

def send_email(subject, body):
    # 创建 MIMEText 邮件
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # 发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, msg.as_string())

def get_product_info(product_url):
    # 获取商品信息
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('h1', class_='h3').text
    price = soup.find('span', class_='h2').text
    stock = soup.find('span', class_='js-product-stock').text
    return (title, price, stock)

def check_product_sold_out(product_url):
    # 检查商品是否已售出
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup.find('div', class_='product-sold-out'):
        return True
    else:
        return False

# 定期检查商品
while True:
    # 获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找商品列表
    product_list = soup.find('div', class_='js-product-list')

    # 检查每个商品是否售出
    for product in product_list.find_all('a', class_='product-card'):
        product_url = product['href']
        product_title = product.find('h2').text
        if check_product_sold_out(product_url):
            # 商品已售出，发送邮件通知
            subject = f'商品已售出：{product_title}'
            body = f'商品名称：{product_title}\n'
            send_email(subject, body)
        else:
            # 商品未售出，检查是否为新商品
            try:
                # 尝试获取商品信息，如果获取失败则说明是新商品
                product_title, product_price, product_stock = get_product_info(product_url)
            except:
                # 新商品，发送邮件通知
                subject = f'新商品上架：{product_title}'
                body = f'商品名称：{product_title}\n库存：{product_stock}\n价格：{product_price}\n'
                send_email(subject, body)

    # 等待一段时间后再次检查
    time.sleep(300)
```

解释：这个就是网店的监控程序，新品上架，商品售出会像间谍一样及时通知你！

再赠送一个：

```
import requests
import hashlib
import time
import smtplib
from email.mime.text import MIMEText

url = 'https://'

def get_hash(url):
    response = requests.get(url)
    return hashlib.sha256(response.content).hexdigest()

def send_email(content):
    sender = ''
    receiver = ''
    password = ''
    smtp_server = ''
    smtp_port = 465

    message = MIMEText(content)
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Website Change Alert'

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

current_hash = get_hash(url)
while True:
    new_hash = get_hash(url)
    if new_hash != current_hash:
        send_email('Website content has changed.')
        current_hash = new_hash
    else:
        time.sleep(30)
```

解释：这个代码很简单，比较的是网页哈希，只要有变化就会邮件通知，可用于任何场景！

# 如何使用

上面的代码是python的，修改后可以直接使用。后台运行的方法：

```
nohup python3 jiankong.py > output.log 2>&1 &
```

[取消回复](https://blog.upx8.com/3276#respond-post-3276)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")