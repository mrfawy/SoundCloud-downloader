import soundcloud
import urllib.request
import os

CLIENT_ID="Please your APP ID here , check Soundcloud doc"

class SCDownloader(object):
	def __init__(self,client_id,):		
		self.client = soundcloud.Client(client_id=client_id)

	def downloadTrack(self,track,outputDir=None):		

		stream_url=None
		title=None
		#if map , i.e Track object
		if(hasattr(track,"__iter__")):
			if 'stream_url' in track:
				stream_url=track['stream_url']
				title=track['title']
				original_format=track['original_format']	
		else:
			stream_url=track.stream_url
			title=track.title
			original_format=track.original_format	

		downloadUrl=self.extractDownloadableStreamUrl(stream_url)	
		outputFileName=title+"."+original_format
		if outputDir!=None:
			os.makedirs(outputDir,exist_ok=True) 
			outputFileName=outputDir+"/"+outputFileName		
		self.download(downloadUrl,outputFileName)

	def downloadURL(self,url,outputDir=None):		
		resource = self.client.get('/resolve', url=url)			
		if resource.kind=="track":
			self.downloadTrack(resource,outputDir)
		elif resource.tracks!=None:
			for track in resource.tracks:
				self.downloadTrack(track,outputDir+"/"+resource.title if (outputDir!=None) else resource.title)

	def extractDownloadableStreamUrl(self,stream_url):
		stream_url = self.client.get(stream_url, allow_redirects=False)			
		return stream_url.location
	
	def download(self,url,fileName):
		data = urllib.request.urlopen(url)
		print("downloading"+url)
		with open(fileName, 'wb') as outputFile:
			outputFile.write(data.read())
		

sc=SCDownloader(CLIENT_ID)
url="https://soundcloud.com/ahmed-abd-el-hamid-1/z2k6bs1e553c"
sc.downloadURL(url,"""C:/Users/Mohamed/Downloads/SCDownloader/""")


#http://api.soundcloud.com/resolve.json?url=https://soundcloud.com/rehab-hany/sets/3frwwndnpirl&client_id=af2bb48f2f847e46e0ed26061554b3be
