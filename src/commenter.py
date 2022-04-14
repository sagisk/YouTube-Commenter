from model import GenerateText
from youtube_api import YoutubeApi

def main():
    ytA = YoutubeApi(root="insert here path to your client secret file")

    model = GenerateText(context="I don't know", text_length=15)
    generated_text = model.greedy()

    ytA.insert_comment(channel_id=None, video_id="XcjqapXfrhk", text=generated_text)

if __name__ == "__main__":
    main()