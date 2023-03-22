import openai  # openai ke ;iye import karte hai 
import pyttsx3      # answer ko bolne ke liye import karte hai
engine = pyttsx3.init() 
voices = engine.getProperty('voices')     #uski voices ko get karte hai male and female
openai.api_key = "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"

while True:
    model = "text-davinci-003"  # engine hai jo question ko poochta hai
    user  = input('''Enter your question?
:- ''')   #user input
    print("Please wait...")
    completion = openai.Completion.create(
    model = "text-davinci-003",  #text format
    prompt = user,   # user input
    max_tokens = 1024,  # response length
    temperature = 0.5, # kitna accurate answer ho
    n = 1,
    stop = None
       )
    response  = completion.choices[0].text
    choice = int(input('''Press 1 to only show the Answer or Press 2 to show and hear the Answer
:- '''))
    if choice == 1:
        print(response)
    elif choice == 2:
        print(response)
        # for voice in voices:
        engine.setProperty('voice', voices[1].id)   # index 0 hone per male and index 1 hone per female ki voice aati hai
        engine.say(response)
        engine.runAndWait()
    else:
        print("Choose correct Choice")
    repeat = input('''Do you want to ask more question? 
:- ''')
    if repeat in ["no","NO","No"]:
        break