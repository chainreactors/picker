---
title: claude code + cc-switch 反编译分析APK
url: https://mp.weixin.qq.com/s/gCDWuDTfXKwksVDcqOjonw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:12.117202
---

# claude code + cc-switch 反编译分析APK

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVllwUqjrkIW0bOOuDFqZic3iaIDzNic7R3jQQ6zE5keFuGRGAlP3ML4Ck5HbBcwZQE1ztoWsicKasqwUCQibkEiczDSBTJQuyCvcu9ic4/0?wx_fmt=jpeg)

# claude code + cc-switch 反编译分析APK

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 723，阅读大约需 4 分钟

开头先说一下，师傅有问题私信我的时候，别问什么在不在的。我没设置消息提醒，你问在不在我该看不到还是看不到。

有什么事情直接说，有什么问题直接发。我看到了自然会回复的。

你问我在吗，我回你有什么事。一来二去，一天过去了，然后啥也没解决，啥也没干成。

## 前言

通过`cc-switch`修改`claude code cli`使用的大模型，支持更换国内的大模型，比如智谱、deepseek。

支持的供应商
![5c64012a6e3fe00974370a9524bbefbe.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmibnPV3WePgVOTLZryI6efOmXP7Xscc5hrTLALA49oBhYiazXg979LmoZZ1mcxjnfwgKtOcgaNLP9qajkuzfdcVOXjGK5iccdmv0/640?from=appmsg "null")

5c64012a6e3fe00974370a9524bbefbe.png

## claude-code

安装

```
sudo npm install -g @anthropic-ai/claude-code

claude --version
```

![4526a1b39c78056f1f907447ca5f3333.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVk791DhEpIvJjcSNGWTyYNnz2IfLE9VAD4kZuFwaTfiaiaSSCMRcsgbkyXxuhnxnNT5ToUY85H1Nbg9NUFfELibiaWnPfDsEYc83Sg/640?from=appmsg "null")

4526a1b39c78056f1f907447ca5f3333.png

接入智谱 AI，新注册的账号有 12kw 的 tokens 额度，无需实名即可使用。
不过模型是 glm-4.5 的就是了。
![deec0c8ce3f44d7d1f26486e8ebf46f1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlRuam75TkKRNnmzh5pKIJy2ibQeno0pmJn5Y1TmTlst2xyWgO5Z8qnMZlJTw8FDnF3FHpgbficTvovD4ibX76FU8kOJiaribh2KyKM/640?from=appmsg "null")

deec0c8ce3f44d7d1f26486e8ebf46f1.png

官方地址：
https://bigmodel.cn/

获取 API key
https://bigmodel.cn/apikey/platform

![b9c3792cd42b7671dd160b3af308d74a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk4drQ4osP8jdIxHE0DLnl4NquecMGEz53uic6kdC4YOSqDltibcQBwsl06MONnchPF16Ndgzomtr4Zp4dgFofZu3UJ0CVA2CnUw/640?from=appmsg "null")

b9c3792cd42b7671dd160b3af308d74a.png

下载 cc-switch
https://github.com/farion1231/cc-switch

配置
![3ce30560354a325137758b62a2d3685a.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkoYYEfpcYvlxxvQ9OtAlzcTRknlCoMcbKtAOVGlm1pj2W6iazlcFAaZIqh0OGzEzZM1IqeW1uwAldVQibIeoXUF25gIS7ibU7AX0/640?from=appmsg "null")

3ce30560354a325137758b62a2d3685a.png

点击启用
![265207523db356f0001ee028ea31a08c.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl6QVQWbrlZAqoapQPfFxVZviciasbFmgyzsEwglyY3MO64RhyEr2icVJqEugTUIE9luXhKv49LIb84icoyfP6UgCBick3ryqibPU1qM/640?from=appmsg "null")

265207523db356f0001ee028ea31a08c.png

后续打开即可：
![2c70361a4ec8376826f26cb19d0c8125.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmDYvqIzAyClkTVJrXR76jFF30cAWXmaQuKpFFjGLwl1pMxkvTq9oiaMTcteUjdYvkBZwvCuqAwROjc1XicibM1dz84p2KBibazpuo/640?from=appmsg "null")

2c70361a4ec8376826f26cb19d0c8125.png

## skills

```
mkdir -p ~/.claude/skills
```

### android-reverse-engineering-skill

```
mkdir -p ~/Desktop/skill-rep
cd ~/Desktop/skill-rep
git clone https://github.com/SimoneAvogadro/android-reverse-engineering-skill.git
```

**注意**
**android-reverse-engineering-skill**里面用到的脚本是 sh 的，只能在 Linux 或者 MacOS 上使用，Windows 不支持。
我也是在 vmware 上运行 ubuntu22 使用的。

Claude Code 配置

```
/plugin marketplace add ~/Desktop/skill-rep/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
```

![94269d35f9480699dd5a77a3ceaff09c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnpj5jBI5n6wVyKRnLccH3FicgMF5lacGLBBZwcrzRntBrkEWsrPFn8liaR00ZWYvCABslic6RARC2iatopnFL51BZEibf5F7ibgMj7c/640?from=appmsg "null")

94269d35f9480699dd5a77a3ceaff09c.png

**Java JDK 17**

```
sudo apt update
sudo apt install -y openjdk-17-jdk
```

**安装 jadx**

```
# 1. 进入临时下载目录
cd ~/Downloads

# 2. 下载 jadx 1.5.5
wget https://github.com/skylot/jadx/releases/download/v1.5.5/jadx-1.5.5.zip

# 3. 创建安装目录
sudo mkdir -p /opt/jadx

# 4. 解压到 /opt/jadx
sudo unzip -o jadx-1.5.5.zip -d /opt/jadx

# 5. 配置全局环境变量（永久生效）
echo 'export PATH=$PATH:/opt/jadx/bin' >> ~/.bashrc

# 6. 立即生效
source ~/.bashrc

# 7. 验证是否成功
sudo chmod +x /opt/jadx/bin/jadx /opt/jadx/bin/jadx-gui
jadx --version
```

![a7ff50d7ec7653e34428924b5f67df1c.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkEJKz34icNgpcw6JNBsRUdQGFazdibQKvraBAK9RN2zwqtpHXao3u88hhoTyuCywsGhGvSddIUTiaLM5zhV9HkGVGqy2LicyaQwgE/640?from=appmsg "null")

a7ff50d7ec7653e34428924b5f67df1c.png

然后在需要分析的 APK 的同目录下，启动 cluade，分析 APK 即可。

## claude 使用技巧

### CLI 命令

```
# 进入交互式会话，可以多轮聊、能回上下文、能改能继续。
claude "任务描述"
# 一次性执行 + 直接退出，不进交互、不保存会话，适合脚本 / 自动化。
claude -p "任务描述"
# 通过会话 ID 恢复对话，或打开交互式选择器（可附带可选搜索关键词）
claude --resume
# 继续上一次的会话，完整恢复之前的上下文
claude -c
```

### 交互式命令

```
# 初始化项目，让 Claude 认识你的项目
/init
# 清空当前上下文，开一个全新会话
/clear
# 压缩上下文 → 大幅降低 Token 消耗
/compact
# 切换 AI 模型（Opus / Sonnet / Haiku）
/model
# 让 Claude 生成开发计划 / 步骤
/plan
# 让 Claude 自动审查代码
/review
# 查看当前会话 Token 花费
/cost
# 检查 Claude 运行环境，查故障
/doctor
```

```
/cost
```

![6a459301c7386819ddb5cff769b4f4d9.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmibOeicdIzSziaG0e2wChYNwxkdlnQtCmTIDRiaAF5JMSclaUyj9fZj3vJUGN0lBvx19KVUnQ66wKAUVIvLkiaD1673CVjtf4m9jOg/640?from=appmsg "null")

6a459301c7386819ddb5cff769b4f4d9.png

## ubuntu 安装 cc-switch

ubuntu

```
sudo dpkg -i CC-Switch-v3.13.0-Linux-x86_64.deb
# 如果报错，修复依赖并自动安装缺失的库
sudo apt install -f -y
# 重新执行
sudo dpkg -i CC-Switch-v3.13.0-Linux-x86_64.deb
```

执行 cc-switch
![3d4ff73dcc53fc7a1d3383ae6234dc56.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkSyyUgDDiagpuwTHXL4LspjMl4CD8HX5YD4ZNbibQY0cRFaVnp1RZ2fG3W9icVgF1Fxp8eodVnnNxewjKgmglmRyrZVibgE5ew5C8/640?from=appmsg "null")

3d4ff73dcc53fc7a1d3383ae6234dc56.png

## 参考资料

* • GLM-5.1 接入 Claude Code [https://mp.weixin.qq.com/s/xMWeFAOJU0M3lykbP0Aipw](https://mp.weixin.qq.com/s?__biz=MzcwNjA1MTQ4OA==&mid=2247484639&idx=1&sn=775ba30eff45fb1e57d09a130801c1e2&scene=21#wechat_redirect)
* • Codex 入门教程 [https://mp.weixin.qq.com/s/bwRrJTE-K4UIonyWQsk7bw](https://mp.weixin.qq.com/s?__biz=Mzk0OTc5NTgxOQ==&mid=2247488969&idx=1&sn=856c49ee07018d2f89739490a67eb8d5&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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