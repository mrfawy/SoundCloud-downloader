# SoundCloud-downloader
Download soundCloud files given browser URL ( either track or playlist) 

#### Features
* Simple util,with a few lines of py script, with no dependencies .Just download and  run via python (3+)
* Works on Linux/Windows 
* Accepts single url or a file (line separated) list of urls 
* Optional save file to selected dir 
* detect if URL is a single track , it'll download track  in output folder
* detect if URL is a playlist it'll create a folder named as playlist title and download all tracks inside
* Supports working behind proxy (Note : supports http/https standard proxies , for NTLM like please use a bridge like CNTLM)

### Example usage 
py SCDownloader.py -u "your SoundCloud browser url " -c "your client ID"

py SCDownloader.py -u https://soundcloud.com/manoeldodriguesfilho/hans-zimmer-inception-time -c "your client ID"

* Notes:
 * To create your client ID please refer to SoundCloud doc , you can access yours at [your apps ] (http://soundcloud.com/you/apps)
 * You can save your client Id , edit the file , set CLIENT_ID( at the very beginning) with your value , don't have to enter -c next time
 * It works similarly with other options ( proxy ,outputdir), pass arguments to override these defaults
 
### Copyrights
This tool  should be only used according to sound cloud copyrights and privacy rules

### Usage
SCDownloader.py (-u URL | -f FILE) [-p PROXY] [-c CLIENT] [-o OUTPUT]

* optional arguments:
  * -h, --help            show this help message and exit
  * -u URL, --url URL     URL to download from
  * -f FILE, --file FILE  A file containing list of URLs to download from
  * -p PROXY, --proxy PROXY  http proxy settings ,e.g. proxy_host:port
  * -c CLIENT, --client CLIENT  Client ID , refer to soundcloud API doc for authentication
  * -o OUTPUT, --output OUTPUT Folder path to save downlaods, defaults to application dir
