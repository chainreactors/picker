---
title: TeamPCP 组织再度攻击：Telnyx 供应链攻击事件总结
url: https://mp.weixin.qq.com/s/_gtGwH7i03Hd1x7JSavoUg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:39.489201
---

# TeamPCP 组织再度攻击：Telnyx 供应链攻击事件总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2xCpgJcagfibhVEsVwsj6agyzusiccAZBxib39zDk3Wial2L1LgxJJu4fPpYjtJbtWDBUsmBaXKBzydmHfiabd8eT65kktltA7OYdiclOIUibPmxMw/0?wx_fmt=jpeg)

# TeamPCP 组织再度攻击：Telnyx 供应链攻击事件总结

松杨网络安全资料库

![]()

在小说阅读器中沉浸阅读

一、事件概览：

| 事件名 | Telnyx 供应链攻击 |
| --- | --- |
| 时间 | 2026年3月27日 |
| 攻击者 | TeamPCP（与3月24日攻击 LiteLLM 的同一组织） |
| 受害者 | Telnyx（通信API SDK，PyPI下载量超380万次） |
| 影响版本 | telnyx 4.87.1、 telnyx 4.87.2 |

**二、关键发现：**

| 项目 | 内容 |
| --- | --- |
| **攻击向量** | 使用被盗的 PyPI API Token 直接发布恶意版本 |
| **攻击手法** | WAV音频文件隐写术 + 多阶段攻击链 |
| **目标平台** | Windows + Linux/macOS（首次加入Windows攻击） |
| **C2服务器** | 83.142.209.203:8080（裸IP，无域名） |
| **归因证据** | RSA-4096公钥与LiteLLM攻击完全一致 |

三、事件的时间线：

| 时间 | 事件 |
| --- | --- |
| 2026-03-27 03:51 | 发布恶意版本 4.87.1（因拼写错误 `Setup()` vs `setup()` 导致payload未执行） |
| 2026-03-27 04:07 | 发布修复版本 4.87.2（完整攻击链生效） |
| 2026-03-27 04:10 | Endor Labs 发现并报告给 Telnyx 维护者 |
| 事件后续 | PyPI 隔离恶意版本 |

安全版本：telnyx@4.87.0

**四、攻击链：**

**Linux/macOS攻击路径**

```
import telnyx    ↓FetchAudio() 启动分离子进程    ↓下载 ringtone.wav（WAV隐写术）        ↓从音频帧提取 XOR 加密的 Python 代码        ↓执行 332 行凭证窃取脚本        ↓加密打包为 tpcp.tar.gz    ↓POST 到 C2 服务器
```

**Windows 攻击路径**

```
import telnyx    ↓setup() 检查 Startup 文件夹    ↓下载 hangup.wav    ↓提取并植入 msbuild.exe（伪装成微软构建工具）    ↓添加到启动文件夹实现持久化
```

**五、恶意行为：**

| 类别 | 具体目标 |
| --- | --- |
| SSH | ~/.ssh/id\_rsa，id\_ed25519，id\_ecdsa，authorized\_keys |
| 云服务 | ~/.aws/credentials，~/.config/gcloud/， ~/.azure/， ~/.kube/config |
| 凭证文件 | ~/.docker/config.json（Docker登录凭证）、~/.npmrc(npm 包管理器的 Token / 私有仓库认证)、~/.git-credentials(Git 账号密码)、~/.vault-token（HashiCorp Vault 的访问 Token） |
| 数据库 | .pgpass、my.cnf、redis.conf、.mongorc.js |
| 加密钱包 | Bitcoin, Ethereum keystores, Solana keypairs, Cardano keys |
| TLS/SSL | All .pem, .key, .p12, .pfx files, LetsEncrypt certificates |
| 环境文件 | nv, .env.local, .env.production, .env.development - searched 6 directories deep |
| shell历史 | bash, zsh, MySQL, PostgreSQL, Redis CLI |
| 系统文件 | /etc/passwd, /etc/shadow, authentication logs |

**六、云环境攻击：**

* AWS IMDS：枚举IAM角色，获取临时凭证
* AWS Secrets Manager：列出并获取所有密钥
* AWS SSM Parameter Store：枚举配置参数

**七、Kubernetes 横向移动：**

* 枚举所有命名空间的凭证
* 部署特权 Pod 到每个节点
* 挂载宿主机根文件系统
* 更改根目录，到宿主机安装持久化后门

**八、与 LiteLLM 攻击的对比**

| 攻击技术要素 | LiteLLM (3月24日) | Telnyx (3月27日) |
| --- | --- | --- |
| Payload位置 | 内嵌完整窃取器（34,460字符） | 瘦投放器（4,428字符） |
| Payload交付 | Base64内嵌 | WAV隐写术 + C2下载 |
| C2通信 | models.litellm.cloud | 83.142.209.203:8080 |
| 平台支持 | 仅Linux/macOS | Windows + Linux/macOS |
| Windows持久化 | 无 | msbuild.exe + 12小时锁 |
| Linux持久化 | sysmon.service | audiomon.service |
| 持久化轮询 | 固定50分钟 | 抖动45-55分钟 |
| 混淆方式 | Base64 | Base64 + WAV隐写 + XOR |

**九、与 LiteLLM 攻击技术的区别：**

1. **WAV隐写术**

   — Payload隐藏在音频中，绕过网络检测
2. **瘦投放器架构**

   — 包体积减少87%，真实Payload运行时获取
3. **分离子进程**

   — `start_new_session=True` 绕过沙箱检测
4. **跨平台攻击**

   — 首次加入Windows攻击路径
5. **可更新Payload**

   — C2可随时更新攻击代码，无需重新发布包

十、缓解措施：

1.确认版本：安全版本是4.87.0，危险版本是4.87.1和4.87.2。

2.linux用户，检查~/.config/audiomon/和audiomon.service。

3.windows用户，检查启动文件夹msbuild.exe。

4.注意83.142.209.203IP相关的网络日志。

5.若使用了危险版本，请替换所有凭证。

6.轮换相关凭证。

**十一、**

**检测命令**

```
1.检查是否安装了恶意版本：pip show telnyx 2>/dev/null | grep -i version pip freeze 2>/dev/null | grep telnyx2.检查持久化痕迹：Linux/macOS：ls -la ~/.config/audiomon/audiomon.py#检查audiomon植入物ls -la ~/.config/systemd/user/audiomon.service#检查systemd用户服务windows：dir "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\msbuild.exe"#检查启动文件夹中的伪装 msbuild.exe3.检查Kubernetes 横向移动痕迹：kubectl get pods -n kube-system | grep node-setup4.检查是否连接C2：网络日志查看是否存在连接IP：83.142.209.203的记录5.清理：Linux/macOS清理：版本回退：pip install telnyx==4.87.0停止并禁用 systemd 服务：systemctl --user stop audiomon.service，systemctl --user disable audiomon.service删除植入物和服务文件：rm -rf ~/.config/audiomon/rm -f ~/.config/systemd/user/audiomon.servicerm -f /tmp/.initd_state重载 systemd：systemctl --user daemon-reloadWindows 清理：%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\ 目录下：msbuild.exemsbuild.exe.lock6.网络层阻断83.142.209.203的连接
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

松杨网络安全资料库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n3sKsNaia7UAicqBXkY6PekQB9TvES6wdib3Tunt6tg5AEAXILtr3peiatYdFs6Nwy0flHMTxxFOT5ibm10zY6tw1gQ/0?wx_fmt=png)

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