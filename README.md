# PDF Bruteforcer Demo

[![Test Status](https://github.com/jo-hoe/pdf-bruteforcer/workflows/unittests/badge.svg)](https://github.com/jo-hoe/pdf-bruteforcer/actions?workflow=unittests)

One of the big health insurance companies sends personal information
in an encrypted PDF via mail. The mail that contains the PDF also 
contained details about the structure of the password 
(i.e. the birth date of the data subject + formatting details).
The project demonstrates how a password secured PDF can be attacked 
with this information.

## Purpose

This project is only for educational purposes.
It demonstrates how easily a password can be guessed given
information about the password is provided.

### Real Attacks

In a real world scenario an attacker might us a faster
programming language (e.g. C++) instead of Python to reduce
the runtime. If no additional details about the password about
are known, attackers might use lists of common passwords and
passphrases.

## Run

```powershell
python3 demo.py
```

## Environment

This is a python 3 project.
You may create a virtual python environment like so:

```powershell
python -m venv .venv
```

and afterwards install your dependencies:

```powershell
.\.venv\Scripts\pip.exe install -r requirements.txt
```
