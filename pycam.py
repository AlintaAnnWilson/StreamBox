"""
This script is to record a video, convert it to mp4 and upload it to google drive using rclone, while displaying progress. 
YouTube API integration will be added later. 
"""
import picamera
#from time import sleep
from subprocess import call
import os
import RPi.GPIO as GPIO
import time

video_convert = "ffmpeg -r 30 -i video.h264 -vcodec copy gdrive/outputfile.mp4"

os.system('clear')
print('Recording...')
#Lighting LED. This just keep the LED on, no blinking.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
for i in range(0,10):
    GPIO.output(40,1)
    time.sleep(1)
    GPIO.output(40,0)
    time.sleep(1)

#Recording Video
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

    #For turning off LED
    GPIO.output(40,0)


os.system('clear')
print('Recording...... \nStopping recording')

sleep(1)

#Converting the raw h.264 to mp4
call ([video_convert], shell=True)
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting File........[y]')
print('Deleting temp files....[y]')
os.system('rm video.h264')
os.system('rm /gdrive/outputfile.mp4')
print('Uploading')
#Uploading files to google drive using rclone
os.system('rclone copy /home/pi/pythoncam/gdrive googledrive:gdrive')
os.system('clear')
print('Recording..............[y] \nStopping recording.....[y] \nConverting.............[y] \nDeleting temp files....[y] \nUploading..............[y]')
print('\nCompleted')
