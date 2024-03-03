from tkinter.filedialog import askopenfilename
import moviepy.editor
from tkinter import *

vid= askopenfilename()
video= moviepy.editor.VideoFileClip(vid)

aud= video.audio
aud.write_audiofile("demo.mp3")

print("--End--")

#the dilaog box will open and you have to select the video file that will convert to audio file after the sucessful running of an program.
