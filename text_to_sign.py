import tkinter as tk
from tkinter import *
from tkinter import font

import cv2
import imageio
from PIL import Image, ImageTk


# from IPython.display import Image, display, Video


# Streaming Video
# --------------------------------------------------------------
#
# def stream(video, delay):
#     f1 = Frame()
#     l1 = Label(f1)
#     try:
#         image = video.get_next_data()
#         frame_image = Image.fromarray(image)
#         frame_image = ImageTk.PhotoImage(frame_image)
#         l1.config(image=frame_image)
#         l1.image = frame_image
#         l1.after(delay, lambda: stream())
#     except:
#         video.close()
#         return
#
#
# # Global Variables
# video_play = False
#
#
# def listToString(s):
#     str1 = ""
#     for ele in s:
#         str1 += ele
#     return str1
#
#
# def btn_start(text):
#     global video_play
#     print('Text is:', text)
#     new_clean_text = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in text.split("\n")]
#     new_clean_text_string = listToString(new_clean_text)
#     new_clean_text_string.lower()
#     print('New clean Text is:', new_clean_text)
#
#     img_array = []
#     for i in new_clean_text_string:
#         k = i + ".jpg"
#         img_array.append(k)
#
#     new_img_array = []
#     for filename in img_array:
#         img = cv2.imread(filename)
#         height, width, layers = img.shape
#         size = (width, height)
#         new_img_array.append(img)
#
#     # fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     # out = cv.VideoWriter('test.avi', fourcc, 60, (320, 240))
#     out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'XVID'), 1, (1440, 1080))
#
#     # out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 1, (1440, 1080))
#     for i in range(len(new_img_array)):
#         out.write(new_img_array[i])
#     out.release()
#     print('Video Done')
#
#     video_name = "project.avi"  # Image-path
#     video = imageio.get_reader(video_name)
#     delay = int(1000 / video.get_meta_data()['fps'])
#
#     l1 = Label()
#     l1.grid(row=3, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
#     try:
#         image = video.get_next_data()
#         frame_image = Image.fromarray(image)
#         frame_image = ImageTk.PhotoImage(frame_image)
#         l1.config(image=frame_image)
#         l1.image = frame_image
#         l1.after(delay, lambda: stream())
#     except:
#         video.close()
#         video_play = False
#         return
# --------------------------------------------------------------
# f1 = Frame()
# l1 = Label(f1)
# f1.grid(row=3, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
# l1.grid(row=3, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
# try:
#     image = video.get_next_data()
#     frame_image = Image.fromarray(image)
#     frame_image = ImageTk.PhotoImage(frame_image)
#     l1.config(image=frame_image)
#     l1.image = frame_image
#     l1.after(delay, lambda: stream())
# except:
#     video.close()
#     return

# stream(video, delay)

# my_label = tk.Label(self.root)
# my_label.grid(row=2, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)

# player = tkvideo("project.avi", my_label, loop=0, size=(1280, 720))
# player.play()

# player = tkvideo("project.avi", my_label, loop=0, size=(1280, 720))
# player.play()


# Application :


class application_ts:

    def __init__(self):
        global text, user_text, video_play
        self.root = tk.Tk()
        self.root.title("LinguaVox")
        #self.root.iconbitmap("logo.ico")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("600x650")
        self.root.resizable(False, False)

        for r in range(10):
            self.root.rowconfigure(r, weight=1)
        for c in range(8):
            self.root.columnconfigure(c, weight=1)

        self.T = tk.Label(self.root)
        self.T.place(x=60, y=5)
        self.T.config(text="Text Language To Sign Conversion", font=("Helvetica", 21, "bold"))
        Frame1 = tk.LabelFrame(self.root, text="Type Text", borderwidth=3)
        Frame1.grid(row=1, column=0, rowspan=1, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
        user_text = Entry(self.root, borderwidth=3, font="Helvetica 25")
        user_text.grid(sticky=W + E + S + N, row=1, column=0, rowspan=1, columnspan=8, padx=25, pady=50)

        myFont = font.Font(family='Helvetica', size=11, weight='bold')
        # Button(master, text=start_btn, width=12, command=start).grid(row=9, column=7, sticky=E + W + N, padx=10,
        #                                                              pady=10)

        Frame2 = tk.LabelFrame(self.root, text="Sign Video", borderwidth=3)
        Frame2.grid(row=2, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)

        Button(self.root, text='Convert', width=12, bg='#BDC3C7', fg='#000000', font=myFont,
               command=lambda: self.btn_start(user_text.get())).grid(row=1, column=7, sticky=E + W + S, padx=20,
                                                                     pady=17)

        # new_clean_text = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in text.split("\n")]
        #
        # def listToString(s):
        #     str1 = ""
        #     for ele in s:
        #         str1 += ele
        #     return str1
        #
        # new_clean_text_string = listToString(new_clean_text)
        # new_clean_text_string.lower()
        #
        # img_array = []
        # for i in new_clean_text_string:
        #     k = i + ".jpg"
        #     img_array.append(k)
        #
        # new_img_array = []
        # for filename in img_array:
        #     img = cv2.imread(filename)
        #     height, width, layers = img.shape
        #     size = (width, height)
        #     new_img_array.append(img)
        #
        # out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 1, (1440, 1080))
        # for i in range(len(new_img_array)):
        #     out.write(new_img_array[i])
        # out.release()

    def destructor(self):
        print("Closing Application...")

        self.root.destroy()

    # Streaming Video

    def stream(self, video, delay, l1):
        try:
            image = video.get_next_data()
            frame_image = Image.fromarray(image)
            frame_image = frame_image.resize((550, 450), Image.ANTIALIAS)
            frame_image = ImageTk.PhotoImage(frame_image)
            l1.config(image=frame_image)
            l1.image = frame_image
            l1.after(delay, lambda: self.stream(video, delay, l1))
        except:
            video.close()
            return

    def listToString(self, s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    def btn_start(self, text):
        global video_play
        print('Text is:', text)
        new_clean_text = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in text.split("\n")]
        new_clean_text_string = self.listToString(new_clean_text)
        new_clean_text_string.lower()
        print('New clean Text is:', new_clean_text)

        img_array = []
        for i in new_clean_text_string:
            if i == ' ':
                k = "space.jpg"
            else:
                k = i + ".jpg"
            img_array.append(k)

        new_img_array = []
        for filename in img_array:
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            new_img_array.append(img)

        out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'XVID'), 1, (1440, 1080))
        for i in range(len(new_img_array)):
            out.write(new_img_array[i])
        out.release()
        print('Video Done')
        self.play()

    def play(self):
        video_name = "project.avi"  # Image-path
        video = imageio.get_reader(video_name)

        delay = int(1000 / video.get_meta_data()['fps'])

        Frame2 = tk.LabelFrame(self.root, text="Sign Video", borderwidth=3)
        Frame2.grid(row=2, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
        l1 = Label(Frame2, text='hello')
        l1.grid(row=3, column=1, rowspan=7, columnspan=7, sticky=W + E + N + S, padx=10, pady=10)
        # Frame2.grid(row=2, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
        try:
            image = video.get_next_data()
            frame_image = Image.fromarray(image)
            frame_image = frame_image.resize((550, 450), Image.ANTIALIAS)
            frame_image = ImageTk.PhotoImage(frame_image)
            l1.config(image=frame_image)
            l1.image = frame_image
            l1.after(delay, lambda: self.stream(video, delay, l1))
        except Exception as e:
            print('In except: ', e)
            video.close()
            return

        # f1 = Frame()
        # l1 = Label(f1)
        # f1.grid(row=3, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
        # l1.grid(row=3, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)
        # try:
        #     image = video.get_next_data()
        #     frame_image = Image.fromarray(image)
        #     frame_image = ImageTk.PhotoImage(frame_image)
        #     l1.config(image=frame_image)
        #     l1.image = frame_image
        #     l1.after(delay, lambda: stream())
        # except:
        #     video.close()
        #     return

        # stream(video, delay)

        # my_label = tk.Label(self.root)
        # my_label.grid(row=2, column=0, rowspan=8, columnspan=8, sticky=W + E + N + S, padx=10, pady=10)

        # player = tkvideo("project.avi", my_label, loop=0, size=(1280, 720))
        # player.play()

        # player = tkvideo("project.avi", my_label, loop=0, size=(1280, 720))
        # player.play()

