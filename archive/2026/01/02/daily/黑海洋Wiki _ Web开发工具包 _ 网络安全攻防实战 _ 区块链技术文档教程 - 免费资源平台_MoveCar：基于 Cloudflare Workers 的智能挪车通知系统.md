---
title: MoveCar：基于 Cloudflare Workers 的智能挪车通知系统
url: https://blog.upx8.com/4937
source: 黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-01-02
fetch_date: 2026-01-03T03:22:28.807087
---

# MoveCar：基于 Cloudflare Workers 的智能挪车通知系统

# [黑海洋 | Wiki](/ "黑海洋Wiki | Web开发工具包 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# MoveCar：基于 Cloudflare Workers 的智能挪车通知系统

发布时间:
2026-01-02 New Article

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
1983

## 智能挪车通知新体验：保护隐私，及时响应

**MoveCar** 是一套基于 Cloudflare Workers 的轻量级挪车通知系统，无需服务器即可运行，车主只需将生成的二维码贴在车上，别人扫码即可通知挪车，全程无需暴露电话号码，有效避免骚扰和隐私泄露。

### 常见困扰：挪车难题

* 🚗 被挡车找不到车主，急得团团转
* 📱 传统挪车码暴露电话，频繁收到骚扰
* 😈 恶意扫码、重复通知打扰正常生活
* 🤨 路人好奇扫码，导致误触通知

### MoveCar 的解决方案

* **不公开手机号**：所有沟通均通过推送消息完成
* **双向实时定位**：确认对方是否真的在车辆附近
* **延迟机制防骚扰**：未授权定位则延迟 30 秒发送通知
* **支持多端推送**：默认集成 Bark，安卓可替换为 Pushplus、Server 酱等
* **完全免费部署**：基于 Cloudflare 免费额度，无需服务器，零运维压力

---

## 适用场景

* 私家车车主
* 小区物业、停车场管理方
* 城市管理部门挪车协助平台
* 自媒体运营项目拓展场景（定制化服务）

### 通知流程一览

#### 对挪车请求者

1. 扫描车主二维码
2. 填写留言（如：“您挡住出口了”）
3. 允许定位（或延迟 30 秒通知）
4. 点击「通知车主」，等待车主响应

![MoveCar：基于 Cloudflare Workers 的智能挪车通知系统](https://cdn.skyimg.net/up/2026/1/2/978f8d84.webp)

#### 对车主

1. 接收 Bark 推送
2. 点击进入确认页面
3. 查看对方位置，判断是否确实需要挪车
4. 可选择共享自己位置，便于对方找到车辆

![MoveCar：基于 Cloudflare Workers 的智能挪车通知系统](https://cdn.skyimg.net/up/2026/1/2/e929ee93.webp)

---

## 简单 5 步部署：0 成本上线

1. **注册 Cloudflare 账号**，创建 Worker 项目
2. **粘贴代码**，部署 moveCar 服务
3. **创建 KV 存储绑定**，保存请求状态
4. **配置推送地址与备用电话**
5. （可选）绑定自定义域名 + 美化挪车二维码

完整部署教程详见 GitHub 项目：[https://github.com/lesnolie/movecar](https://github.com/lesnolie/movecar "MoveCar")

---

## 生成专属挪车二维码与美化挪车牌

* 使用二维码生成工具（草料二维码 / QR Code Generator）生成链接码
* 搭配 AI 工具（如 Nanobanana Pro、ChatGPT）生成个性化图案与装饰
* 添加提示文字如「扫码通知车主」，打印过塑贴车

💡 *让挪车牌不再沉闷，展现车主个性！*

---

## 强烈建议：开启境外流量屏蔽

曾有用户遭遇境外恶意攻击，建议为 Worker 添加以下安全措施：

* 使用 **Cloudflare WAF** 设置「仅限中国访问」规则
* 或在代码中添加 IP 国家筛选逻辑，拦截非中国流量

```
async function handleRequest(request) {
  const country = request.cf?.country;
  if (country && country !== 'CN') {
    return new Response('Access Denied', { status: 403 });
  }
  // 原有业务逻辑
}
```

---

## 项目地址：<https://github.com/lesnolie/movecar>

[取消回复](https://blog.upx8.com/4937#respond-post-4937)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2026 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号")