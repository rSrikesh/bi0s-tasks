Login into the game using ```ssh banditX@bandit.labs.overthewire.org -p 2220``` where X is the required level along with the password you will get from the previous level. <br />

## bandit0 -> bandit1
Login into bandit0 with the password **bandit0** <br />
In this level the password is stored in the file **readme** <br />
We can view contents of a file using the command ```cat <filename>``` <br />
So now required command is **cat readme** <br />
Password for bandit1 is **boJ9jbbUNNfktd78OOpsqOltutMc3MY1** 

## bandit1 -> bandit2
In this level password is stored in a file named ```-``` in the home directory. <br />
To read files containing special characters we should use escape characters <br />
so the required command is ```cat ./-```. <br />
Password for bandit2 is **CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

## bandit2 -> bandit3
In this level password is stored in a file named **spaces in this filename**  in the home directory. <br />
To read files whose filename is having spaces , we should enclose the filename within double-quotes. <br />
So required command is ```cat "spaces in this filename"```. <br />
Password for bandit3 is **UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

## bandit3 -> bandit4
In this level the password is stored in a hidden file within a directory named **inhere** <br />
In order to move to directory **inhere** , use the command ```cd inhere```. <br />
To list all hidden files, use command ```ls -a```. <br />
We shall find a hidden file named **.hidden** (hidden files always start with '.'). <br />
Use ``` cat .hidden``` to view the password. <br />
Password for bandit4 is **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

## bandit4 -> bandit5
Password for next level is stored in the only human-readable file in inhere directory.<br/>
First to move to a different directory do ```cd <directory>```. In this case it is 
```cd inhere``` <br />
Human readable files mean they have ASCII text within them. 
To find its type, do ```file <filename>``` <br />
Since many files are there, do ```file ./*``` to get information about type of each file <br />
Password can be found in a file named **-file07**(Since it is ASCII type) <br />
After which do ```cat ./file07``` to get the password. <br />
Passowrd for bandit5 is **koReBOKuIDDepwhWk7jZC0RTdopnAYKh** 

## bandit5 -> bandit6
Commands to be used are <br />
```cd inhere``` <br />
```find -size 1033c``` <br />
```cat ./maybehere07/.file2``` <br />
Password for bandit6 is **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

## bandit6 -> bandit7
Commands to be used are <br />
```find / -user bandit7 -group bandit6 -size 33c``` <br />
```cat /var/lib/dpkg/info/bandit7.password``` <br />
Passowrd for bandit7 is **HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**








