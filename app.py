# from pytube import YouTube

# def download_video(url):
#     try:
#         youtube = YouTube(url)
#         video = youtube.streams.get_highest_resolution()
#         video.download('./downloads')
#         print('Video downloaded successfully.')
#     except Exception as e:
#         print('Error:', str(e))

# # Example usage:
# video_url = input("Enter the YouTube video URL: ")
# download_video(video_url)

# # python main.py

#///////////////////////////////// V2 //////////////////////////

from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    try:
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download('./downloads')
        message = 'Video downloaded successfully.'
    except Exception as e:
        message = 'Error: ' + str(e)
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()