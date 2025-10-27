---
title: 防御任意SSH远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485842&idx=1&sn=6a462334aa94328aa7689f1ddf80be6a&chksm=fb04cafacc7343ec8a7d7b6f7a1e22e59e7773a2e66dcb46fb8d7e678f64be58e3ae3921bf3f&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2024-07-03
fetch_date: 2025-10-06T17:43:26.890209
---

# 防御任意SSH远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBAPib2CIqcabfppL6jUqYdY98mnplQGry8a3GZ20licPxqt66rmLiaPdYCAsTHcwl7432sKL1IgB8llw/0?wx_fmt=jpeg)

# 防御任意SSH远程代码执行漏洞

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBAPib2CIqcabfppL6jUqYdY9Z4DqvNr3KJl4SMdGUbuICGfPbCFSQiaQCNblr0xPNk613t5SesymQfg/640?wx_fmt=jpeg)

近期，OpenSSH服务器(sshd)中发现了一个严重的远程代码执行漏洞(CVE-2024-6387)，被称为"regreSSHion"。这个漏洞影响了大量互联网上的SSH服务器，可能导致未经授权的远程攻击者以root权限执行任意代码。在这种背景下，spiped（开源）作为一个安全管道守护进程，为我们提供了一种额外的防御层，可以有效地缓解此类SSH漏洞的风险。

spiped的工作原理：spiped通过在SSH服务之前添加一层加密和认证，为SSH连接提供了额外的保护。它使用预共享的密钥来加密通信，这意味着即使攻击者能够利用SSH服务器的漏洞，他们仍然需要突破spiped的加密层。

使用spiped保护SSH的步骤：

1. 安装spiped：在Ubuntu或Debian系统上，可以使用 `sudo apt install spiped` 安装。
2. 生成密钥：

   ```
   sudo dd if=/dev/urandom bs=32 count=1 of=/etc/ssh/spiped.key
   sudo chmod 600 /etc/ssh/spiped.key
   ```
3. 配置spiped服务：创建一个systemd服务文件 `/etc/systemd/system/spiped-ssh.service`：

   ```
   Copy

   [Unit]
   Description=Spiped for SSH
   After=network.target

   [Service]
   ExecStart=/usr/bin/spiped -d -s '[0.0.0.0]:8022' -t '[127.0.0.1]:22' -k /etc/ssh/spiped.key
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
4. 启动spiped服务：

   ```
   Copy

   sudo systemctl enable spiped-ssh.service
   sudo systemctl start spiped-ssh.service
   ```
5. 配置防火墙：阻止直接访问SSH端口(22)，只允许通过spiped端口(8022)访问：

   ```
   Copy

   sudo ufw allow 8022/tcp
   sudo ufw deny 22/tcp
   sudo ufw reload
   ```
6. 客户端配置：在客户端的 `~/.ssh/config` 中添加：

   ```
   Copy

   Host your_server
       ProxyCommand spipe -t %h:8022 -k ~/.ssh/spiped_your_server_key
   ```

通过这种配置，即使SSH服务器存在漏洞，攻击者也无法直接利用它，因为所有的连接都需要先通过spiped的加密层。这大大提高了系统的安全性。

spiped的优势：

1. 额外的加密层：即使SSH本身存在漏洞，攻击者也需要先突破spiped的加密。
2. 灵活性：可以轻松地在不同的服务器之间移植和部署。
3. 简单性：相比复杂的VPN解决方案，spiped更加轻量和易于配置。
4. 与现有系统兼容：不需要修改SSH服务器的配置。

结论：在面对如CVE-2024-6387这样的严重SSH漏洞时，spiped提供了一种简单而有效的额外防御手段。通过在SSH服务前添加这一层保护，组织可以显著降低被远程攻击的风险。然而，需要注意的是，spiped应该被视为深度防御策略的一部分，而不是唯一的安全措施。定期更新系统、应用安全补丁、实施强密码策略等基本安全实践仍然是必不可少的。

通过结合使用spiped和其他安全最佳实践，我们可以大大提高SSH服务器的安全性，为敏感的远程访问提供更强大的保护。

```
附录A：
有关OpenSSH"regreSSHion"漏洞(CVE-2024-6387)的主要信息:
1. 漏洞概述:   - 这是OpenSSH服务器(sshd)中的一个远程未经身份验证的代码执行(RCE)漏洞。   - 它是一个信号处理器竞争条件,允许在基于glibc的Linux系统上以root权限执行远程代码。   - 这个漏洞影响了sshd的默认配置。
2. 影响范围:   - 超过1400万个可能易受攻击的OpenSSH服务器实例暴露在互联网上。   - 约70万个外部面向互联网的实例易受攻击,占全球客户基础中所有面向互联网的OpenSSH实例的31%。
3. 受影响的版本:   - 4.4p1之前的版本(除非修补了CVE-2006-5051和CVE-2008-4109)。   - 8.5p1到9.8p1之间的版本(不包括9.8p1)。   - 4.4p1到8.5p1之间的版本不受影响。
4. 漏洞的历史:   - 这是2006年报告的CVE-2006-5051漏洞的回归。   - 该回归是在2020年10月(OpenSSH 8.5p1)引入的。
5. 潜在影响:   - 可能导致完全的系统入侵,允许攻击者以最高权限执行任意代码。   - 可能导致数据泄露、恶意软件安装、安全机制绕过等严重后果。
6. 缓解措施:   - 尽快应用可用的OpenSSH补丁。   - 限制SSH访问,加强访问控制。   - 实施网络分段和入侵检测系统。
7. 其他注意事项:   - OpenBSD系统不受此漏洞影响。   - 虽然漏洞利用具有挑战性,但深度学习的进步可能会增加成功利用的可能性。
```

```
附录B：OpenSSH "regreSSHion"漏洞（CVE-2024-6387）的具体利用方法解读：
1. 攻击原理：   - 利用SIGALRM信号中断PAM（可插拔认证模块）相关函数的调用。   - 使PAM的结构处于不一致状态。   - 在SIGALRM处理程序中利用这种不一致状态。
2. 攻击难度：   - 平均需要约10,000次尝试才能成功利用这个竞争条件。   - 在特定配置下（MaxStartups=10，LoginGraceTime=120秒），平均需要1-2天才能获得远程root shell。
3. 针对Debian 12.5.0（OpenSSH 9.2p1）的具体攻击：   - 使用SIGALRM中断malloc()调用（在sshd的公钥解析代码中）。   - 使堆处于不一致状态。   - 在SIGALRM处理程序中（具体在syslog()内）利用这种不一致状态。
4. Debian版本的攻击效率：   - 平均需要约10,000次尝试。   - 在特定配置下（MaxStartups=100，LoginGraceTime=120秒），约需3-4小时。   - 由于ASLR（地址空间布局随机化），最终获得远程root shell平均需要6-8小时。
5. 研究状态：   - 目前仅针对虚拟机环境，未在物理服务器上测试。   - 测试环境网络链路相对稳定（约10ms数据包抖动）。   - 研究人员认为攻击方法还有很大改进空间。   - 正在开发针对amd64架构的漏洞利用，但难度更大。
需要强调的是，这些信息描述了高度技术性的攻击方法，仅供安全研究和防御目的使用。任何未经授权的实际攻击行为都是非法和不道德的。组织应该尽快应用安全补丁来防御这种漏洞。
```

参考资料：

https://www.daemonology.net/blog/2012-08-30-protecting-sshd-using-spiped.html

https://github.com/Tarsnap/spiped

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
 **APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
4. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
5. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
6. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a9017498efb3fd2da46de5c38c0d4599c2e01100&scene=21#wechat_redirect)
7. [NSA TAO负责人警告私营部门不要搞“黑回去”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485250&idx=1&sn=a35def8b58f86f8a149e335f3df3a1c9&chksm=fb04c42acc734d3cdfd1e8f2ae852731c3569533ab8fa83bd0126b788ea20673a2f912cdf011&scene=21#wechat_redirect)

**入侵分析与红队攻防**

1. [入侵分析与痛苦金字塔](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485464&idx=1&sn=f05718bec99d4506a8fe1c49dc2bf337&chksm=fb04cb70cc734266a436d4225d4eb0486becaed5f0258748e6ff3de46a22caaa01b0da1b0e4f&scene=21#wechat_redirect)
2. [资深红队专家谈EDR的工作原理与规避](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485494&idx=1&sn=f45125e76dd412a291cfa3bccd5943c5&chksm=fb04cb5ecc734248332218f7df17be9a31d4b09777b8cd846b69821248a5e75b44baa6bfbfe4&scene=21#wechat_redirect)

**天御智库**

1. [独家研判：五眼情报机构黑客纷纷浮出水面](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485100&idx=1&sn=b88f8864594b76d4e1412db7cf204f77&chksm=fb04c5c4cc734cd2f5440ee760377afce1745a3abade998a40b9fe3752acb3be14574e6e6f9a&scene=21#wechat_redirect)
2. [美军前出狩猎并不孤单，美国网络外交局优先事项...