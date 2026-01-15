---
title: WebDAV+frp内网穿透工具实现像访问本地硬盘一样访问远程NAS
url: https://mp.weixin.qq.com/s/08ebn1aR50JIG4hArDzu9w
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:34.541272
---

# WebDAV+frp内网穿透工具实现像访问本地硬盘一样访问远程NAS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJY7JOfO9sQ9kaRI6duzo4X4EGSRcVdYwsicia2Uy3WQ7TUN0tWc1GXB8g/0?wx_fmt=jpeg)

# WebDAV+frp内网穿透工具实现像访问本地硬盘一样访问远程NAS

原创

yuanfan2012

Linux运维实践派

![]()

在小说阅读器中沉浸阅读

# WebDAV+frp内网穿透工具实现像访问本地硬盘一样访问远程NAS

# 场景及问题

![](https://mmbiz.qpic.cn/mmbiz_png/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJ0KLnBSEKpfAnW9QJOw7WMnzsgRI5aXzzVQx9zzAmh8f7fqiaaj6RHFw/640?wx_fmt=png&from=appmsg)

#

1、家庭宽带下的家用NAS有时因在外面临时需要访问

2、例如有些文档需要在线编辑且需要自动同步到NAS上（群晖的Drive Office在线编辑不太满足需求）

3、想通过内网穿透的方式将群晖NAS的SMB 445端口通过云服务器映射出来，但是运营商会封锁445这种高危端口

4、所以想到使用WebDAV这个协议来解决这个问题

# 具体步骤

## 1、群晖上下载WebDAV Server套件

并开启WebDAV Server服务 默认端口5005

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJ7BhRu1u0mzmWerFJ0H37pM0iaibQaXn2hZnBvwlNpmd1JUGKUICJIkXQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJb9wa1fBMWdLBXpwhT9WlC2lWRduz8pFqnW4DmB5L6fE24hQjMDeXfA/640?wx_fmt=jpeg&from=appmsg)

## 2、云服务器部署内网穿透FRPS服务端

可以参考之前的文章

[腾讯云主机上部署FRP+Teamviewer穿透内网进行远程运维](https://mp.weixin.qq.com/s?__biz=MzU2MjU1OTE0MA==&mid=2247489650&idx=1&sn=b7361175e9edb1021c6cd99dedbfe40f&scene=21#wechat_redirect)

[使用FRP内网穿透工具实现"安全访问"家中群晖NAS](https://mp.weixin.qq.com/s?__biz=MzU2MjU1OTE0MA==&mid=2247497998&idx=1&sn=39018a13a38b0205c833e8e21a1bec23&scene=21#wechat_redirect)

具体配置frps.ini参考如下

```
[common]
bind_address = 0.0.0.0
bind_port = FRPS的监听端口

authentication_method = token
authenticate_heartbeats = false
authenticate_new_work_conns = false
token = FRPS服务TOKEN

log_file =  /usr/local/frp/logs/frps.log
log_level = info
log_max_days = 30
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJyCKycejJGW5483mbx9BArQurticnHmgaRiaGMgedu6Xj3QibN7MojJKqw/640?wx_fmt=jpeg&from=appmsg)

## 3、群晖部署内网穿透工具FRPC客户端

并映射webdav的服务端口

```
[common]
server_addr = 云服务器公网IP
server_port = FRPS的监听端口
authentication_method = token
authenticate_heartbeats = false
token = FRPS服务TOKEN
log_file =  /usr/local/frp/logs/frpc.log
log_level = info
log_max_days = 30

[918_synologyds220_ssh]
type = tcp
local_ip = 192.168.31.200
local_port = 22
remote_port = 29122

[918_synologyds220_http]
type = tcp
local_ip = 192.168.31.200
local_port = 5000
remote_port = 45000

[918_synologyds220_webdav]
type = tcp
local_ip = 192.168.31.200
local_port = 5005
remote_port = 5005
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJWFcQgO4cSJ8icZTLnn1zcv387d4ibyliaRiarXibVuxI2Bbia3uoXXGib6xOw/640?wx_fmt=jpeg&from=appmsg)

## 4、云服务器安全组放开5005 WebDAV端口

云服务器安全组上要设置5005端口对外开放，如果有安全考量，可以设置单独开放给固定的公网IP

## 5、win11系统运行下面脚本开启WebDAV 服务并设置成开机自启

```
@echo off
chcp 65001 >nul
title 配置WebClient服务

REM 检查是否以管理员权限运行
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo 请以管理员身份运行此脚本！
    pause
    exit /b 1
)

echo 正在修改注册表...
echo.

REM 修改注册表值
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters" /v BasicAuthLevel /t REG_DWORD /d 2 /f

if %errorLevel% equ 0 (
    echo 注册表修改成功！
) else (
    echo 注册表修改失败！
    pause
    exit /b 1
)

echo.
echo 正在配置WebClient服务...
echo.

REM 重启WebClient服务
net stop WebClient /y
timeout /t 2 /nobreak >nul

REM 设置服务为自动启动并启动服务
sc config WebClient start= auto
net start WebClient

if %errorLevel% equ 0 (
    echo.
    echo WebClient服务已成功配置为自动启动并已启动！
    echo.
    echo 配置完成！
) else (
    echo.
    echo 服务配置过程中出现错误！
)

REM 显示服务状态
echo.
echo WebClient服务当前状态：
sc query WebClient | findstr /C:"STATE"

pause
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJMFMngoFicLU0G9AxaReibdyYtnJdINkwgp6JubicRGjibbEWEjpH1eu9qw/640?wx_fmt=jpeg&from=appmsg)

## 6、挂载远程NAS的WebDAV目录

添加网络位置，输入云服务器的公网IP+端口5005和具体目录 输入NAS的账号与密码即可进行挂载

效果截图如下

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJSSgMzjt0ic47HGdomgzlzwTbxa3mOyW66W2ia0wn6lXLCvqwicGHYhNhQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJeeYp9aico8txP1l1q1PwYCv9fQYDcgNtHiaEzWgUpqqth7fia5th7prIQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/n8kWxMqYcWX12TepMNl8NqXdHA2mmMsJHCOt4aIeBE216svmTx3tpVCWB9jb4FMgaSFDlZTfPwslia754LUM1eg/640?wx_fmt=jpeg&from=appmsg)

* 1、有此类需求的网友可以联系作者V:yuanfan2012协助部署黑群晖+frp内网穿透工具
* 2、非Win11系统可以使用RaiDrive免费工具来进行挂载

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n8kWxMqYcWWS0vr9oejHFQdX6f1Bibk8ZkRv5UaViaZjHKTfIbmv2N4ibFebWqCQoHBAo3VY8cgRtHAKYMy7dt8VQ/0?wx_fmt=png)

Linux运维实践派

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n8kWxMqYcWWS0vr9oejHFQdX6f1Bibk8ZkRv5UaViaZjHKTfIbmv2N4ibFebWqCQoHBAo3VY8cgRtHAKYMy7dt8VQ/0?wx_fmt=png)

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