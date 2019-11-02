# SteamCat
Simple python script to aid in categorising Steam games based on data from external trackers

## Requirements  
* Latest Version of Python - https://www.python.org/downloads/  
* Account on https://completionist.me/
* Preferred Text Editor (Notepad is fine, but Notepad++ is better)

## Before Starting
Make a backup of both your **localconfig.vdf** and your **sharedconfig.vdf** from your Steam directories. These can be found in:
* \<Install Directory\>\Steam\userdata\\<Steam3 ID\>\config\localconfig.vdf
* \<Install Directory\>\Steam\userdata\\<Steam3 ID\>\7\remote\sharedconfig.vdf

Default Install Directory for Steam is C:\Program Files x86\.

If you only have one account, there will only be one folder in \userdata\ - If you have used multiple accounts on your device, check your Steam3 ID using a tool such as https://steamdb.info/calculator/ 

## Steps
1. Download "SteamCat.py", "unparsed.txt" and store them in the same folder. Optionally, download "sharedconfig.vdf" if you want a file with no categories to start afresh with.

1. Open your "Games" page on https://completionist.me/ and filter it according to a single category you wish to make.

1. Set the display to "mosaic" using the icons on the top right.

1. Open the Page's Source (Ctrl+U on most browsers, also accessible via right click menu)

1. Copy the page's source to and paste it into **unparsed.txt** If there are multiple pages of results for the filter you used, copy each page's source to the text file without overwriting.

1. Run SteamCat.py

1. Enter the name of the category you wish to make and press enter. This should make a file called "addToVDF.txt"

1. **If you wish to assign more categories, replace the contents of "unparsed.txt" with a new page source then run the script again. Repeat this until you are done assigning categories.**

1. If you have not already, close Steam.

1. Open "sharedconfig.vdf" either in your Steam directory (or the blank one provided) and paste the contents of "addToVDF.txt" **between the curly braces after "Apps"**, then save.

1. Place the new sharedconfig.vdf in your \<Install Directory\>\Steam\userdata\\<Steam3 ID\>\7\remote\ folder.

1. Launch Steam, wait for library to load.

1. In your **normal web browser (Chrome/FF/Edge - NOT STEAM)**, enter steam://resetcollections in your browser (or click it as a link)

1. In your library, you should have a dialogue confirming to reset your categories to those in the sharedconfig.vdf. If the categories are what you assigned using the script, confirm and your collections will be replaced with the new categories.
