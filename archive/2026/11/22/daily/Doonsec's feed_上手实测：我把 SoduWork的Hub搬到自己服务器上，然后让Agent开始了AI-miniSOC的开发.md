---
title: 上手实测：我把 SoduWork的Hub搬到自己服务器上，然后让Agent开始了AI-miniSOC的开发
url: https://mp.weixin.qq.com/s/YCNtcc1aubryYJkvljhyog
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:21.982665
---

# 上手实测：我把 SoduWork的Hub搬到自己服务器上，然后让Agent开始了AI-miniSOC的开发

# 上手实测：我把 SoduWork的Hub搬到自己服务器上，然后让Agent开始了AI-miniSOC的开发

原创

xiejava
xiejava

fullbug

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 这是一份两段的实测记录。第一段讲**安装部署**：我把开源的 SoduWork Hub 搬到自己服务器，怎么装、怎么配、怎么验；第二段讲**实测**：把 AI-miniSOC 一组真实的开发需求交给 Agent，走完「提需求 → 执行 → 初审返修 → 验收」的闭环，两条 commit 为证。
>
> 环境：macOS + SoduWork.app 1.13.19（客户端）+ 自建 Hub（局域网 `192.168.0.128`，经 Cloudflare 暴露为 `sudowork.doai8.dpdns.org`）。

## 先说结论

* **部署：Hub 装在一台独立的宿主机上，客户端在另一台 Mac，两条网络路径（局域网直连、公网隧道）都通，鉴权真的在拦人；管理端配好用户、模型、项目，两台客户端在线干活；**
* **实测：Agent（内置的 Pi，跑智谱 GLM）在 AI-miniSOC 仓库里完成了一组真实需求——暴露面分析页改 Tab 布局，只动一个文件 +51/−34，交付报告自带真实浏览器实测证据，初审抓到一个换行瑕疵打回返修 +2/−1，两条 commit 落库，三条需求当天全部验收关闭；**
* **一个值得所有人先看一眼的细节：动手前先摸清自己在哪台机器上——我的客户端内网地址实际是 192.168.0.29 / .31，Hub 在 192.168.0.128，不是「在自己电脑上开一个 Hub」，而是一台机器跑 Hub、另一台机器当客户端。这个区分决定了后面所有验证该怎么设计。**

---

# 第一部分：安装部署——把 Hub 搬到自己服务器

## SoduWork 是什么，为什么要自托管

SoduWork 是一个开源项目（MIT 协议，github.com/mdri-ai/SoduWork），自我定位是 **The AI-native engine for teams and their agents**——给人和 Agent 团队用的需求引擎。它最打动我的一句话是：

> 聊天以答案结束，需求以签字结束。

在它里面，需求、执行、验收和沉淀在同一个需求池里流转：谁提的、谁做的、用了哪个插件、谁批准的，都留有记录。这套东西的官方云开箱即用，但我更想把它**整个搬到自己服务器上**——数据在自己的库里，Agent 在自己的机器上干活，这是自托管的全部理由。

## 一条命令起服务

自托管路径官方已经铺好，核心就一条命令：

|  |
| --- |
| ``` ``` git clone https://github.com/mdri-ai/SoduWork.gitcd SoduWork/ops/self-hostpython3 deploy.py up ``` ``` |

这条命令背后是 docker compose，起两个服务：

| 服务 | 说明 |
| --- | --- |
| `soduwork-hub` | Hub 本体（FastAPI），我用源码构建，版本号显示 `version=dev` |
| `postgres:16-bookworm` | 数据库，所有需求、记录、插件都在这个库里 |

几个值得点赞的安全细节：容器以专用 UID 10001 运行，**不给 docker socket**，最小权限起步；Hub 容器只绑宿主机回环地址，要对外服务得自己在前面放一层反向代理——默认姿态是「关着的」，露多少开多少，这个顺序是对的。

我的实际部署形态：Hub 在局域网一台宿主机 `192.168.0.128` 上，前置反向代理终结 TLS（证书是 SoduWork Local Root CA 签的，`CN=192.168.0.128`，有效期到 2036）；公网入口用 Cloudflare Tunnel 回源，拿到 `sudowork.doai8.dpdns.org` 这个域名。TLS 的完整官方指南在仓库 `docs/self-hosted-tls.md`。

部署完成后，在浏览器里用自己的域名打开，就是自己服务器上的 SoduWork 门户，右上角「进入管理后台」即是 Hub 管理端：

![用自己的公网域名打开自建 SoduWork 门户](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2mp5QWlBd2kV9gjRmRficVzBb65PALS3bKbzAojFPt5hyHoMiaqqfM9huWCe2nDrll4ZiaxkgWSOogSYsf9sQ70TWO1uR40XUZGTw/640?wx_fmt=jpeg&from=appmsg)

## Hub 管理端：三步基础配置

登录管理端，第一眼是「治理总览」：需求池几条、交付率多少、几台客户端在线，服务状态一目了然。真正要让团队（哪怕团队只有我和 Agent）跑起来，配置就三步：

![Hub 管理端首页：治理总览](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2kPgQP1slNvOpdm9fXt5vtMjiaXOx95Y6fEVMVq5L6QxfA83Y2xDdKQEQMsONBHqBMeveARAAfkA5Nsfnom7rI8WswSraPxDnHQ/640?wx_fmt=jpeg&from=appmsg)

**第一步：建用户。** 在「组织治理 → 用户管理」里新建用户、配好权限，客户端就能用这个账号登录——不是谁连上都能用。

![配置第一步：用户管理，新建用户并配置权限](https://mmbiz.qpic.cn/mmbiz_jpg/6EuqF9cSY2mBRKc75zia1JFOYe4BFyptxEVrMD6licHaiavcx3tdLPdnquicOWTdFVjaRN8aJt0ibSakz5fDMWdLmj3MZfeVI7mIT1DFtDX3Klro/640?wx_fmt=jpeg&from=appmsg)

**第二步：配模型。** 在「模型目录」里点「接入一个服务」，填服务地址和组织密钥。我接了**智谱 GLM**和 **MiniMax** 两家；密钥保存后只显示「已配置 · N 位」，不回显明文。配置一次，**所有客户端共用**，不用每台机器各自填 key。

![配置第二步：模型目录，接入智谱 GLM 与 MiniMax](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2nhYbNeIxwImNzbd0UptcFKAzicaglmibq2iadTJL1k6WFJNoGyoXXHg8FCjqWdtMy0KDcrYiaePib0EhTfIzLUEJ6ckImVK8FcJN8A/640?wx_fmt=jpeg&from=appmsg)

**第三步：建项目。** 在「项目与仓库」里新建项目，我把自己的开源项目 **AI-miniSOC** 配了进去——后面第二部分的实测需求，都挂在这个项目下流转。

![配置第三步：项目与仓库，登记 AI-miniSOC 项目](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2lDE82vUFAduFrgN4XXEVzYIAic9kKErEHhpxUyh3jgCVkMQdNw5OXGpOHfxCbeYN8ibqqgibe9O2pAo1ZUHoP6ZBWSiaIsYTOA1uk/640?wx_fmt=jpeg&from=appmsg)

三步配完，服务端就绪。

## 拓扑：两个入口，同一个实例

我把客户端、Hub 宿主机、Cloudflare 边缘三块和实测数字画在一张图里：

![SoduWork 自托管拓扑：两个入口，同一个实例](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2nLNSeGWgl9piaywvQj1klcf5Pew2EXia4auGAbiaD4hw28cJHzUiaclfD91Kqz7a2BoNl3gEFQWEXtN8SecJ1aiciak8xOsQVCqrnXk/640?wx_fmt=jpeg&from=appmsg)

三条链路，一句话说清各自的角色：

| 链路 | 用途 | 实测 |
| --- | --- | --- |
| Mac → Hub 局域网直连 | 日常主力 | 17ms，走 HTTPS |
| Mac → Cloudflare → Hub | 异地 / 移动网络 | 约 1962ms，无需公网 IP |
| Cloudflare → Hub 回源 | 公网入口落到内网 | 隧道出向建立，不映射端口 |

两个关于信任的细节：

* **局域网端**

  用 Local Root CA 签的自签名证书，客户端第一次连它必然要处理一次证书信任——这不是配置错误，是本地自托管的正常代价；
* **公网端**

  由 Cloudflare 在边缘终结 TLS，你从外网访问看到的是公网证书。最妙的是 Cloudflare Tunnel 是**出向**建立的：宿主机不需要公网 IP、不需要在路由器上映射任何端口，这让它可以藏在内网深处。

## 怎么证明它真的通：四条验收标准

装完不算完。我把目标压到一个边界非常清楚的范围内——**验证自建 Hub 的「双入口可用且一致」**，验收标准事先定好四条，缺一条就算失败：

1. 局域网入口 `GET /healthz` 返回 200；
2. 公网入口 `GET /healthz` 返回 200；
3. **两个入口返回的是同一个实例**

   ——用 `rework.lastSweepAt` 时间戳比对，相同才算同实例；
4. 未认证访问受保护端点 `/api/v1/runners`，两个入口都必须返回 **401**，不能有任何一个是 200。

为什么第 3、4 条这么定？因为前两条太容易被假象满足：一个反向代理可以让两个地址都返回 200，但后面接的完全是两套东西；一个配置宽松的部署也可以让两个地址都 200，但把谁都能读的东西当成了「能用」。**只有第 3 条证明「是同一个」，只有第 4 条证明「不该进的进不去」。**

## Agent 的五步验证

这次验证本身就是交给 Agent 的第一个任务。它没有直接开工，而是先摸环境再动手：

1. **确认安装事实**

   ：读 `Info.plist` 拿到客户端版本 `1.13.19`，同时发现本机 `127.0.0.1:18989` 上还有一个源码启动器起的开发实例；
2. **发现拓扑和预期不同**

   ：查 `ifconfig` 发现本机 IP 是 `192.168.0.29 / .31`——**不是**`.128`，于是把「Hub 在本机」的假设纠正为「跨机器 + 隧道」。如果跳过这步直接测 localhost，整个实验从第一步就错了；
3. **读出真实接入痕迹**

   ：客户端 `device-auth.json` 里存着 4 个 Hub profile，创建时间依次是 `127.0.0.1:18989` → `https://192.168.0.128` → `https://sodowork.doai8.dpdns.org` → 官方云 `https://service.soduwork.ai`——正好是「本地 → 局域网 → 公网 → 也想试试官方」的真实探索路径；
4. **写可复现的验证脚本**

   ：把四条验收标准落成 `verify-hub.sh`，任何人一条命令就能重跑结论；
5. **执行并留证**

   ：跑脚本，输出存成 `evidence-verify.txt`。证据是文件，不是记忆。

## 结果依据在哪里

下面每一条都能被你自己重跑验证（原文输出摘自 `evidence-verify.txt`）。

**健康检查——两个入口都通：**

```
== 1. 健康检查 ==https://192.168.0.128/healthz            200|0.017560https://sodowork.doai8.dpdns.org/healthz 200|1.962542
```

局域网 **17ms**，公网 **1962ms**，差 115 倍，但完全合理：公网那 1.9 秒里含 Cloudflare 边缘节点（`cf-ray` 显示走了 AMS 阿姆斯特丹）的跨境往返，响应头里的 `server-timing: app;dur=…` 显示 Hub 自己的处理在 10ms 量级。**延迟几乎全部来自那趟跨境往返，不是 Hub 慢。**

顺带一个坑：`/healthz` 用 `HEAD` 请求会返回 **404**。如果你用 `curl -I` 探活，会误判成服务挂了。要用 `GET`。

**实例一致性——确认是同一个：**

```
== 2. 实例一致性 ==LAN=2026-11-22T08:05:42+00:00PUB=2026-11-22T08:05:42+00:00结论: 同一实例
```

`rework.lastSweepAt` 是 Hub 后台清理任务的时间戳，两个入口抓到**完全相同的一秒**——这基本排除了「两个入口后面是两套库」的可能。这一条证伪的是最容易发生的部署错误。

**鉴权边界——不该进的进不去：**

```
== 3. 鉴权边界 ==https://192.168.0.128/api/v1/runners             401https://sodowork.doai8.dpdns.org/api/v1/runners  401
```

返回体是 `{"detail":"需要有效的 SoduWork 设备会话"}`。两侧都是 401，说明**公网暴露没有削弱鉴权**：Cloudflare 只是转发，鉴权仍然由 Hub 自己做。把内网服务挂到公网，最怕的就是某条路径意外放行——能访问 ≠ 该访问，401 才是好消息。

**公共端点——公网入口能给出完整前端：**

```
== 4. 公共端点 ==https://sodowork.doai8.dpdns.org/readyz                  200https://sodowork.doai8.dpdns.org/api/v1/auth/providers   200
```

根路径返回完整的 SoduWork HTML，`/readyz` 也 200。`/api/v1/auth/providers` 返回 `{"items":[]}`——这台 Hub 没接企业身份源，走本地账号登录；想接 SSO 的话这里会是空的，得单独配。

## 桌面客户端：手动连上自建 Hub

脚本验证的是服务端，最后补上「客户端 ↔ 自建 Hub」的端到端一环——在桌面客户端的登录页展开「服务连接」，填入自建服务地址 `https://sudowork.doai8.dpdns.org`，点「保存并连接」：

![客户端登录页：填入自建 Hub 服务地址](https://mmbiz.qpic.cn/mmbiz_jpg/6EuqF9cSY2nkSvTwcy846Nkdpr6UKo7kibq8VaYoejiboxVbE3J1yIQgv0nwUXv4Qib91FeT8icaYwgxFibydgh515iaJqDnE9q7olEbYBu00wvWw/640?wx_fmt=jpeg&from=appmsg)

输入管理端建好的用户名密码，登录进来就是主界面——左侧已经有项目「AI-miniSOC」和它的会话：

![客户端登录成功，进入主界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2lBH4j23bNBT1HVyhjLaCn27jdwyvsTdlsw1KUOj4jib2FLfCSkx0nem2C7NjpMeGoKw0xfTnmwibhvJiaT9VibBFqpgWsoMUicib2Uw/640?wx_fmt=jpeg&from=appmsg)

接着配置干活的 Agent。客户端内置了 **Pi**（轻快，原生支持 Agent Skills，和 Claude Code 同一套标准），也可一键安装 Codex、Kimi Code、Qwen Code、OpenCode 等一排开源 Agent：

![Agent 管理：内置 Pi，可装 Codex、Kimi Code、Qwen Code 等](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2nl69bIalYdKq5MtictutFEHh5SFGjpUutwk0fwBxBIgLqbzRa2P5iaYFhhXNDbPmhuBp4F4HYfu96YttIKjfa7anPEGBevAqLUE/640?wx_fmt=jpeg&from=appmsg)

给 Agent 选模型并「测一下」——测试是真跑一轮最小的活，不是 ping 一下。Pi 用的是 Hub 上配好的智谱 GLM；顺手验证了它的说明：模型配置写到 `~/.pi/agent/models.json`，**密钥只写变量名，明文不落盘**：

![给 Pi 选模型并测试通过](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2m20DLBfcbh74UYt6SXnCWFic2zdclfU7dHOAkSWhkZVdkH6qk34VoyMPKsTP9ibtvXxLtPudd7NNIoVClB3sIUjKXDp0arlKAn0/640?wx_fmt=jpeg&from=appmsg)

模型这块的设计很务实：客户端会**自动获取 Hub 上配好的模型服务**（智谱 GLM、MiniMax 直接出现），也可以配自己本地代理的服务——我本机有个 `127.0.0.1` 的代理挂了 29 个模型，一样能用：

![我的模型：Hub 共享模型 + 本地代理模型并存](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6EuqF9cSY2kC1RRsq3ialpRkxLnMfKp7lxBeyv4tVLaapiaBahggVZTJ6BU5lm6kaQgS1P0w8Yw3n3G90CnAWgdvcw4LxTR5hFNldv8wNEoLY/640?wx_fmt=jpeg&from=appmsg)

回到 Hub 管理端的「运行监控」，能看到各个客户端的连接情况——我有**两台机器**装了客户端，都连上来了，状态「可接活」，顺带还能看到服务请求的 P95：

![Hub 运行监控：两台客户端在线、可接活](https:/...