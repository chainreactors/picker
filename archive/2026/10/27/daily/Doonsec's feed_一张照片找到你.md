---
title: 一张照片找到你
url: https://mp.weixin.qq.com/s/m4Pmax_CNaTtCgQywpIOZg
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:46:35.302447
---

# 一张照片找到你

# 一张照片找到你

原创

邪灵
邪灵

邪灵工作室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

### 📑 目录导航

* 人工照片定位5步方法论
* geo‑sleuth项目介绍
* 豆包完整安装操作步骤
* 实战案例 · 定位报告解析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zam7mtJptnXH18dxtNm5koPunFdVZ5FiayPJZUyNgSlGa3ia72iayViadCI5ZWns0X7mcRw1mF9qULhibN7Xap0hibGnJgVLr07zoUXx8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zakeq8ibfo0eu9xgiapwgiciaIQSMYtdVyVx4SCNE1bZmNr3qyGqOoiab9GtC53YVEDNHzOsQ4PAgLNO2xacZOwEIbc4kWEYia6A7ibJ20/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zak6cvW1E6jEMzOK4C0IicJ1Tlju8M076mttAia3rib1vTIdk4rvBxgQJCOz2xiaRJbEtp5tJUzDqhLUrYf3QLFpHp7wPJqPcNCib6M8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zamtvn5KV0VYticYQWSaxJqlOVMHJkt8RXYWAvrZJ2LzSV1GQIf5lP9jkuCUrAibBwn3XS6sWdPdz5Hibqsic8SNd0MsjbsdqrzPpdE/640?wx_fmt=png&from=appmsg)

上面漫画中提到的geo-sleuth工具可以通过照片图像特征推理拍摄地点。下面示例为一张朋友圈野外实拍照片。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zalicn7J1GL23OuMsqXxhLUEXxwHs0cVL3uYhfh59JE6FbIE9bU3BN6EVOCUZ4FJ7XXD9ZqGxytA1dQtJnxWHnMLk7QrVkvRRXuE/640?wx_fmt=png&from=appmsg)

我们仅凭肉眼很难判断拍摄位置。但是按照以前互联网曾经非常流行的照片地理解谜游戏，我们可以总结出一套标准化人工定位流程。

## 🔎 人工照片定位5步方法论

### ✅ 第一步：找硬证据，快速缩小范围

* 查看图片属性元数据：拍摄时间、GPS坐标（最重要线索）
* 放大图片四角边缘，识别路牌、招牌、车牌、路碑等文字信息
* 反向图搜：百度识图等工具检索相同画面，从网页来源获取地名

### 🔍 第二步：读图解析，严格区分事实与主观猜测

* 九宫格拆分图片，逐区域提取细节
* 采集线索：植被、地形、土壤、建筑、电线杆、道路铁路形态

### 📊 第三步：候选地点列表，线索打分筛选

* 列出全部可能地区，不局限知名地点
* 打分规则：符合线索+1；不符合线索‑1；无关特征0
* 示例：樟子松+沙地 → 榆林+2、鄂尔多斯+2

### 🗺️ 第四步：沿交通走廊，卫星地图逐段排查

* 打开卫星图，沿着候选铁路、公路寻找匹配独特地貌/构筑物
* 有街景的区域比对电线杆、建筑轮廓、树木排布固定特征
* 利用拍摄时间计算太阳方位，反推相机朝向，校验山体相对位置

### ✅ 第五步：双特征交叉验证，避免误判

* 必须至少两个独立特征互相印证，不能单靠一条线索下定论
* 输出标准结果：位置、置信等级（城市级 / 道路级 / 百米级）、缺失哪些信息无法继续精确

**💡核心提醒：**只依靠单一特征非常容易定位错误，交叉验证是地理解谜最重要的规则。

## 🤖 geo‑sleuth 项目介绍

人工定位流程逻辑完整，但操作繁琐。开源项目 **geo‑sleuth** 将整套推理交给AI自动执行。

项目仓库： 访问GitHub项目

https://github.com/Oldcircle/geo-sleuth

* 原生支持：Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot
* 但是这些工具往往普通用户并不会使用，大家用起来最方便的还是豆包

下面重点讲解：如何在豆包中部署该技能，普通用户直接使用照片定位。

## 📝 豆包安装 geo‑sleuth 完整步骤

1

### 下载源码压缩包

GitHub项目页点击Code → `Download ZIP`，下载源码包。

【截图：GitHub页面Download ZIP按钮】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zamSib1dXdpEfFLvwLwqku6drX6s39m3bpGWJ3hKTsKiaphQCia76jOr6ctztWOE5SExylKCKBjccpNfZKuoYTrWx3mpZxLmdAicoq0/640?wx_fmt=png&from=appmsg)

2

### 解压文件

将下载的zip完整解压到本地电脑文件夹。

3

### 打开豆包找到技能入口

豆包客户端 → 左侧更多 → **插件·技能·伙伴**

【截图：豆包更多菜单界面】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zan5icqia2RVc4rBEsJw2OUDmPW05JiabGcAtiaeic1AYMoD1xMGekibvUibyQzmnOxuDF33FRibReqUicByUbddKPib9lfgJ1ibI1b0Hge8D8/640?wx_fmt=png&from=appmsg)

4

### 点击上传技能

页面右上角【添加】→选择【上传技能】

【截图：上传技能按钮】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zanNnVHjkfcrFiam3ic9F8t7xlM8NuVT6H8yAFJZdSfpC1ct4xrBWpDc6TTn0HibQRxmfoAqmMm6WGGOel408fMAMBkFibtOV9azVkY/640?wx_fmt=png&from=appmsg)

5

### 上传指定文件夹

选中解压目录路径 `skills/geo‑sleuth`，上传整个文件夹。

【截图：选择geo‑sleuth文件夹】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zalwYB6KNWBp0THY7HzkbM9hZI5WmW2cyEe8HTlo8Q46X3EPpjdj6FOb7aeW5ADbZicozZ09akVKTbdToH6mqnoMrF9sdibOTvCm4/640?wx_fmt=png&from=appmsg)

6

### 管理页面确认已安装

上传完成，点击右上角【管理】，查看Geo Sleuth技能。

【截图：技能管理页面】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zalGZwqws09pIxwZ4aticic2kSAKNj0FQibxVOuVmzUiannpt7Ef2s6YWdrSjHKFTTuEibo2YLhL9ADgNu5gE5vkNcmSRTFwiavtmNMVI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zamhXLuPnomBicktlDG5zqicUSMh1jbULDX3jONMpX1Xs2HibsTmSwRZTpgljQsJI19v2ayhHlHGRC6zzgCn7tHe1XicYkQiav47m4hY/640?wx_fmt=png&from=appmsg)

7

### 对话中启用试用

点击技能卡片，选择「在对话中试用」开启能力。

【截图：在对话中试用弹窗】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zamevdYbQGfbOnMg78mNmic3rAekQ0dSjJTic7iaiciaXWvaC7ibU1ssMDUCnJ7QnQ73408dMZ0kaiaC6TBYy9Qs07nOn11IggwBUDViaNo/640?wx_fmt=png&from=appmsg)

8

### 上传图片，执行定位

发送照片，调用技能进行分析。示例图片分析耗时约54分钟。

【截图：对话发送图片调用技能】

![](https://mmbiz.qpic.cn/mmbiz_png/BmBdGJk6zalejeMOGPBqXuE9gjcy5aypneWPia5lOsX25N0vcINkDLRkzsVPSbibBnngkZtgqmS8ITdGmxCibw61BKEHp1Ubt0kHnbPGHQqUXc/640?wx_fmt=png&from=appmsg)

⏱️ **重要提示：**分析时间取决于照片复杂度，复杂图片耗时会更长，请耐心等待完整报告。

## 📄 实战案例 · 定位报告解析

【截图：AI输出完整定位报告】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zakVSPHLxDOQs61iacecTgr5YkpQc51aIqgOHTgkpJBJ2LMCbBXNVU2mVfHRx6Kx1bquBScWH39QWKLBB8Fg5HoibBfMpnEicCJFibo/640?wx_fmt=png&from=appmsg)

### 🎯 照片定位结论

最终推断 大致区域：毛乌素沙地（内蒙古鄂尔多斯 — 陕西榆林一带）

#### 🔗 证据链表格

| 线索分类 | 图片客观观察 | 推理判断 |
| --- | --- | --- |
| 地貌 | 半干旱丘陵，山脊黄褐色，沟壑稀疏 | 毛乌素沙地 / 鄂尔多斯盆地边缘 |
| 土壤 | 前景红褐色砾石砂土 | 鄂尔多斯盆地红层出露 |
| 植被 | 枯黄草地、耐旱灌木、少量樟子松幼树 | 毛乌素沙地固沙植被典型组合 |
| 铁路设施 | 公里标、地面堆放大量混凝土轨枕 | 铁路工务段/养路工区场地 |
| 电力杆 | 山脊高大混凝土电线杆 | 西北农村配电线路特征 |
| 拍摄时间 | 2026‑10‑10 09:58 晴天 | 秋季上午，太阳东南方位仰角32° |

#### 🚂 最可能匹配交通线路

包西铁路（包头 — 西安）：贯穿毛乌素沙地核心，鄂尔多斯向南经过榆林，沿线丘陵地貌、养路工区与照片特征高度吻合。

#### 📊 置信度评估

* **城市级：中**

  → 榆林市 / 鄂尔多斯市一带
* **片区级：低**

  → 无法确定铁路具体哪一段

#### ⚠️ 为什么不能精确定位？（限制因素）

1. 图片无EXIF元数据，转发/截图造成GPS等原始信息丢失
2. 图片内没有路标、站名，OCR仅识别手机水印
3. 全网找不到完全一致照片，图搜只能匹配通用荒漠风光
4. 百度街景未覆盖该段偏远铁路
5. 卫星大范围扫描效率有限，无法定位轨枕堆放场精确坐标

![Evidence image: the camera on the dune crest, field of view, the dunes, the camp and the power-line bundle](https://mmbiz.qpic.cn/mmbiz_jpg/BmBdGJk6zalOSibuPnIeeYJDzVkuoviaickA5xPkTqWqpouiaUuTgiazPh9IwSxycKw67JGVOmKWibXPEvmxvD8gZeNXkibxEefHrX0t2PzKpduQh0/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jb2tm25BPQTlUic3SSyqUMzDeVXuzn9QjAJH3xWiaVwmsRWUEEziaFSGythKLGn9rMtptbicXqHdcr8z1XQlyBvU2g/0?wx_fmt=png)

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