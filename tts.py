# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Import the required module for text 
# to speech conversion 

from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
#loop lgana padega jitne label ho uske hisaab se
mytext = 'This is a plot between X AXIS TITTLE and Y AXIS TITTLE.The value of FIRST LABEL is, 50.The value of FIRST LABEL is, 50'

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("raghav.mp3") 

# Playing the converted file 
os.system("mpg123 raghav.mp3") 