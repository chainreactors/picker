#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""Notification bot implementations"""

from __future__ import annotations
import base64
import hashlib
import hmac
import time
import json
from urllib import parse
import os
from typing import Dict, List, Tuple, Any, Optional

import yaml
import requests
import smtplib
import subprocess
from email.header import Header
from email.mime.text import MIMEText
from pathlib import Path
from datetime import datetime
from pyrate_limiter import Duration, Limiter, Rate

from utils import Color

__all__ = ["feishuBot", "wecomBot", "dingtalkBot", "qqBot", "mailBot", "init_bot"]
today = datetime.now().strftime("%Y-%m-%d")


def get_env_key(name: str, pick: bool = False) -> Optional[str]:
    """
    Get environment variable with optional PICKER_ prefix

    Args:
        name: Environment variable name
        pick: If True, add PICKER_ prefix

    Returns:
        Environment variable value or None
    """
    prefix = "PICKER_" if pick else ""
    return os.getenv(f"{prefix}{name}")


def init_bot(bot_conf: Dict[str, Any], proxy_url: str = '', pick: bool = False) -> List[Any]:
    """
    Initialize notification bots from configuration

    Args:
        bot_conf: Bot configuration dictionary
        proxy_url: Optional proxy URL
        pick: If True, this is for picker bots

    Returns:
        List of initialized bot instances
    """
    bots: List[Any] = []

    # Check environment variables for bot keys
    env_bot_keys = {
        'dingtalk': get_env_key('DINGTALK_KEY', pick),
        'feishu': get_env_key('FEISHU_KEY', pick),
        'wecom': get_env_key('WECOM_KEY', pick),
        'qq': get_env_key('QQ_KEY', pick)
    }

    for name, v in bot_conf.items():
        # Enable bot if environment variable is set
        if env_bot_keys.get(name):
            v['enabled'] = True
            v['key'] = env_bot_keys[name]

        if not v.get('enabled'):
            continue

        try:
            if name == 'dingtalk':
                secret = get_env_key('DINGTALK_SECRET', pick) or v.get('secret', '')
                bot = dingtalkBot(v['key'], secret, proxy_url)
                bots.append(bot)

            elif name == 'feishu':
                bot = feishuBot(v['key'], proxy_url)
                bots.append(bot)

            elif name == 'wecom':
                bot = wecomBot(v['key'], proxy_url)
                bots.append(bot)

            elif name == 'qq':
                qq_id = get_env_key('QQ_ID', pick) or v.get('qq_id')
                group_id = get_env_key('QQ_GROUP_ID', pick) or v.get('group_id')
                if isinstance(group_id, str):
                    group_id = [int(id.strip()) for id in group_id.split(',')]
                bot = qqBot(group_id)
                if bot.start_server(qq_id, v['key']):
                    bots.append(bot)

            elif name == 'mail':
                receiver = get_env_key('MAIL_RECEIVER', pick) or v.get('receiver')
                bot = mailBot(
                    v['address'],
                    v['key'],
                    receiver,
                    v.get('from'),
                    v.get('server')
                )
                bots.append(bot)

        except Exception as e:
            Color.print_failed(f'[-] {name}Bot initialization failed: {e}')

    return bots


class feishuBot:
    """
    飞书群机器人
    https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN
    """

    def __init__(self, key: str, proxy_url: str = '') -> None:
        self.key: str = key
        self.proxy: Dict[str, Optional[str]] = (
            {'http': proxy_url, 'https': proxy_url} if proxy_url
            else {'http': None, 'https': None}
        )

    @staticmethod
    def parse_results(results: Dict[str, Any]) -> List[Tuple[str, str]]:
        """Parse article results into message format"""
        text_list: List[Tuple[str, str]] = []
        for feed, value in results.items():
            text = f"{feed}:\n"
            for title, article_data in value.items():
                # Support both old format (string) and new format (dict with url and summary)
                if isinstance(article_data, str):
                    link = article_data
                    summary = None
                else:
                    link = article_data.get('url', '')
                    summary = article_data.get('summary')

                text += f'- [{title}]({link})\n'
                if summary:
                    text += f'  > {summary}\n'
            text_list.append((feed, text.strip()))
        return text_list

    @staticmethod
    def parse_pick(results: Dict[str, List[Tuple[str, str, str]]]) -> List[Tuple[str, str]]:
        """Parse picked articles into message format"""
        text_list: List[Tuple[str, str]] = []
        for feed, articles in results.items():
            text = f"[{today} 精选] {feed}:\n"
            for title, link, issue_url in articles:
                text += f'  - [{title}]({link}) - [discussion]({issue_url})\n'
            text_list.append((feed, text))
        return text_list

    def send(self, text_list: List[Tuple[str, str]]) -> None:
        """Send multiple messages"""
        for title, text in text_list:
            print(f'{len(text)} {text[:50]}...{text[-50:]}')
            self.send_raw(title, text)

    def send_raw(self, title: str, text: str) -> None:
        """Send single raw message to Feishu"""
        data = {"msg_type": "text", "content": {title: title, "text": text}}
        headers = {'Content-Type': 'application/json'}
        url = f'https://open.feishu.cn/open-apis/bot/v2/hook/{self.key}'

        try:
            r = requests.post(
                url=url,
                headers=headers,
                data=json.dumps(data),
                proxies=self.proxy,
                timeout=10
            )
            if r.status_code == 200 and r.json().get("code") == 0:
                Color.print_success('[+] feishuBot 发送成功')
            else:
                Color.print_failed(f'[-] feishuBot 发送失败: {r.text}')
        except Exception as e:
            Color.print_failed(f'[-] feishuBot 发送失败: {e}')


class wecomBot:
    """企业微信群机器人
    https://developer.work.weixin.qq.com/document/path/91770
    """

    def __init__(self, key, proxy_url='') -> None:
        self.key = key
        self.proxy = {'http': proxy_url, 'https': proxy_url} if proxy_url else {
            'http': None, 'https': None}

    @staticmethod
    def parse_results(results: list):
        text_list = []
        for result in results:
            (feed, value), = result.items()
            text = f'## {feed}\n'
            for title, link in value.items():
                text += f'- [{title}]({link})\n'
            text_list.append(text.strip())
        return text_list

    def send(self, text_list: list):
        limiter = Limiter(Rate(20, Duration.MINUTE))
        for text in text_list:
            limiter.try_acquire('wecom_bot')
            print(f'{len(text)} {text[:50]}...{text[-50:]}')

            data = {"msgtype": "markdown", "markdown": {"content": text}}
            headers = {'Content-Type': 'application/json'}
            url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={self.key}'
            r = requests.post(url=url, headers=headers,
                              data=json.dumps(data), proxies=self.proxy)

            if r.status_code == 200:
                Color.print_success('[+] wecomBot 发送成功')
            else:
                Color.print_failed('[-] wecomBot 发送失败')
                print(r.text)


class dingtalkBot:
    """
    钉钉群机器人
    https://open.dingtalk.com/document/robots/custom-robot-access
    """

    def __init__(self, key: str, secret: str, proxy_url: str = '') -> None:
        self.key: str = key
        self.secret: str = secret
        self.proxy: Dict[str, Optional[str]] = (
            {'http': proxy_url, 'https': proxy_url} if proxy_url
            else {'http': None, 'https': None}
        )

    @staticmethod
    def parse_results(results: dict):
        text_list = []
        for result in results.items():
            feed, value = result
            text = feed + ":\n"
            for title, article_data in value.items():
                # Support both old format (string) and new format (dict with url and summary)
                if isinstance(article_data, str):
                    link = article_data
                    summary = None
                else:
                    link = article_data.get('url', '')
                    summary = article_data.get('summary')

                text += f'- [{title}]({link})\n'
                if summary:
                    text += f'  > {summary}\n'
            text_list.append([feed, text.strip()])
        return text_list

    @staticmethod
    def parse_pick(results: dict):
        text_list = []
        for feed, articles in results.items():
            text = f"[{today} 精选] " + feed + ":\n"
            for title, link, issue_url in articles:
                text += f'  - [{title}]({link}) - [discussion]({issue_url})\n'
            text_list.append((feed, text))
        return text_list

    def sign(self, timestamp):
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc,
                             digestmod=hashlib.sha256).digest()
        return parse.quote_plus(base64.b64encode(hmac_code))

    def send(self, text_list: list):
        limiter = Limiter(Rate(19, Duration.MINUTE + 1))
        for (feed, text) in text_list:
            limiter.try_acquire('dingtalk_bot')
            print(f'{len(text)} {text[:50]}...{text[-50:]}')
            data = {"msgtype": "markdown", "markdown": {
                "title": feed, "text": text}}
            headers = {'Content-Type': 'application/json'}
            timestamp = str(round(time.time() * 1000))
            url = f'https://oapi.dingtalk.com/robot/send?access_token={self.key}&timestamp={timestamp}&sign={self.sign(timestamp)}'
            r = requests.post(url=url, headers=headers,
                              data=json.dumps(data), proxies=self.proxy)
            if r.status_code == 200 and r.json()["errcode"] == 0:
                Color.print_success('[+] dingtalkBot 发送成功')
            else:
                Color.print_failed('[-] dingtalkBot 发送失败')
                print(r.text)

    def send_raw(self, title, text):
        data = {"msgtype": "markdown", "markdown": {
            "title": title, "text": text}}
        headers = {'Content-Type': 'application/json'}
        timestamp = str(round(time.time() * 1000))
        url = f'https://oapi.dingtalk.com/robot/send?access_token={self.key}&timestamp={timestamp}&sign={self.sign(timestamp)}'
        r = requests.post(url=url, headers=headers,
                          data=json.dumps(data), proxies=self.proxy)
        if r.status_code == 200 and r.json()["errcode"] == 0:
            Color.print_success('[+] dingtalkBot 发送成功')
        else:
            Color.print_failed('[-] dingtalkBot 发送失败')
            print(r.text)


class qqBot:
    """QQ群机器人
    https://github.com/Mrs4s/go-cqhttp
    """
    cqhttp_path = Path(__file__).absolute().parent.joinpath('cqhttp')

    def __init__(self, group_id: list) -> None:
        self.server = 'http://127.0.0.1:5700'
        self.group_id = group_id

    @staticmethod
    def parse_results(results: list):
        text_list = []
        for result in results:
            (feed, value), = result.items()
            text = f'[ {feed} ]\n\n'
            for title, link in value.items():
                text += f'{title}\n{link}\n\n'
            text_list.append(text.strip())
        return text_list

    def send(self, text_list: list):
        limiter = Limiter(Rate(20, Duration.MINUTE))
        for text in text_list:
            limiter.try_acquire('qq_bot')
            print(f'{len(text)} {text[:50]}...{text[-50:]}')

            for id in self.group_id:
                try:
                    r = requests.post(
                        f'{self.server}/send_group_msg?group_id={id}&&message={text}')
                    if r.status_code == 200:
                        Color.print_success(f'[+] qqBot 发送成功 {id}')
                    else:
                        Color.print_failed(f'[-] qqBot 发送失败 {id}')
                except Exception as e:
                    Color.print_failed(f'[-] qqBot 发送失败 {id}')
                    print(e)

    def start_server(self, qq_id, qq_passwd, timeout=60):
        config_path = self.cqhttp_path.joinpath('config.yml')
        with open(config_path, 'r') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            data['account']['uin'] = int(qq_id)
            data['account']['password'] = qq_passwd
        with open(config_path, 'w+') as f:
            yaml.dump(data, f)

        subprocess.run('cd cqhttp && ./go-cqhttp -d', shell=True)

        timeout = time.time() + timeout
        while True:
            try:
                requests.get(self.server)
                Color.print_success('[+] qqBot 启动成功')
                return True
            except Exception as e:
                time.sleep(1)

            if time.time() > timeout:
                qqBot.kill_server()
                Color.print_failed('[-] qqBot 启动失败')
                return False

    @classmethod
    def kill_server(cls):
        pid_path = cls.cqhttp_path.joinpath('go-cqhttp.pid')
        subprocess.run(f'cat {pid_path} | xargs kill',
                       stderr=subprocess.DEVNULL, shell=True)


class mailBot:
    """邮件机器人
    """

    def __init__(self, sender, passwd, receiver: str, fromwho='', server='') -> None:
        self.sender = sender
        self.receiver = receiver
        self.fromwho = fromwho or sender
        server = server or self.get_server(sender)

        self.smtp = smtplib.SMTP_SSL(server)
        self.smtp.login(sender, passwd)

    def get_server(self, sender: str):
        key = sender.rstrip('.com').split('@')[-1]
        server = {
            'qq': 'smtp.qq.com',
            'foxmail': 'smtp.qq.com',
            '163': 'smtp.163.com',
            'sina': 'smtp.sina.com',
            'gmail': 'smtp.gmail.com',
            'outlook': 'smtp.live.com',
        }
        return server.get(key, f'smtp.{key}.com')

    @staticmethod
    def parse_results(results: list):
        text = f'<html><head><h1>每日安全资讯（{today}）</h1></head><body>'
        for result in results:
            (feed, value), = result.items()
            text += f'<h3>{feed}</h3><ul>'
            for title, link in value.items():
                text += f'<li><a href="{link}">{title}</a></li>'
            text += '</ul>'
        text += '<br><br><b>如不需要，可直接回复本邮件退订。</b></body></html>'
        return text

    def send(self, text: str):
        print(f'{len(text)} {text[:50]}...{text[-50:]}')
        print(text)

        msg = MIMEText(text, 'html')
        msg['Subject'] = Header(f'每日安全资讯（{today}）')
        msg['From'] = self.fromwho
        msg['To'] = self.receiver

        try:
            self.smtp.sendmail(self.sender, self.receiver, msg.as_string())
            Color.print_success('[+] mailBot 发送成功')
        except Exception as e:
            Color.print_failed('[+] mailBot 发送失败')
            print(e)
