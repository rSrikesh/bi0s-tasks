The Given Image was <br />
![sus](https://vpframework.s3.amazonaws.com/files/challenge/sus_45ea0966-6107-4c56-9355-059237fa11bf.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA5YJ5ZUB23SNKMN6X%2F20210524%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20210524T102639Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=40227018407e079803642a816d10b6e33913b0c6815a23434fc185f54585cd9c)

It was said that there are multiple files and images embeded within this images. To get details about all of them I used binwalk tool  and came to know that there are 4 JPEG images.

Then I used ```dd if=sus.png of=flag.jpeg skip=7821 bs=1``` .

The resultant flag.jpeg was 
