import urllib.request
import json
import os


CLIENT_ID="please add your CLIENT_ID"

class SCDownloader(object):
	def __init__(self,client_id):		
		self.client_id=client_id

	def requestUrl(self,url):
		opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
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

	def downloadURL(self,url,outputDir=None):
		print("Processing URL:"+url)
		serviceUrl='http://api.soundcloud.com/resolve.json?url={0}&client_id={1}'.format(url,self.client_id)			
		res= self.requestUrl(serviceUrl)	
				
		# with open("SCoutput.txt", 'w') as outputFile:
		# 	outputFile.write(res.read().decode('utf-8'))
		

		resource=json.loads(res.read().decode('utf-8'))			
		
		if 'kind' in resource and resource['kind']=="track":
			print("Detected Single Track :")
			print(resource['title'].encode('utf-8'))
			self.downloadTrack(resource,outputDir)
		elif resource['tracks']!=None:
			print("Detected Playlist with "+ str(resource['track_count'])+" track(s)")
			for track in resource['tracks']:
				self.downloadTrack(track,outputDir+"/"+resource['title'] if (outputDir!=None) else resource['title'])
		else:
			print("Can't determine link type !! , Skipping ...")
	
	def downloadStream(self,stream_url,fileName):
		serviceUrl='{0}?client_id={1}'.format(stream_url,self.client_id)
		data = urllib.request.urlopen(serviceUrl)		
		with open(fileName, 'wb') as outputFile:
			outputFile.write(data.read())
		print("downloaded to : ")
		print(fileName.encode('utf-8'))
		
