# SoundCloud-downloader
Download soundCloud files given browser URL ( either track or playlist) 

#### Features
* Simple util , with no depencies , just download , run via python (3+)
* Works on Linux/Windows 
* Accepts signle url or a file (line separated) list of urls 
* Option to download to your chosen dir 
* detect if URL is a single track , it'll donwload track with in output folder
* detect if URL is a playlist it'll create a folder named as playlist title and download all tracks isnide
* Supports working behind proxy (Note : suppports http/https standard proxies , for NTLM like please use a bridge like CNTLM)

### Example usage 
SCDownloader.py -u "your soundcloud browser url " -c "your client ID"

### Usage
SCDownloader.py (-u URL | -f FILE) [-p PROXY] [-c CLIENT] [-o OUTPUT]

* optional arguments:
  * -h, --help            show this help message and exit
  * -u URL, --url URL     URL to download from
  * -f FILE, --file FILE  A file containng list of URLs to download from
  * -p PROXY, --proxy PROXY  http proxy settings ,e.g. proxy_host:port
  * -c CLIENT, --client CLIENT  CliendID , refer to soundcloud API doc for authentication
  * -o OUTPUT, --output OUTPUT Folder path to save downlaods, defaults to application dir
