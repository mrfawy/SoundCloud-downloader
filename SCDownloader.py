import urllib.request
import json
import os
import argparse

CLIENT_ID="please add your APP ID"
HTTP_PROXY=None
OUTPUT_DIR="./SCDownloads"

class SCDownloader(object):
	def __init__(self,client_id,outputDir=None,http_proxy=None):		
		self.client_id=client_id
		self.outputDir=outputDir
		self.http_proxy=http_proxy


	def requestUrl(self,url):
		opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
		if self.http_proxy:			
			opener.add_handler(urllib.request.ProxyHandler({'http': self.http_proxy}))
			opener.add_handler(urllib.request.ProxyHandler({'https': self.http_proxy}))
			print("added handler "+self.http_proxy)
		
		urllib.request.install_opener(opener)
		req = urllib.request.Request(url)		
		res= urllib.request.urlopen(req)		
		return res

	def downloadTrack(self,track,outputDir=None):	
		
		stream_url=track['stream_url']
		title=track['title']
		original_format=track['original_format']	
		
		outputFileName=title+"."+original_format
		if outputDir!=None:
			os.makedirs(outputDir,exist_ok=True) 
			outputFileName=outputDir+"/"+outputFileName	

		self.downloadStream(stream_url,outputFileName)

	def downloadURL(self,url):
		print("Processing URL:"+url)
		serviceUrl='http://api.soundcloud.com/resolve.json?url={0}&client_id={1}'.format(url,self.client_id)			
		res= self.requestUrl(serviceUrl)	
				
		# with open("SCoutput.txt", 'w') as outputFile:
		# 	outputFile.write(res.read().decode('utf-8'))
		

		resource=json.loads(res.read().decode('utf-8'))			
		
		if 'kind' in resource and resource['kind']=="track":
			print("Detected Single Track :")
			print(resource['title'].encode('utf-8'))
			self.downloadTrack(resource,self.outputDir)
		elif resource['tracks']!=None:
			print("Detected Playlist with "+ str(resource['track_count'])+" track(s)")
			for track in resource['tracks']:
				self.downloadTrack(track,self.outputDir+"/"+resource['title'] if (self.outputDir!=None) else resource['title'])
		else:
			print("Can't determine link type !! , Skipping ...")
	
	def downloadStream(self,stream_url,fileName):
		serviceUrl='{0}?client_id={1}'.format(stream_url,self.client_id)
		data = urllib.request.urlopen(serviceUrl)		
		with open(fileName, 'wb') as outputFile:
			outputFile.write(data.read())
		print("Saved to : ")
		print(fileName.encode('utf-8'))


parser = argparse.ArgumentParser(description='Download tracks/Playlists from soundcloud')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-u', '--url',help='URL to download from')
group.add_argument('-f', '--file',help='A file containng list of URLs to download from')
parser.add_argument('-p','--proxy',help="http proxy settings ,e.g. proxy_host:port")
parser.add_argument('-c','--client',help='ClientID , refer to soundcloud API doc for authentication')
parser.add_argument('-o','--output',help='Folder path to save downlaods, defaults to application dir')

args = parser.parse_args()

if args.client :
	CLIENT_ID=args.client
if args.proxy:
	HTTP_PROXY=args.proxy
if args.output:
	OUTPUT_DIR=args.output

sc=SCDownloader(CLIENT_ID,OUTPUT_DIR,HTTP_PROXY)
if args.url:
	sc.downloadURL(args.url)
if args.file:
	urls = [line.strip() for line in open(args.file)]
	for url in urls:
		sc.downloadURL(url)
