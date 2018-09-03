import tkinter
from tkinter import *
import os
import psutil
import random
import pickle

root = Tk()
root.title('')
root.configure(background="#424242")

entry = Entry(root, width = 25, fg="#ffffff", bg="#515151")
entry.pack(side = TOP,padx = 10,pady = 10)

def ok():
    if entry.get() == "t":
        t = Tk()
        t.title('Time Table')
        t.configure(background="#424242")
        Label(t, text="Period", fg="#ffffff", bg="#424242").grid(row=0, column=0)
        Label(t, text="1", fg="#ffffff", bg="#424242").grid(row=1, column=0)
        Label(t, text="2", fg="#ffffff", bg="#424242").grid(row=2, column=0)
        Label(t, text="3", fg="#ffffff", bg="#424242").grid(row=3, column=0)
        Label(t, text="4", fg="#ffffff", bg="#424242").grid(row=4, column=0)
        Label(t, text="5", fg="#ffffff", bg="#424242").grid(row=5, column=0)
        Label(t, text="6", fg="#ffffff", bg="#424242").grid(row=6, column=0)
        # Days
        Label(t, text="Monday", fg="#ffffff", bg="#424242").grid(row=0, column=1)
        Label(t, text="Tuesday", fg="#ffffff", bg="#424242").grid(row=0, column=2)
        Label(t, text="Wednesday", fg="#ffffff", bg="#424242").grid(row=0, column=3)
        Label(t, text="Thursday", fg="#ffffff", bg="#424242").grid(row=0, column=4)
        Label(t, text="Friday", fg="#ffffff", bg="#424242").grid(row=0, column=5)
        # Monday
        Label(t, text="Maths", fg="#ffffff", bg="#424242").grid(row=1, column=1)
        Label(t, text="English", fg="#ffffff", bg="#424242").grid(row=2, column=1)
        Label(t, text="Science", fg="#ffffff", bg="#424242").grid(row=3, column=1)
        Label(t, text="Home Ec.", fg="#ffffff", bg="#424242").grid(row=4, column=1)
        Label(t, text="Home Ec.", fg="#ffffff", bg="#424242").grid(row=5, column=1)
        Label(t, text="Maths", fg="#ffffff", bg="#424242").grid(row=6, column=1)
        # Tuesday
        Label(t, text="English", fg="#ffffff", bg="#424242").grid(row=1, column=2)
        Label(t, text="History", fg="#ffffff", bg="#424242").grid(row=2, column=2)
        Label(t, text="Maths", fg="#ffffff", bg="#424242").grid(row=3, column=2)
        Label(t, text="Business", fg="#ffffff", bg="#424242").grid(row=4, column=2)
        Label(t, text="History", fg="#ffffff", bg="#424242").grid(row=5, column=2)
        Label(t, text="HPE", fg="#ffffff", bg="#424242").grid(row=6, column=2)
        # Wednesday
        Label(t, text="Assembly", fg="#ffffff", bg="#424242").grid(row=1, column=3)
        Label(t, text="Maths", fg="#ffffff", bg="#424242").grid(row=2, column=3)
        Label(t, text="English", fg="#ffffff", bg="#424242").grid(row=3, column=3)
        Label(t, text="Business", fg="#ffffff", bg="#424242").grid(row=4, column=3)
        Label(t, text="Business", fg="#ffffff", bg="#424242").grid(row=5, column=3)
        Label(t, text="Home Ec.", fg="#ffffff", bg="#424242").grid(row=6, column=3)
        # Thursday
        Label(t, text="English", fg="#ffffff", bg="#424242").grid(row=1, column=4)
        Label(t, text="ICT", fg="#ffffff", bg="#424242").grid(row=2, column=4)
        Label(t, text="Science", fg="#ffffff", bg="#424242").grid(row=3, column=4)
        Label(t, text="Science", fg="#ffffff", bg="#424242").grid(row=4, column=4)
        Label(t, text="HPE", fg="#ffffff", bg="#424242").grid(row=5, column=4)
        Label(t, text="English", fg="#ffffff", bg="#424242").grid(row=6, column=4)
        # Friday
        Label(t, text="Life Skills", fg="#ffffff", bg="#424242").grid(row=1, column=5)
        Label(t, text="Maths", fg="#ffffff", bg="#424242").grid(row=2, column=5)
        Label(t, text="ICT", fg="#ffffff", bg="#424242").grid(row=3, column=5)
        Label(t, text="Geography", fg="#ffffff", bg="#424242").grid(row=4, column=5)
        Label(t, text="Geography", fg="#ffffff", bg="#424242").grid(row=5, column=5)
        Label(t, text="ICT", fg="#ffffff", bg="#424242").grid(row=6, column=5)
        mainloop()
    if entry.get() == "cmd":
        os.system('start cmd.exe')
    if entry.get() == "calc":
        os.system('start calc.exe')
    if entry.get() == "edge":
        os.system("start microsoft-edge:")
    if entry.get() == "hdd":
        t = Tk()
        t.title("Storage")
        t.configure(background="#424242")
        obj_Disk = psutil.disk_usage('/')
        Label(t, text="---------------------------------------------", fg="#424242", bg="#424242").grid(row=0)
        Label(t, text=("Total Disk Space: ", obj_Disk.total / (1024.0 ** 3)), fg="#ffffff", bg="#424242").grid(row=1)
        Label(t, text=("Disk Space Used: ", obj_Disk.used / (1024.0 ** 3)), fg="#ffffff", bg="#424242").grid(row=2)
        Label(t, text=("Disk Space Free: ", obj_Disk.free / (1024.0 ** 3)), fg="#ffffff", bg="#424242").grid(row=3)
        Label(t, text=("Disk Percenatge: ", obj_Disk.percent), fg="#ffffff", bg="#424242").grid(row=4)
        Button(t, text = "Refresh", command = ok, fg="#ffffff", bg="#515151").grid(row=5)
        Label(t, text="---------------------------------------------", fg="#424242", bg="#424242").grid(row=6)
        mainloop()
    if entry.get() == "rand":
        def roll():
           roll_num = random.randint(1,6)
           Label(t, text=roll_num, fg="#ffffff", bg="#424242").grid(row=1, column=6)
        def flip():
            flip_num = random.randint(1,2)
            if flip_num == 1:
                outcome = "Heads"
            else:
                outcome = "Tails"
            Label(t, text=outcome, fg="#ffffff", bg="#424242").grid(row=2, column=6)
        t = Tk()
        t.title("Random")
        t.configure(background="#424242")
        Button(t, text = "Roll = ", command = roll, fg="#ffffff", bg="#515151").grid(row = 1)
        Button(t, text = "Flip = ", command = flip, fg="#ffffff", bg="#515151").grid(row = 2)
    if entry.get() == "case":
        t = Tk()
        t.title("CS:GO Case Opening")
        t.geometry("300x105")
        t.configure(background="#424242")
        hydra_case = ['USP-S | Blueprint', 'FAMAS | Macabre', 'M4A1-S | Briefing',
                      'MAC-10 | Aloha', 'MAG-7 | Hard Water', 'Tec-9 | Cut Out',
                      'UMP-45 | Metal Flowers', 'AK-47 | Orbit Mk01', 'P2000 | Woodsman',
                      'P250 | Red Rock', 'P90 | Death Grip', 'SSG 08 | Deaths Head',
                      'Dual Berettas | Cobra Strike', 'Galil AR | Sugar Rush',
                      'M4A4 | Hellfire', 'Five-SeveN | Hyper Beast', 'AWP | Oni Taiji']

        spectrum_case = ['PP-Bizon | Jungle Slipstream', 'SCAR-20 | Blueprint',
                         'Desert Eagle | Oxide Blaze','Five-SeveN | Capillary', 'MP7 | Akoben',
                         'P250 | Ripple', 'Sawed-Off | Zander', 'Galil AR | Crimson Tsunami',
                         'M249 | Emerald Poison Dart', 'MAC-10 | Last Dive', 'UMP-45 | Scaffold',
                         'XM1014 | Seasons', 'AWP | Fever Dream', 'CZ75-Auto | Xiangliu',
                         'M4A1-S | Decimator', 'AK-47 | Bloodsport', 'USP-S | Neo-Noir']

        glove_case = ['CZ75-Auto | Polymer', 'Glock-18 | Ironwork', 'MP7 | Cirrus', 'Galil AR | Black Sand',
                      'MP9 | Sand Scale', 'MP9 | Sonar', 'MAG-7 | Sonar', 'P2000 | Turf', 'Bual Berettas | Royal Consorts',
                      'G3SG1 | Stinger', 'M4A1-S | Flashback', 'Nova | Gila', 'USP-S | Cyrex',
                      'FAMAS | Mecha Industries', 'P90 | Shallow Grave', 'Sawed Off | Wasteland Princess',
                      'SSG 08 | Dragonfire', 'M4A4 | Buzz Kill']

        def open_hydra_case():
            Label(t, text="______________________________", fg="#424242", bg="#424242").grid(row=1, column=5)
            hydra_case_weapon = random.randint(0, 16)
            if hydra_case_weapon == 0:
                Label(t, text=hydra_case[0], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 1:
                Label(t, text=hydra_case[1], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 2:
                Label(t, text=hydra_case[2], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 3:
                Label(t, text=hydra_case[3], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 4:
                Label(t, text=hydra_case[4], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 5:
                Label(t, text=hydra_case[5], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 6:
                Label(t, text=hydra_case[6], fg="#4B69FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 7:
                Label(t, text=hydra_case[7], fg="#8847FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 8:
                Label(t, text=hydra_case[8], fg="#8847FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 9:
                Label(t, text=hydra_case[9], fg="#8847FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 10:
                Label(t, text=hydra_case[10], fg="#8847FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 11:
                Label(t, text=hydra_case[11], fg="#8847FF", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 12:
                Label(t, text=hydra_case[12], fg="#D32CE6", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 13:
                Label(t, text=hydra_case[13], fg="#D32CE6", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 14:
                Label(t, text=hydra_case[14], fg="#D32CE6", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 15:
                Label(t, text=hydra_case[15], fg="#EB4B4B", bg="#424242").grid(row=1, column=5)
            if hydra_case_weapon == 16:
                Label(t, text=hydra_case[16], fg="#EB4B4B", bg="#424242").grid(row=1, column=5)

        def open_spectrum_case():
            Label(t, text="______________________________", fg="#424242", bg="#424242").grid(row=2, column=5)
            hydra_case_weapon = random.randint(0, 16)
            if hydra_case_weapon == 0:
                Label(t, text=spectrum_case[0], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 1:
                Label(t, text=spectrum_case[1], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 2:
                Label(t, text=spectrum_case[2], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 3:
                Label(t, text=spectrum_case[3], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 4:
                Label(t, text=spectrum_case[4], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 5:
                Label(t, text=spectrum_case[5], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 6:
                Label(t, text=spectrum_case[6], fg="#4B69FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 7:
                Label(t, text=spectrum_case[7], fg="#8847FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 8:
                Label(t, text=spectrum_case[8], fg="#8847FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 9:
                Label(t, text=spectrum_case[9], fg="#8847FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 10:
                Label(t, text=spectrum_case[10], fg="#8847FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 11:
                Label(t, text=spectrum_case[11], fg="#8847FF", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 12:
                Label(t, text=spectrum_case[12], fg="#D32CE6", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 13:
                Label(t, text=spectrum_case[13], fg="#D32CE6", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 14:
                Label(t, text=spectrum_case[14], fg="#D32CE6", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 15:
                Label(t, text=spectrum_case[15], fg="#EB4B4B", bg="#424242").grid(row=2, column=5)
            if hydra_case_weapon == 16:
                Label(t, text=spectrum_case[16], fg="#EB4B4B", bg="#424242").grid(row=2, column=5)

        def open_glove_case():
            Label(t, text="________________________________", fg="#424242", bg="#424242").grid(row=3, column=5)
            hydra_case_weapon = random.randint(0, 16)
            if hydra_case_weapon == 0:
                Label(t, text=glove_case[0], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 1:
                Label(t, text=glove_case[1], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 2:
                Label(t, text=glove_case[2], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 3:
                Label(t, text=glove_case[3], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 4:
                Label(t, text=glove_case[4], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 5:
                Label(t, text=glove_case[5], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 6:
                Label(t, text=glove_case[6], fg="#4B69FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 7:
                Label(t, text=glove_case[7], fg="#8847FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 8:
                Label(t, text=glove_case[8], fg="#8847FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 9:
                Label(t, text=glove_case[9], fg="#8847FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 10:
                Label(t, text=glove_case[10], fg="#8847FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 11:
                Label(t, text=glove_case[11], fg="#8847FF", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 12:
                Label(t, text=glove_case[12], fg="#D32CE6", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 13:
                Label(t, text=glove_case[13], fg="#D32CE6", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 14:
                Label(t, text=glove_case[14], fg="#D32CE6", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 15:
                Label(t, text=glove_case[15], fg="#EB4B4B", bg="#424242").grid(row=3, column=5)
            if hydra_case_weapon == 16:
                Label(t, text=glove_case[16], fg="#EB4B4B", bg="#424242").grid(row=3, column=5)

        def reset():
            Label(t, text="________________________________", fg="#424242", bg="#424242").grid(row=1, column=5)
            Label(t, text="________________________________", fg="#424242", bg="#424242").grid(row=2, column=5)
            Label(t, text="________________________________", fg="#424242", bg="#424242").grid(row=3, column=5)
            Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=1, column=5)
            Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=2, column=5)
            Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=3, column=5)

        Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=1, column=5)
        Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=2, column=5)
        Label(t, text="Case Unopened", fg="#ffffff", bg="#424242").grid(row=3, column=5)
        Button(t, text ="Open Hydra Case", command=open_hydra_case, fg="#ffffff", bg="#515151").grid(row=1)
        Button(t, text="Open Spectrum Case", command=open_spectrum_case, fg="#ffffff", bg="#515151").grid(row=2)
        Button(t, text="Open Glove Case", command=open_glove_case, fg="#ffffff", bg="#515151").grid(row=3)
        Button(t, text="Reset", command=reset, fg="#ffffff", bg="#515151").grid(row=4, column=0)
        mainloop()

    if entry.get() == "a":
        t = Tk()
        t.title("Assessment Calender")
        S = Scrollbar(t)
        T = Text(t, height=30, width=130, fg="#ffffff", bg="#424242")
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        assessment = '''
        ________________________________________________________________________________________________________________
        Week 1: Pupil Free Day
        Monday:
        Tuesday:
        Wednesday:
        Thursday:
        Friday: Athletics Carnival
        ________________________________________________________________________________________________________________
        Week 2:
        Monday:
        Tuesday:
        Wednesday:
        Thursday:
        Friday:
        ________________________________________________________________________________________________________________
        Week 3:
        Monday:
        Tuesday:
        Wednesday: Food Tech: Task 1 Absorption Of Iron -- Document Due
        Thursday:
        Friday:
        ________________________________________________________________________________________________________________
        Week 4:
        Monday:
        Tuesday:
        Wednesday:
        Thursday:
        Friday:
        ________________________________________________________________________________________________________________
        Week 5:
        Monday:
        Tuesday:
        Wednesday: Business Standards of Living Test P4 - 5
        Thursday:
        Friday:
        ________________________________________________________________________________________________________________
        Week 6:
        Monday:
        Tuesday:
        Wednesday:
        Thursday:
        Friday: History Test and Stimulus Response P4 - 5
        ________________________________________________________________________________________________________________
        Week 7:
        Monday:
        Tuesday:
        Wednesday: English: Essay Exam, Food Tech: Recipe Journals Due
        Thursday:
        Friday:
        ________________________________________________________________________________________________________________
        Week 8:
        Monday:
        Tuesday:
        Wednesday:
        Thursday:
        Friday: Noosa Show Day
        ________________________________________________________________________________________________________________
        Week 9:
        Monday:
        Tuesday:
        Wednesday:
        Thursday: Science Chemistry Exam
        Friday: Digital Technology EV3 Robotics
        ________________________________________________________________________________________________________________
        Week 10:
        Monday: English: Romeo and Juliet Performance, Food Tech: Group Video Presentation Due, Math: Math Exam
        Tuesday: Geography Report and Multi-Modal Presentation P2 and P5
        Wednesday: Business Economics Report Due
        Thursday:Science Chemistry Lab Journal
        Friday: History Multi-Modal Presentation P4 - 5
        ________________________________________________________________________________________________________________
        '''
        T.insert(END, assessment)
        mainloop()

    if entry.get() == "d":
        t = Tk()
        t.title("Diary")
        t.configure(background="#424242")
        def save():
            f = open(file_name.get(), 'wb')
            pickle.dump(diary_entry.get(), f)
            f.close()
        def load():
            f = open(load_file_name.get(), 'rb')
            diary = pickle.load(f)
            f.close()
            t = Tk()
            t.title("Diary Entry")
            t.configure(background="#424242")
            Label(t, text=diary, fg="#ffffff", bg="#424242").pack(side=TOP)
            mainloop()

        Label(t, text="File Name(Put .pckl on the end of the file name):", fg="#ffffff", bg="#424242").pack(side=TOP)
        file_name = Entry(t, width=50, fg="#ffffff", bg="#515151")
        file_name.pack(side=TOP, padx=10, pady=2)
        Label(t, text="Diary Entry:", fg="#ffffff", bg="#424242").pack(side=TOP)
        diary_entry = Entry(t, width=50, fg="#ffffff", bg="#515151")
        diary_entry.pack(side=TOP, padx=10, pady=5)
        Button(t, text='Save Entry', command=save, fg="#ffffff", bg="#515151").pack(side=LEFT)
        Button(t, text='Load Entry:', command=load, fg="#ffffff", bg="#515151").pack(side=LEFT)
        load_file_name = Entry(t, width=35, fg="#ffffff", bg="#515151")
        load_file_name.pack(side=LEFT, padx=5)

        mainloop()

    if entry.get() == "patch":
        t = Tk()
        t.title("Patch Notes")
        t.configure(background="#424242")
        Label(t, text="Version 1.2 Update Patch Notes:", fg="#ffffff", bg="#424242").pack(side=TOP)
        Label(t, text="-Added Diary function, type d to access it.", fg="#ffffff", bg="#424242").pack(side=TOP)
        mainloop()

def info():
    t = Tk()
    t.title('Info')
    t.configure(background="#424242")
    Label(t, text="---------------------------------------------", fg="#424242", bg="#424242").grid(row=0)
    Label(t, text="Powered With TKinter", fg="#ffffff", bg="#424242").grid(row=1)
    Label(t, text="And Python", fg="#ffffff", bg="#424242").grid(row=2)
    Label(t, text="", fg="#ffffff", bg="#424242").grid(row=3)
    Label(t, text="By Tobey Gronow", fg="#ffffff", bg="#424242").grid(row=4)
    Label(t, text="", fg="#ffffff", bg="#424242").grid(row=5)
    Label(t, text="Version 1.2", fg="#ffffff", bg="#424242").grid(row=6)
    Label(t, text="---------------------------------------------", fg="#424242", bg="#424242").grid(row=7)
    mainloop()

Button(root, text = 'OK', command = ok, fg="#ffffff", bg="#515151").pack(side = LEFT)
Button(root, text = 'INFO', command = info, fg="#ffffff", bg="#515151").pack(side = LEFT)
mainloop()
