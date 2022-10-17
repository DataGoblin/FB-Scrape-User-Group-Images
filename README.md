# FB-Scrape-User-Group-Images
Small selenium script to scrape images posted by a user in a FaceBook group.

# Info
This was created for a one-time use so it lacks features and polishing. 

> The script logs into FaceBook with cookies. You can use the extension
> below to export the correct cookie format to use. 
> https://github.com/ktty1220/export-cookie-for-puppeteer
> 
> You will likely need to replace the chromedriver in the tools folder
> to match your chrome version. 
> https://chromedriver.chromium.org/downloads

# How to 
Set your desired URL on line 23, image limit on line 27 and you are good to go!

The URL format is:
https://www.facebook.com/groups/***************/user/***************/

# Known /bugs/

 - [ ] The script will never end if your image limit is greater than the total available. (This can be fixed by creating a break exception when the infinite scrolling has reached the end)
