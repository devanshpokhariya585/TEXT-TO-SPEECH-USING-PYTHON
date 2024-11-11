
import win32com.client 


speaker = win32com.client.Dispatch("SAPI.SpVoice") 



while True:
	text =input("ENTER YOUR TEXT THAT YOU WANT TO CONVERT INTO SPEECH : ")
	speaker.Speak(text) 
	if text=="q":
		break

speaker.speak("Assignment completed")