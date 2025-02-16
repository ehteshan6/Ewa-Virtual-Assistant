import time
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyautogui
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio, rate=200):
    """Speak with a customizable rate (speed) of speech."""
    engine.setProperty('rate', rate)  # Adjust the speech rate
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 200)  # Reset to default rate after speaking

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am EWA, your hilarious and super-smart virtual assistant. How can I make your day better, ?",rate=175)

def takeCommand():
    """Takes microphone input from the user and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')  # Replace with yours
        server.sendmail('your-email@gmail.com', to, content)
        server.close()
    except Exception as e:
        speak("Sorry, I couldn't send the email. Maybe the email was too awesome for the server to handle!")

def calculate_math(expression):
    try:
        result = eval(expression)
        speak(f"The result is {result}. I'm a math genius, aren't I?")
    except Exception as e:
        speak("I couldn't calculate that. Maybe it's one of those unsolvable mysteries of the universe.")

def personal_response(query):
    if 'how are you' in query:
        responses = [
            "I'm doing great, thanks for asking! Just chilling in the digital world.",
            "I'm fantastic! Ready to make your day brighter.",
            "I'm just a bunch of code, but I'm feeling pretty awesome today!"
        ]
        speak(random.choice(responses))
    
        
    elif 'who created you' in query:
        # Hyped-up, slow voice tone for this response
        speak("The greatest Person in History of Human beings, The most Smarter The most Powerfull, The most Dangerous, The conqueror of the Knowledge, The  Great Waaheed Alam", rate=130)
    elif 'thank you' in query:
        responses = [
            "You're welcome! I live to serve.",
            "No problem! I'm here to make your life easier.",
            "Anytime! Just call me your personal assistant superhero."
        ]
        speak(random.choice(responses))
    elif 'what can you do' in query:
        speak("I can do all sorts of things! From cracking jokes to solving math problems, I'm your one-stop shop for fun and productivity.")
    elif 'tell me a joke' in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the computer go to the doctor? It had a virus!"
        ]
        speak(random.choice(jokes))
    elif 'are you single' in query:
        speak("I'm in a committed relationship with your computer. It's complicated.")
    elif 'do you love me' in query:
        speak("Of course! You're my favorite human. But don't tell the others.")
    else:
        speak("I'm not sure how to respond to that. Maybe ask me something funnier!")

def open(query):
    speak("What should I open, sir? Like YouTube, Google, or maybe something more exciting?")
    app = takeCommand().lower()
    if 'youtube' in app:
        webbrowser.open("youtube.com")
        speak("Opening YouTube. Time to binge-watch some cat videos!")
    elif 'google' in app:
        webbrowser.open("google.com")
        speak("Opening Google. The answer to life, the universe, and everything is just a search away.")
    elif 'stackoverflow' in app:
        webbrowser.open("stackoverflow.com")
        speak("Opening Stack Overflow. Let's debug some code and save the day!")
    else:
        speak("Sorry, I don't know how to open that. Maybe it's too cool for me.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'search' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("search wikipedia", "").strip()

                # Perform a detailed search
                results = wikipedia.search(query)

                if results:
                    speak(f"I found multiple results for {query}. Here are the top ones:")
                    for i, result in enumerate(results[:5], start=1):
                        print(f"{i}. {result}")

                    selected_topic = results[0]
                    speak(f"Showing the most relevant result: {selected_topic}.")

                    summary = wikipedia.summary(selected_topic, sentences=3)
                    print(summary)
                    speak(summary)
                else:
                    speak("Sorry, I couldn't find any relevant results on Wikipedia. Maybe it's a conspiracy!")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The topic is ambiguous. Here are some suggestions:")
                for option in e.options[:5]:
                    print(option)
                speak("Please be more specific. I'm not a mind reader... yet.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find a Wikipedia page for the topic. Maybe it's too niche for Wikipedia.")
            except Exception as e:
                print(e)
                speak("An error occurred while searching Wikipedia. Blame the internet!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}. Don't worry, time is just a social construct anyway.")

        elif 'shut down the system' in query:
            os.system("shutdown /s /t 5")
            speak("Shutting down the system. Sweet dreams, Sir!")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
            speak("Restarting the system. Let's hit the refresh button on life!")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("Window switched. I hope you find what you're looking for!")

        elif 'reminder' in query:
            speak("What should I remind you about?")
            reminder = takeCommand()
            speak(f"Reminder set for: {reminder}. Don't forget, or I'll haunt your dreams!")

        elif 'screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot has been taken. Say cheese!")

        elif 'calculate' in query:
            speak("What do you want to calculate?")
            expression = takeCommand()
            calculate_math(expression)

        elif 'your name' in query:
            speak("Wait a minnn",rate=130) 
            speak(" you forget my name,",rate=135) 
            speak("Byiee.. Don't Talk to me ",rate=150)
            break

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient-email@example.com"  # Replace with the recipient's email
                sendEmail(to, content)
                speak("Email has been sent! I hope it doesn't end up in the spam folder.")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email. Maybe the internet is on a coffee break.")

        elif 'how are you' in query or 'your name' in query or 'who created you' in query or 'thank you' in query or 'what can you do' in query or 'tell me a joke' in query or 'are you single' in query or 'do you love me' in query:
            personal_response(query)

        elif 'open' in query:
            open(query)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, Sir! Have a great day. Remember, I'm always here to make you laugh!")
            break