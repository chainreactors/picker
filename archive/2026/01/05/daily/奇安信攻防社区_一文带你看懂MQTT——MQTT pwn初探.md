---
title: 一文带你看懂MQTT——MQTT pwn初探
url: https://forum.butian.net/share/4691
source: 奇安信攻防社区
date: 2026-01-05
fetch_date: 2026-01-06T03:26:18.730612
---

# 一文带你看懂MQTT——MQTT pwn初探

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 一文带你看懂MQTT——MQTT pwn初探

* [CTF](https://forum.butian.net/topic/52)

本文详细讲解了MQTT协议的基本原理，环境搭建，并以两道经典MQTT-pwn例题详细讲解了MQTT协议在通信过程中的利用

MQTT讲解
======
MQTT（Message Queuing Telemetry Transport，消息队列遥测传输协议），是一种基于发布/订阅（publish/subscribe）模式的“轻量级”通讯协议，该协议构建于TCP/IP协议上，由IBM在1999年发布。
MQTT最大优点在于，用极少的代码和有限的带宽，为连接远程设备提供实时可靠的消息服务。
作为一种低开销、低带宽占用的即时通讯协议，使其在物联网、小型设备、移动应用等方面有较广泛的应用。
协议原理
----
实现MQTT协议需要客户端和服务器端通讯完成，在通讯过程中，MQTT协议中有三种身份：发布者（Publish）、代理（Broker）（服务器）、订阅者（Subscribe）。其中，消息的发布者和订阅者都是客户端，消息代理是服务器，消息发布者可以同时是订阅者。
MQTT传输的消息分为：主题（Topic）和负载（payload）两部分：
（1）Topic，可以理解为消息的类型，订阅者订阅（Subscribe）后，就会收到该主题的消息内容（payload）；
（2）payload，可以理解为消息的内容，是指订阅者具体要使用的内容。
### \*\*发布者 (Publisher)\*\*
功能： 负责产生数据和消息，并将这些指定topic的消息发送（发布/Publish）到 Broker。
### 代理/服务器（broker）
可以理解为提供 mqtt 服务的代理服务器 ，通俗一点来讲就是”邮局”或者说是”消息中转中心”，每个 client 之间的通信都必须通过 Broker 来进行。
简单来说，Broker就是一个中间人，负责管理所有客户端的连接，并确保消息能够从一个客户端安全、高效地传递到另一个或多个客户端。
### 订阅者（Subscribe）
功能： 负责接收它感兴趣的消息。它会提前告诉Broker它对哪个”主题”（Topic）的消息感兴趣（这个行为叫做订阅/Subscribe），就会接收订阅相同topic的client。
### \*\*客户端\*\*（\*\*Client\*\*）
客户端可以充当发布者，也可以充当订阅者，也可以同时充当两个角色
Client 是指任何连接到 Broker 的设备或应用程序 ，可以理解为”寄信人”和”收信人”。在物联网场景中，一个 `Client` 可以是一个温度传感器、一个智能灯泡、一部手机上的App，或者是一个在服务器上运行的数据分析程序。
### 示意图
client1，2，3，4同时连接broker，client1，2，3订阅topic"diag" ,这时client4发送topic为"diag" msg="hello"给broker，broker会向同时订阅topic="diag"的client1，2，3发送这个消息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-6b0e5e186edd42862f8fd027da76c672665ce183.png)
环境配置
----
### 1.使用安装 Mosquitto MQTT
sudo apt update
sudo apt install mosquitto mosquitto-clients
### 2.启动服务并设置开机自启
```php
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```
### 3.配置conf
```php
sudo vim /etc/mosquitto/mosquitto.conf
```
在文件中添加
```php
listener 1883 #设置监听端口为 1883
allow\_anonymous true # 可选，允许匿名访问（默认）
```
摁“Esc”+“：wq”退出后终端输入
```php
sudo systemctl restart mosquitto # 重启服务
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-f96a35fc79679855152bb58158f0298d298fc867.png)
netstat -lnvp查看一下，可以看到1883端口已经开始监听
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-9e0f9a1884dc569ce8984140f21d74e1b33d88c2.png)
### 下载mqttx
[MQTTX Download](https://mqttx.app/downloads?os=windows)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-fb0f76d78194af3729d3cad7a8d4e09adea645b3.png)
点击新建连接，我这里是wsl启动的，但是监听了所有ip的端口，所以ip直接填0.0.0.0
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-b1ea63f86a78a2e37bc39125406ff54d986c9822.png)
添加一个订阅
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c6dbd5c19d111b6cc56d66c51732c60b2e49df04.png)
利用终端进行连接测试
终端输入
```php
mosquitto\_pub -h localhost -t testtopic -m "Hello MQTT"
```
可以看到在客户端已经收到了消息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-000fe5a7b6c744aafb90e61fe5fa3a1af99521a3.png)
终端输入
```php
mosquitto\_sub -h localhost -t testtopic
```
用来订阅这个消息，在客户端输入主题testtopic
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-fdb69f41f2785d963d55d2cb758cf7bcbe3948be.png)
发送之后，在客户端和终端界面均可以看到刚才发的消息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-f54981d0190e22308b2acf37a6e2ba8a24e1e749.png)
python使用mqtt
------------
```php
pip install paho-mqtt
```
### 发送端
```php
# -\*- coding: utf-8 -\*-# -\*- coding: utf-8 -\*-
import paho.mqtt.client as mqtt
import time
def on\_connect(client, userdata, flags, rc):
print("链接")
print("Connected with result code: " + str(rc))
def on\_message(client, userdata, msg):
print("消息内容")
print(msg.topic + " " + str(msg.payload))
# 订阅回调
def on\_subscribe(client, userdata, mid, granted\_qos):
print("订阅")
print("On Subscribed: qos = %d" % granted\_qos)
pass
# 取消订阅回调
def on\_unsubscribe(client, userdata, mid, granted\_qos):
print("取消订阅")
print("On unSubscribed: qos = %d" % granted\_qos)
pass
# 发布消息回调
def on\_publish(client, userdata, mid):
print("发布消息")
print("On onPublish: qos = %d" % mid)
pass
# 断开链接回调
def on\_disconnect(client, userdata, rc):
print("断开链接")
print("Unexpected disconnection rc = " + str(rc))
pass
client = mqtt.Client()
client.on\_connect = on\_connect
client.on\_message = on\_message
client.on\_publish = on\_publish
client.on\_disconnect = on\_disconnect
client.on\_unsubscribe = on\_unsubscribe
client.on\_subscribe = on\_subscribe
client.connect('127.0.0.1', 1883, 600) # 600为keepalive的时间间隔
while True:
client.publish(topic='testtopic', payload='amazing', qos=0, retain=False)
time.sleep(2)
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-448bc81a0973104105d9e827d1e1ef8f158cd649.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-5e06480251dc3bd0681ab1d2c5fb07ed29f43615.png)
### 接收端
```php
# -\*- coding: utf-8 -\*-# -\*- coding: utf-8 -\*-
import paho.mqtt.client as mqtt
import time
def on\_connect(client, userdata, flags, rc):
print("链接")
print("Connected with result code: " + str(rc))
def on\_message(client, userdata, msg):
print("消息内容")
print(msg.topic + " " + str(msg.payload))
# 订阅回调
def on\_subscribe(client, userdata, mid, granted\_qos):
print("订阅")
print("On Subscribed: qos = %d" % granted\_qos)
pass
# 取消订阅回调
def on\_unsubscribe(client, userdata, mid, granted\_qos):
print("取消订阅")
print("On unSubscribed: qos = %d" % granted\_qos)
pass
# 发布消息回调
def on\_publish(client, userdata, mid):
print("发布消息")
print("On onPublish: id = %d" % mid)
pass
# 断开链接回调
def on\_disconnect(client, userdata, rc):
print("断开链接")
print("Unexpected disconnection rc = " + str(rc))
pass
client = mqtt.Client()
client.on\_connect = on\_connect
client.on\_message = on\_message
client.on\_publish = on\_publish
client.on\_disconnect = on\_disconnect
client.on\_unsubscribe = on\_unsubscribe
client.on\_subscribe = on\_subscribe
client.connect('127.0.0.1', 1883, 600) # 600为keepalive的时间间隔
client.subscribe('testtopic', qos=0)
client.loop\_forever() # 保持连接
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-9f9835b40447f98741df5e80a2dbc37ae50fcdfe.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e0a07b532eb0129535038e3686cce06d0554b19d.png)
例题讲解
====
CISCN2025——final mqtt
---------------------
### 题目分析
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e6b8c0143d6babbac0ad5b0812ba2ac8167fa8b0.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-f0954c82c04b479a5cc2f737c483ffa3dac88803.png)
程序首先会读取两个文件，如果文件不存在则直接退出
所以首先需要创建两个文件
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-c041def583467cbcd797ce33a688e5bf50ceab03.png)
接着会创建一个mqtt客户端，但是这里要求broker的监听端口是9999，所以我们需要改一下端口，修改方式上文说过
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-6d5ad365c141232734968c4a8505eee6ba6d3cef.png)
成功启动服务
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-4feb6cd1952ae8189df47c4aebd33e6612304e01.png)
首先程序会在订阅的diag主题中接受auth，cmd，arg三个参数，而且arg参数存放在bss段上
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-57a59d94e579970f503ab65824ba61f6b8caf9e1.png)
在start\\_routine函数中，会首先进行一个认证
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-aa19f9cd5b30c1973ff4fa0d42dcc6d9f0a1aca2.png)
认证的逻辑就是将接收到的VIN码转成十六进制（其实就是在考察mqtt接受数据），不多赘述了
随后根据cmd值，可以调用set\\_vin命令
![image.png](https://cdn-yg-zzbm.yun.qianxin...