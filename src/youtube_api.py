import os

import requests
from bs4 import BeautifulSoup

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import googleapiclient.errors

class YoutubeApi:
  def __init__(self, root="insert here path to your client secret file"):
    api_service_name = "youtube"
    api_version = "v3"
    SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    
    self.CLIENT_SECRET_FILE = root
    self.response = ""
    
    # Get credentials and create an API client
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    self.youtube = build(
        api_service_name, api_version, credentials=credentials)
    
  def insert_comment(self, channel_id, video_id, text):
    request = self.youtube.commentThreads().insert(
        part="snippet",
        body={
          "snippet": {
            "channelId": "{0}".format(channel_id),
            "videoId": "{0}".format(video_id),
            "topLevelComment": {
              "snippet": {
                "textOriginal": "{0}".format(text)
              }
            }
          }
        }
    )
    self.response = request.execute()
    print(self.response)

  def _parse_custom_channel_id(self, custom_id):
    resp = requests.get(f'https://www.youtube.com/c/{custom_id}')
    soup = BeautifulSoup(resp.text, 'html.parser')
    channel_id = soup.select_one('meta[property="og:url"]')['content'].strip('/').split('/')[-1]
    return channel_id

  def search_channel(self, channel_id, max_number_of_videos=5, is_custom_id=False):
    if is_custom_id:
      channel_id = self._parse_custom_channel_id(channel_id)
    else:
      channel_id = channel_id
    request = self.youtube.search().list(channelId=channel_id,
                          part='snippet',
                          type='video',
                          maxResults=max_number_of_videos,
                          order='viewCount')
    self.response = request.execute()
    return self.response

  def search_video(self, video_id):
    request = self.youtube.videos().list(
        part="statistics",
        id=video_id
    )
    self.response = request.execute()
    return self.response