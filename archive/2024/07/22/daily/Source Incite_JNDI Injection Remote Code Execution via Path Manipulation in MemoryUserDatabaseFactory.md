---
title: JNDI Injection Remote Code Execution via Path Manipulation in MemoryUserDatabaseFactory
url: https://srcincite.io/blog/2024/07/21/jndi-injection-rce-via-path-manipulation-in-memoryuserdatabasefactory.html
source: Source Incite
date: 2024-07-22
fetch_date: 2025-10-06T17:40:35.820497
---

# JNDI Injection Remote Code Execution via Path Manipulation in MemoryUserDatabaseFactory

[![Source Incite](/assets/si.png)](/)

[About](/about/) [Blog](/blog/) [Advisories](/advisories/) [Exploits](/exploits/) [Research](/research/)

[Training](/training/)

[Syllabus](/training/syllabus/) [Prerequisites](/training/prerequisites/) [Challenge](/training/challenge/) [Schedule/Signup](/training/schedule-signup/) [Testimonials](/training/testimonials/) [Faq](/training/faq/)

[Contact](/contact/)

# JNDI Injection Remote Code Execution via Path Manipulation in MemoryUserDatabaseFactory

Jul 21, 2024

![](/assets/images/jndi-injection-rce-via-path-manipulation-in-memoryuserdatabasefactory/logo.jpg "Java JNDI")

In this blog post, I’m going to describe a ~~relative new~~ vector to achieve remote code execution via a JNDI Injection that I found independently to [other researchers](https://b1ue.cn/archives/529.html). The concept of exploiting an object lookup process for a JNDI injection is nothing new. If you are unfamiliar with this, I invite you to read [this](https://www.veracode.com/blog/research/exploiting-jndi-injections-java) excellent blog post written by Michael Stepankin.

I decided to retire some of the content from [Full Stack Web Attack](/training/), so if you enjoy this level of Java (and/or C#) analysis, feel free to sign up to my [next class](/training/schedule-signup/) which will be held in Rome.

## MemoryUserDatabaseFactory

When exploring types that implement from `ObjectFactory` I found an interesting class called `org.apache.catalina.users.MemoryUserDatabaseFactory`. This is within the `tomcat-catalina` library and is the same library that contains the (in)famous `org.apache.naming.factory.BeanFactory`. The importance of this will become apparent later.

Let’s start at the `getObjectInstance` inside of the `MemoryUserDatabaseFactory` class.

```
/*     */   public Object getObjectInstance(Object obj, Name name, Context nameCtx, Hashtable<?, ?> environment) throws Exception {
/*     */     ...
/*  81 */     Reference ref = (Reference)obj;
/*     */     ...
/*  88 */     MemoryUserDatabase database = new MemoryUserDatabase(name.toString());
/*  89 */     RefAddr ra = null;
/*     */
/*  91 */     ra = ref.get("pathname"); // 1
/*  92 */     if (ra != null) {
/*  93 */       database.setPathname(ra.getContent().toString());
/*     */     }
/*     */
/*  96 */     ra = ref.get("readonly"); // 2
/*  97 */     if (ra != null) {
/*  98 */       database.setReadonly(Boolean.parseBoolean(ra.getContent().toString()));
/*     */     }
/*     */     ...
/* 107 */     database.open(); // 3
/*     */
/* 109 */     if (!database.getReadonly()) // 6
/* 110 */       database.save(); // 7
/* 111 */     return database;
/*     */   }
```

Some interesting code stands out here, at *[1]* we can see that an attacker can control the `pathname` property on the `MemoryUserDatabase` instance.

At *[2]* an attacker can also disable the `readonly` setting as well. But the interesting code appears at *[3]* with the call to `open` on the database instance. Let’s check it out:

```
/*     */   public void open() {
/* 418 */     this.writeLock.lock();
/*     */
/*     */     try {
/*     */       ...
/* 425 */       String pathName = getPathname(); // 4
/* 426 */       try (ConfigurationSource.Resource resource = ConfigFileLoader.getSource().getResource(pathName)) {
/*     */         ...
/* 430 */         digester = new Digester();
/*     */         try {
/* 432 */           digester.setFeature("http://apache.org/xml/features/allow-java-encodings", true);
/*     */         }
/* 434 */         catch (Exception e) {
/* 435 */           log.warn(sm.getString("memoryUserDatabase.xmlFeatureEncoding"), e);
/*     */         }
/* 437 */         digester.addFactoryCreate("tomcat-users/group", new MemoryGroupCreationFactory(this), true);
/*     */
/* 439 */         digester.addFactoryCreate("tomcat-users/role", new MemoryRoleCreationFactory(this), true);
/*     */
/* 441 */         digester.addFactoryCreate("tomcat-users/user", new MemoryUserCreationFactory(this), true);
/*     */
/*     */
/*     */
/* 445 */         digester.parse(resource.getInputStream()); // 5
/* 446 */       } catch (IOException ioe) {
/* 447 */         log.error(sm.getString("memoryUserDatabase.fileNotFound", new Object[] { pathName }));
/* 448 */       } catch (Exception e) {
/*     */         ...
/*     */       }
/*     */     } finally {
/* 456 */       this.writeLock.unlock();
/*     */     }
/*     */   }
```

At *[4]* the code uses the attacker controlled `pathname` to download a file from remote and parse the file at *[5]*. This of course leads to an external entity injection (but I digress!). The important point to make here is that an attacker can set the `users`, `groups` or `roles` variables using properties from within an XML file. This is just standard `tomcat-users.xml`:

```
<tomcat-users>
    <role rolename="admin" />
</tomcat-users>
```

The above XML will add the role “admin” to the `roles` Map inside of the `MemoryUserDatabase` instance. Returning back to `getObjectInstance`, if the attacker disables read-only at *[6]* then they can reach `save` at *[7]*.

```
/*     */   public void save() {
/*     */     ...
/* 555 */     if (!isWriteable()) { // 8
/* 556 */       log.warn(sm.getString("memoryUserDatabase.notPersistable"));
/*     */
/*     */       return;
/*     */     }
/*     */
/* 561 */     File fileNew = new File(this.pathnameNew); // 9
/* 562 */     if (!fileNew.isAbsolute()) {
/* 563 */       fileNew = new File(System.getProperty("catalina.base"), this.pathnameNew);
/*     */     }
/*     */
/* 566 */     this.writeLock.lock();
/*     */     try {
/* 568 */       try(FileOutputStream fos = new FileOutputStream(fileNew);
/* 569 */           OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8);
/* 570 */           PrintWriter writer = new PrintWriter(osw)) {
/*     */
/*     */
/* 573 */         writer.println("<?xml version='1.0' encoding='utf-8'?>");
/* 574 */         writer.println("<tomcat-users xmlns=\"http://tomcat.apache.org/xml\"");
/* 575 */         writer.print("              ");
/* 576 */         writer.println("xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"");
/* 577 */         writer.print("              ");
/* 578 */         writer.println("xsi:schemaLocation=\"http://tomcat.apache.org/xml tomcat-users.xsd\"");
/* 579 */         writer.println("              version=\"1.0\">");
/*     */
/*     */
/* 582 */         values = null;
/* 583 */         values = getRoles();
/* 584 */         while (values.hasNext()) {
/* 585 */           writer.print("  ");
/* 586 */           writer.println(values.next()); // 10
/*     */         }
/* 588 */         values = getGroups();
/* 589 */         while (values.hasNext()) {
/* 590 */           writer.print("  ");
/* 591 */           writer.println(values.next());
/*     */         }
/* 593 */         values = getUsers();
/* 594 */         while (values.hasNext()) {
/* 595 */           writer.print("  ");
/* 596 */           writer.println(((MemoryUser)values.next()).toXml());
/*     */         }
/*     */       ...
/* 607 */       } catch (IOException e) {
/*     */           ...
/*     */       }
/* 613 */       this.lastModified = fileNew.lastModified();
/*     */     } finally {
/* 615 */       this.writeLock.unlock();
/*     */     }
/*     */     ...
/* 626 */     File fileOrig = new File(this.pathname);
/*     */     ...
/* 636 */     if (!fileNew.renameTo(fileOrig)) { // 11
/* 637 */       if (fileOld.exists() &&
/* 638 */         !fileOld.renameTo(fileOrig)) {
/* 639 */         log.warn(sm.getString("memoryUserDatabase.restoreOrig", new Object[] { fileOld }));
/*     */       }
/*     */
/* 642 */       throw new IOException(sm.getString("memoryUserDatabase.renameNew", new Object[] { fileOrig
/* 643 */               .getAbsolutePath() }));
/*     */     }
/* 645 */     if (fileOld.exists() && !fileOld.delete()) {
/* 646 */       throw new IOException(sm.getString("memory...