""""
This is the final script.
Don't edit master, create a pull request
"""
#How to import picam video recorder?
import picamera
from subprocess import call
import os
import RPi.GPIO as GPIO
from time import time, sleep, strftime, gmtime
from multiprocessing import Process
import itertools


#Have to change this with the codes to record video using picam :)
def RecordVideo():
        camera.hflip = True
        camera.vflip = True
        camera.start_recording('video.h264')

def RecordAudio():
    call ([alsa_rec], shell=True)
    exit()

    #Define StopRecording so that that can be done with another
    #button input
    #sleep(5)
    #camera.stop_recording()


#Have to change to stop video using picam.
def StopRecording():
    camera.stop_recording()

def StopAudio():
    call ([alsa_stop], shell=True)
    exit()

def ConvertVideo():
    call ([VideoConvert], shell=True)
    exit()


def DeleteTempFiles():
    os.remove("video.h264")
    os.remove("outputfile.mp4")


def UploadFiles():
    command = ([rclone copy /gdrive/ googledrive:gdrive/])
    result = subprocess.Popen(command)
    result.communicate()

    """
    command = ([RCLONE, 'move', '--log-file=rclone_upload.log', '--transfers', RCLONE_TRANSFERS, '--drive-chunk-size=16M', '--exclude', 'filepart', LOCAL_DIR + dir + '/', REMOTE_NAME  + REMOTE_DIR + dir + '/'])
    result = subprocess.Popen(command)
    result.communicate()
    """


def LedStandby():
        for num in itertools.count(1): #creates an infinite loop
            GPIO.output(SLed, 1)
            sleep(1)
            GPIO.output(SLed, 0)
            sleep(1)


def LedRecording():
        for unm in itertools.count(1):
            GPIO.output(RLed, 1)
            sleep()
            GPIO.output(RLed, 0)
            sleep(1)


def LedUploading():
        for unm in itertools.count(1):
            GPIO.output(ULed, 1)
            sleep()
            GPIO.output(ULed, 0)
            sleep(1)




if __name__ == "__main__":   #start of the program?


#Use code 89 in case 90 fails.
#VideoConvert = "ffmpeg -r 30 -i video.h264 -vcodec copy outputfile.mp4"
DateFilename=strftime("%Y-%m-%d %H.%M", gmtime())
VideoConvert = "ffmpeg -r 30 -i video.h264 -vcodec copy %s.mp4" %DateFilename
alsarec = "code to record audio"
camera = picamera.PiCamera()

SLed = 5
RLed = 7
ULed = 8
Button1 = 10
Button2 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SLed, GPIO.OUT)
GPIO.setup(RLed, GPIO.OUT)
GPIO.setup(ULed, GPIO.OUT)
GPIO.setup(Button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Button 1 and Button2 are set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both





#Progrm starts here:
while True:
    if (GPIO.input(Button1)):






#The last lines of codes.
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
