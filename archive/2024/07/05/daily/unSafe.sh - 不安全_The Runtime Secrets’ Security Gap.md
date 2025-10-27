---
title: The Runtime Secrets’ Security Gap
url: https://buaq.net/go-248882.html
source: unSafe.sh - 不安全
date: 2024-07-05
fetch_date: 2025-10-06T17:38:50.384983
---

# The Runtime Secrets’ Security Gap

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/61828557db842cbf1113687edbb90982.jpg)

The Runtime Secrets’ Security Gap

Claude Robitaille CEO and Founder of NearEDGESecrets management remains one of the
*2024-7-4 23:47:8
Author: [securityboulevard.com(查看原文)](/jump-248882.htm)
阅读量:6
收藏*

---

|  |  |
| --- | --- |
| ![The Runtime Secrets' Security Gap](https://blog.gitguardian.com/content/images/2024/07/The-Runtime-Secrets--Security-Gap.png) | Claude Robitaille CEO and Founder of **[NearEDGE](https://blog.gitguardian.com/the-runtime-secrets-security-gap/www.nearedge.net)** |

Secrets management remains one of the hardest problems in application security. With [over 12.8 million secrets](https://blog.gitguardian.com/the-state-of-secrets-sprawl-2024/) detected in GitHub public repos in 2023, it’s even fair to say hard-coded plaintext credentials are a serious problem!

In this blog post, I'm going to introduce a new way to deliver encrypted secrets anywhere in your infrastructure without having to worry about managing the decryption key, which has been a headache for many sysadmins for too long.

## The Challenge of Secure Secret Delivery

Different secret management architectures exist, but ultimately, they all follow the same principle: a secret is provisioned, delivered to the runtime execution environment, and consumed by a legitimate application. The problem is that whether you provision secrets through a [Kubernetes secret operator](https://blog.gitguardian.com/how-to-handle-secrets-in-kubernetes/) or an SDK, pull them from a vault, or share them via a mounted volume, the secret ends up exposed via an environment variable or a file.

Therefore, this approach has a gap: **“What if a container gets compromised, and malware gets the same access to a secret as my legitimate app running in the container?”** Once inside your container, a malicious payload can read your secrets in [many ways](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-security/docker-breakout-privilege-escalation?ref=blog.gitguardian.com) and cause havoc.

![The Runtime Secrets' Security Gap](https://blog.gitguardian.com/content/images/2024/07/image-1.png)

Secrets are delivered in clear-text, creating a security gap at the point of use.

What line of defense can we adopt to mitigate this risk?

## A No-Secret Model?

The absolute best secrets security strategy is not using secrets at all. But how can we manage access to resources without secrets? One solution is to rely on infrastructure configuration or tools like [Istio](https://istio.io/?ref=blog.gitguardian.com) to restrict resources a container instance has access to, negating the need for the application to use tokens or other secure identifiers.

Since it's externally managed, a malicious container cannot access it. However, this approach still has a problem: how do you distinguish malware from a legitimate application running on your container fleet?

Most security controls and policies look at container behavior, not what runs inside, meaning they are not able to discriminate malicious calls from legitimate ones. The orchestrator isn’t in control of the runtime inside the containers, either.

## The Solution: Shift Right and Extend Protection to the Execution Environment

To solve this problem, we need to expand our security model to include the execution environment. This means removing plaintext secrets from files and environment variables. Instead, **we deliver secrets directly into the application's memory**.

By doing this, you can keep your unsealed secrets hard to reach in memory. You'll only use the filesystem or environment for storing sealed secrets.

This can be implemented by using innovative open-source tools: `tang`, `clevis`, and `latchy`.

### `tang`

Put simply, tangis is a very basic server that makes data available only when the system containing the data is connected to a specific, secure network.

It exposes only 2 endpoints that work like this:

* First, the client gets a list of public keys with a simple `HTTP GET` to the `/adv` ("advertise") endpoint to encrypt the data. Since the keys are asymmetric, this is not a sensitive call.
* The client then uses one of these keys to generate a unique, cryptographically strong encryption key. The data is then encrypted using this key. **Once the data is encrypted, the key is discarded. Yes, you read that right; the unique key used to encrypt the data is destroyed. This is why this protocol is called "no-secret".**
* When the client needs to access its data, it simply performs an `HTTP POST` call (sending a bit of metadata generated during the previous step) to the "recovery" endpoint `/rec` to recover the encryption key.

This process ensures that sensitive information is only accessible when the client is on a secure network.

There are two big advantages compared to key escrow systems, where the encryption key is stored and then retrieved:

1. This protocol is **stateless**: you don't need to manage as many keys as there are client requests, but only two key pairs, which is very convenient in terms of secrets management. This way, you avoid a large swath of infrastructure typically required to secure a key management system: secure backup of keys, use of SSL/TLS everywhere, and comprehensive authentication policy.
2. Communication is not sensitive, meaning that you don't need to manage certificates to implement the TLS protocol between `tang` and your workloads.

**Using `tang` in production means that we can encrypt all the secrets required by our container fleet immediately after they are generated, and decrypt them on the fly before delivery directly to the application's memory.** This way, no files are ever written, and no environment variables are created. The secrets can never be compromised and malware only ever sees encrypted data.

![The Runtime Secrets' Security Gap](https://blog.gitguardian.com/content/images/2024/07/image2.png)

End-to-end protection using tang to deliver the secret

`tang` can be found on most popular Linux distributions. Docker images are also available on Docker Hub. You can install it via apt on Debian-based distros:

```
sudo apt install tang
```

And run it via `systemctl`:

```
sudo systemctl enable tangd.socket --now
```

The service listens on port 80; you can alter this by changing the `tangd.socket` file.

Check that all is up and running with `curl`:

```
curl localhost:80/adv
```

You should see a JWS (a signed object) that contains public keys in the form of a JWKSet. See [https://github.com/latchset/tang](https://github.com/latchset/tang?ref=blog.gitguardian.com) (or `man tang`) for more information (note that with this `systemd` service definition, the location for the keys is `/var/lib/tang`).

### **`clevis`**

[clevis](https://github.com/latchset/clevis?ref=blog.gitguardian.com) is our encryption tool. It is fully compatible with tang. Secrets are protected by encrypting them and putting the result into a JWE file:

```
$ echo “Hello World” | clevis encrypt tang '{"url": "http://localhost:80"}' > mysecret.jwe
The advertisement is signed with the following keys:
        kWwirxc5PhkFIH0yE28nc-EvjDY

Do you wish to trust the advertisement? [yN] y
```

In this example, we encrypt the message "Hello World" using the `tang` pin. The only parameter needed in this case is the URL of the Tang server. During the encryption process, the `tang` pin requests the key advertisement from the server and asks you to trust the keys. This works similarly to SSH.

💡

Note: it's also possible to work offline by preparing the advertisement from Tang beforehand (a JWS file) ...