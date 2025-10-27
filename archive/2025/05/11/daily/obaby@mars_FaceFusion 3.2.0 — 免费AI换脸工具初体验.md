---
title: FaceFusion 3.2.0 — 免费AI换脸工具初体验
url: https://h4ck.org.cn/2025/05/20613
source: obaby@mars
date: 2025-05-11
fetch_date: 2025-10-06T22:24:42.711160
---

# FaceFusion 3.2.0 — 免费AI换脸工具初体验

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[业余爱好『Favourite』](https://h4ck.org.cn/cats/cxsj/%E4%B8%9A%E4%BD%99%E7%88%B1%E5%A5%BD%E3%80%8Efavourite%E3%80%8F), [个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# FaceFusion 3.2.0 — 免费AI换脸工具初体验

2025年5月10日
[57 条评论](https://h4ck.org.cn/2025/05/20613#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/05/微信图片_20250510183941.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510183941.jpg)

‌FaceFusion‌是一款功能强大的AI换脸软件，支持图片、视频和直播的换脸功能，其换脸效果真实、自然。FaceFusion不仅支持N卡处理程序（如Azure），还提供了CPU处理模式，适合各种硬件配置的用户使用‌。

功能特点：

1. ‌多平台兼容‌：支持NVIDIA和AMD等主流显卡平台，满足不同用户的硬件需求‌。
2. ‌多种处理模式‌：提供人脸替换、人脸高清修复和背景高清修复等多种策略，每种策略下包含多个模型可自由切换‌。
3. ‌自定义设置‌：用户可以自定义执行线程、执行队列、最大内存和输出路径，电脑配置好的情况下可以适当调大这些参数‌。
4. ‌预览功能‌：提供预览功能，可以自由选择换脸对象和多人换脸，单人换脸通过方位选择人脸、年龄选择人脸、以及性别选择人脸‌。
5. ‌唇形同步‌：引入wave2lip处理器，同步口型动作，使视频更加自然‌。
6. ‌面部对齐改进‌：通过68比5的地标变换，提高面部对齐的精确度‌。
7. ‌新模型支持‌：增加uniface\_256模型，提供更高质量的换脸选项；集成yoloface作为默认的人脸检测器模型，提升检测效率‌。

换脸这个东西，起之前也尝试过faceswap，然而，这个东西使用起来的确麻烦，需要提供的素材数量比较多，训练过程比较繁琐，并且最终的效果在样本数量不够大的时候就会发现实际效果一般：

> [让自己变成AV的主角【faceswap】](https://h4ck.org.cn/2021/12/9586)

当然，图片换脸目前腾讯元宝提供了免费的传图换脸的功能，整体效果还是挺不错的。下面的是基于腾讯元宝来实现的：

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192606-811x1024.jpg "微信图片_20250510192606")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192606.jpg "微信图片_20250510192606")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192652-733x1024.jpg "微信图片_20250510192652")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192652.jpg "微信图片_20250510192652")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192653-784x1024.jpg "微信图片_20250510192653")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192653.jpg "微信图片_20250510192653")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192654-886x1024.jpg "微信图片_20250510192654")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192654.jpg "微信图片_20250510192654")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192655-427x1024.jpg "微信图片_20250510192655")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192655.jpg "微信图片_20250510192655")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192656-806x1024.jpg "微信图片_20250510192656")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192656.jpg "微信图片_20250510192656")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192657-876x1024.jpg "微信图片_20250510192657")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192657.jpg "微信图片_20250510192657")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192658-780x1024.jpg "微信图片_20250510192658")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192658.jpg "微信图片_20250510192658")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_20250510192659-887x1024.jpg "微信图片_20250510192659")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250510192659.jpg "微信图片_20250510192659")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926521-873x1024.jpg "微信图片_202505101926521")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926521.jpg "微信图片_202505101926521")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926522-898x1024.jpg "微信图片_202505101926522")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926522.jpg "微信图片_202505101926522")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926523-728x1024.jpg "微信图片_202505101926523")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926523.jpg "微信图片_202505101926523")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926531-838x1024.jpg "微信图片_202505101926531")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926531.jpg "微信图片_202505101926531")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926532-806x1024.jpg "微信图片_202505101926532")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926532.jpg "微信图片_202505101926532")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926533-801x1024.jpg "微信图片_202505101926533")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926533.jpg "微信图片_202505101926533")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926541-815x1024.jpg "微信图片_202505101926541")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926541.jpg "微信图片_202505101926541")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926542-876x1024.jpg "微信图片_202505101926542")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926542.jpg "微信图片_202505101926542")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926551-760x1024.jpg "微信图片_202505101926551")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926551.jpg "微信图片_202505101926551")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926552-809x1024.jpg "微信图片_202505101926552")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926552.jpg "微信图片_202505101926552")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926553-806x1024.jpg "微信图片_202505101926553")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926553.jpg "微信图片_202505101926553")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926554-852x1024.jpg "微信图片_202505101926554")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926554.jpg "微信图片_202505101926554")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926561-787x1024.jpg "微信图片_202505101926561")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926561.jpg "微信图片_202505101926561")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926562-898x1024.jpg "微信图片_202505101926562")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926562.jpg "微信图片_202505101926562")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926563-1024x683.jpg "微信图片_202505101926563")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926563.jpg "微信图片_202505101926563")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926571-801x1024.jpg "微信图片_202505101926571")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926571.jpg "微信图片_202505101926571")

[![](https://lang.ma/wp-content/uploads/2025/05/微信图片_202505101926572-683x1024.jpg "微信图片_202505101926572")](https://h4ck.org.cn/wp-content/uploads/2025/05/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_202505101926572.jpg "微信图片_202505101926572")

[![](https://lang.ma/wp-cont...