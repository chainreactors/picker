---
title: 2026 年第三届 “聚合 獬豸杯” WP|通过ai学取证系列|检材3-服务器取证详细解题思路
url: https://mp.weixin.qq.com/s/W3KOIbJUV_WM4IPEGRWDbA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:46:57.727347
---

# 2026 年第三届 “聚合 獬豸杯” WP|通过ai学取证系列|检材3-服务器取证详细解题思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RPq1g3ib528ia2LzibdkFeDRjXyTsB9uIyL0a04nB53HoshsIlticb3nlePQSRkksS5oVl2R1eSzQOBuwBdc2eQPibwR64bA8OMd9F7WHic5m0AaM/0?wx_fmt=jpeg)

# 2026 年第三届 “聚合 獬豸杯” WP|通过ai学取证系列|检材3-服务器取证详细解题思路

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 📢 免责声明

本文所述技术仅用于合法授权的安全研究、教学演示及防御机制开发。作者及发布平台不承担因读者误用、滥用本内容所导致的任何法律责任。请严格遵守《中华人民共和国网络安全法》及相关法律法规。

```
所有内容仅供参考：比赛平台：https://forensics.didctf.com/contests/8检材正式发布夸克网盘：https://pan.quark.cn/s/5b6461610d07百度网盘：https://pan.baidu.com/s/13gYBnh1Mw8N2uS0XzmWMRA?pwd=hvysSHA-256校验值：82143788C36FCF1B4C549DD83514C2670A89C494F644F3A3C4FA415246EDD394检材密码：EVJbYf&+eStnx5B+C^bj%YPSr)gr
```

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528hicdvicicteHDo4NjlMibFKLrsthxrnia2Zz92yrFtLfojIA5EYC9GTsPocjXWTOnu0rnae7F6UNMRZaRPUm3X5Tbb3UniciavtE8TcY/640?wx_fmt=png&from=appmsg)

# 检材3-服务器取证

服务器用了 \*\*LVM\*\*，根分区是 \*\*XFS\*\*（CentOS 7 默认），所以挂载分三层：E01 → 回环设备 → LVM → 文件系统。

1. 第 1~12、14、15、20 题（检材3 本机可解）
2. 第 13、16~19 题（跨检材：解密 windows检材中的 BitLocker 取真账本）

### 跨检材取证：第 13、16~19 题  为什么这几题在检材3 本机查不到

```
sudo cat .../fk/config.php          # "host" => "192.168.203.155"  ← 网站连的是【远程】数据库
sudo ls /casework/ev3/var/lib/mysql/fk/     # 空目录（本地业务库已被删）
```

* 本地 `/opt/faka.sql` 只是**演示/种子数据**：`shua_orders` 仅 3 条 2023 年、金额为 0 的测试单。
* `/tmp/db_backup/*.sql.gz`

  自动备份全是 20 字节空文件（本地库空，备份也空）。
* 对整盘做原始字符串扫描，**检材3 内不存在任何 2025 年订单数据**。

结论：真账本不在检材3，需顺着取证链找到嫌疑人电脑（检材2）。

---

## 0-镜像仿真

### 1.1. 网络环境

服务器仿真，最好先看一下网络环境，在DHCP租约文件里`cl(7UtLZ8-1t5H-dfYW-SDnK-4V6Y-OitP-voJrld)/分区1/var/lib/dhclient`可以找到`本机实际获得的IP``192.168.203.153`。

根据实际`IP`进行设置网络环境，

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528hzVYfl2KacttmuXS8icNs0nVic1ibXD7yZpSe1P1szphdibJrYEWznQGCBlpzPvKMsfSyjKFIKLeREoSe68qblKeTy2QBLFSLL4Fc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528iarqs0YVnYZic6gd60hSQd02Gh79VibIV7kA5HiaaMB2DoGXyXJmToZwQQlEO2nuItTkoZUKktPjGvfL9nOict2CsXUwmzVUiaXnXTQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528jeHKQL3wpPBjChia15mkP7jyK9489zaPwu9HrS2MM8e1e26iaicCWZN1DIA4ubbvPqPyAjaFMZibvQMzJn9B83SMK8y09T4UV91ME/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528g3aficyu8b9I6azNAtica49hQW4NxHiaaV1NUXGiaQZgNpr4JcSlQIFL6jQqj4rdo2OOiarUicO4CYcibSZzX6N02srnYrYOGu2CvQew/640?wx_fmt=png&from=appmsg)

### 1.2. 如果需要使用ssh进行连接，请关闭`服务器第四题`AI部署的“守卫” 脚本，否则你会被自动踢下线

检材3 装了那个 AI 守卫(network-check.py):非白名单IP(非 192.168.203.100)远程登录,5分钟后被 pkill 强制踢出。你仿真时登录IP肯定不是它,不关掉会莫名其妙掉线。

```
systemctl stop net-monitor.service          # 立即停止 net-monitor.service这个systemd服务systemctl disable net-monitor.service       # 禁止它开机自启 net-monitor.service这个systemd服务atrm $(atq | awk 'print $1') 2>/dev/null    # 顺手清掉可能已排队的踢人任务pkill -f network-check.py 2>/dev/null				# 杀掉命令行里包含 network-check.py 的进程
```

### 1.3. 开启三大服务：数据库、PHP FastCGI 进程管理服务、Nginx（默认仿真起来是都开着的）

```
systemctl start mysqld php-fpm nginx       systemctl status mysqld php-fpm nginx
```

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528iayicicYMAwXwS6qoARMgEoB2rPb0AGdIAAKAQwz159ggOfwp4em8J284R1zf5fJLcGwA9xsxxMhvet5zbYItJW61jqOQkxv0BCk/640?wx_fmt=png&from=appmsg)

### 1.4. 给数据库喂数据（原机数据库是空的）

第一步：首先确认`本机`是否可以通过`Root@123456`登进本地MySQL：

```
mysql -uroot -p'Root@123456' -e "show databases;"
```

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528jiaNCusYIcu5xRreiamPHttUooGRrDPA7DFm1CDvAhicaau6jfQPfHdKEqlUic4vSbEmstmnB5HaPU85hpw5jGEVMNhfQcnZOLfkE/640?wx_fmt=png&from=appmsg)

第二步：想要`真实数据（2025订单）`->把检材2 BitLocker卷里的 `faka_backup.sql`拷近这台机器（`scp`）；（本机备份的`/opt/faka.sql`是演示数据）

```
scp faka_backup.sql root@192.168.203.153:/root
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528ht45ICcDraNeRaNFIKLTyuQqVUhwjF0A2icibEgUXrKR0vtvSMibvjPmzibqgAkmJ92mfTfSPsibBkSNgka4lmqzPllrIkFibJjW6iaw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528iaLo4icX4Fic4naPdk6VN66hP2g0uESfn0aBLQicwn4Vciab9MYzYgkbudEicfTwvxwMxlgt4Vm3saEzudORwtsMjqYB3LqmB5ibVcFw/640?wx_fmt=png&from=appmsg)

第三步：将真实的数据导入`mysql`数据库

```
# 创建名为 fk 的数据库mysql -uroot -p'Root@123456' -e "CREATE DATABASE IF NOT EXISTS fk DEFAULT CHARACTER SET utf8mb4;"# 将备份sql数据导入 fk 数据库中mysql -uroot -p'Root@123456' fk < /root/faka_backup.sql# 验证数据是否成功导入mysql -uroot -p'Root@123456' -e "SELECT COUNT(*) FROM fk.shua_orders;"
```

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528gJLIKPXpV8ic7GQ3c9P5ibyruiaFiaKw1rXzQX0gxvuugh49pEibkMffTvnJicQl65EQP5gKsQmYMCnSRkOpKnCcHo7yRic2LupPAFhQ/640?wx_fmt=png&from=appmsg)

第四步：更改网站`config.php`将host指回本机

```
 vi /usr/share/nginx/html/fk/config.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528hJeo6FbDVgyQdqFHmJmhLVQ6OKBibbby9so2eegic6J4urrgRnKH3huUUHByTialM6siaAjvhOlbPnVicrkNYUoMAicocmSbFlbgHYs/640?wx_fmt=png&from=appmsg)

### 1.5. 获取网站`admin`真实密码

在本机备份的`/opt/faka.sql`中有明文的`admin`密码`wy0719`，但后续尝试的登录发现不是。

在`检材2 BitLocker卷里的``faka_backup.sql`文件中可以知道`password`进行了加密并且`盐值`为：`2025baofu!`，加密方式：`$pass = hash('sha256', $pass .PWD);`

使用`hashcat`进行破解`hashcat -m 1410 -a 0 "94bd34e3010a6468f312eafe359e9d926fc16bba62c0b6cf646d041a5c281bf2:2025baofu\!" /usr/share/wordlists/rockyou.txt`

得到`abc123456`

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528gaM8PcVabXAMeSQnjzwXPxAic0Vd00YnWv9KN6Yz6pnqjuleb72MCTbbSncGvhlmKF9JfZSLQNvI7icANxVcUw0gCSPtCpqb7Eg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528hvBzgViaibvibvIwWP1ZpucU3xnKIssfCTstWxkqqUNVVTfM9WDMia8m2Ikc9cQwBvTvdQ3J71GDiaR7anz7pf512z2UxxH52LM5fc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528jh2laXtGSUbC1FMQ1fy8o19eMicTEUGl9qV0FWzhldCSZF0M8ewMrnT7rCCicVZFwqLeiap3KwiaF1dEy6VNkLcX0bOocvFkdFZFE/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528gpuWezBAv78F28p4UUSkx6XloxAibzvwtpkZIlyGj5scwM9GXseaIW80nBZSFlaibPLy2V9260Cx5Os8R963KsaaV0al8VkjvtA/640?wx_fmt=png&from=appmsg)

### 1.6. 网站放行

#### 1.6.1. # 防火墙放行 8081

```
firewall-cmd --add-port=8081/tcp --permanent && firewall-cmd --reload
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528hTgQibd9pic9IWmKKPz7zXb4sIjV7TFFSSJibOloMAA9nEu1BSkWjJ9CfZOpWcNp65YERX0HmErlc5ZGicjHfyxhrwibiaXGa9rdJ4E/640?wx_fmt=png&from=appmsg)

#### 1.6.2. # SELinux 若开启会挡 nginx 连 php/网络,仿真环境直接设宽松

```
setenforce 0
```

#### 1.6.3. 重启 php-fpm 生效

```
systemctl restart php-fpm
```

### 1.7. 解决网站登录过程中一直弹窗的问题

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528jaSN1W7lm5CagHeiah5ntQwkRrdM2ZCVibBh6RyBZYDoCvYibe9gfC86r4piboxez93ZSRdQibZBiaQuiaKhRtuiagrV3Jf1r5DIEfT8o/640?wx_fmt=png&from=appmsg) 首先说原因：因为PHP的 `session`根本寸不进去，验证码答案丢了；

验证码的答案是写进  `$_SESSION['vc_code']`的，而session文件要写到 `/var/lib/php/session`。但这个目录是 `root:root`、`770`，`php-fpm`是 `apache`用户，既不是`root`也不再`root组`->`apache`没权限写 `session`->你刷新出来的验证码答案根本没存下 -> 提交时 `$_SESSION['vc_code']`是空的 -> 永远“验证码错误”

```
php-fpm 运行用户：apache （www.conf:user=apache）session 保存目录：/var/lib/php/session   该目录属主/权限：root:root drwxrwx---(770)
```

方法一：增加权限，把`session`目录给 `php-fpm`的运行用户`apache`

```
chown -R apache:apache /var/lib/php/sessionchmod 770 /var/lib/php/session
```

方法二：直接通过`验证码`开关将功能关闭，直接将`/usr/share/nginx/html/fk/static/login.php`中的`第5行:把 = 1; 改成 = 0;(只动第5行,不碰别处)`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528iaE5F6cUuVObUAcXEaQ2ibgDtpa6M9CrEqU8zN2Udxov5ovqFqy1vL2U1wg8ic8TKw9xbwvBL0sNficlc3ZzFuShkgW3fR1LbnN0I/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528hvXlBia9scS0AUhaVYRF80eWiap7BrmanrRNwW2sib04SzL71JNW4ZTB5pcq5icz2Lkt4a6KEKnUOqydzvvLoTlvFa29ET1F0CqibU/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528hPD2TC2qe4tuNSpLmPvsaSr3EpX84gX460vzc7bic5IYZCzsLMdYichJaF3XWPTiaibX2FzUYzWJoZg1MFTib2OyvqhwE8VdpLmFXs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528iaICD4hQicyarsyFPQjJCqIicDRmXSicWzs1TwloricaWQeSBia7uTbA5IZico02X37MzCBvE7DicSEUfF7VNM8JYmRkqn9sPdwiay2s1A/640?wx_fmt=png&from=appmsg)

---

## 1.  请分析检材3：服务器的内核版本号是多少？【答案格式：4.25.0】

内核版本号 → `3.10.0-1160.119.1.el7.x86_64`

内核都在 `/boot`，但装了两个，要看 GRUB 默认启动的是哪个：

```
ls /casework/ev3boot | grep vmlinuz#   vmlinuz-3.10.0-514.el7.x86_64#   vmlinuz-3.10...