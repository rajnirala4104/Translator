from googletrans import LANGUAGES, Translator
from gtts import gTTS
from playsound import playsound
from os import remove

trans = Translator()
# print(LANGUAGES)
def translator(yourText, yourLanguage, wantLanguage):
    a = trans.translate(yourText, dest=wantLanguage)
    converter = gTTS(a.text, lang=yourLanguage)
    converter.save("sound.mp3")
    playsound("sound.mp3")
    remove("sound.mp3")


if "__main__" == __name__:
    yourText = input("Enter  your text : ")
    yourLanguage = input("In which language you have enter the text: ")
    wantLanguage = input("In which language do you want to convert: ")
    translator(yourText, yourLanguage,wantLanguage )