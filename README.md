# Gitea to hashcat 
## Simple Python Script to extract from Gitea DB file and convert the credentials to crackable hashes though hashcat

![N|Solid](https://about.gitea.com/gitea-text.svg)

This simple python script will help to extract the credentials from Gitea DB and convert the extracted content to crackable hashes in hashcat 

Follow below steps to succeed the cracking 

```sh
git clone https://github.com/cybersentinal/Gitea2hashcat.git

cd Gitea2hashcat 

python3 gitea2hashcat.py <gitea.db> > hash

hashcat -m 10900 hash /usr/share/wordlists/rockyou.txt
```

*This code was originally from #ipsec and full credit goes to him. I just regenerated the code to work in my project (titanic.htb)*

