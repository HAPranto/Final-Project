#from command import *
import sys

from voice import *
from ctypes import resize
from  tkinter import *
import datetime
# from PIL import ImageTK,Image
from time import strftime
tk = Tk()
tk.title('Voice Based Desktop Assistant ')
tk.geometry("700x700")
#-----------Screen Height & Width------------
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

screen_centerx = screen_width / 2
screen_centery = screen_height / 2

tk.rowconfigure(0,weight=1)
tk.columnconfigure(0,weight=1)
# tk.state('zoomed')

# page_1 = Frame(tk)
# page_2 = Frame(tk)

# for frame in (page_1):
#     frame.grid(row = 0,column = 0, sticky = 'nsew')

# def show_frame(frame):
#     frame.tkraise()
    
# show_frame(page_1)

# frame.tkraise()

#------Page1-------
tk.config(background='blue')
Label01 = Label(tk,text='31.0 C',font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white')
Label01.place(x=20,y=100)

projectNameLabel = Label(tk, bg="black",font='Helvetica 22 bold', fg="white", text="Welcome on Desktop Voice Assisstant Home Page",  pady=12, width=82, height=1)
projectNameLabel.place(x = 20,y=20)

def time():
	string = strftime('%H:%M:%S %p')
	Label02.config(text = string)
	Label02.after(1000, time)

def commandForUser():
	userInput=commandBox.get("1.0","end-1c")
    #userInput = commandBox
	#print(userInput)
	return userInput

#userInput = ''
	#onlyText(userInput)


def onlyText():
    userInput = commandForUser()
    while True:
        #userInput = commandBox.get("1.0","end-1c")
        #print(userInput)
        #userInput=commandForUser()


        # Logic for executing tasks based on userInput
        if 'open google' in userInput:
            speak("sir, what should i search on google")
            cm = userInput.lower()
            webbrowser.open(f"{cm}")

        elif 'wikipedia' in userInput:
            speak('Searching Wikipedia...')
            userInput = userInput.replace("wikipedia", "")
            results = wikipedia.summary(userInput, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open calculator" in userInput:
            speak("ok sir.")
            subprocess.call("calc.exe")

        elif "close calculator" in userInput:
            speak("okay sir,closing calculator")
            os.system("taskkill /f /im Calculator.exe")

        elif "open notepad" in userInput:
            speak("ok sir, opening notepad.")
            subprocess.call("notepad.exe")

            # elif "close notepad" in userInput:
            #     speak("okay sir,closing notepad")
            #     time.sleep(3)
            #     pyautogui.leftClick(1160,218,1)
            #
        elif "close notepad" in userInput:
            speak("okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open cmd" in userInput:
            speak("ok sir, opening Command Prompt.")
            subprocess.call("cmd.exe")

        elif "close cmd" in userInput:
            speak("okay sir,closing Command Prompt")
            os.system("taskkill /f /im cmd.exe")

        elif 'play youtube' in userInput:
            speak("ok sir what shoud i play on youtube")
            cm = userInput.lower()
            kit.playonyt(f"{cm}")
            print(cm)

        elif 'play music' in userInput:
            music_dir = 'F:\\Arefin00'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(rd)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song bangla' in userInput:
            music_dir = 'F:\\Video Song\\Bangla Song'
            vbsongs = os.listdir(music_dir)
            print(vbsongs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song english' in userInput:
            music_dir = 'F:\\Video Song\\English Song'
            vesongs = os.listdir(music_dir)
            print(vesongs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'play video song hinde' in userInput:
            music_dir = 'F:\\Video Song\\Hinde Song'
            vhsongs = os.listdir(music_dir)
            print(vhsongs)
            os.startfile(os.path.join(music_dir, rd))
            # elif 'set alarm' in userInput:
            #     nn = int(datetime.datetime.now().hour)
            #     if nn == 22:
            #         music_dir = "F:\\Alarm"
            #         songs = os.listdir(music_dir)
            #         os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open stackoverflow' in userInput:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in userInput:
            webbrowser.open("facebook.com")

        elif 'open free codecamp' in userInput:
            webbrowser.open("free codecamo.org")

        elif 'open w3school' in userInput:
            webbrowser.open("w3school.com")

        elif 'open bangladesh rail' in userInput:
            webbrowser.open("eticket.railway.gov.bd")

        elif 'open geeks for geeks' in userInput:
            webbrowser.open("geeksforgeeks.org")

        elif 'open cricbuzz' in userInput:
            webbrowser.open("cricbuzz.com")

        elif 'open map' in userInput:
            webbrowser.open("maps.google.com")

        elif 'open translate' in userInput:
            webbrowser.open("translate.google.com")

        elif 'open chrome' in userInput:
            chromePath = "chrome.exe"
            os.startfile(chromePath)

            ############################################################################
        elif "close chrome" in userInput:
            speak("okay sir,closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'open brave' in userInput:
            bravePath = "brave.exe"
            os.startfile(bravePath)

        elif "close brave" in userInput:
            speak("okay sir,closing brave")
            os.system("taskkill /f /im brave.exe")

            # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif 'open pycharm' in userInput:
            pycharmPath = "pycharm64.exe"
            os.startfile(pycharmPath)

        elif "close pycharm" in userInput:
            speak("okay sir,closing pycharm")
            os.system("taskkill /f /im pycharm64.exe")

        elif 'open codeblocks' in userInput:
            codeblocksPath = "codeblocks.exe"
            os.startfile(codeblocksPath)

        elif "close code block" in userInput:
            speak("okay sir,closing code block")
            os.system("taskkill /f /im codeblocks.exe")

        elif 'open vs code' in userInput:
            vsCodePath = "Code.exe"
            os.startfile(vsCodePath)
        elif "close vs code" in userInput:
            speak("okay sir,closing vs code")
            os.system("taskkill /f /im Code.exe")

        elif "open camera" in userInput:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'where i am' in userInput or 'where we are' in userInput:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').txt
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo' + ipAdd + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state =geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to network issue i am not able to find where we are.")
                pass

            ############################################################
        elif 'read pdf' in userInput:
            pdf_reader()
        elif "IP address" in userInput:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            ############################################################
        elif 'do some calculations' in userInput or 'can you calculate' in userInput:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate, example: 3 plus 3")
                print("listening.....")
                my_string = userInput
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+': operator.add(),
                    '-': operator.sub(),
                    '*': operator.mul(),
                    '/': operator.__truediv__()
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            speak("Your result is : ")
            speak(eval_binary_expr(*(my_string.split())))

        elif "screenshot" in userInput or "take a screenshot" in userInput:
            speak("sir, please tall me the name for this screenshot file")
            name = userInput.lower()
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder, now im ready for next command.")
            #############################################################################################################
        elif 'tell me a joke' in userInput:
            joke = pyjokes.get_jokes()
            speak(joke)
        elif 'switch the window' in userInput:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            # Full screen size.-----------------
        elif "minimize the window" in userInput:
            speak("ok sir i will do this")
            pyautogui.leftClick(1247, 14, 1)
        elif "max the window" in userInput:
            speak("ok sir i will do this")
            pyautogui.leftClick(1247, 14, 1)
        elif "close the window" in userInput:
            speak("ok sir closeing the window")
            pyautogui.leftClick(1247, 14, 1)
# select,cut,copy,pest,undu,redu.----------------------------------------------
        elif "select this line" in userInput:
            time.sleep(3)
            pyautogui.tripleClick()

        elif "select this " in userInput:
            time.sleep(3)
            pyautogui.click()
            speak("ok sir selected")

        elif "select all" in userInput:
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'a')
            speak("ok sir selected all")

        elif "copy this file" or "copy this folder" or "copy this line" or "copy this" in userInput:
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'c')
            speak("Sir copy done.")

        elif "pest this file" or "pest this folder" or "pest this line" or "pest this" in userInput:
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'v')
            speak("Sir pest done.")

        elif "undu" in userInput:
            pyautogui.hotkey('ctrl', 'z')

        elif "redu" in userInput:
            pyautogui.hotkey('ctrl', 'y')

            # ---min
            # pyautogui.leftClick(1247,14,1)
            # ---Max
            # pyautogui.leftClick(1293,12,1)
            # ---close
            # pyautogui.leftClick(1341,14,1)
            # ---------------------------------------------------------------------------
        elif "tell me news" in userInput:
            speak("please wait sir, feteching the latest news")
            news()
            # ------------------sytdown,restart,sleep------------------------
        elif 'sut down the system' in userInput:
            os.system("shutdown /s /t 5")
        elif 'restart the system' in userInput:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in userInput:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            # -------------------------Exit----------------------------------------------------
        elif 'no thanks' in userInput or 'exit' in userInput:
            speak("thanks for using me sir, have a good day sir.")
            sys.exit()
        messageAreaBox.delete("1.0", "end-1c")
        speak("sir, do you have other work")
#..................................................................................................

#Design..................

Label02 = Label(tk,text = time,font=('Arial',15,'bold'),fg='blue',padx=14,pady=8,bg='white')
Label02.place(x = screen_width - 180,y=100)

time()

messageAreaBox = Text(tk, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 20, width=90)
messageAreaBox.place(x = 250,y=150)


commandBox = Text(tk, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 2, width=70)
commandBox.place(x = 250,y=screen_height-150)

sendBtn = Button(tk,text='Send',font=('Arial',15,'bold'),fg='blue',padx=15,pady=5,bg='white',command=onlyText)
sendBtn.place(x = screen_width - 505,y=screen_height-150)

speakBtn = Button(tk,text='Speak',font=('Arial',15,'bold'),fg='blue',padx=15,pady=5,bg='white',command=allVoice)
speakBtn.place(x = screen_width - 400,y=screen_height-150)



#------Page1 Picture in Center-------
# center_pic = Image.open('center1.png')
# center_pic = PhotoImage(file = 'center1.png')
# playbtn_pic = PhotoImage(file = 'playBtn1.png')
# wave_pic = PhotoImage(file = 'soundwave.png')

# picture_btn = Button(tk,image = center_pic,)
# picture_btn.place(x = screen_centerx - 270 , y = screen_centery - 250)

# next_btn = Button(page_1,text='Next',font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white', command=lambda: show_frame(page_2))
# next_btn.place(x = screen_width -300, y = screen_height - 140 )

#------Page2-------

# page_2.config(background='blue')
# lablePage_2 = Label(page_2, bg="blue",font='Helvetica 22 bold', fg="white", text="Welcome on Desktop Voice Assisstant Home Page",  pady=10, width=80, height=1)
# lablePage_2.grid(row=0)
 
# txtPage_2 = Text(page_2, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 31, width=138)
# txtPage_2.grid(row=1, column=0, columnspan=2)
 
# ePage_2 = Entry(page_2, bg="blue",font='Helvetica 18 bold', fg="white",width=75)
# ePage_2.grid(row=2, column=0)
 
# sendPage_2 = Button(page_2, text="Send",font='Helvetica 16 bold',  bg="blue",fg="white",width=6,).place(x=screen_width-200,y= screen_height - 120)
# MicrophoneBtnPage_2 = Button(page_2, text="Voice",font='Helvetica 16 bold',  bg="blue",fg="white",width=6,).place(x=screen_width-300,y= screen_height - 120)

#init()
wishMe()
tk.mainloop()

