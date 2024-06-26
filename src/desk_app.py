from _thread import start_new_thread
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
import os

import time

import numpy as np
import cv2
from keras.preprocessing import image
from scipy.ndimage import rotate

root=Tk()
root.geometry('780x550+20+0')
import pymysql
# -----------------------------
# face expression recognizer initialization
from keras.models import model_from_json

model = model_from_json(open("model/facial_expression_model_structure.json", "r").read())
model.load_weights('model/facial_expression_model_weights.h5')  # load weights

# -----------------------------
con=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='autism')
cmd=con.cursor()
# lb = tk.Listbox(root)
# lb.pack()
flag=False
rec_emotions=[]
def ff():
   start_new_thread(ffplay, ())
   start_new_thread( detect_emotion(),())

def st():
    root.destroy()



def ffplay():
        global rec_emotions

    # if lb.curselection():
    #     file = lb.curselection()[0]
        import subprocess

        # This command could have multiple commands separated by a new line \n
        cmd.execute("SELECT file,id FROM questions ")
        s = cmd.fetchall()
        q = []
        global flag
        for i in s:
            flag=True
            print(i[0])
            some_command = "static\\ffmpeg\\bin\\ffplay.exe -autoexit static\\videos\\"+i[0]
            print(some_command)
            p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)

            # (output, err) = p.communicate()

            # This makes the wait possible
            p_status = p.wait()

            # This will give you the output of the command being executed
            print(        "Command output: " + str(""))
           # os.startfile("https://www.youtube.com/watch?v=3iEijtC4BrY")#lb.get(file))
           #  os.system(r"")
            flag=False
            pos_cnt=rec_emotions.count("happy")+rec_emotions.count("neutral")
            ratio=pos_cnt/len(rec_emotions)
            global stu
            print("stud==========",stu)
            print(i[1],ratio)
            print("INSERT INTO video_frame VALUES(null," + str(i[1]) + "," + str(ratio) + "," + str(stu) + ")")
            cmd.execute("INSERT INTO video_frame VALUES(null,"+str(i[1])+","+str(ratio)+","+str(stu)+")")
            con.commit()
            rec_emotions=[]
        cmd.execute("SELECT v_f_id,max(ratio),id FROM video_frame WHERE std_id=" + str(stu) + " AND ratio > 0.5")
        s = cmd.fetchone()
        print(s)
        cmd.execute("SELECT mat_type FROM questions WHERE id=" + str(s[2]))
        r=cmd.fetchone()
        print(r)
        lr = Label(root, text=r)
        lr.place(relx=0.50, rely=0.60)


def course():
    global stu
    cmd.execute("SELECT v_f_id,max(ratio) FROM video_frame WHERE std_id="+str(stu)+" AND ratio > 0.5")
    s = cmd.fetchone()
    print(s)


# for file in os.listdir():
#     if file.endswith(".mp4"):
#         lb.insert(0, file)

def detect_emotion():
    global rec_emotions
    face_cascade = cv2.CascadeClassifier('model/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)


    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    i=0
    global flag
    while(True):
     while(flag):
        ret, img = cap.read()

        # img = cv2.imread('../11.jpg')
        # cv2.imwrite(str(i)+".jpg",img)
        i=i+1

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #print(faces) #locations of detected faces
        emotion=None

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image

            detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis = 0)

            img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

            predictions = model.predict(img_pixels) #store probabilities of 7 expressions

            #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
            max_index = np.argmax(predictions[0])

            emotion = emotions[max_index]
            rec_emotions.append(emotion)
            print (emotion)
            time.sleep(5)

            # if cv2.waitKey(1):
        # cv2.imshow('img', img)

        # if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        #     break

        # kill open cv things
    cap.release()
    cv2.destroyAllWindows()
		# 	pass
	# return emotion
		#write emotion text above rectangle



def student_details():
    stud = MAPPING[box.get()]
    global stu
    stu=stud
    print("stud----------",stud)
    cmd.execute("SELECT `std_name`,`dob`,`place`,`gender`,`phone_no`,`description` FROM `student` WHERE student.std_id='"+str(stud)+"'")
    s=cmd.fetchone()
    print(s)
    l6 = Label(root, text="Student Name :")
    l6.place(relx=0.35, rely=0.35)
    l2 = Label(root, text=s[0])
    l2.place(relx=0.50, rely=0.35)
    l7 = Label(root, text="dob  :")
    l7.place(relx=0.35, rely=0.40)
    l3 = Label(root, text=s[1])
    l3.place(relx=0.50, rely=0.40)
    l8 = Label(root, text="Place  :")
    l8.place(relx=0.35, rely=0.45)
    l4 = Label(root, text=s[2])
    l4.place(relx=0.50, rely=0.45)
    l9 = Label(root, text="Gender  :")
    l9.place(relx=0.35, rely=0.50)
    l5 = Label(root, text=s[3])
    l5.place(relx=0.50, rely=0.50)
    l10 = Label(root, text="Phone No  :")
    l10.place(relx=0.35, rely=0.55)
    l11 = Label(root, text=s[4])
    l11.place(relx=0.50, rely=0.55)
    l10 = Label(root, text="Description  :")
    l10.place(relx=0.35, rely=0.60)
    l11 = Label(root, text=s[5])
    l11.place(relx=0.50, rely=0.60)



l1= Label(root,text="SELECT STUDENT")
l1.place(relx=0.20,rely=0.25)
cmd.execute("SELECT std_id,std_name FROM student ")
s = cmd.fetchall()

# combo1 = Combobox(root,value=s[1])
# combo1.place(relx=0.35,rely=0.25)
# combo1.current(1)

box_value = StringVar()
# mydict = {'A': 'Haha What', 'B': 'Lala Sorry', 'C': 'Ohoh OMG'}
cmd.execute("SELECT std_name FROM student ")
s = cmd.fetchall()
sname=[]
for i in s:
    sname.append(i[0])
mydict=sname
print("student-----",mydict)
cmd.execute("SELECT std_id FROM student ")
s2 = cmd.fetchall()
id=[]
for i in s2:
    id.append(i[0])
print("key-------",id)
MAPPING= dict(zip(mydict,id))
print("mappind------",MAPPING)
# print("haii-",hai)
# MAPPING = {'Item 1' : 1, 'Item 2' : 2, 'Item 3' : 3}
# box_values=list(mydict.values())
box = ttk.Combobox(root, textvariable=box_value, values=mydict, state='readonly')
box.current(0)
box.grid(column=9, row=0,padx=270,pady=140)

b1=Button(root,text="SHOW",command=student_details)
b1.place(relx=0.54,rely=0.25)
# bstart = ttk.Button(root, text="START")
b2=Button(root,text="START",command=ff)
b2.place(relx=0.35,rely=0.65)
import threading

t1=threading.Thread(target=ffplay)

# bstart.pack()
# lb.insert(0,"chrome.mp4")
# bstart.bind("<ButtonPress-1>", ff)
b3=Button(root,text="STOP",command=st)
b3.place(relx=0.45,rely=0.65)
root.mainloop()