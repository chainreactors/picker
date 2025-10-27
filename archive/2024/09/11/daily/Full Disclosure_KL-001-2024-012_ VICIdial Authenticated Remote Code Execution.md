---
title: KL-001-2024-012: VICIdial Authenticated Remote Code Execution
url: https://seclists.org/fulldisclosure/2024/Sep/26
source: Full Disclosure
date: 2024-09-11
fetch_date: 2025-10-06T18:30:30.790690
---

# KL-001-2024-012: VICIdial Authenticated Remote Code Execution

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# KL-001-2024-012: VICIdial Authenticated Remote Code Execution

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 10 Sep 2024 14:31:14 -0500

---

```
KL-001-2024-012: VICIdial Authenticated Remote Code Execution

Title: VICIdial Authenticated Remote Code Execution
Advisory ID: KL-001-2024-012
Publication Date: 2024-09-10
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-012.txt

1. Vulnerability Details

     Affected Vendor: VICIdial
     Affected Product: VICIdial
     Affected Version: 2.14-917a
     Platform: GNU/Linux
     CWE Classification: CWE-78: Improper Neutralization of Special
                         Elements used in an OS Command
                         ('OS Command Injection')
     CVE ID: CVE-2024-8504

2. Vulnerability Description

     An attacker with authenticated access to VICIdial as an "agent"
     can execute arbitrary shell commands as the "root" user. This
     attack can be chained with CVE-2024-8503 to execute arbitrary
     shell commands starting from an unauthenticated perspective.

3. Technical Description

     VICIdial is an open-source contact center suite, mainly used
     by call centers. The "vicidial.com" website boasts over 14,000
     registered installations. There is a public SVN repository to
     access the source code, as well as an ISO that can be used to
     install the software. The ISO was used in a virtual machine
     for testing purposes.

     Users can be added to specific "groups" that enable them to log
     into the "agent" web client if that group is associated with a
     "campaign".  This web client is for agents to manage inbound
     and outbound phone calls, displaying pertinent information
     regarding the "lead", such as the personal information of the
     individual on the other end of the call.

     An agent has the ability to record the phone call using the
     "START RECORDING" button. When clicked, an HTTP request is sent
     to the server which is processed by the "manager_send.php"
     PHP script. The "filename" parameter included in the request
     is sanitized with the "preg_replace" PHP function to prevent
     SQL injection, as shown by this snippet:

    if (isset($_GET["filename"])) {$filename=$_GET["filename"];}
    elseif (isset($_POST["filename"])) {$filename=$_POST["filename"];}
    ...
    $filename = preg_replace("/\'|\"|\\\\|;/","",$filename);

     The regular expression used to sanitize this parameter is
     very permissive, only removing single quotes, double quotes,
     backslashes, and semicolons.

     Later in the execution of "manager_send.php", the "filename"
     variable is added to a SQL database through an "INSERT"
     statement, along with other user-controlled variables such as
     "exten":

    $stmt="INSERT INTO vicidial_manager values('','','$NOW_TIME',
        'NEW','N','$server_ip','','Originate','$vmgr_callerid',
        'Channel: $channel','Context: $ext_context',
        'Exten: $exten','Priority: $ext_priority',
        'Callerid: $filename','','','','','');";
    if ($format=='debug') {echo "\n<!-- $stmt -->";}
    $rslt=mysql_to_mysqli($stmt, $link);

     On the server-side, an asyncronous cron job is executing the
     perl script "ADMIN_keepalive_ALL.pl":

    vicibox11:/ # crontab -l | grep keepalive
    ### keepalive script for astguiclient processes
    * * * * * /usr/share/astguiclient/ADMIN_keepalive_ALL.pl

     This perl script ensures several worker perl scripts
     are running.  Included in these worker perl scripts is
     "AST_manager_send.pl", as shown by this snippet from
     "ADMIN_keepalive_ALL.pl":

    if ($psline[1] =~ /AST_manager_se/)
      {
      $runningAST_send++;
      if ($DB) {print "AST_send RUNNING:   |$psline[1]|\n";}
      }
    ...
    if ( ($AST_send_listen > 0) && ($runningAST_send < 1) )
      {
      if ($DB) {print "starting AST_manager_send...\n";}
      # add a '-L' to the command below to activate logging
      `/usr/bin/screen -d -m -S ASTsend
        $PATHhome/AST_manager_send.pl $debug_string`;

     The "AST_manager_send.pl" script will continuously monitor the
     "vicidial_manager" table in the SQL database for records with
     the "status" column equal the string "NEW". Values from that
     row are then URL-encoded and used as command-line arguments
     to invoke the "AST_send_action_child.pl" perl script:

    while ($endless_loop > 0)
      {
      my $stmtA = "SELECT count(*) from
        vicidial_manager where server_ip = '"
        . $conf{VARserver_ip} . "' and status = 'NEW';";
      ...
      $originate_command .= $vdm->{cmd_line_e} . "\n"
        if ($vdm->{cmd_line_e});
      $originate_command .= $vdm->{cmd_line_f} . "\n"
        if ($vdm->{cmd_line_f});
      $originate_command .= $vdm->{cmd_line_g} . "\n"
        if ($vdm->{cmd_line_g});
      ...
      $vdm->{cmd_line_e} =~ s/([^A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg;
      $vdm->{cmd_line_f} =~ s/([^A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg;
      $vdm->{cmd_line_g} =~ s/([^A-Za-z0-9])/sprintf("%%%02X", ord($1))/seg;
      ...
      $launch .= " --cmd_line_e=" . $vdm->{cmd_line_e}
        if ($vdm->{cmd_line_e});
      $launch .= " --cmd_line_f=" . $vdm->{cmd_line_f}
        if ($vdm->{cmd_line_f});
      $launch .= " --cmd_line_g=" . $vdm->{cmd_line_g}
        if ($vdm->{cmd_line_g});
      ...
      $launch .= " >> " . $conf{PATHlogs} . "/action_send." .  logDate()
        if ($SYSLOG);
      system($launch . ' &');

     The "AST_send_action_child.pl" will then initiate a telnet
     connection to the "Asterisk Call Manager" and issue various
     commands as they appear in the command-line arguments:

    my $tn = new Net::Telnet (Port => $telnet_port,
        Prompt => '/\r\n/',
        Output_record_separator => '',
        Errmode    => "return");
    ...
    $tn->open("$telnet_host");
    $tn->waitfor('/Asterisk Call Manager\//');
    ...
    $originate_command .= $cmd_line_e . "\n" if ($cmd_line_e);
    $originate_command .= $cmd_line_f . "\n" if ($cmd_line_f);
    $originate_command .= $cmd_line_g . "\n" if ($cmd_line_g);
    ...
    my @list_channels = $tn->cmd(String => $originate_command,
        Prompt => '/.*/');

     These commands are then processed by the Asterisk
     Management interface (AMI). The configuration file
     "extensions-vicidial.conf" contains useful information on
     how AMI processes the value of the user-controlled "Exten"
     command. The following is a relevant snippet:

    exten => 8309,1,Answer
    exten => 8309,2,Monitor(wav,${CALLERID(name)})
    exten => 8309,3,Wait(3600)
    exten => 8309,4,Hangup()
    ...

     When supplying an "Exten" value of "8309", the "Monitor"
     application is invoked, which will record the current call and
     write the recorded data into a file. The default directory
     is "/var/spool/asterisk/monitor". In this case, the name
     of the file is derived from the "CALLERID", which is also
     user-controlled.

     This can be leveraged by an attacker to write file names
     that contain malicious shell commands. Take for example the
     following HTTP request:

    POST /agc/manager_send....