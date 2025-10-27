---
title: 红队攻防 | 外网打点不靠0day组合拳拿下目标系统
url: https://forum.butian.net/share/4573
source: 奇安信攻防社区
date: 2025-09-27
fetch_date: 2025-10-02T20:45:24.930094
---

# 红队攻防 | 外网打点不靠0day组合拳拿下目标系统

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
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 红队攻防 | 外网打点不靠0day组合拳拿下目标系统

* [渗透测试](https://forum.butian.net/topic/47)

本案例所使用的素材来源于过往参与的攻防对抗比赛及众测项目，选取比较有意思的案例分享，旨在拓展外网打点的思路与技巧。文中涉及的图片及相关信息均已进行了脱敏与处理，如有与实际场景存在相似或雷同之处，纯属巧合！

### 前言
如果你要问我在红队攻防中最喜欢哪一环，我的答案毫无疑问是\*\*外网打点\*\*，它是整个攻防链条的起点，也是最具探索乐趣的阶段。从零开始，面对一个完全陌生的目标，你需要通过公开信息、域名解析、网站目录探测等手段，逐步描绘出目标的外部轮廓。每一条信息、每一个细节都可能成为突破口，正是这种从无到有、逐步拿下的过程，让外网打点成为红队攻防中最令人兴奋和成就感最强的一环!
### 前期准备防溯源
临时VPS：[https://aws.amazon.com/cn/campaigns/nc20241001/?trk=870dbb43-c500-4476-8a82-5ea9637bd7a7&amp;sc\\_channel=psm](https://aws.amazon.com/cn/campaigns/nc20241001/?trk=870dbb43-c500-4476-8a82-5ea9637bd7a7&amp;sc\_channel=psm)
代理节点IP：<https://www.feiyuip.com/>
记得勾选掉线禁用网卡✔，防止网络切换过程中泄露真实出口IP
![image-20241107115436931](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241107115436931.png)
### 演习规则解读
| 注意事项 | 内容 |
|---|---|
| 优先目标 | 攻击范围：提前沟通好目标分子公司是否算范围内 多倍积分：关注多倍积分目标，方法用对，事半功倍 |
| 协同合作 | 人员分工：A负责外网打点，B负责内网横向等 成果同步：避免浪费人力，成果通过语雀或雨墨同步 |
| 现场洞察预判 | 拿分目标：研读得分规则，关注大屏攻击动态，找侧重目标 关注动态：关注大屏防守方扣分情况，根据出局线预判即将下线单位，可优先集火攻击 |
| 场外信息获取 | 从裁判处合理获取信息，如目标、时间信息、成果是否值得深入等 |
| 成果最大化 | 突出危害：数据量和危害性，危害、影响描述尽可能大 报告展示：所有成果按攻击路径依次罗列，标注好入口和横向方式 |
### JS隐藏注册页面--短信验证回显--断点调试获取动态密钥--越权获取其他用户手机--登入管理员后台
在渗透测试过程中，要善于通过js挖掘隐藏接口，找到那些没有在前端页面明面暴露的遗留或测试接口
- 可通过全局检索js代码，查找路由配置、接口注释或服务端代码中的注册逻辑
- 通过修改常见的注册接口路径（如 `/api/register`， `/user/signup`， `/auth/create`）尝试访问，看看是否有响应。
- 结合字典爆破（如使用 dirbuster、ffuf 等工具）扫描可能的接口路径
这里通过全局检索js代码 `register`字段
![image-20250808142828356](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250808142828356.png)
正想拿小号接收个短信验证码，突然发现 `/xxx/sendsmscode/`接口泄露了验证码内容信息
![image-20250907164521729](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907164521729.png)
存在短信验证码回显，意味着我们可以伪造任意手机号进行系统登录，但如何获得管理员的手机号呢？
这时候脑海里有三个思路
- 社工手段获取目标管理员手机号（通过各种搜索引擎，打电话均无结果，放弃）
- 手机号爆破（尝试爆破了几万次，成功次数为0，也放弃）
- 最后决定进入后台挖掘越权漏洞
随意手机号注册系统，抓包发现数据包为加密字段
![image-20241128165126443](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128165126443.png)
通用思路，首先确认加密函数位置，设置条件断点（如访问 `encrypt` 字段或调用 AES-GCM 函数时触发）
然后观察函数参数，尤其是密钥和初始化向量（IV）参数，接着跟踪密钥的来源，看是否硬编码或通过密钥交换生成
这里全局搜索`encrypt`字段，发现使用的AES-GCM加密方式，加断点动态调试获取session key
![image-20240827100335708](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20240827100335708.png)
PS：这里的session key是一次性，刷新页面就会变化
使用AES-transfer 插件自动替换字段
![image-20241128164326497](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128164326497.png)
成功获取明文数据
![image-20241128170009559](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128170009559.png)
成功解密出数据后，开始寻找可能存在越权的接口
\*\*这里有小技巧: 可以通过搜索存在id参数的接口，配合hae插件泄露用户信息提示快速挖掘越权\*\*
最终通过 `/xxx/xxx/Getinfo?pageIndex=1&pageSize=15&key=1&id=72`
成功找到越权点获取管理员的手机号
![image-20250808150027133](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250808150027133.png)
最后利用管理员的手机号--短信验证回显成功登录后台
![image-20250830162036135](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250830162036135.png)
### 小程序弱口令爆破--Fuzz相似api接口越权--hash碰撞获取管理员密码--接管高权限账户
通过微信小程序搜索目标单位，发现一处后勤管控平台资产
![image-20241112190031206](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241112190031206.png)
shiro框架的，爆破一波key试试，好吧不成功
![image-20241115154324658](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241115154324658.png)
像这样的系统一般以员工工号作为用户名，通过google语法搜出工号位数为5位数字（类似10001，10002）
固定密码为123456，祭出我的Top1000用户名进行爆破，成功爆破出三个弱口令
![image-20241115153943943](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241115153943943.png)
这时候继续翻找功能点，毕竟弱口令才20分一个
从history中翻出这么一个接口，StaffListV2返回包提示没权限，尝试Fuzz相似接口
![image-20241105182344754](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241105182344754.png)
尝试把 `StaffListV2` 修改为 `StaffListV1、StaffListV3、StaffList`
发现`StaffList`没做鉴权，能够获取所有员工的邮箱和工号信息
![image-20250830162414689](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250830162414689.png)
接着通过小程序解包找到web后台管理地址：<https://api.xxxx-admin.com>
小程序解包项目：<https://github.com/Ackites/KillWxapkg>
![image-20250817170821666](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250817170821666.png)
利用小程序爆破出的账号密码进行登录
![image-20241128170524178](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128170524178.png)
但由于我们爆破出的账号为普通员工账号，因此后台没有数据，所以我还需要去尝试接管管理员账号
![image-20241128172251280](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128172251280.png)
翻看history数据包，发现在修改密码功能有一个api接口返回了用户名`pwd\_hash`
![image-20250817165841898](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250817165841898.png)
通过传入userid可以越权查看他人的pwd\\_hash，刚好我们在StaffList接口能够获取所有员工的userid
接着分析pwd\\_hash，虽然无法直接解密，但返回包中包含了随机的salt值
![image-20241128172046124](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128172046124.png)
分析后发现 pwd\\_hash=(password md5--salt)sha256，根据此编写对应的碰撞脚本
1.使用密码和盐值生成基于 MD5 和 SHA-256 的哈希值。
2.从指定文件中读取密码列表，每行一个密码。
3.将密码文件中的每个密码与提取的盐值和哈希进行比对，找到匹配项
![image-20241128171554010](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128171554010.png)
成功碰撞出高权限账户密码 1qaz@WSX
![image-20241128171419990](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20241128171419990.png)
### 反编译app找到系统--暴力破解bypass--配置文件获取数据库账密--获取数万用户数据
通过jadx反编译app，找到管理系统域名地址
![image.png](https://photoscloud.oss-cn-shanghai.aliyuncs.com/20240315143134.png)
在攻防对抗中，通过弱口令获得权限的情况占据90%以上，很多企业员工用类似test123、test888这种账号拼音或其简单变形，或者123456、888888、手机号后6位等作为密码，生成简单的密码字典进行枚举即可获取有效账户密码拿下目标系统
这个系统有2个难点：
- 首先是登录页面有数字验证码，不能直接暴力破解
- 密码是加密的，需要找到password字段加密相关函数
![image-20250907163332975](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907163332975.png)
\*\*验证码解决方法：\*\*
[https://github.com/smxiazi/NEW\\_xp\\_CAPTCHA](https://github.com/smxiazi/NEW\_xp\_CAPTCHA)
直接`pip install muggle\_ocr`安装会报错，由于官方对其模块进行下架
使用命令`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple muggle\_ocr`
默认监听本地的8899端口，可通过server.py进行修改
![image-20250907162051856](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907162051856.png)
定位验证码功能的url，抓包发送到验证码识别模块
![image-20250907161627571](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907161627571.png)
对验证码设置参数，转到payloads模块进行如下配置
![image-20250907161726641](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907161726641.png)
实现效果：
![image-20250907162238264](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907162238264.png)
\*\*password加密解决方法：\*\*
通过搜索encrypt字段找到密码加密的函数位置
![image-20250907162705728](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907162705728.png)
编写脚本对密码字段进行RSA批量加密
![image-20250905163800168](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250905163800168.png)
成功爆破出有效的账户密码
![image-20250907165150003](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907165150003.png)
找到许可证功能点--文件上传，没有任何拦截很舒服
![image-20250904164637581](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250904164637581.png)
getshell后发现为iis权限，权限太低只能浏览部分文件，很多命令无法执行
![image-20250904165019287](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250904165019287.png)
通过 `web.config` 文件找到数据库账密，根据表名定位用户数据表，可获取数万用户数据
![image-20250904165724436](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250904165724436.png)
mysql&gt; select count(\\*) from xxx;
+----------+
| count(\\*) |
+----------+
| 134783 |
+----------+
1 row in set
![image-20250907171442867](https://photoscloud.oss-cn-shanghai.aliyuncs.com/image-20250907171442867.png)
### 被动指纹识别--swagger信息泄露获取token--命令执行
![image-20250907173931197](https://photoscloud.os...