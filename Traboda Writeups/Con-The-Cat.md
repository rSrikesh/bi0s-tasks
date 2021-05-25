The Given Image was <br />
![sus](https://github.com/rSrikesh/bi0s-tasks/blob/main/Traboda%20Writeups/con/sus.png)

It was said that there are multiple files and images embeded within this images. To get details about all of them I used binwalk tool  and came to know that there are 4 JPEG images.

Then I used ```dd if=sus.png of=flag.jpeg skip=7821 bs=1``` .

The resultant flag.jpeg was <br />
![flag](https://github.com/rSrikesh/bi0s-tasks/blob/main/Traboda%20Writeups/con/flag.jpeg)
