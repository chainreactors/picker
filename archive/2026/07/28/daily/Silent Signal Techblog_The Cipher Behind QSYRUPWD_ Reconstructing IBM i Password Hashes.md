---
title: The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes
url: https://blog.silentsignal.eu/2026/07/28/the-cipher-behind-qsyrupwd-reconstructing-ibm-i-password-hashes/
source: Silent Signal Techblog
date: 2026-07-28
fetch_date: 2026-07-29T05:04:22.116142
---

# The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes](/img/im-in-hack.gif)

# The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes

[pz](/authors/pz.html) 2026-07-28

## Intro

QSYRUPWD (Retrieve Encrypted User Password) is an IBM i API that returns password-related
data for a specified user profile in encrypted form to authorized callers.
IBM i is IBM’s integrated enterprise platform, originating from the AS/400 line,
and is still widely used for business-critical workloads such as ERP, finance,
logistics, and manufacturing.
The API primarily exists to support system functions such as password synchronization,
migration, replication, and other administrative scenarios where password material
must be transferred without exposing the cleartext password. IBM documents QSYRUPWD
as part of its security-related API set for handling encrypted password data.

During one of our IBM i penetration tests, I noticed that the client’s server was
configured with `QPWDLVL = 2`. On IBM i, the [QPWDLVL](https://www.ibm.com/docs/en/i/7.5.0?topic=passwords-password-level-qpwdlvl)
system value determines both
the password rules accepted by the operating system and the verifier formats maintained
for authentication compatibility. IBM documents that password levels 0 and 1 correspond
to the older DES-based scheme, [levels 2 and 3](https://www.ibm.com/docs/en/i/7.5.0?topic=passwords-password-level-qpwdlvl) use a SHA-1-based scheme,
and [level 4](https://www.ibm.com/docs/en/i/7.5.0?topic=passwords-password-level-qpwdlvl)
introduces a PBKDF2-based verifier model. IBM also states that when `QPWDLVL`
is set to 2, the operating system keeps compatibility with multiple password-verifier
forms rather than removing earlier ones.

This distinction is important when interpreting `QSYRUPWD` output.
John the Ripper includes dedicated IBM i cracking formats for legacy IBM i material,
specifically `as400_des` and `as400_ssha1`, which reflects support for the older
DES-based and salted SHA-1-based representations. However, in our testing, the `QSYRUPWD`
output obtained from systems running at QPWDLVL 2–4 did not match the form expected by
John the Ripper’s IBM i formats, whereas the legacy QPWDLVL 0–1 case is compatible with
the QSYRUPWD-derived material handled by those modules. In other words, for QPWDLVL 2–4,
the content returned by `QSYRUPWD` changes in a way that makes direct use with the existing
John the Ripper IBM i formats unsuccessful. This is an empirical observation from our
testing and tooling analysis, not a claim that IBM publicly documents the exact returned
structure for those levels.

As a result, even with `*ALLOBJ` and `*SECADM` (which are required to call `QSYRUPWD`), the API
could no longer be used for practical password-strength testing. After this engagement,
I decided to analyze the `QSYRUPWD` API in detail.

## Tools

To examine the API behavior directly, I wrote a small CL program that invokes
`QSYRUPWD` with the `UPWD0100` format, retrieves the returned buffer, and emits
it for further analysis.
The goal was not to build a full extraction tool, but to verify what kind of
password-related data the API returns under different `QPWDLVL` settings.
This made it possible to compare the actual output format across systems and
determine whether the returned data matched the input expected by existing
cracking tools such as John the Ripper.

```
PGM PARM(&USER)
    DCL VAR(&USER) TYPE(*CHAR) LEN(10)
    DCL VAR(&RCV) TYPE(*CHAR) LEN(4000)
    DCL VAR(&LEN) TYPE(*INT) LEN(4) VALUE(4000)
    DCL VAR(&FMT) TYPE(*CHAR) LEN(8) VALUE('UPWD0100')
    DCL VAR(&ERR) TYPE(*CHAR) LEN(8) VALUE(X'0000000000000000')
    DCL VAR(&N) TYPE(*INT) LEN(4)
    DCL VAR(&N4) TYPE(*CHAR) LEN(4)
    DCL VAR(&NCH) TYPE(*CHAR) LEN(11)

    CALL PGM(QSZS/QSYRUPWD) PARM(&RCV &LEN &FMT &USER &ERR)
       MONMSG CPF0000 EXEC(DO)
            SNDPGMMSG MSGID(CPF9898) MSGF(QCPFMSG) MSGDTA('QSYRUPWD failed') MSGTYPE(*ESCAPE)
       RETURN
       ENDDO

    CHGVAR VAR(&N4) VALUE(%SST(&RCV 1 4))
    CHGVAR VAR(&N) VALUE(%BIN(&N4))
    CHGVAR VAR(&NCH) VALUE(%CHAR(&N))
    SNDPGMMSG MSGID(CPF9898) MSGF(QCPFMSG) MSGDTA('QSYRUPWD ok, bytes:' *BCAT &NCH) MSGTYPE(*INFO)
    SNDPGMMSG MSGID(CPF9898) MSGF(QCPFMSG) MSGDTA('Data: ' *BCAT &RCV) MSGTYPE(*INFO)
ENDPGM
```

## Trace

After I compiled the `PWDDUMP` program, I wondered whether we could
generate a call trace. Luckily, IBM i provides a tool called `STRTRC` that can be
used to collect evidence about the calls made within `QSYRUPWD`.
So I logged in with a user that has `*ALLOBJ` and `*SECADM` authority
(required to run `PWDDUMP`), and ran the following commands:

```
STRTRC SSNID(MYTRACE) JOB(*ALL/QSECOFR/QPADEV0005) JOBTRCTYPE(*ALL)
CALL USERB1/PWDDUMP USERB1
ENDTRC SSNID(MYTRACE) PRTTRC(*YES)
PRTTRC  DTALIB(QGPL) DTAMBR(MYTRACE)
```

These commands create a spool file with the required call-trace information,
but the structure is a bit confusing at first glance, here is a sample
snippet of the spool file:

```
                                                                                                         |         |    SYNCHRONOU
                                                                                                   CALL  |   CPU   |   READS |  WR

TIME            THREAD    FLAG  FUNCTION PROGRAM                       LIBRARY     ENTRY   EXIT    LVL   |   TIME  |  DB  NDB|  DB
----------------------------------------------------------------------------------------------------------------------------------
12:53:35.829041 00000065        CALL     QCMD                          QSYS       x000519 x000519     1     .000000    0    0    0
12:53:35.829041 00000065        CALL     QUICMENU                      QSYS       x0000C1 x0000C1     2     .000000    0    0    0
12:53:35.829041 00000065        CALL     QUIMNDRV                      QSYS       x00061E x00061E     3     .000000    0    0    0
12:53:35.829041 00000065        CALL     QUIMGFLW                      QSYS       x0004D9 x0004D9     4     .000000    0    0    0
12:53:35.829041 00000065        CALL     QUICMD                        QSYS       x00056F x00056F     5     .000000    0    0    0
12:53:35.829041 00000065        XCTL     QSCSNTRC                      QSYS       x000A70 x000A70     6     .000000    0    0    0
12:53:35.829041 00000065        CALL     QCMDEXC                       QSYS       x00012F x00012F     7     .000000    0    0    0
12:53:35.829041 00000065        XCTL     QYPESTRP                      QSYS        000000  000000     8     .000000    0    0    0
```

I wrote a scraper that converts the raw spool file content into a more readable
format, for example:

```
PWDDUMP / PWDDUMP
QCLRSLV
QCLCLCPR -> QMHSNDPM -> return PWDDUMP
QSYRUPWD / QSYRUPWD
QLEIT / Q LE sinit_processor -> itl_callInit__FPV12ITL_COM_AREA -> QPWFSMONOC -> return QSYRUPWD
QZLSRTPW / _CXX_PEP__Fv -> main
QZLSSRV1 / QzlsGetNTPassword__FPcP15QzlsNTPasswords
QSYSERV / QSYSRVRTV / qsy_rtv_user_ent__FPCcN21CcCiP20_qsy_serv_rtn_data_TPi
QSYSERV / QSYSRVUTL / caller_is_authorized__FPCcPcPPvCs
QSYMIUTLS / QSYGETSYP /
    qsy_getSYP__FPCcT1C11_OBJ_TYPE_TPPvPs
    qsy_getSYP_long__FPCcT1C11_OBJ_TYPE_TPPvPs
QSYAUTUTLS / QSYCHKAUT /
    qsy_chkaut__FPvsT2cPs
    qsy_chkaut__FPvsT2cT4Ps
QSYMIUTLS / QSYTESTAU / qsy_testau__FPvsT2Ps
return QSYSERV / QSYSRVRTV / qsy_rtv_user_ent__FPCcN21CcCiP20_qsy_serv_rtn_data_TPi
QSYSERV / QSYSRVRTV / rtv_user_entries__FPCcN21CcCiP20_qsy_serv_rtn_data_TPi
QSYSERV / QSYSRVUTL / get_security_index__FPCcPPv
QSYMIUTLS / QSYGETSYP /
    qsy_getSYP__FPCcT1C11_OBJ_TYPE_TPPvPs
    qsy_getSYP_long__FPCcT1C11_OBJ_TYPE_TPPvPs
QSYMIUTLS / QSYMATSOBJ / qsy_matsobj__FPvP16_MSOB_Template_TPs
return QSYSERV / QSYSRVRTV / rtv_user_entries__FPCcN21CcCiP20_qsy_serv_rtn_data_TPi

QSYSERV / QSYSRVRTV / qsy_rtv_user_ent__F...