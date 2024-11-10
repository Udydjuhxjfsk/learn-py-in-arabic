from gtts import gTTS
from playsound import playsound
mytext = "I love PYTHON"
myjob = gTTS(text = mytext)
myjob.save('welcome.mp3')
playsound("welcome.mp3")