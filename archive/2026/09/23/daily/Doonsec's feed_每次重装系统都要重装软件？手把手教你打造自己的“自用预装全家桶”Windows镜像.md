---
title: 每次重装系统都要重装软件？手把手教你打造自己的“自用预装全家桶”Windows镜像
url: https://mp.weixin.qq.com/s/cQZLTbGq01Zc5i5xJCfibw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:01:34.972474
---

# 每次重装系统都要重装软件？手把手教你打造自己的“自用预装全家桶”Windows镜像

# 每次重装系统都要重装软件？手把手教你打造自己的“自用预装全家桶”Windows镜像

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

每次重装系统，装完Windows还要一个个下载微信、Chrome、驱动……半天时间就没了。其实，你可以自己做一个“装完即用”的定制镜像。今天这篇文章，就带你从零开始，把常用软件直接封装进系统，以后装机就是喝杯茶的功夫。

---

##

## **一、为什么不用网上的“盗版系统”？**

##

很多人图省事，会下载一些所谓的“优化版”“装机版”系统。但这些系统往往捆绑了一堆推广软件，甚至留有后门，安全性完全无法保证。

而我们自己动手，用微软原版ISO + 自己常用的软件，打造一个**纯净、安全、专属于你** 的镜像。原理其实很简单：在虚拟机里装好系统，装好所有软件，然后把这个“母盘”打包成一个系统映像文件，替换回原版ISO里，以后重装直接拿这个镜像装，不用再一个个装软件。

---

##

## **二、准备工作**

##

核心工具是Windows自带的 **Sysprep**（系统准备工具）。它能把一个已经装好软件、配置好的系统“通用化”——清除硬件绑定信息，把它做成一个能反复用的装机镜像。

## 此外准备：

##

* **原版Windows ISO：从微软官方或合法授权渠道获取原版 ISO**
* **虚拟机：VMware Workstation**
* **PE镜像：推荐微PE**
* **镜像编辑软件：anyburn（UltraISO免费替代品）**

---

##

## **三、详细步骤**

###

### **1. 安装系统，进入审核模式**

###

在虚拟机中挂载原版ISO，正常安装。当首次启动进入OOBE（让你选区域、输用户名）时，**不要继续**，同时按下 `Ctrl + Shift + F3`。系统会自动重启，以内置Administrator账户进入**审核模式**。

### **2. 安装软件与配置**

###

现在你可以像平常一样双击安装驱动、运行库、软件等。

注意：

* 软件**必须支持全局级安装**；若只向当前用户目录写入配置的软件，封装后普通用户账户会丢失配置，还可能造成 sysprep 通用化报错。
* 不要安装杀毒、系统管家类安全软件，会出现文件锁定，导致通用化失败或者捕获镜像异常。
* 不要登录微软等个人账号：避免绑定个人信息。

### **3. 运行Sysprep通用化**

###

软件装完、配置好后，以管理员身份打开命令提示符，执行：

```
%windir%\system32\sysprep\sysprep.exe /generalize /oobe /shutdown
```

```

```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMIBk2lkAbHUU59RKojYibHibU2blaO6ADISBBZ2zjiaF242vPbzp9vI3ibiaAphElAXIFib9Fxia1wcMz40uaezx6dpavKNPkJD8nsf20/640?wx_fmt=png&from=appmsg)

或者打开 `sysprep.exe` 图形界面，选择：

* 系统清理操作：**进入系统全新体验(OOBE)**
* **勾选“通用”**
* 关机选项：**关机**

点击确定，系统开始通用化，完成后自动关机。**关机后绝对不要再开机，一旦开机 sysprep 通用状态失效，需要重新执行通用化操作**，直接进入下一步。

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMJVHQmN1Ub7rzzM46K5tgWeEiamzpwqZ8x2eeZkL2FORLibHNqic38IJMzc0AeHWe97OhtLIPv3WfVv9K9ibzx4AvcGVQxq9KqhR7I/640?wx_fmt=png&from=appmsg)

### **4. 用PE捕获install.wim**

###

* 在虚拟机设置中，将CD/DVD指向PE的ISO。开机选择从光驱启动，进入PE。
* 在PE中打开分区工具（如DiskGenius），找到那个几十GB的NTFS系统分区，**分配盘符**（比如 `C`）。同时确保存放镜像的目标盘（U盘或第二块虚拟硬盘）也有盘符（比如 `D`），且为NTFS格式、空间充足。
* 打开命令提示符，执行捕获命令，将命令里的盘符替换为你实际识别到的盘符：

  ```
  dism /Capture-Image /ImageFile:D:\install.wim /CaptureDir:C:\ /Name:"My Custom Windows" /Compress:max
  ```

  ```

  ```

  **`/ImageFile:D:\install.wim`**：把打包好的文件存到 D 盘，叫 `install.wim`
  **`/CaptureDir:C:\`**：捕获 C 盘（你的系统盘）的内容。
  **`/Name:"My Custom Windows"`**：给镜像起个名字

  /Compress:max：最大压缩，生成的文件最小

* 等待进度条走完，提示“操作成功完成”。

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMKzARaZcqpSSic2zEP71WGm9Es7zZ05iaZywYJ2hEBiaaJTSGmOTMAWyX6WW4eZrybThsdvfPJhoiaYicoWN5sK0xAZHQmZHGHwNvJo/640?wx_fmt=png&from=appmsg)

### 5. 替换ISO

###

* 把生成的 `install.wim` 拷贝回主机。
* 用anyburn打开原版ISO，将 `sources\install.wim` 替换为你捕获的文件

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMLFzKyM6J96EEe6dM9icfIrGOPqoUsGqbzfZy63otDiaxorK7AmWSCFHmZCZ8GB1b16ArMg8mYVDnovLzVnP9wBkVlicibHb3TPyRw/640?wx_fmt=png&from=appmsg)
* 另存为新的ISO，这个新 ISO 就是你的母盘，以后装机反复用。
* 备注：本文使用 MSDN DVD 多合一零售介质，替换为单索引自定义 wim，因此需要在 sources 目录新增 EI.cfg 文件，新建文本文档，修改后缀为`EI.cfg`，写入下面内容：

  ```
  [Channel]Retail[VL]0
  ```

  ```
  如果你的原版本身就是单版本 ISO，则不需要添加 EI.cfg。
  ```

6.测试

在虚拟机中用新ISO全新安装一次，验证软件是否已正常安装到位：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMIZ7WQvezibaw714OHrCvwibLw20kCcomuTqL0AjxKVUyHpexIeBXGkyXjsBrNicknwkMXIFWT28DMDuY2EmiakN824nHtOic1C4xQA/640?wx_fmt=png&from=appmsg)

**提醒**：本文技术仅供个人学习自用，请使用正版Windows授权，不要用于商业分发。

---

**参考链接**

[1]https://learn.microsoft.com/zh-cn/windows-hardware/manufacture/desktop/capture-and-apply-windows-using-a-single-wim?view=windows-11

[2]https://www.anyburn.com/cn/download.htm

---

**相关阅读**

[VMware 26H1 正式发布：来看看更新了哪些内容？](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247488776&idx=1&sn=5af7f901d1d82efe84e79a0c4789f2b2&scene=21#wechat_redirect)

[U盘启动盘升级攻略：如何在Ventoy中添加微PE镜像？](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247487130&idx=1&sn=b00d7b848830cc3ca435e34cd552ec18&scene=21#wechat_redirect)

[离谱！百度搜 MSDN 我告诉你，少一个字母就是钓鱼站](https://mp.weixin.qq.com/s?__biz=MzkzMDQ0NzQwNA==&mid=2247489198&idx=1&sn=d447ee6018ba12a88275fcc797ae1a1c&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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