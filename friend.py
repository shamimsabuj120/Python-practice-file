import pyttsx3

friend = pyttsx3.init()
speech = input("hey, say something:")
friend.say(speech)
friend.runAndWait()