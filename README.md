# apodBackgroundImage
A scrapybot python based that downloads today's image from Apod Nasa and set a random image to be your background image for the day.

In this project I'm using python, scrapy, subprocess, os, random and loguru, all the changes needed to use this in another website are changing the url, domain and the response.css, if needed.

To use this in your linux, just change the var img_path in line 11 to the path of your project.

If desires to set it to run everyday, set it on your /etc/crontab using the command

* 10 * * *	root	scrapy runspider {projectPath}