# SoundCloud-downloader
Download soundCloud files given browser URL ( either track or playlist) 


usage: SCDownloader.py [-h] (-u URL | -f FILE) [-p PROXY] [-c CLIENT] [-o OUTPUT]

optional arguments:
-h, --help            show this help message and exit
-u URL, --url URL     URL to download from
-f FILE, --file FILE  A file containng list of URLs to download from
-p PROXY, --proxy PROXY  http proxy settings ,e.g. proxy_host:port
-c CLIENT, --client CLIENT  CliendID , refer to soundcloud API doc for authentication
-o OUTPUT, --output OUTPUT Folder path to save downlaods, defaults to application dir
