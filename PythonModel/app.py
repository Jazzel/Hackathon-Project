from flask import Flask, request
import os
from moviepy.editor import VideoFileClip
from moviepy.video.fx.resize import resize
from flask_cors import CORS
from imutils.video import FPS
import numpy as np
from datetime import datetime
import cv2
import os
import time
import pandas as pd
from openpyxl.workbook import Workbook
from tensorflow import keras
import argparse
from flask import request
from flask import Flask

from fatigue_detect import main


app = Flask(__name__)
CORS(app)



@app.route('/api/upload', methods=['POST'])
def upload_video():
    video_file = request.files['video']
    video_path = 'temp_video.avi'  # Path to temporarily store the video

    # Save the video file
    video_file.save(video_path)
    time.sleep(5)
    temp = main()
    print(f'perlos is{temp[0]}')
    print(f'pom is{temp[1]}')


   
    return 'Video merged and saved successfully!'

    # # Merge the video
    # merged_video_filename = 'merged_video.avi'
    # folder = 'PythonModel'
    # # Filename for the merged video
    # merged_video_path = os.path.join(os.path.dirname(
    #     video_path), folder,  merged_video_filename)  # Path to store the merged video

    # # Set the duration of the video (in seconds)
    # duration = 10.0  # Replace with the actual duration of the recorded video

    # # Convert webm to avi using moviepy
    # video_clip = VideoFileClip(video_path)
    # # Resize the video to the specified duration
    # video_clip_resized = resize(video_clip, duration=duration)

    # # Set the codec and fps of the merged video
    # video_clip_resized.write_videofile(
    #     merged_video_path, codec='mpeg4', fps=video_clip_resized.fps, audio=False)

    # # Delete the temporary video file
    # os.remove(video_path)


@app.route('/api/turns', methods=['POST'])
def upload_turns():
    turns = request.json['turns']
    print(turns)
    return 'Turns uploaded successfully!'


@app.route('/api/reactTime', methods=['Post'])
def upload_reactTime():
    reactTime = request.json['reactTime']
    print(reactTime)
    return 'ReactTime uploaded successfully!'




# def videoAnalyzer():
#     # run the YOLO model which will calls the LSTM model
#     (perlos, pom) = main()
#     return (perlos, pom)


if __name__ == '__main__':
    app.run()
