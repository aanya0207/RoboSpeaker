import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker1.1 Created by Aanya")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            break
        engine.say(x)
        engine.runAndWait()
