---
title: Casper The Password Ghost
url: https://blog.unauthorizedaccess.nl/2023/03/08/casper-the-password-ghost.html
source: Unauthorized Access Blog
date: 2023-03-09
fetch_date: 2025-10-04T09:01:14.764608
---

# Casper The Password Ghost

## Skip links

* [Skip to primary navigation](#site-nav)
* [Skip to content](#main)
* [Skip to footer](#footer)

[Unauthorized Access Blog](/)

Toggle menu

![Donny Maasland](/assets/img/profile.png)

### Donny Maasland

I sometimes discover something interesting by accident, and people seem to enjoy reading about it.

Follow

* Between keyboard and chair
* [Twitter](https://twitter.com/donnymaasland)
* [LinkedIn](https://www.linkedin.com/in/donny-maasland-13801720)
* [GitHub](https://github.com/dmaasland)

# Casper The Password Ghost

15 minute read

---

# == DISCLAIMER ==

I wrote this blog years ago (2019) using a Jamf Pro version that probably isn’t even supported anymore. I have no clue what the current version is or if what is written here even applies anymore. I’m only publishing this in the interest of knowledge sharing 😄.

This is by no means a vulnerability, it’s just the nature of encrypting things. Somewhere, somehow, it needs to be decrypted to be useful. For example:

* [Reverse engineering and decrypting CyberArk vault credential files](https://jellevergeer.com/reverse-engineering-and-decrypting-cyberark-vault-credential-files/)
* [Thick Client Penetration Testing – Part 4](https://blog.securelayer7.net/static-analysismemory-forensics-reverse-engineering-thick-client-penetration-testing-part-4/)

Enjoy!

---

# Casper the password ghost

## Decrypting Jamf Pro / Casper Suite storage

### Intro

Most organisations use some sort of central management tool to manage and maintain their systems. For Microsoft Windows environments, this is mostly done using tools like System Center Configuration Manager (SCCM), System Center Operations Manager (SCOM), Intune, etcetera. These products will likely ring a bell with most people working somewhere in the magical space that is IT.

But what if you’re infrastructure consists of mostly Apple systems? While there are a multitude of solutions available for managing Apple systems, one of the largest names in this space is Jamf. Their signature product [Jamf Pro](https://www.jamf.com/products/jamf-pro/ "Jamf Pro"), formerly known as Casper Suite, is one of the best known products offering a central dashboard for managing and maintaining Apple based systems.

### Security

A central dashboard is awesome for administrators because it offers them a one-stop shop for all their administrative needs. The same holds true for attackers though, as these types of products usually contain truckloads of juicy info such as:

* Usernames and passwords;
* Corporate software signing certificates and matching private keys;
* Device encryption keys;
* Settings for external connections such as LDAP and SMTP;
* Etcetera.

Obviously this information isn’t stored in plain-text. Jamf even offer a detailed [security](https://www.jamf.com/security/) page on their website, explaining all the measures they are taking to ensure all information is safe. When it comes to storing sensitive information in the database, they have this to say:

> “[…] data at rest uses industry standard AES-256 to encrypt fields in the database that contain sensitive information, such as passwords and FileVault individual recovery keys. […] all other passwords are encrypted using industry standard AES-256 with a unique, random key for each database.”

Sounds good. This should mean there are no hardcoded or default encryption keys in use, and that every instance of the software uses unique keys. In other words, customer A cannot decrypt the database of customer B. Let’s put this to the test.

### Validating the claims

Installing Jamf Pro is simple enough. It is a Java application that runs on a Tomcat server and uses MySQL as it’s database backend. Let’s install Jamf Pro and see what happens.

![Jamf Pro](/assets/img/casper/screenshot_01.png "Jamf Pro")

Cool, that works. Let’s insert some test data and see if we can find it in the database. We’ll create a new policy that adds a so-called **`Management Account`** to all systems. We’ll give ths new account the password **`IWantT0Beli3v3!`**.

![New Management Account](/assets/img/casper/screenshot_02.png "New Management Account")

After some digging in the database, it turns out that the password is stored in the **`Policies`** table under the **`managed_password_encrypted`** column.

```
mysql> SELECT name,managed_password_encrypted FROM policies;
+-----------------------------+----------------------------+
| name                        | managed_password_encrypted |
+-----------------------------+----------------------------+
| Update Inventory            |                            |
| Default management accounts | Au/IuzGbOQ7oaRMTGNWYqA==   |
+-----------------------------+----------------------------+
2 rows in set (0.00 sec)

mysql>
```

Nice, that seems to be it. Base64 decoding it doesn’t really yield anything useful. But seeing as how it’s supposed to be encrypted, this makes sense.

```
pentest@cortana:~$ echo Au/IuzGbOQ7oaRMTGNWYqA== | base64 -d | hd
00000000  02 ef c8 bb 31 9b 39 0e  e8 69 13 13 18 d5 98 a8  |....1.9..i......|
00000010
pentest@cortana:~$
```

No worries, we do seem to have a lead. All encrypted values in the database have column names ending in **`_encrypted`**. Let’s open up the Jamf Pro .war file in a Java decompiler. In our case, JD-GUI. It seems that all the juicy stuff is going on in **`com.jamfsoftware.jss.utils.PasswordServiceImpl.class`**

![readKeyFromDatabase](/assets/img/casper/screenshot_03.png "readKeyFromDatabase")

Here we find two funcions called **`readKeyFromDatabase`** and **`readEncryptionTypeFromDatabase`**. Let’s see what they do.

```
public static boolean readKeyFromDatabase()
{
  boolean foundKey = false;
  PreparedStatement ps = null;
  ResultSet rs = null;
  try
  {
    String STATEMENT = "SELECT * FROM encryption_key LIMIT 1";
    ps = DataSource.prepareStatementForExecuteQuery(STATEMENT);
    rs = DataSource.executeQuery(ps);
    while (rs.next())
    {
      try
      {
        setEncryptionAlgorithm(PasswordServiceImpl.EncryptionAlgorithm.fromDbType(rs.getInt("encryption_type")));
      }
      catch (Exception e)
      {
        setEncryptionAlgorithm(PasswordServiceImpl.EncryptionAlgorithm.DES);
      }
      PasswordServiceImpl.Encrypter keyEncryptor = new PasswordServiceImpl.Encrypter(getStorageKey(), getEncryptionAlgorithm());
      setEncryptionKey(keyEncryptor.decrypt(rs.getString("encryption_key")), getEncryptionAlgorithm());

      foundKey = true;
    }
  }
  catch (SQLException e)
  {
    if (DatabaseConnectorHelper.isSqlSyntaxErrorException(e))
    {
      jamfLog.debug("Key table does not exist, defaulting to previous algorithm.");
      setEncryptionAlgorithm(PasswordServiceImpl.EncryptionAlgorithm.DES);
      setEncryptionKey(getLegacyEncryptionKey(), getEncryptionAlgorithm());
    }
    else
    {
      jamfLog.error("Reading key", e);
    }
  }
  catch (Exception e)
  {
    jamfLog.error("Reading key", e);
  }
  finally
  {
    DataSource.closeResultSet(ps, rs);
  }
  return foundKey;
}

public static PasswordServiceImpl.EncryptionAlgorithm readEncryptionTypeFromDatabase()
{
  PasswordServiceImpl.EncryptionAlgorithm currentType = null;
  PreparedStatement ps = null;
  ResultSet rs = null;
  try
  {
    String STATEMENT = "SELECT encryption_type FROM encryption_key LIMIT 1";
    ps = DataSource.prepareStatementForExecuteQuery(STATEMENT);
    rs = DataSource.executeQuery(ps);
    while (rs.next()) {
      currentType = PasswordServiceImpl.EncryptionAlgorithm.fromDbType(rs.getInt("encryption_type"));
    }
  }
  catch (Exception e)
  {
    jamfLog.error("Reading type", e);
  }
  finally
  {
    DataSource.closeResultSet(ps, rs);
  }
  return currentType;
}
```

Alright, long story short, the encryption key seems to be stored in the database. Let’s see what happens when we run the query from the **`readKeyFromDatabase`** function.

```
mysql> SELECT * FROM encryption_key LIMIT 1;
+-------------------------------------------------...