# yal4ss
yet another log4shell scanner written in Python

## Intro

### General
- the purpose of this script is to scan multiple servers for the log4shell vulnerability
- it allows set custom payloads and injection points via its ```config.cfg``` file
- the file ```targets.txt``` needs to contain the systems you want to test
  
### IMPORTANT
- the script just tests if the vulnerability exists, but does not exploit it!
- the script is meant to be used by sysadmins to check if their systems are vulnerable or not
- you are not allowed to use this script against systems where the owner did not allow you to do so! 

---

## Requirements
```shell
$ pip3 install -r requirements.txt
```

---

## Usage
### Customize ```config.cfg``` file
- change ```back_connect_IP=127.0.0.1``` to the IP of your testing machine
- change ```back_connect_PORT=8080``` to a value of your desire
- if you want to add a test injection string just add a line like this ```INJ_STRING:${jndi:ldap://<IP>:<PORT>/<RND>}```
- ```<IP>``` is the placeholder where the ```yal4ass.py``` inserts your ```back_connect_IP``` when testing your targets
- ```<PORT>``` is the placeholder where the ```yal4ass.py``` inserts your ```back_connect_PORT``` when testing your targets
- ```<RND>``` is the placeholder where the ```yal4ass.py``` inserts a random value when testing your targets
- if you want to add a test injection point for a http header just adda line like this ```INJ_POINT:HEADER:User-Agent```
- if you want to add a test injection point for a specific get parameter just adda line like this 
  ```INJ_POINT:GET:hackme```
  
### Adding targets to ```targets.txt```
- just add one target/service per line
- format: ```[http|https]://[TARGET_IP]:[TARGET_PORT]```
- example: ```http://192.168.1.100:8080```

### Starting the script
```shell
$ python3 yal4ass.py -h

Yet another log4shell testing script.

optional arguments:
  -h, --help            show this help message and exit
  -d DELAY, --delay DELAY
                        Delay between every request in ms.
```
start without any parameters for plain testing
```shell
$ python3 yal4ass.py
```
start with a specific delay (ms) 
```shell
$ python3 yal4ass.py -d 500
```
example output
```bash
$ python3 yal4ass.py
[+] Started back connect server on 192.168.2.31:8080

[*] testing http://192.168.2.121:8001
sending requests to http://192.168.2.121:8001 |████████████████████████████████████████| 13/13 [100%] in 6.9s (1.89/s)

[*] testing http://192.168.2.121:8080
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 0: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 7: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 7: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 7: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 7: 	[+]192.168.2.121:b'JRMI\x00\x02K'
on 8: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 8: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 10: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 10: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 10: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 10: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
on 12: 	[+]192.168.2.121:b'0\x0c\x02\x01\x01`\x07\x02\x01\x03\x04\x00\x80\x00'
sending requests to http://192.168.2.121:8080 |████████████████████████████████████████| 13/13 [100%] in 7.0s (1.85/s)

[*] All targets tested.
[*] The following targets seem to be vulnerable
	[+] 192.168.2.121

[*] Press CTRL+c to stop the script
```
