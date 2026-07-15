---
title: 手把手教你IDA自动逆向分析样本
url: https://mp.weixin.qq.com/s/WPPuJHpk0b4cVo9DUYG0HA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:15.262881
---

# 手把手教你IDA自动逆向分析样本

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EYGYnyEdzQXt9BgULeIeuPAMtwmOLTDB52TIVWIJvBSRC2ribEibeSpjb8jTPNZZatwSmSIwV4ia9bd4icyMon8FYBNWff7S6CZ5BChDBEFGhMQ/0?wx_fmt=jpeg)

# 手把手教你IDA自动逆向分析样本

原创

Hello888
Hello888

安全天书

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统等目的，一切后果由使用者自行承担！！！

安装配置

1、安装Node.JS

进入 Node.JS官网：https://nodejs.org/en/download/ 选择Windows Installer (.msi) 下载

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVSVtfv38iaWtq0BmFI2GJX1KpnGnOzwW4PC6245Wu67eZhDI2PgQjpYicnKveE6onUHMawVkOvhz2HibO6C16x2jnLj8GFbibibb4w/640?wx_fmt=png&from=appmsg)

双击运行下载的.msi 文件，进行安装：点击install，一直确定安装即可。

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQW35x8ZRE4k2hiaNONFfVlT9VRr5dBvKH9qSK51C5leJFhOjpALj6pvpdR8lb2icXycPbr0HtiaVjdvxh1t95wX63WBhticFKhRqyQ/640?wx_fmt=png&from=appmsg)

验证安装是否成功：打开cmd界面输入 node -v  回车，显示版本号即可。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQU14wlttzdcKFcNia3eGOmZFspXotDw4pPrunZr2cWmLnPzzMYUD8UHlZz1TibOMBbjicn6SK2q0zTTEwA55hibKiadD68EzebEFric8/640?wx_fmt=png&from=appmsg)

2、安装 Git for Windows

下载地址：https://git-scm.com/install/windows

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVfciaOicvibwRZYFtp8fQwtNd1fc1hMWMhU46KDhWM9CRibIdVExAIsuUrpNoSfkfiaAqmaMeEqQ4t9BicjwQ5GaE0OhqDGElvdOmSA/640?wx_fmt=png&from=appmsg)

进行安装：点击next，一直next确定安装即可。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUe31TIwBffAxNEAaUVbONaPicM9Ln1gT8UMMnANJbX4Q9nfD5bCyRsSbgSibqCMsTTEsoMtPaMbtE05ZiavKEblVXiaC68ZYibe74I/640?wx_fmt=png&from=appmsg)

安装好后点击Finish，会自动打开浏览器就说明安装成功。

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVbPsnKER5ibQ624ibUUB7jG67LfJurEhOmObUHWzhhVdzhEOv2ibbvxwHf1e8jOzibID3UkmIHRSAbKQHkXMoANC2FVUofYCmGctM/640?wx_fmt=png&from=appmsg)

3、安装 Claude Code

CMD命令行窗口,输入以下指令：

```
npm install -g @anthropic-ai/claude-code
```

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUTTkKibb2KXoicRLdHYnNWwH1S5JeACzNKl56GtoH3VMCeVhTOMuUEINXZSn7IUq8QtU59Fv9MBOtdO3JyGJh53S1kRgwDvVS0U/640?wx_fmt=png&from=appmsg)

等安装完成后，输入 ：claude -version  查看版本号确认安装。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQWKJFYjYf7B5nbibvWQuEc1ANfzcXGvr5XRUsYgIhxn2GeQAq8E9uzfBmWibicdlqFvye0XegYKGaKbhxCJyiavjryFBY0F3Hib0Hdw/640?wx_fmt=png&from=appmsg)

4、安装CC switch

下载地址：https://github.com/farion1231/cc-switch/releases/

选择对应的即可。

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQVBBt6kDOBY34YD9yV5PoplvflGNjwND6ul83uHzumIJibYnp93FErlriaP084oILG3TQGlNiaxBa4JoEicZAQ5coqTaEV5DxHqV1c/640?wx_fmt=png&from=appmsg)

配置对应的key后保存即可

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXp2dkmyZeWYA2AVTP6hu2dqqs6Ks0jboUUmiaudyZdb8cFMG8T7vKgO6gpyvyjfjAWLXksPCXzeAsCC1KmNURJNIxy2HZjPcI8/640?wx_fmt=png&from=appmsg)

运行测试，power shell打开使用命令：claude，确认是否成功。

碰到以下问题AI解决下。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQX7HBrv9Pa6FuhzDV3vs1CPncm03yQlChicH85yAkr7lTcmgcwhewgLcgRwv5dD9YibeHh4uE2ETsTU0KZXf2GXwQvCVoRaibjNaI/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUEWsvpQ3In2N6XO8vVNaJ6ibXxY7qjtd8SZQhMg5Uic6h20GND3aeIafFOOpntBv4m46a411MEibNibghpGice4uCKdgWbAD5jiayKM/640?wx_fmt=png&from=appmsg)

联动IDA

1、安装IDA9.3版本

```
https://bbs.kanxue.com/thread-289611.htm
```

注意：管理员安装后，要执行python脚本去破解要在管理员下执行。

如果没有安装ida-pro-mcp，插件里面是没有MCP选项。

2、安装ida-pro-mcp

管理员下执行以下命令：

```
pip uninstall ida-pro-mcp   //如果没有安装过不用执行pip install https://github.com/mrexodia/ida-pro-mcp/archive/refs/heads/main.zipida-pro-mcp --install   //这一步可以选择你对应的编辑器，也可以不选，有疑问可以找个AI问下
```

网络问题可以手动下载main.zip，使用命令：

pip install ida-pro-mcp-main.zip

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQVM8zF1pFbJ6UKmNgzLGFlqcYZbibNhVy7Kt9VLMEJf9Vv9bl42HcZH5UmoybnUzN5dmGPjU4YbdK5b2K9G6jlIkFUhADu54OUY/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQX2iaxs53PkuJoUYxrpXMpIlDicib9RV89znib8vMRlhfbXDGcL34T8Mr7UxICAqKj9GichA89QFPmYsC4BOe3UwxmS1z2Dl0yRA5w0/640?wx_fmt=png&from=appmsg)

3、配置运行

新建一个文件夹，把要逆向分析的程序放在文件夹中，然后在文件夹中放置一个.mcp.json文件，然后重启claude。

.mcp.json：

```
{  "mcpServers": {    "ida": {      "command": "ida-pro-mcp",      "args": [],      "env": {},      "autoApprove": [        "check_connection",        "get_metadata",        "decompile_function",        "disassemble_function",        "rename_function",        "set_comment"      ]    }  }}
```

启动逆向分析

因为我们的json里面没有配置IDA的启动路径，所以需要手动去加载要逆向的文件，然后再去启动MCP插件！

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQXNzO5gtyexEBcfqwsmm80LZb1Rf0ibTaQNwxhLUwE1BdhcKibERQReTMj1BdLVO3Ce025mCPJEsEILpbYyHPic3k6HeLichr24xfU/640?wx_fmt=png&from=appmsg)

如下图启动MCP会出现一个本地地址连接

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUTa55Se7pwibsPS4OribysIcAL46DZF2AtRV49aTGEMbvfStUJOv1e622FbtibiboP7AMxrRvvLmueE5icYTibshibTUHwCYWjRTuKtA/640?wx_fmt=png&from=appmsg)

![0](https://mmbiz.qpic.cn/mmbiz_png/EYGYnyEdzQWxOibT8x7ialDM0aibmkjq7VscF3n995W51L5iaA1Gk0KWa5mencdk0qvEMdRb8OyibicdGmE3H9FSEfz2zXqCVsdFsOPEJzbicgCzvs/640?wx_fmt=png&from=appmsg)

/mcp查看，出现√就说明正确配置成功。

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUrIpqNNb61YznPTbPiapy0cQg9tHxzCOjaZHU3icWTI5Pzl0miaFYmToeXvNsbjK6SpVfV5yPdBKibzXIxvWr6InztqrxrJ9lbngE/640?wx_fmt=png&from=appmsg)

```
使用IDA，分析当前加载的DLL文件，判断是否存在执行shellcode操作？解密shellcode出来输出bin文件
```

claude --dangerously-skip-permissions（这个参数的作用是自动批准所有 MCP 操作，不再弹窗确认）

![0](https://mmbiz.qpic.cn/sz_mmbiz_png/EYGYnyEdzQUYzUViaq8exEXuVHFuPKicicAt6DjJSzmNn7iboFo9vJd2AYaeqArdTEjyicWY1LxFHqibibJXBDicm48RGDdia6UTRCFBfD4xmJnibAtZQ/640?wx_fmt=png&from=appmsg)

**红蓝偶像练习生小圈子**

**更多工具思路文章请加入纷传，圈子主要研究方向渗透测试、红蓝对抗、钓鱼手法思路、武器化，红队工具二开与免杀。圈内不定期分享红队技术文章，攻防经验总结以及自研工具与插件，**目前圈子已满400人，欢迎各位进圈子交流学习！****

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQVlAoWxBjDF7s7CSWJQCckUPJAo69esq8FlpYzNk5KfaPc1D5dqPLMOPicFtQPMNIIs9N0CvNZSROQOibsGxUNzyH8icVoFMRFlv4/640?wx_fmt=jpeg&from=appmsg)

****圈子目前更新相关技术文章：**

***** HeavenlyBypassAV内部版工具-轻松免杀各大杀软
* HeBypassAV内部版Patch免杀工具-轻松绕过杀软EDR
* Heavenly自动化红队后渗透工具免杀生成器
* Heavenly白加黑自动化生成免杀工具
* HeavenlyProtectionCS内部CS插件
* 冰蝎webshell免杀工具

* 哥斯拉webshell免杀工具
* 红队场景下lnk钓鱼Bypass免杀AV
* Frp免杀隧道工具

* lnk钓鱼思路视频讲解
* lnk钓鱼Bypass天擎
* msi钓鱼
* chm钓鱼
* Kill360核晶
* AV对抗-致盲AV（核晶）
* 捆绑免杀360
* Kill火绒
* 火绒6.0内存免杀
* kill-windows Defender

* Defender分离免杀
* Defender知识点
* EDR对抗思路
* 进程注入知识点

* 360自启动思路
* **多种维权手法**

* Fscan免杀核晶
* QVM解决思路

* 渗透测试文章思路
* 内网对抗文章思路
* **还有更多红队工具文章！期待您的加入！！！********

******往期推荐**

**[安全天书免杀课来袭｜助力实战免杀钓鱼(文末送福利)](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485167&idx=1&sn=7ab4393e75cf94d13cb79e22b92fb8d0&scene=21#wechat_redirect)**

**[【红队工具】攻防后渗透工具自动化免杀！！！](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485305&idx=1&sn=3b4c50d0f88a753089767db5304b6626&scene=21#wechat_redirect)**

**[【红队工具】红队内网后渗透CobaltStrike插件更新](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485006&idx=1&sn=e3bcf2070226fcfc93b565ae2c9d85ad&scene=21#wechat_redirect)**

**[免杀更新--Heavenly自动化生成白加黑3.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485679&idx=1&sn=991c111e2627ec8835dc13b8bc919eb3&scene=21#wechat_redirect)**

**[绕过360安全卫士实现维权](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485280&idx=1&sn=467194cdf681646597a84e7f08b638bf&scene=21#wechat_redirect)******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BvSCMR82FwFJAbuLxnpEkoczbwU8nmFmKaFw3zgem3QN1qrEVzBcicTB89hFKwPia7PYosgibSltTEK1h9YEhiblkA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过