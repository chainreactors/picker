---
title: 开源AI渗透测试工具Z3r0部署与使用
url: https://mp.weixin.qq.com/s/48cIca39y2lJD7Lt2yAdkA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:43:26.836570
---

# 开源AI渗透测试工具Z3r0部署与使用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hzXgvqPiczO3T5QDFqmic1b3UKHTDqu0yXrx9mbjxVtbbUxdU74SRTcHGicxYgV0bH0YjfHVicmzwO5Ve9rxDmTBjAjcFZHrq3q16bH6BAqopaU/0?wx_fmt=jpeg)

# 开源AI渗透测试工具Z3r0部署与使用

第59号

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**0****1**

**Z3r0 简介**

Z3r0 是面向红队协作的控制平面型工作台。它将 React 操作台、FastAPI 管理平面、会话级多智能体运行时、项目级证据记录、分布式 Docker 沙箱资源和受控出口层组合在一起。Z3r0 的设计目标是让智能体辅助的安全工作具备清晰边界和可复核性。对话不是唯一事实来源；项目范围、资产、漏洞发现、关系图、攻击路径、沙箱资源、出口策略和可回放时间线都作为显式应用数据管理。

Z3r0 项目开源地址为：

https://github.com/yv1ing/Z3r0

![image1.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO3nL2ibVVhqBpj8l3FWYlHqibC8LcIt3nxlkw9QokBPSum2cYRKORhatdd1Lz0h4LfS6Yqv2JSn2hggm8VLffWibIGyw41xztt30M/640?wx_fmt=png&from=appmsg)

**0****2**

**Z3r0 架构**

Z3r0 将系统划分为四个架构平面：

* 控制平面：用户、系统配置、智能体、会话、WorkProject、托管主机、沙箱镜像、沙箱容器和出口代理。
* 运行时平面：多智能体会话执行、实时事件流、长周期任务连续性、历史投影和时间线回放。
* 证据平面：项目范围、资产、漏洞发现、关系图、攻击路径、任务进度和智能体摘要。
* 执行平面：Docker 主机、沙箱容器、Shell/文件/noVNC 访问、命令执行、沙箱技能和出站网络策略。

Z3r0 架构如下图所示

![image2.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO0IKaFcmhX6pKmf1M0DKQet9eVjiaYmOx7SJQxLaALjMS8S3ybLuNBcMq2U7bsKmfMLeXSrAEy8OLs0qQRHATejfrWbo5dicjsC8/640?wx_fmt=png&from=appmsg)

**0****3**

**Z3r0 本地部署**

通过 GitHub 获取最新代码：

git clone https://github.com/yv1ing/Z3r0.git && cd Z3r0

![image3.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO2icyRBvEicmeibBqpLgnPPxZZq33NNySSsFiabEd5OrRRj77u8OBsP39YS8shWyVNuRSEB8YQNR7BDCSoplasbxF70Z7SduD6aSx4/640?wx_fmt=png&from=appmsg)

构建对应的沙盒镜像

cd sandbox && bash build.sh

![image4.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO2dQOCrLytR0skibN9U4icEAcqdn0olicdN43ibFsVHto4RsgBowwGlMYLOjhANGkSmNicLeXLQgmr34coKF2OYLoic9Ckmf49oiav15o/640?wx_fmt=png&from=appmsg)

拷贝并编辑配置文件

cp .z3r0/config.json.example .z3r0/config.json

![image5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO0qhR8EIBtOKmz58Ju1K3zibGfCKLXx1eQ5227CEVpGpb5oAAg9BiczM9iaPmVdzOpiaibcrULqrPJkCkOygQCBMickQsJ8I1wqm3Bh0/640?wx_fmt=png&from=appmsg)

![image6.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO0Hs8fWPPBiauQdaicHra4NImKiadZSSoHhCkqicDlVBhoxEiaMwRzbAIRiak0F62400aYCEfeShNM6YRXcdicwSicxZOuP1BDw7UR0LeI/640?wx_fmt=png&from=appmsg)

最后启动环境

docker compose -f docker-compose.prod.yml up -d --build

![image7.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO1FLPMRFicnLMZRY1rzGnH5G0ghfL1fZHbKmuucT3ZNg973B3mRGVDCWqe03OwWvcUQ7jEhgEFiaEAwlEGauS6GACjhBumyQNeGQ/640?wx_fmt=png&from=appmsg)

![image8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO23ve7wjguve7gt5ibpu1eXhz9gtkegva5W6AVtjeZmhEbyHZVKnh8LTUibDUHJ2SKKKvLlfxkJrGQxKkxKkoXQ6KpPzutLjgTvU/640?wx_fmt=png&from=appmsg)

浏览器访问 http://ip:8000/，输入配置的账号密码登录即可。

![image9.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO1E7iavLGaXhVenp61ljhPUDlMYKLapMaZNStfgvnITSfjg23pVs8SGFLPuHic9s3oibiahG5r45ibbiaMjAXckzYNIgKQnS6aaMVkRg/640?wx_fmt=png&from=appmsg)

**0****4**

**Z3r0 使用测试**

在 Chat 窗口中，输入目标 URL 即可开始自动化渗透测试

![image10.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO0oiatUpcUicuicHZek6lqxBVu3h2XPlHcSF5bvFd8SJIN0WSQtFCBSCPRaek5qAa1E6fuWjlchj2EnBhSTrkx3rovo5lKPDymv10/640?wx_fmt=png&from=appmsg)

会实时输出当前测试阶段、状态和调用的 tools。

![image11.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO2hzdLPOGDrb0uAaYa1rTzGjclrAafEFroNn1GQMtUh5icwJfdZCqkdNqkgpfFUpWRGGiaxJNttMvAIBqiaibsfsaslovr5WgJb5hY/640?wx_fmt=png&from=appmsg)

**05**

**总结**

Z3r0 作为一款 AI 驱动的安全测试框架，其核心优势在于构建了由多专家智能体组成的“虚拟红队”，能够模拟人类安全团队的协作模式，有效应对逻辑漏洞等复杂场景；同时，它采用证据驱动和可复核的数据管理机制，将所有操作记录为可回放的时间线，便于审计复盘，并通过 Docker 沙箱集成常用安全工具，提供受控的执行环境和灵活的代理策略，长周期任务的后台运行能力也避免了阻塞等待，且部署可通过 Docker Compose 完成，门槛较低。Z3r0 每个专家智能体均需独立配置第三方大模型 API，使用成本和稳定性高度依赖外部服务；此外，作为较新的开源项目，生态尚不成熟，生产环境下的稳定性和功能覆盖度仍有待更多实践验证。

### RECOMMEND **往期推荐** [![](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO0SMNCPvU1vDiaPcEq4Vao3xibl6NgY0XhvzDywAmpcIJcACra9Qnl8uKRhzf7VMc09sKnRmhB42mE9HEv3AAHiaeYryFsZ8NP5QI/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247497943&idx=1&sn=437b4befe634abf7e26b4b62dd95cfde&scene=21#wechat_redirect) [![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gauNkjeXJb5VLZrR03Q2JTsgTB124MibzBJkibVbX0vzYpsYlkbuRmw5ic8xnnw6s4r3BkgmSkVBuicS54iapQBia9xA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247497312&idx=1&sn=02380f9e0dd0f812a2cbbd8822c824be&scene=21#wechat_redirect) [![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gauNkjeXJb5VLZrR03Q2JTsgTB124MibzoB7CNJhZOic4plXRgWm3W5EpOhgF19UNUGMyOWcNbwmqoXwIq1MLBJA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247497100&idx=1&sn=aa07c87a223bb9d8b98f88eeef80f29a&scene=21#wechat_redirect) [![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gauNkjeXJb5VLZrR03Q2JTsgTB124MibzjJbHwJu3XhiamSXibbu5Kic8v9akqIdLeWibYMSEnVtnVSKMl0CEgp1Emg/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI0NDgxMzgxNA==&mid=2247497212&idx=1&sn=00a35c04afea6209b67e089293c1b5d3&scene=21#wechat_redirect) ![图片](https://mmbiz.qpic.cn/mmbiz_gif/C6nwdaicQKwWT4HLCv7hz9cCjEYLXqWZJayhCdh0Ix1GdDpSicv8wAlW178gA8TSndNp9mZcsYGr6ubhibS8Odomg/640?wx_fmt=gif&) 美创科技第59号安全实验室，建有余杭区首家“网络与信息安全管理员技能大师工作室”，专注于数据安全技术领域研究，聚焦于安全防御理念、攻防技术、漏洞挖掘等专业研究，进行知识产权转化并赋能于产品。自2021年起，累计向 CNVD、CNNVD 等平台提报数千个高质量原创漏洞，并入选国家信息安全漏洞库（CNNVD）技术支撑单位（二级）、信创政务产品安全漏洞库支撑单位，团队申请发明专利二十余项，发表多篇科技论文，著有《Java代码审计实战》《数据安全实践指南》、《内网渗透实战攻略》等。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gauNkjeXJb7iaVEL8YPqBia2DFmwcRWazrwrXXUlEFG1hPqHS7ZRB0rIKtr5akHcick35AvQ15c9ts5FSZBAW0cSw/0?wx_fmt=png)

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