---
title: 26软件安全区域赛pth_attack复现
url: https://mp.weixin.qq.com/s/rpjXeXGwPHZCjk-pPNoKVg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:33:59.190578
---

# 26软件安全区域赛pth_attack复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rkPWAUPG1UnicdG3WLXlmcuFVyO9YbXavKhvRxN1icIceO03NT8A0c4ZRiabicWKG5ic6UbX7mAUMrdHiaGfuOc9fXmwN9vEQBc2Vs9M/0?wx_fmt=jpeg)

# 26软件安全区域赛pth\_attack复现

咕咕咕
咕咕咕

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

比赛的时候提取完winrm流量解码完就没进展了，当时就觉得解码后的流量怎么这么少😳，然后比赛之后复现发现还真是，复现的时候，我是真的绷不住了，一波三折，快给我整不会了😭。还得是ai大人伸出援手（屋檐了），让我成功复现😄

## 正文

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmb2uuI0LLdxb2SbBTuOYQVv12MxMicZvIrqcB7YHxn3tTg4mfic5l7NUdsNkfSThuniaJww6LxBOlu1Lp6nHAUN28pJ7lFsucuU8/640?wx_fmt=png&from=appmsg)

首先是题目原件是两个流量包，题目提示是这两个流量包是内网渗透流量 打开第一个![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkZukx9fj5Zs6tnBNIhEImFRF64UV9ib157RShVMXb9WpyWgMUyu3upsaGzZCYnTWU4ONuibkFh274IJicIMia4oqKDPcIMzcfnacg/640?wx_fmt=png&from=appmsg)

然后就是想直接使用hashcat进行hash爆破了`hashcat -m 5600 -a 0 hash.txt rockyou.txt`然后很难过的事情发生了，kail的这个默认字典文件rockyou.txt爆破失败了 那么不得不进一步分析了，然后前面不是发现还有winrm流量吗，了解到winrm流量，NTLMRawUnHide.py这个脚本是提取不到的，那么是时候手搓了 形式是这样的`$NETNTLMv2$USERNAME+domain$server challenge$NTProofstr$blob`![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlJYKrsrWEOWawMLjRoz6joVepicgzv4yb1riceM65r9OJia9hYVZxDvVdb4XF5orcH1jO0ZgtTwSQ8P7SBia8Q9UqMBrU9U8ibVsGg/640?wx_fmt=png&from=appmsg)所需的内容从这样一对数据包中找，前一个 是ntlm\_challeng,后一个是ntlm\_auth流量![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkgksAhhebGHfe2ia0z95uMKGiblicmq3IXd2MqIBKmavcx2p2KXrmkgsTXeiabq7ERAIibsH8sTxfX2X6c1SQyXfs6njWP6f5yvMOg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkprC2picnqE1TpOv0bv0fFgQicxv5T0P9FUegO9Aoekk5SZkiaxfOBPx8Kj732zf1jo3OnXQVbv7Tg5YapS0zic3ibGkmbTGelXMrw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlPUwv1cjxibJpKptDPVshm9kK3YPKhUGRgJD3ooQJBicF4qVKjMCK4oZph638LgqujnfBgBxdvHKnnP3EzRDescMtmxEZZvWFuo/640?wx_fmt=png&from=appmsg)`$NETNTLMv2$ADMINISTRATORpc$cd0a6722277096c9$3fa965e4d9af9a92bde5cefcdd309acb$010100000000000022a2d32cbc72dc01ff545caf96411c670000000002000a0044004500310041005900010004005000430004001200640065003100610079002e0063006f006d0003001800500043002e00640065003100610079002e0063006f006d0005001200640065003100610079002e0063006f006d000700080022a2d32cbc72dc010600040002000000080030003000000000000000000000000030000026544cc05c735b21ae876ab6adeaf35030fb649315896d1d685326c99ddb5f6b0a001000000000000000000000000000000000000900220048005400540050002f00310030002e00310030002e00310030002e00320030003100000000000000000000000000`然后使用john爆破![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmMWBmQyPDCY2dYgjibbEHFZvHFYo7adficm6zZ2FLa3HLCfpQJSVl05mVf5ibTp7GJuUcXtdiaXylbBlIsZCQG8m5ANS9R3MY2mLo/640?wx_fmt=png&from=appmsg)拿到了密码`pass@word1`然后就可以将winrm流量包的内容提取出来了（后面的经历我已经想流泪了） 最开始我是想直接用NATe直接提取的![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmEgtVzQyia5Xkd2mzJodacMRP9K2YzC7jXfLkVBCtFYC7OBpibatvhJypXXBYOPxqXDl7lZDj0OhUgjapmCe7D1xgaNA6uABDBk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rniaficWEeXw6tDD5vlS7MF3WgtrzQndxqNWo0snYFARxNRbSmASibHsYcsicicRo7eWO51PlzzHfgW7vnGf6MyNnt48afib61BoQsrE/640?wx_fmt=png&from=appmsg)但是得到txt文件的内容不全，然后不得不去请出ai大人（当然可能是我不会用 NETA，有不对的地方请大佬指正）

```
#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# PYTHON_ARGCOMPLETE_OK

# Copyright: (c) 2020 Jordan Borean (@jborean93) <jborean93@gmail.com>

# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

# Fork / modifications by Haoxi Tan (haoxi.tan@gmail.com)

# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

# Further modified to use scapy instead of pyshark (no tshark dependency)

"""

Script that can read a Wireshark capture .pcap/.pcapng for a WinRM exchange and decrypt the messages.

Currently only supports exchanges that were authenticated with NTLM.

"""

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import argparse

import base64

import collections

import hashlib

import hmac

import os

import binascii

import sys

import struct

import xml.dom.minidom

from scapy.all import rdpcap, TCP, IP, Raw

from Crypto.Hash import MD4

from cryptography.hazmat.primitives.ciphers import (

    algorithms,

    Cipher,

)

from cryptography.hazmat.backends import (

    default_backend,

)

try:

    import argcomplete

except ImportError:

    argcomplete = None

class SecurityContext:

    def __init__(self, port, nt_hash):

        self.port = port

        self.tokens = []

        self.nt_hash = nt_hash

        self.complete = False

        self.key_exch = False

        self.session_key = None

        self.sign_key_initiate = None

        self.sign_key_accept = None

        self.seal_handle_initiate = None

        self.seal_handle_accept = None

        self.__initiate_seq_no = 0

        self.__accept_seq_no = 0

    @property

    def _initiate_seq_no(self):

        val = self.__initiate_seq_no

        self.__initiate_seq_no += 1

        return val

    @property

    def _accept_seq_no(self):

        val = self.__accept_seq_no

        self.__accept_seq_no += 1

        return val

    def add_token(self, token):

        self.tokens.append(token)

        if token.startswith(b"NTLMSSP\x00\x03"):

            # Extract the info required to build the session key

            nt_challenge = self._get_auth_field(20, token)

            b_domain = self._get_auth_field(28, token) or b""

            b_username = self._get_auth_field(36, token) or b""

            encrypted_random_session_key = self._get_auth_field(52, token)

            flags = struct.unpack("<I", token[60:64])[0]

            encoding = 'utf-16-le'if flags & 0x00000001 else'windows-1252'

            domain = b_domain.decode(encoding)

            username = b_username.decode(encoding)

            # Derive the session key

            nt_proof_str = nt_challenge[:16]

            response_key_nt = hmac_md5(self.nt_hash, (username.upper() + domain).encode('utf-16-le'))

            key_exchange_key = hmac_md5(response_key_nt, nt_proof_str)

            self.key_exch = bool(flags & 0x40000000)

            if self.key_exch and (flags & (0x00000020 | 0x00000010)):

                self.session_key = rc4k(key_exchange_key, encrypted_random_session_key)

            else:

                self.session_key = key_exchange_key

            # Derive the signing and sealing keys

            self.sign_key_initiate = signkey(self.session_key, 'initiate')

            self.sign_key_accept = signkey(self.session_key, 'accept')

            self.seal_handle_initiate = rc4init(sealkey(self.session_key, 'initiate'))

            self.seal_handle_accept = rc4init(sealkey(self.session_key, 'accept'))

            self.complete = True

    def unwrap_initiate(self, data):

        print('unwrap_initiate', file=sys.stderr)

        return self._unwrap(self.seal_handle_initiate, self.sign_key_initiate, self._initiate_seq_no, data)

    def unwrap_accept(self, data):

        print('unwrap_accept', file=sys.stderr)

        return self._unwrap(self.seal_handle_accept, self.sign_key_accept, self._accept_seq_no, data)

    def _unwrap(self, handle, sign_key, seq_no, data):

        header = data[4:20]

        enc_data = data[20:]

        dec_data = handle.update(enc_data)

        b_seq_num = struct.pack("<I", seq_no)

        checksum = hmac_md5(sign_key, b_seq_num + dec_data)[:8]

        if self.key_exch:

            checksum = handle.update(checksum)

        actual_header = b"\x01\x00\x00\x00" + checksum + b_seq_num

        if header != actual_header:

            print("Signature verification failed", file=sys.stderr)

        return dec_data

    def _get_auth_field(self, offset, token):

        field_len = struct.unpack("<H", token[offset:offset + 2])[0]

        if field_len:

            field_offset = struct.unpack("<I", token[offset + 4:offset + 8])[0]

            return token[field_offset:field_offset + field_len]

def hmac_md5(key, data):

    return hmac.new(key, data, digestmod=hashlib.md5).digest()

def md4(m):

    h = MD4.new()

    h.update(m)

    return h.digest()

def md5...