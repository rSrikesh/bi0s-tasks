This writeup is for Naive Cipher Challenge
I was given a encrypted text in the form of ```dixoae{oczz_ocz_hvnozm_ja_xvznzm_xdkczm}```.<br />
On seeing this text, first thing that came to my mind is the six alphabets before the curly brackets ie **dixoae**. Since the flag format is inctfj{....}, I started figuring the relaion between inctfj and dixoae. I found out that there is a shift of 5 in the left direction. Since i have the key, it became easier to decrypt the text.

The flag is ```inctfj{thee_the_master_of_caeser_cipher}```
