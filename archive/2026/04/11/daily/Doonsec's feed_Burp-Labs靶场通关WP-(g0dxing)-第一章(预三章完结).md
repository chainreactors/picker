---
title: Burp-Labs靶场通关WP-(g0dxing)-第一章(预三章完结)
url: https://mp.weixin.qq.com/s/0WirLwiK4IMnumSyMbUP3Q
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:46:18.467394
---

# Burp-Labs靶场通关WP-(g0dxing)-第一章(预三章完结)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zFpHumWDiczp70UNNxdQ8zNh2P2OXRrufIM0Vh1gSKGmdQjLCib9ECEibLj3BcGPwwMpcx043IicUSEErkJPiaMsKcLCcLhAgxhibWUGE8hgpLoRA/0?wx_fmt=jpeg)

# Burp-Labs靶场通关WP-(g0dxing)-第一章(预三章完结)

原创

Xudde
Xudde

Xudde-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

项目地址：https://github.com/g0dxing/burp-labs

靶场介绍：该靶场初衷是为了学习使用burpsuite对登录框场景进行暴力破解登录账户，靶场分为基础篇(4关)、中级篇(5关)、高级篇(7关)、专家篇(15关)和综合篇(2关)，关卡难度呈逐渐递增式，靶场仅用于教育目的和授权测试。请勿将所学技术用于非法用途。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczptKD3ibh7H9yu1dHX05ETFDegGIgQVOBGmib4c5A6rLTbTASwlzYsibxOLJOb3Ob2uf8nn4XFD6O6NiaV1e2TL9hoqTYHc5aibrJP8/640?wx_fmt=png&from=appmsg)

安装方式：下载项目，使用PHPstudy，无需安装数据库

本次更基础篇、中级篇和高级篇

基础篇

## Level 1

### 基础爆破

通关方法：

    将登录的包发送至Intruder模块，选择password参数的值，将其设置为payload，导入password的top1000字典，爆破

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczr0JKcZ8szO9nSuQhPowTWjkXEprpYgoJxfEibtiaFSslibdARxLnRD3UApk6syVubhZeiaA9zGyVgk2dC8L1PpbuDtTuX4Laibn6A0/640?wx_fmt=png&from=appmsg)

    爆破完成的时候点击视图过滤功能，输入登录成功返回的字段success，可以看见这关的密码为123456789

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczquvgicF555WDsDostmcKAWfqibMuO8u3a3WHj0BaDgMKnKK0kEuLdIWSGliaF0WVguKZGJGdkT2PlQcoNpV6PUwicEV984fWXeJhM/640?wx_fmt=png&from=appmsg)

tips~

    在不确定登录成功的时候返回的字段是什么字段的时候可以使用正则表达式匹配，或者使用长度大小模糊查看判断是否登录成功

## Level 2

### 响应过滤

通关方法：

    一样的操作，将登录请求包发到Intruder模块，选定payload点，导入top1000的密码字典，账号依旧是admin，点击视图过滤功能输入登陆成功字段即可快速判断，爆破结果密码为password，这关的登录成功和登录失败的响应长度被改成一样的了，所以用视图过滤比较快

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczq7c7HHL2z1JgqBpTSwhBDZm0KIqGaasYlumvzia6Bm4cSRuqs1xyQs27tld02lHiabohEez9UUFcLWgzVkvpEHU8o9K3soLxJWU/640?wx_fmt=png&from=appmsg)

## Level 3

### 用户名枚举

通关方法：

    这关需要枚举用户名，然后才能爆破密码，登录admin的时候提示用户名错误（username error），先爆破用户名，将登录包发送到Intruder模块，选定用户名参数值，添加payload位置，导入用户名top500，开始爆破，然后利用响应包返回的长度判断用户名，或者视图过滤password error字符串为存在的用户名

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczqOuHzkA5uEOBicDQRfB7zo3aWxN9TgVicGOS3ApXniap1DjUzVg9KWFpDeYgpFAib0Vu3NoO3sEvHWicXFgicyP0wYILsU11d2sYpZs/640?wx_fmt=png&from=appmsg)

    修改用户名继续爆破密码，导入密码top1000爆破，最终密码结果为123456789

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczodxZMRWPncmRAqZ58Ww6OKFribaNc1DsnymHiaE6texoYg1DKkS8ysEOsEAyIe1GBTibNH4QibeczxhGMMXib5GcaOibrib6sCOAf5Bo/640?wx_fmt=png&from=appmsg)

## Level 4

### 高级过滤

通关方法：

    这关admin用户依旧提示username error，重复Level 3方法，依靠响应包返回的长度判断，发现用户名为test，提示的是login error!!!

爆破密码导入为top1000字典，密码爆破结果为123456789

    以上就是基础篇，一些使用burpsuite爆破的基础使用操作和判断方法

中级篇（5关）

## Level 1

### POST攻击

通关方法：

    在基础篇上，本关换成了POST请求方法，登录请求包发送到Intruder模块，password参数添加payload位置，导入密码top1000字典，梭哈！视图过滤输入success字符串，即可爆破结果为admin/123456789

## Level 2

### 中文响应

通关方法：

    作者在登录框中提示多尝试几个字典，根据题意，登录成功的话响应可能是登录成功的字段了，爆破完之后试图过滤就对号入座了，但是结果并不是，这关可以通过响应头长度判断是否登录成功，最终使用top1000字典，出的结果为admin/77777

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrk2bfmcUPdy6dWIHCHPNjlcWoe43EgHysP4GAnUldqtLDs5w0gq19L2CFn8shIia6RcVBsNaKFByXkqRRqsrTLGheCmxiaoicdicI/640?wx_fmt=png&from=appmsg)

## Level 3

### 重定向处理

通关方法：

    根据提议，如果登录成功就看响应状态码是否为重定向，这次对战中密码top1000字典战败了，请来了个更强大的大哥，密码top3000，结果也是失败告终，无奈之下密码top6000大哥闪亮登场！几下霍霍之间拿下战功！状态码302重定向跳转出现，账号密码就是admin/admin@123

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrv6ickhNJfiahibXXuhCzbZic3YoEpZ4HvY7jU3soq3GqItzHaGibUiaLYkbbbonVRQNB62Kia9o772ZhmBZJ3lMv6CA7xgSy1uVxwb8/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczqhtBpLnO0xMq2tvqtYZ71KYQltboia99SMhAgQmchOjFicgBUOtkMDBTSLBicCBUNuqJRjf6DiaSAQPdVV5wNbg0eCYTcAUB92Yqc/640?wx_fmt=png&from=appmsg)

## Level 4

### Base64编码

通关方法：

    根据题意或者根据前端Javascript脚本明白，本关对密码进行了base64编码加密

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczrfFScED8m3cYwktMcyzx1wRunIthxutT0W0YMQXhSfFhSBtKSNdmhemZ0Qv9DuD6X4wjGn37dLZdmstMZhMLYQr2Jy31B9Mzo/640?wx_fmt=png&from=appmsg)

    但是在传输的过程中呢，对base64加密有等于号=的结果进行了URL编码，将等于号=编码成了%3D，按这个操作，破解base64加密传输密码，但是后面又试了一下，发现不用URL编码也行

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczpx8wnjrVoFicKHicUVBq02zOkzKyc06GNSst1ib4rUUbfYM0UsyMLzIDJMpVSdibrEWribicavxSBRkX6ECNA33cpFPhh6KVNzKj5V0/640?wx_fmt=png&from=appmsg)

    最后，发现原本的top密码全部倒下了，看了一下字典的字母都是小写字母，将字母全部变成了大写，用top6000字典终于过了，最终密码是LOVE5201314，翻了一下其他密码字典发现LOVE5201314这个密码在rockyou-part1的100万位置，方法是在payload处理处先写入转换为大写，把base64编码放到后面

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczqJRxqibK1iaBIKQ6hCiaBurZydUfqxgicC8u96GwibpCzNHnyAz0CIHeL1vtaONhq0tNMd7y0VHTX5J1gIXe8HnIkVeOLlcvXicphia4/640?wx_fmt=png&from=appmsg)

## Level 5

### MD5加密

通过方法：

本关对密码传输的时候使用了md5加密

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczq5b24Vyer1sVlgOkWBZhGic1b9iczhEsqT4ouhoCfScaWRBRbaahmZfh6rU65x0AsTgXOcN0iaJGlA5H5HB1sxs7yv63tvobDOfg/640?wx_fmt=png&from=appmsg)

    获取请求包，payload处理处添加，选Hash，下拉找到MD5确定，爆破结束后依靠响应包长度判断登录成功，查看请求包序号，找到top6000密码，爆破结果密码为8个1，admin/11111111

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrdrMyaGDkloqFzU8eUQz4PI0rld6JQAHdTZPZBFxvuM0mHH2CjicZnDY9t3F5UeG7teMJPpx9rMMj2U7WodCxShOaQYIoGW7ow/640?wx_fmt=png&from=appmsg)

高级篇（7关）

## Level 1

### 双参数攻击

通关方法：

    Intruder模块调整为Pitchfork攻击模式，给两个参数上top6000密码字典，第二个参数需要MD5加密

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrwk1ic4ndunlEkT82jic82KaLra31XgdKoYdxC0XVaerAJn9aYGicQoSF8dEpHRAicFkKCgTHr5tqhNJ7MYQw8O0t5goSYiaDbqfC8/640?wx_fmt=png&from=appmsg)

    最终爆破结果，admin/abc123456

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrTLuaBbibaPhBg2ls2MWibr53kJsWVJ7rxSUfsNJWhduuhzKnzSdg4CNvrEeibAoufianOM3DPKD0ibaibuwdByz03HHKBpHDsJwmlM/640?wx_fmt=png&from=appmsg)

##

## Level 2

### 前缀处理

通关方法：

    你可以这样

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczraGHfJH21KFmLLgWNabRsXMyAtOB9ho1l5Ty3TOf1F9y9LibD1oxUhuqxdlaQRDVkMtnEflk8HhRliaQsYcWGJRZVoeYNcJHwbU/640?wx_fmt=png&from=appmsg)

    也可以这样

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczrEApMQtIQWh8btEpR7ta74rmbDy3lGh5iboAjENLstkRMeSAFtbwWdOKZYnVwd53I0LJrKSiaPHXcxq506MhEezleqGUQe4icV2k/640?wx_fmt=png&from=appmsg)

    最终使用top1000字典，账号密码为admin/123456，长度错误和成功的长度一样，需要用视图过滤success字符串

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczoQEHcl1NoRrB5hOAzFwdibD2w35O2BzTfzDvl4twiaJibjqtUQrDJFbJfI6MkPxrpehy3q7CrgfVKdet98knEbmu8EZNSgSeHpZc/640?wx_fmt=png&from=appmsg)

##

## Level 3

### 时间戳验证

通关方法：

    这关有点麻烦，burpsuite找不到时间戳，应该是没有了，只能装插件，但不知道哪个有，听说Yakit的热加载牛，网上翻了也是用Yakit解的，我也没怎么用过Yakit哈

启动Yakit后点击临时项目

    首页有个MITM交互式劫持，设置好监听端口启动就行，跟burpsuite的proxy代理模块是一个意思

    导入字典步骤

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczpBuibCCHss7brPOQxdJEum5AlnVMmSScTSNmw9C1ZaOlSlPYVCKqBgIRHhoibUQYV1Iicme6WGl4WRRzice9woGWhgpjudfHnrTFQ/640?wx_fmt=png&from=appmsg)

    在MITM交互式劫持中抓到登录包，发送到WebFuzzer模块，这个模块跟burpsuite的Repeater模块和Intruder模块是重合的，像是burpsuite的加强版，但是我用不熟哈

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczpdnHgZqfr4Udbz3Ts8A7EIuMXwVHDEeRte4TX9Lc7ibHIYZuzytmEz5ibbqkjthzSxCqIwqI7ORGXlXZGU5sda8F7UbkBOpIW5k/640?wx_fmt=png&from=appmsg)

    任意点一个地方鼠标停留就有这个插入标签，找到插入Payload和时间戳，点击password参数值选中插入Payload，指点是你导入的名字，Timestamp参数点时间戳就行，发送请求就可以开始爆破了

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczpxyMx3a6mfSickqFFphySfc7YgY1iazhQu0kgq88rnrLrMwuPxaVqlULEjU7rQHCW1l0gibibltSOXaru7txbiaqzwFVqdp9Nw1qTg/640?wx_fmt=png&from=appmsg)

    在MITM交互式劫持这里过滤处欢迎这关字符串就可以看到爆破成功的密码了，最后显示是admin/78963245

![0](https://mmbiz.qpic.cn/mmbiz_png/zFpHumWDiczo5HgfavP3SF0PM3p3a7hoYCKAGVxL3dYMibRO4LOoGclbiafjXWeZomaepJumaLf0HS8k6hceswwKb4kUwzm8Lb8PiaU6Psq8Rb8/640?wx_fmt=png&from=appmsg)

    如果后面你其他浏览器突然不能正常使用了，就打开控制面板，系统安全，网络和Internet，按照这个步骤关掉代理服务器就可以正常使用了

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczqV4feGL69jH3pwWmz2SHsG1VycM7GWL04bZHV4FQu79YyictJuZ7DdibzvZhM9t2yYCSmbluG7ric3GfvlC68t3D0pb4W3wvOc3I/640?wx_fmt=png&from=appmsg)

Level 4

JSON格式

通关方法：

    登录请求包可以看到请求使用了JSON格式， 响应包也回显JSON格式，返回的中文变成了Unicode编码，但是我们可以看到success的值是false，登录失败是false，那么成功就是true了，最后使用top1000字典爆出密码是1314521521

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrEX2sYxQvNsxT7D22WNtibJ9VMzvrvNLX8snk3u0rKcEskaZalp3dLDAiagFkFxhDhZO4KJe4ZcymodUPcucBFicksQEjXdJ69Zc/640?wx_fmt=png&from=appmsg)

## Level 5

### Base64+JSON

通关方法：

    有看到使用了Base64编码和JSON格式的数据传输

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/zFpHumWDiczrOBp4A8HS4nZKKtFPlMcjuEmVibeialdibKqv...