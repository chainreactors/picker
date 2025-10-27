---
title: 利用ESP8266开发板做WiFi攻击器
url: https://blog.upx8.com/3722
source: 黑海洋 - WIKI
date: 2023-07-30
fetch_date: 2025-10-04T11:53:21.383510
---

# 利用ESP8266开发板做WiFi攻击器

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 利用ESP8266开发板做WiFi攻击器

发布时间:
2023-07-29

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
14013

![6nkWuaZJdqsDYeS.jpg](https://loukas.cn/wp-content/uploads/2020/04/4230470727.jpg)

## 准备工具

**1. esp8266开发板（淘宝有，15软妹币左右吧）**

**2. 一根Micro-usb数据线**

**3. 一台电脑**

## 攻击原理

**主要利用取消身份验证洪水攻击，取消身份验证洪水攻击的原理是一个 AP 连接了路由器在正常访问网络，这个时候 Hacker 利用自己电脑或者其他设备进行伪造取消身份认证的报文，路由器就会以为是 客户端发过来的需要和客户端断开连接，已经连接的设备会自动断开。**

## 工作流程

**（1）客户端的连接这个 WiFi 发送认证请求，AP收到然后给与客户认证响应；**
**（2）客户端再发送认证请求，AP 再发送认证响应客户端传输数据给 AP；**
**（3）此时攻击者发送取消身份认证，客户端还是在发送数据，结果 AP Blocked（本意是此路不通）不接受客户端的数据；**
**（4）AP 就发送取消身份认证，客户端就断开连接了（攻击者让 AP 误以为 是客户端发送的解除认证，AP 就发送解除认证给客户端从而解除认证了），如果攻击者不停止攻击的话你怎么连接都连接不上去的。**

## 开始教程

#### 简单说一下部署方法和注意事项

**esp8266\_deauther是使用arduino开发的因此也是开源的我们需要准备arduion IDE、esp8266开发包、nodemcu一块。**

**下面开始**

**1.首先安装Arduino IDE**

![94apxteMjLQhiRq.png](https://loukas.cn/wp-content/uploads/2020/04/1578582266.png)

**2.下载固件**
**https://github.com/spacehuhn/esp8266\_deauther**
**解压**

**3.安装后打开arduino，菜单依次打开 文件\首选项,找到附加开发板管理器网址选项，填入**
**http://arduino.esp8266.com/stable/package\_esp8266com\_index.json**
**https://raw.githubusercontent.com/wiki/tobozo/Arduino/package\_deauther\_index.json**

![ip8SlbrAIhfKjkt.png](https://loukas.cn/wp-content/uploads/2020/04/1019827370.png)

**4.打开菜单 工具\开发板\开发板管理器，搜索“ esp8266”并先安装esp8266 ，然后是arduino-esp8266-deauther 选择版本2.0.0（必须2.0.0）**
![pzv1EiAhdJIUtlB.png](https://loukas.cn/wp-content/uploads/2020/04/2258298001.png)
**5.打开菜单 工具\管理库 搜索arduinojson 安装5.13.5版本**
![CsMLE5.png](https://loukas.cn/wp-content/uploads/2020/04/3901210782.png)
**6.用arduino IDE打开下载的esp8266\_deauther源码包里的esp8266\_deauther\esp8266\_deauther.ino**
![2CnG8QmgKoZvLVd.png](https://loukas.cn/wp-content/uploads/2020/04/1443574788.png)

**7.在Tools-> Board上选择你的开发板，并确保它位于ESP8266 Deauther Modules （而不是 ESP8266 Modules ）**
![ljGH5L.png](https://loukas.cn/wp-content/uploads/2020/04/1941176536.png)

**8.菜单操作 “工具\开发板\NodeMcu 1.0 (ESP-12E Module)”,这里根据自己购买的esp8266开发板选择对应的板子。注意开发板的端口要选择正确，否则不能下载编译好的固件，然后点工具栏里的上传按钮，编译和上传固件。**
![gA5Gzr.png](https://loukas.cn/wp-content/uploads/2020/04/3284716805.png)

**无法访问/ dev / ttyUSB0**
就在我以为一切顺利的时候，串口驱动出了问题..
![Qk9lcd.png](https://loukas.cn/wp-content/uploads/2020/04/3045631660.png)
经过一晚上的折腾后，还是找不到问题..啊啊啊啊..先不说了.睡一觉顶不住了啊
**第二天**
在我的不懈努力下..
终于找到了解决方法
**解决方法如下**
利用esptool串口工具烧录
安装esptool
`sudo pip install esptool`
安装完成后 打开arduino 菜单 项目\导出已编译的二进制文件
![t2KbSA.png](https://loukas.cn/wp-content/uploads/2020/04/3284906048.png)
然后点击 项目\显示项目文件夹 （为了方便把固件复制到/home/admin/Arduino/）
**擦除**
`su`
`esptool.py --port /dev/ttyUSB0 erase_flash`
![Ze3ADB.png](https://loukas.cn/wp-content/uploads/2020/04/3995504911.png)
**烧录**
`esptool.py --port /dev/ttyUSB0 -b 115200 write_flash 0x0000 /home/admin/Arduino/固件名称.bin`
**烧录完成**
![6LKFqT.png](https://loukas.cn/wp-content/uploads/2020/04/229415384.png)

## 使用

烧录成功后，会生成一个名称为pwned的热点，如果没有按一下板子上的RST，密码是:deauther,连接成功后，浏览器输入192.168.4.1，进入后台页面。
![RE87cJ.png](https://loukas.cn/wp-content/uploads/2020/04/314468872.png)
点击I have read and understood the notice above
**设置中文**
点击Setting 找到LANG 输入cn
![AdR5lV.png](https://loukas.cn/wp-content/uploads/2020/04/1014564256.png)
保存设置 按一下板子上的RST
重新连接wifi 退出浏览器重新打开 输入192.168.4.1进入后台页面（如果没有生效，清除浏览器缓存试试）
![KyWMqO.png](https://loukas.cn/wp-content/uploads/2020/04/2338332420.png)
ok成功设置成中文

## 攻击教程

**攻击模式介绍**
**Deauth**
通过向您选择的接入点和客户端设备发送解除认证帧来关闭WiFi设备的连接。
因为很多设备不使用802.11w-2009标准来抵御这种攻击。
请只选择一个目标！当您开始攻击的不同信道上的多个目标时，它将在这些信道之间快速切换，届时您将无法重新连接到此Web界面。
**Beacon**
信标帧(Beacon)数据包用于宣告接入点。通过不断发送信标帧数据包，看起来就像您创建了新的WiFi网络。
您可以通过SSID指定网络名称。
**Probe**
探测请求帧由客户端设备发送，以询问一个已知网络是否在附近。
通过请求您在SSID列表中指定的网络，以此来混淆WiFi跟踪器。
您可能不会在家庭网络中看到此次攻击的任何影响。

**示范**
**在扫描页面选择好目标后点击添加**
**进入攻击页面选择Deauth模式 点击开始攻击**
![XwMS4I.png](https://loukas.cn/wp-content/uploads/2020/04/2427809091.png)

**被攻击目标**
![NE6FBGYwuhncRrq.gif](https://loukas.cn/wp-content/uploads/2020/04/1893864807.gif)
从图片中能看到 目标已经连接不上了

[取消回复](https://blog.upx8.com/3722#respond-post-3722)

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