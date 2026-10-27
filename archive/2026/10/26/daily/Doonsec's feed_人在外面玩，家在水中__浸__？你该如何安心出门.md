---
title: 人在外面玩，家在水中\"浸\"？你该如何安心出门
url: https://mp.weixin.qq.com/s/0OKlnRlGHXyByGNxOwIlfQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:43.491443
---

# 人在外面玩，家在水中\"浸\"？你该如何安心出门

# 人在外面玩，家在水中"浸"？你该如何安心出门

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 开开心心的在外面玩，突然想起自己走时忘记关了水电。或者家中漏水了，自己第一时间不知道，"人在外面玩，家在水中泡"。哪么，如何解决自己出行时的顾虑呢？跟随作者，一期来解决吧！

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBoreuibs1SDMkxz1I6Tnht74oklMCibrFtZLq3qdRGrQ9PhVCvzgWlaNP5QgH4hLQeAfEtEoGcVLRoWaOUIv6mouWu3xXoaHI4DzOw/640?wx_fmt=gif&from=appmsg)第一部分：控制你的“电”![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordibiawE4mzKwE0yqP0VM3XwQic0gSzuYibWmr4sgeMZEI8G3gnMN9UY3ZjH6bYn8EWMsc13iaXlntotnruUbfmgrcLOdO2HW1golKE/640?wx_fmt=gif&from=appmsg)

当下，物联网的广泛普及。对“远程”控制电已经成为现实。在上期文章中，作者介绍过利用模块，无需对线路进行大规模的改造，从而实现远程控制开关的状态、实时功率等。详情参考下方文章。

但在部分生活场景中，线路的改造相对比较麻烦。而智能插座彻底解决你的烦恼。本文以`Plug CN Gen3`这款为例，介绍它的使用和进阶玩法。

### 01产品实物展示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcziadBuhhPCnIWdAficBByB0nEV3CPYDpHscww6GXHakKicIiaPPn9XQKVKiaNhmVEzSAksRax6Ox30sIlY2nTOuJjkAjfa8ibNDJg8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfXR5g45FbX0tQzqLueBceTL33kJ1MeqEKAPQRXoZhV4cKcmItvjbufuc3UPnBoYsxtdqQnqwyxpBzqwzQeSMWztciahB7COmvI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordRkehqe1l76JVpibroH43EWGicTz4os512wcfs3sWFVKvb8iaZfa480fPiaqqaJruXmibVicNP22SnPBqonqwLibLssaZ2sqjv3LXMOw/640?wx_fmt=png&from=appmsg)

### 02 快速接入

接下来，我们快速接入设备到Shelly APP。轻松管理设备！

![轻松三步 快速加入](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcBublG6NiboeRjtQQ1hArpRPJLoiclQXg8LLqNicMelK1xMVCsia9rs8mtYjdtcU7uyZQPTRibGmd6FvD3LicQHYqrpFWuHhTrH87Qw/640?wx_fmt=png&from=appmsg)

轻松三步 快速加入

### 03 小试牛刀

和其他市面上常见的智能插座一样，该有的功能一个也不会少。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordlUxgTpO6mnrKdWepKCLibhzQJtjBGlib55GcNiaZF9BTWPJetkLgz7zovoyssiacLYWS7LXQcNibjv1K4yHrt2wEjS4KDdFhtg8p0/640?wx_fmt=png&from=appmsg)

### 04 接入HomeAssistant

设备支持WiFi接入和蓝牙网关接入。首先在蓝牙设置中开启蓝牙网关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorcmtRic5lia6hiaR2OT1ABibuUbSOXibg9BHlR17iaxx0N5dvMnzW0QGzBBmTOt2XGVpn5WgkQviaxralotaWcJicd7UsIcibgiagIXroxicU/640?wx_fmt=png&from=appmsg)
接下来，在HA集成中，会自动发现设备。（如发现不了，请用WiFi方式添加）![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBore2HicTOhYh1YWIz9KzjL9FaK3YfM0szPJMQlvfuicXBj4BwMIndQCepO6sncNsFddeBHBOEMiaBCmhQLHKhJWtvfnF6c9XEvw0rs/640?wx_fmt=png&from=appmsg)加入能源
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorctrfAvia9icC7nFQu1oYIjYeTTweCg7Fb4z1sSCSCZ7H1ibdrMlqXDrF2ib5gppS3goITdAiaWRcSW2O6havYRJeK8w9nzQEMyJqfg/640?wx_fmt=png&from=appmsg)![实时功率](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreVQyuKy0wBLIRibc757NueF8GfLw9ZsclfcGba0JFTjHxzPuaMJiaUrPZQ6qPkNALjkWPYGauQUiauzhQflUliave5bYQQWT5dBWQ/640?wx_fmt=png&from=appmsg)

实时功率

利用Bemfa插件，我们便可以接入米家，控制设备更方便。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordsjjWNQWlLjpLm1N51vwx9cBEj197op5JYv1yj0Gicud8syXKvSYISfnFclFoWtf6VSCvpwGZ6PvxZnia941Aln8mTVusicx2jlI/640?wx_fmt=png&from=appmsg)

### 05 进阶玩法

其实很多人会说，目前市面上这类产品多不盛数，这有什么可写的呢？其他`Shelly`系列的产品，最大的特色在于开放性。用户可以自己编写属于自己的特定脚本，支持MQTT、WSS、UDP等常见的开源协议，不仅让你用的愉快，更让你玩的开心。接下来，通过几个小场景来看看吧！

**📧负载自动断电并通知**
当功率大于阈值时，自动断电，并通过Server酱微信通知。方便我们第一时间掌握设备情况。
**示例代码**

```
var POWER_LIMIT    = 50;          // 功率阈值（W），超过即断电（当前为测试值，正式使用时改回 2500）var CHECK_INTERVAL = 5000;        // 检测周期（毫秒），建议 3~10 秒var ALERT_COOLDOWN = 300000;      // 报警冷却时间（毫秒），避免恢复供电后又超限时频繁刷屏var SENDKEY        = "SCxxxxxxxxxxxNG7o2r";  // Server酱 SendKey var lastAlertAt = 0;  // 上次推送时间戳 // 补零function pad(n) { return (n < 10 ? "0" : "") + n; } // Espruino 不支持 Date.toLocaleString，手动格式化本地时间function formatTime(d) {  return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()) +         " " + pad(d.getHours()) + ":" + pad(d.getMinutes()) + ":" + pad(d.getSeconds());} // 发送 Server酱 通知（新版 ServerChan API，JSON 格式，避免依赖 encodeURIComponent）function notify(title, desp) {  Shelly.call("HTTP.Request", {    method: "POST",    url: "https://sctapi.ftqq.com/" + SENDKEY + ".send",    body: JSON.stringify({ title: title, desp: desp }),    headers: { "Content-Type": "application/json" }  }, function (res, errCode, errMsg) {    if (errCode === 0 && res && res.code === 200) {      console.log("[Server酱] 推送成功");    } else {      console.log("[Server酱] 推送失败:", "errCode=" + errCode,                  "errMsg=" + errMsg, "http=" + (res ? res.code : "none"));    }  });} // 主检测逻辑function checkPower() {  var st = Shelly.getComponentStatus("switch", 0);  if (!st) {    console.log("[检测] 未获取到 switch:0 状态，跳过（确认设备带功率计量）");    return;  }   var power = st.apower || 0;        // 当前有功功率（W）  var isOn  = st.output === true;    // 继电器是否处于闭合（通电）状态   if (isOn && power > POWER_LIMIT) {    // 自动断电    Shelly.call("Switch.Set", { id: 0, on: false });    console.log("[断电] 功率 " + power + "W 超过阈值 " + POWER_LIMIT + "W，已自动断开继电器");     // 冷却期内不重复推送    var now = Date.now();    if (now - lastAlertAt >= ALERT_COOLDOWN) {      lastAlertAt = now;       var info = Shelly.getDeviceInfo();      notify(        "⚠️ 设备功率超限，已自动断电",        "设备名称: " + (info.name || info.id) + "\n" +        "设备 ID: " + info.id + "\n" +        "检测功率: " + power + " W\n" +        "功率阈值: " + POWER_LIMIT + " W\n" +        "处理动作: 自动断开继电器\n" +        "触发时间: " + formatTime(new Date())      );    }  }} // 启动周期检测（第二个参数 true 表示循环执行）Timer.set(CHECK_INTERVAL, true, checkPower);console.log("[启动] 功率过载保护已就绪，阈值 " + POWER_LIMIT + "W，检测周期 " + CHECK_INTERVAL + "ms");
```

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordbzk0Vv00QmxEElFUHRD4wYVJRZIGEYHv83yicD7qn0EIcicedm2Z2eHzvP4JjJicy2TV4uAnUdxWmQeJqoQ1TccVGbhO7JjVuyM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBord4nABMb8OczCHHpyLAMia2F5vDyn1gopG6iaLMTQD8PnKypOHNnO86WhVibCjo9Ricqx7FzqjUHZy0RyJv4UFMRn4kUasMNvJ8IhI/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBoreX7h3QqPzU2HFPJAnibvFlRFP1hUwch0aw7SFK375YlL7r0JEVFfDsib5RNnqeJlZYTPOJv8eonjrRg2ictV0vZvBf2OqTNkLyk0/640?wx_fmt=png&from=appmsg)
聪明的你，也许会说自己不会写。但现在是AI时代，只要你有好的想法，剩下的交给AI就行了。
**😘接入MQTT**
对于Shelly的设备，最好玩的莫过于接入MQTT了，将数据接入数据库，小程序等，控制更方便。![配置MQTT](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreiaDIQzctzcCG9eLt6NwSNuicvfWT2GQUy137WOLGX6z8e3ctsVXvWCiaEYVJJ4aLNYbPOcLWknsRPjV3qmlicZwPWPKXEGCUWFxw/640?wx_fmt=png&from=appmsg)

配置MQTT

**✈️通过mqtt消息开启关闭设备**
向主题`shellyplugcng3-48f6eebe9b0c/command/switch:0`发送数据如下：

```
#开启设备on#关闭设备off
```

**🧲详细信息**
`shellyplugcng3-48f6eebe9b0c/status`监听主题，效果如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorc3mLpIJNib6b0oeibPiad59nBANsH5F1yPib7UbDTuyFqJ1lN4eBOTlJwGUgjcNtibibwD5fDDwbZzxYwbHagppyLqn8zcXIDqrGto8/640?wx_fmt=png&from=appmsg)
了解MQTT的数据形式后，我们便可以轻松接入小程序。![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordNFPBeZldAnpDs3mqW6AVvq5kibwETEY9GJnwQSiaflLibkrlRcJJzw8uyctiaWUkDORf8BXdcSPmiaOgyobrwUEOApKia9a1mTZicgE/640?wx_fmt=png&from=appmsg)
此外，定时任务、场景联动等基础功能，可以根据自己的实际情况去部署，这里不在啰嗦。

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorc1nbn7gOb1JM9c8TP505nOic1jtUUXJrty9CZ2frPOrEGxAPn9IkS1wg5Nwp7S68kBwic8lDVXMPnxovdmZR8KCXWgqfFLCSsgo/640?wx_fmt=gif&from=appmsg)第二部分：控制你的“水”![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBoreKdqeDIjmribbfmcKSoetSBHKDl7b7p3rXYxjZk7PC7ySXbedHH85aVM1j6T4WNEaXjs7ztvBRGvHsu9xds2Q0Ex6D2T6prqKQ/640?wx_fmt=gif&from=appmsg)

说完了电，现在谈谈水吧！相对而言，水的危害也相当大。外出游玩，水管爆裂，整个家浸在水中，而你却一无所知。这时我们仅需一个水浸传感器便可以解决你的烦恼。
这次，我们采用的设备型号为`Shelly Flood Gen4`。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBorfU7E7DVBRdD7vWOzL7TDxicbXqRFQ6kvBcpHF1YB4NDYUficW5eHmu0qkplw9EoicrUib2v5kc3LzSsUCFxP9mb0NtHXnKpQrGmP0/640?wx_fmt=png&from=appmsg)

### 01 部署和入手

设备的接入和之前一样，轻松几步接入APP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBore6y2vPN2Zw2iaK8bvjc3MoIOIF9K6gDTrQLiaeQicq2dV4Buvnic5E9VsibtSKkeP5D0pWSF7b1gD9s7uIzkO8iarhibCVCIask90cdw/640?wx_fmt=png&from=appmsg)
需要注意的是，设备采用4节干电池供电，虽然连接的WiFi网络，但它很省电，因为只有在监测到有水时才开机，其他时间处于休眠状态。

**实物部署效果**

![线可以在接头能常见漏水的地方多绕几圈](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1N1JeeKBorenxmI0hicw1aecxUrk9lKZOcZysdpYqicP6xAGic3ziaib22KGc2qP0xP3d4RLo8kwrMWibGZ9d4ZnwKvoMpoDKic9me66Ef0GNBle94/640?wx_fmt=jpeg&from=appmsg)

线可以在接头能常见漏水的地方多绕几圈

当设备监测到水浸时，在APP中也能第一时间收到提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1N1JeeKBoreTjhib2vHQVAWoYI2g7TOIa5zicjF0kO6VB99w1bo55mr4nSlAj4TlNags66C6sSo7BPKhoNIdhG06y4bnvjsVx10HgKl0lABoI/640?wx_fmt=png&from=appmsg)

### ...