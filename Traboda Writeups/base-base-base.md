First I used  <br />
```echo "R1k0U0FOVEZFQTNER0lCWEdRUURNTlJBR1pRU0FOM0NFQTNERUlCVEdRUURPTVpBR01aU0FOWlRFQTJXTUlCVEdRUURPTVJBR01aU0FOTEdFQTNER0lCVEdBUURHTUJBR01ZQ0FNWlFFQVpUQUlCVEdBUURHTUJBR01ZQ0FOVERFQTNXST09PQ==" | base64 --decode```.<br />
Then i got a base32 string for which I used <br />
```echo "GY4SANTFEA3DGIBXGQQDMNRAGZQSAN3CEA3DEIBTGQQDOMZAGMZSANZTEA2WMIBTGQQDOMRAGMZSANLGEA3DGIBTGAQDGMBAGMYCAMZQEAZTAIBTGAQDGMBAGMYCANTDEA3WI===" | base32 --decode```. <br />
Then i got Hex string , which on decoding got the flag. The flag is ```inctfj{b4s3s_4r3_c00000000l}```