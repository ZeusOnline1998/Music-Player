from tkinter import *
import random
from tkinter import messagebox
import os
import pygame
from tkinter.filedialog import *


root = Tk()
root.title("Music Player")

#Declare Variables

play_list=[]
track_index=0

pygame.mixer.init()


background_image=PhotoImage(file="Icons/pic.gif")


background_label = Label(root, image=background_image)

background_label.place(bordermode=OUTSIDE, x=0, y=0)

s=StringVar()
update_song=Label(root, textvariable=s, bg='lightgrey', fg='blue', width=60)
index=0

def What_is_this():
	messagebox.showinfo("About Us", "Music Player")

#Directory Function


def add_audio_file():
	audio_file = askopenfilename(filetypes=[('All supported', '.mp3 .wav'), ('.mp3 files', '.mp3'),('.wav files', '.wav')])
	if audio_file:
		file_path, file_name = os.path.split(audio_file)
		list_box.insert(END, file_name)
		play_list.append(audio_file)
		pygame.mixer.music.load(play_list[0])

def remove_selected_files():
	try:
		selected_indexes = list_box.curselection()
		for index in reversed(selected_indexes):
			list_box.delete(index)
			del play_list[index]
	except IndexError:
		pass
		
def get_all_audio_file_from_directory():
	directory=askdirectory()
	os.chdir(directory)
	for audio_file in os.listdir(directory):
		if audio_file.endswith(".mp3"):
			file_path, file_name = os.path.split(audio_file)
			list_box.insert(END, file_name)
			play_list.append(audio_file)
			pygame.mixer.music.load(play_list[0])
			
def empty_play_list():
	play_list.clear()
	list_box.delete(0, END)
	
#Music Function

def playsong():
	selected_indexes = int(list_box.curselection()[0])
	check = pygame.mixer.music.get_busy()
	if check == True:
		pygame.mixer.music.load(play_list[selected_indexes])
		pygame.mixer.music.play()
	elif selected_indexes:
		pygame.mixer.music.load(play_list[selected_indexes])
		pygame.mixer.music.play()
	else:
		pygame.mixer.music.unpause()
	s.set(play_list[selected_indexes])
        

def pausesong():
        pygame.mixer.music.pause()


def stopsong():
        pygame.mixer.music.stop()


def previoussong():
        global track_index
        track_index -= 1
        pygame.mixer.music.load(play_list[track_index])
        pygame.mixer.music.play()
        if play_list[track_index]==play_list[0]:
                track_index=-1
        updatesong()


def nextsong():
        global track_index
        track_index += 1
        pygame.mixer.music.load(play_list[track_index])
        pygame.mixer.music.play()
        if play_list[track_index]==play_list[-1]:
                track_index=0
        updatesong()

def volumemute():
        check = pygame.mixer.music.get_volume(0.0)
        if check==0.0:
                pygame.mixer.music.set_volume(1.0)
        else:
                pygame.mixer.music.set_volume(0.0)

def updatesong():
        global index
        global track_index
        s.set(play_list[track_index])


def quitplayer():
	root.destroy()
	pygame.mixer.quit()

def shuffle_play():
              random.shuffle(play_list)


#for searching
def search(event):
        global play_list
        data = str(e1.get())
        length = len(play_list)
        for i in range(0, length, 1):
            if data.lower() == play_list[i].lower():
                Listbox.selection_set(first=i)
                break
        else:
            messagebox.showinfo("message", "No result found")
e1 = Entry(root, bd=1, width=50)
e1.pack()
e1.bind("<Return>", search)
e1.place(x=50,y=120)

searchlabel = Label(root, text='Search', fg="yellow",bg='grey1',width=5)
searchlabel.pack()
searchlabel.place(x=5,y=120)

update_song=Label(root, textvariable=s, bg='lightgrey', fg='blue', width=60)


#Menu Function
#File Menu
menu=Menu(root)
root.config(menu=menu)

filesubMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=filesubMenu)

filesubMenu.add_command(label="Open File",command=add_audio_file)
filesubMenu.add_command(label="Open Folder",command=get_all_audio_file_from_directory)
filesubMenu.add_separator()
filesubMenu.add_command(label="Quit",command=quitplayer)


#Edit Menu

editsubMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editsubMenu)
editsubMenu.add_command(label="Play",command=playsong)
editsubMenu.add_command(label="Pause",command=pausesong)
editsubMenu.add_command(label="Stop",command=stopsong)

editsubMenu.add_separator()

editsubMenu.add_command(label="Previous",command=previoussong)
editsubMenu.add_command(label="Next",command=nextsong)


editsubMenu.add_separator()

#About Menu

aboutsubMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="About",menu=aboutsubMenu)
aboutsubMenu.add_command(label="Credits",command=What_is_this)

#GUI Panel 

playimg = PhotoImage(file="Icons/play.gif")

pauseimg = PhotoImage(file="Icons/pause.gif")

stopimg = PhotoImage(file="Icons/stop.gif")

nextimg = PhotoImage(file="Icons/next_track.gif")

previousimg = PhotoImage(file="Icons/previous_track.gif")

volmute = PhotoImage(file="Icons/mute.gif")

add_fileimg=PhotoImage(file="Icons/add_file.gif")

add_dirimg=PhotoImage(file="Icons/add_directory.gif")

clear_sel_pl_listimg=PhotoImage(file="Icons/clear_play_list.gif")

clear_pl_listimg=PhotoImage(file="Icons/clear_play_list.gif")

shuffle_img=PhotoImage(file="Icons/shuffle.gif")

list_box=Listbox(root, bg='lightcyan', width=85, height = 13)
list_box.place(x=5,y=140)

M_P_label = Label(root,text='Music Player',bg='black',fg='lightyellow',font=("times",15))
M_P_label.place(x=120,y=10)

update_song.place(x=5,y=40)

play = Button(root,image=playimg,command=playsong)
play.place(x=5,y=70)


pause = Button(root,image=pauseimg,command=pausesong)
pause.place(x=60,y=70)

stop = Button(root,image=stopimg,command=stopsong)
stop.place(x=120,y=70)

        
previous = Button(root, image=previousimg,command=previoussong)
previous.place(x=180,y=70)

next = Button(root,image=nextimg,command=nextsong)
next.place(x=240,y=70)


mute = Button(root,image=volmute,command=volumemute)
mute.place(x=300,y=70)

add_file_but=Button(root,image=add_fileimg,command=add_audio_file)
add_file_but.place(x=5,y=355)
add_file_lab = Label(root,text='add file',fg='lightcyan',bg='grey1')
add_file_lab.place(x=5,y=400)

add_dir_but=Button(root,image=add_dirimg,command=get_all_audio_file_from_directory)
add_dir_but.place(x=60,y=355)
add_dir_lab = Label(root,text='add dir',fg='lightcyan',bg='grey1')
add_dir_lab.place(x=60,y=400)

clear_sel_pl_list_but=Button(root,image=clear_pl_listimg,command=remove_selected_files)
clear_sel_pl_list_but.place(x=120,y=355)
clear_sel_lab = Label(root,text='delete',fg='lightcyan',bg='grey1')
clear_sel_lab.place(x=120,y=400)

clear_pl_list_but=Button(root,image=clear_pl_listimg,command=empty_play_list)
clear_pl_list_but.place(x=180,y=355)
clear_pl_lab = Label(root,text='delete all',fg='lightcyan',bg='grey1')
clear_pl_lab.place(x=180,y=400)

shuffle_but=Button(root,image=shuffle_img, command=shuffle_play)
shuffle_but.place(x=240,y=355)
shuffle_lab = Label(root,text='shuffle',fg='lightcyan',bg='grey1')
shuffle_lab.place(x=240,y=400)

root.minsize(width=350,height=430)
root.resizable(width=False, height=False)
root.mainloop()
