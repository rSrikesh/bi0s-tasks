## Forensics

## Glory of the Garden

Used **binwalk garden.jpg** to check if there is any files/folders in this images, since there wasnt any, i used <br />
```dd if=garden.jpg of=flag.txt skip=0 bs=1```.  <br />
I used strings flag.txt to get all human readable strings. The flag was found at the last line. <br />
The flag is ```picoCTF{more_than_m33ts_the_3y3eBdBd2cc}```

## information

It was given a clue that we need to check details of the image. I refered this [link](https://wiki.bi0s.in/steganography/exiftool/) , where they mentioned we can information about an image using **exiftool**. When i used this tool on the image , i got many information about this image. Thats where, the license part of the information was interesting , where it was given in scrambled form. When i checked various examples , there were proper license names. So i thought it must be different type of string.Then i used hex, base64 and many more tools on this license (basically brute-force).When i used base64 tool for this text on my terminal , i got the flag 
The flag is ```picoCTF{the_m3tadata_1s_modified}```

## Matryoksha doll

Used **binwalk -e <image_name>** , **cd [directory]** for different images and folders found within this dolls.jpg . There were 3 images 2_c.jpg,3_c.jpg,4_c.jpg. The flag.txt was found after performing extraction on 4_c.jpg. <br />
The flag is ```picoCTF{ac0072c423ee13bfc0b166af72e25b61}``` 
