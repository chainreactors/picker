---
title: 领取Perplexity Pro 1个月 + 无限刷Cursor Pro 3个月邀请码教程
url: https://blog.upx8.com/4808
source: 黑海洋 - Wiki
date: 2025-05-23
fetch_date: 2025-10-06T22:29:20.121070
---

# 领取Perplexity Pro 1个月 + 无限刷Cursor Pro 3个月邀请码教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 领取Perplexity Pro 1个月 + 无限刷Cursor Pro 3个月邀请码教程

发布时间:
2025-05-22

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
73536

**![](https://img.090227.xyz/api/cfile/AgACAgUAAyEGAASOgsooAAPGaC8m2tduiXbhH9v63Ei0QWJ4okgAArzLMRuwrXlVwcE3IFNwBNsBAAMCAAN4AAM2BA)**

### **一、注册与激活步骤**

1. **注册链接**（二选一）：

   * **含AFF邀请码**（分享者可获额外1个月）：
     👉 [https://plex.it/referrals/W3H0K4OZ](https://blog.upx8.com/go/aHR0cHM6Ly9wbGV4Lml0L3JlZmVycmFscy9XM0gwSzRPWg)
   * **无AFF官网直达**：
     👉 [https://www.perplexity.ai/](https://blog.upx8.com/go/aHR0cHM6Ly93d3cucGVycGxleGl0eS5haS8)
2. **邮箱验证**：

   * 必须使用**教育邮箱（.edu或学校指定域名）** ，但部分学校（如ASU、SJSU）可能不适用。
   * 公共论坛或临时.edu邮箱可能被系统拒绝。
3. **激活账户**：

   * 注册后需**主动提问几次**，否则系统可能判定为非活跃用户，影响福利发放。
4. **领取福利**：

   * **Perplexity Pro**：自动激活1个月免费订阅（无需额外操作）。
   * **Cursor Pro**：
     登录后访问 👉 [https://www.perplexity.ai/account/pro-perks](https://blog.upx8.com/go/aHR0cHM6Ly93d3cucGVycGxleGl0eS5haS9hY2NvdW50L3Byby1wZXJrcw)
     领取**3个月激活码**（需下载Cursor客户端兑换）。

### **二、关键注意事项**

1. **网络要求**：

   * 建议使用**美国原生IP**（部分邮箱验证或福利兑换可能依赖地区限制）。
2. **邮箱限制**：

   * 并非所有.edu邮箱均有效，如亚利桑那州立大学（ASU）、圣何塞州立大学（SJSU）等可能被排除。
3. **服务简介**：

   * **Perplexity Pro**：AI搜索引擎，支持高级问答、文件分析、实时网络检索等。
   * **Cursor Pro**：AI编程助手（需单独安装），支持代码生成、调试、智能补全等。

### **三、无限获取Cursor Pro邀请码（没激活****Cursor Pro的情况下才能刷邀请码****）**

**下面是F12 Console脚本，奔着封车去的。**

```
function generateRandomCode(length = 5) {
  const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
  return Array.from({ length }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
}

function extractReferralLink(text) {
  const match = text.match(/https:\/\/cursor\.com\/referral\?code=[A-Z0-9]+/);
  return match ? match[0] : null;
}

let intervalId = null;

function stopFetching() {
  if (intervalId) {
    clearInterval(intervalId);
    console.log("已停止");
    intervalId = null;
  }
}

function startFetching() {
  stopFetching(); // 确保不重复启动
  console.log("开始获取，输入 stopFetching() 可停止");

  intervalId = setInterval(async () => {
    const url = `https://www.perplexity.ai/account/pro-perks?_rsc=${generateRandomCode()}`;

    try {
      const res = await fetch(url, { method: "GET", credentials: "include" });
      const text = await res.text();
      const link = extractReferralLink(text);
      if (link) console.log(link);
    } catch (e) {}
  }, 500);
}

window.startFetching = startFetching;
window.stopFetching = stopFetching;

startFetching();
```

1. ![Cursor玩不起](//q2.qlogo.cn/headimg_dl?dst_uin=654625&spec=100)

   **Cursor玩不起**

   2025-05-25 12:49:12

   [回复](https://blog.upx8.com/4808/comment-page-1?replyTo=30604#respond-post-4808)

   被全部回收了，玩不起了啊
2. ![米姆米姆](//q2.qlogo.cn/headimg_dl?dst_uin=669155&spec=100)

   **米姆米姆**

   2025-05-23 10:28:22

   [回复](https://blog.upx8.com/4808/comment-page-1?replyTo=30602#respond-post-4808)

   封车了吗

[取消回复](https://blog.upx8.com/4808#respond-post-4808)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")