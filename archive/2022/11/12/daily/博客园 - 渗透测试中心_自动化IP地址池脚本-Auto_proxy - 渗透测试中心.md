---
title: 自动化IP地址池脚本-Auto_proxy - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16879485.html
source: 博客园 - 渗透测试中心
date: 2022-11-12
fetch_date: 2025-10-03T22:32:25.094157
---

# 自动化IP地址池脚本-Auto_proxy - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [自动化IP地址池脚本-Auto\_proxy](https://www.cnblogs.com/backlion/p/16879485.html "发布于 2022-11-11 08:49")

利用Python脚本自动生成Clash配置文件，实现FUZZ自动切换IP。

现在蓝狗封IP速度太快了，想想当年自己用Burp爆破封堵IP的日子就想哭。
不要问我为啥不用飞鱼，太贵了。

### 0x00 购买IP地址池

推荐余额套餐的方式进行购买，该脚本配合余额支付更划算。
<http://http.py.cn/pay/?paytype=banlance>

### 0x01  获取API接口

购买套餐后，选择》API提取》直接提取，推荐配置如下：

* 1.余额提取。
* 2.使用时长按需选择，建议选择25分钟-180分钟。
* 3.提取数量建议为5-10，土豪随意。
* 4.建议省份混拨，并选择自己所在省份或临近省份，提高访问速度。
* 5.目前该代理协议仅支持SOKCS5连接。
* 6.数据格式选择Json格式，方便脚本解析。
* 7.选择属性全部勾选，否则会发生错误。
* 8.IP去重365天。

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090411607-1690240950.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/1.jpg)

### 0x02  部署说明

将Auto\_proxy代码（Auto\_proxy\_example.yaml, Auto\_proxy.py, proxyIgnoreList.plist ）拷贝到Clash配置文件目录下。

* Windows默认：Clash\Data\profiles\
* Mac默认：~/.config/clash/

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090410577-2118250315.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/2.jpg)

修改Auto\_proxy.py相关配置，主要参数如下。

* test\_url：需要监控测试的IP地址。
* py\_api：上一步获取的品易API接口。
* max\_connect\_error：错误连接次数，连续连接错误N次，重新获取代理。

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090411288-1094733470.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/3.jpg)

白名单配置，可参考<https://www.cnblogs.com/PowerTips/p/14775956.html>

* Windows：在Auto\_proxy\_example.yaml添加cfw-bypass配置。
* Mac: 直接使用项目中proxyIgnoreList.plist即可，需重启生效。

注：务必将\*.taolop.com加入白名单中，不然可能会导致代理失效一直重复获取代理。

### 0x03 使用说明

在Clash目录下执行python3 Auto\_proxy.py，同时Clash将配置选为Auto\_proxy。

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090410284-2096815572.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/4.jpg)

需将Clash配置为全局模式，同时设置系统代理，目前脚本设置两种规则：

* 加速模式：根据监控网站选择延迟最低的代理。
* 负载模式：每次请求都会随机一条代理进行连接。

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090410942-27601757.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/5.jpg)

负载模式运行效果：

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090411215-816722526.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/6.jpg)

当运行错误超出设置阀值，会进行提示“IP已被封禁，重新获取代理”，此时Clash提示“重载配置文件”，需手动点击更新。

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090410283-1657727635.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/7.jpg)

### 0x05 使用效果

该效果模式为负载模式，测试Dirsearch, 其它工具请自行测试。

* 靶机端： python3 -m http.server 8000
* 攻击端： python3 dirsearch.py -u [http://X.X.X.X:8000](http://x.x.x.x:8000/) --proxy=[http://127.0.0.1:7890](http://127.0.0.1:7890/)

[![image](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221111090411674-1770756501.jpg)](https://github.com/Mustard404/Auto_proxy/blob/main/demo/8.jpg)

同时10个IP爆破目录，就问你慌不慌！

posted @
2022-11-11 08:49
[渗透测试中心](https://www.cnblogs.com/backlion)
阅读(2639)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025