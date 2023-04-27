from tkinter import *
from PIL import ImageTk
import random
import os
from fpdf import FPDF
root = Tk()
root.state("zoomed")
root.title("JKKNIU Student's Seat Plan")
root.iconbitmap('D:/Python code/Jatiya_Kabi_Kazi_Nazrul_Islam_University_Logo (1).ico')
bg = ImageTk.PhotoImage(file="IMG_4658.jpg")
limg = Label(root, i=bg)
limg.pack()
bg2 = ImageTk.PhotoImage(file="Capture5-removebg-preview.png")
limg2 = Label(root, i=bg2)
limg2.place(x=745, y=100, anchor=CENTER)
bg1 = ImageTk.PhotoImage(file="rsz_jatiya_kabi_kazi_nazrul_islam_university_logo.png")
limg1 = Label(root, i=bg1)
limg1.place(x=725, y=200, anchor=CENTER)
mylabel = Label(root, text="Enter the first roll:", fg="Black")
mylabel.pack()
mylabel.place(x=431, y=365)
e1 = Entry(root, width=63)
e1.pack()
e1.place(relx=0.5, rely=0.5, anchor=CENTER)
mylabel = Label(root, text="Enter the last roll:", fg="Black")
mylabel.pack()
mylabel.place(x=431, y=420)
e2 = Entry(root, width=63)
e2.pack()
e2.place(relx=0.5, rely=0.57, anchor=CENTER)
def te(a,folder,m,x,o):
    if a<rt:
        c = []
        for i in range(a, a + o):
            if (i > rt):
                break
            c.append(i)
        random.shuffle(c)
        if os.path.exists(f"{folder}.txt"):
            os.remove(f"{folder}.txt")
        if os.path.exists(f"{folder}.pdf"):
            os.remove(f"{folder}.pdf")
        f = open(f"{folder}.txt", "w")
        c1 = 0
        n = m.center(100)
        print("\n" + n + "\n", file=f)
        y = x.center(100)
        print("\n" + y + "\n", file=f)
        for i in c:
            print("|", i, "|   ", end="", file=f)
            c1 = c1 + 1
            if (c1 == 6):
                print("\n", file=f)
                c1 = 0
        f.close()
        f = open(f"{folder}.txt", "r")
        pdf = FPDF()
        pdf.add_page()
        pdf.image('jkkniu.png', w=190)
        pdf.set_font("Times", size=15)
        for i in f:
            pdf.cell(200, 10, txt=i, ln=1, align='C')
        pdf.output(f"{m}-{folder}.pdf")
        f.close()
        os.remove(folder + ".txt")
def show():
    a = e1.get()
    b = e2.get()
    if a.isdigit() == False or b.isdigit()==False:
        mylabel = Label(root, text="Invalid Input!", fg="Red")
        mylabel.pack()
        mylabel.place(x=720, y=550,anchor=S)
    else:
        global rf
        rf = int(a)
        global rt
        rt = int(b)
        if(rf<rt):
            # 106
            folder = "106"
            o = 40
            m = "Science Building"
            x = "Room no. 106"
            te(rf, folder, m, x, o)
            # 107
            b107 = rf + 40
            o = 63
            folder = "107"
            m = "Science Building"
            x = "Room no. 107"
            te(b107, folder, m, x, o)
            # 108
            b108 = b107 + 63
            o = 63
            folder = "108"
            m = "Science Building"
            x = "Room no. 108"
            te(b108, folder, m, x, o)
            # 301
            b301 = b108 + 63
            o = 63
            folder = "301"
            m = "Science Building"
            x = "Room no. 301"
            te(b301, folder, m, x, o)
            # 302
            b302 = b301 + 63
            o = 63
            folder = "302"
            m = "Science Building"
            x = "Room no. 302"
            te(b302, folder, m, x, o)
            # 303
            b303 = b302 + 63
            o = 63
            folder = "303"
            m = "Science Building"
            x = "Room no. 303"
            te(b303, folder, m, x, o)
            # 304
            b304 = b303 + 63
            o = 63
            folder = "304"
            m = "Science Building"
            x = "Room no. 304"
            te(b304, folder, m, x, o)
            # 310
            b310 = b304 + 63
            o = 63
            folder = "310"
            m = "Science Building"
            x = "Room no. 310"
            te(b310, folder, m, x, o)
            # 418
            b418 = b310 + 63
            o = 63
            folder = "418"
            m = "Science Building"
            x = "Room no. 418"
            te(b418, folder, m, x, o)
            # 505
            b505 = b418 + 63
            o = 63
            folder = "505"
            m = "Science Building"
            x = "Room no. 303"
            te(b505, folder, m, x, o)
            # 512
            b512 = b505 + 63
            o = 63
            folder = "512"
            m = "Science Building"
            x = "Room no. 512"
            te(b512, folder, m, x, o)
            # 513
            b513 = b512 + 63
            o = 63
            folder = "513"
            m = "Science Building"
            x = "Room no. 513"
            te(b513, folder, m, x, o)
            # 515
            b515 = b513 + 63
            o = 63
            folder = "515"
            m = "Science Building"
            x = "Room no. 515"
            te(b515, folder, m, x, o)
            # 209
            ab209 = b515 + 63
            o = 63
            folder = "209"
            m = "Arts Building"
            x = "Room no. 209"
            te(ab209, folder, m, x, o)
            # 213
            ab213 = ab209 + 63
            o = 63
            folder = "213"
            m = "Arts Building"
            x = "Room no. 213"
            te(ab213, folder, m, x, o)
            # 214
            ab214 = ab213 + 63
            o = 63
            folder = "214"
            m = "Arts Building"
            x = "Room no. 214"
            te(ab214, folder, m, x, o)
            # 215
            ab215 = ab214 + 63
            o = 63
            folder = "215"
            m = "Arts Building"
            x = "Room no. 215"
            te(ab215, folder, m, x, o)
            # 306
            ab306 = ab215 + 63
            o = 48
            folder = "306"
            m = "Arts Building"
            x = "Room no. 306"
            te(ab306, folder, m, x, o)
            # 310
            ab310 = ab306 + 48
            o = 63
            folder = "310"
            m = "Arts Building"
            x = "Room no. 310"
            te(ab209, folder, m, x, o)
            # 415
            ab415 = ab310 + 63
            o = 63
            folder = "415"
            m = "Arts Building"
            x = "Room no. 415"
            te(ab415, folder, m, x, o)
            # 416
            ab416 = ab415 + 63
            o = 63
            folder = "416"
            m = "Arts Building"
            x = "Room no. 416"
            te(ab416, folder, m, x, o)
            # 417
            ab417 = ab416 + 63
            o = 63
            folder = "417"
            m = "Arts Building"
            x = "Room no. 417"
            te(ab417, folder, m, x, o)
            # 418
            ab418 = ab417 + 63
            o = 63
            folder = "418"
            m = "Arts Building"
            x = "Room no. 418"
            te(ab418, folder, m, x, o)
            # 511
            ab511 = ab418 + 63
            o = 40
            folder = "511"
            m = "Arts Building"
            x = "Room no. 511"
            te(ab511, folder, m, x, o)
            # 517
            ab517 = ab511 + 40
            o = 63
            folder = "517"
            m = "Arts Building"
            x = "Room no. 517"
            te(ab517, folder, m, x, o)
            # 101
            fba101 = ab517 + 63
            o = 63
            folder = "101"
            m = "Faculty of Business Administration Building"
            x = "Room no. 101"
            te(fba101, folder, m, x, o)
            # 102
            fba102 = fba101 + 63
            o = 63
            folder = "102"
            m = "Faculty of Business Administration Building"
            x = "Room no. 102"
            te(fba102, folder, m, x, o)
            # 103
            fba103 = fba102 + 63
            o = 63
            folder = "103"
            m = "Faculty of Business Administration Building"
            x = "Room no. 103"
            te(fba103, folder, m, x, o)
            # 104
            fba104 = fba103 + 63
            o = 63
            folder = "104"
            m = "Faculty of Business Administration Building"
            x = "Room no. 104"
            te(fba104, folder, m, x, o)
            # 105
            fba105 = fba104 + 63
            o = 63
            folder = "105"
            m = "Faculty of Business Administration Building"
            x = "Room no. 105"
            te(fba105, folder, m, x, o)
            # 205
            fba205 = fba105 + 63
            o = 63
            folder = "205"
            m = "Faculty of Business Administration Building"
            x = "Room no. 205"
            te(fba205, folder, m, x, o)
            # 207
            fba207 = fba205 + 63
            o = 63
            folder = "207"
            m = "Faculty of Business Administration Building"
            x = "Room no. 207"
            te(fba207, folder, m, x, o)
            # 208
            fba208 = fba207 + 63
            o = 63
            folder = "208"
            m = "Faculty of Business Administration Building"
            x = "Room no. 208"
            te(fba208, folder, m, x, o)
            # 209
            fba209 = fba208 + 63
            o = 63
            folder = "209"
            m = "Faculty of Business Administration Building"
            x = "Room no. 209"
            te(fba209, folder, m, x, o)
            # 301
            fba301 = fba209 + 63
            o = 63
            folder = "301"
            m = "Faculty of Business Administration Building"
            x = "Room no. 301"
            te(fba301, folder, m, x, o)
            # 302
            fba302 = fba301 + 63
            o = 63
            folder = "302"
            m = "Faculty of Business Administration Building"
            x = "Room no. 302"
            te(fba302, folder, m, x, o)
            # 303
            fba303 = fba302 + 63
            o = 63
            folder = "303"
            m = "Faculty of Business Administration Building"
            x = "Room no. 303"
            te(fba303, folder, m, x, o)
            # 304
            fba304 = fba303 + 63
            o = 63
            folder = "304"
            m = "Faculty of Business Administration Building"
            x = "Room no. 304"
            te(fba304, folder, m, x, o)
            # 305
            fba305 = fba304 + 63
            o = 63
            folder = "305"
            m = "Faculty of Business Administration Building"
            x = "Room no. 305"
            te(fba305, folder, m, x, o)
            # 401
            fba401 = fba305 + 63
            o = 63
            folder = "401"
            m = "Faculty of Business Administration Building"
            x = "Room no. 401"
            te(fba401, folder, m, x, o)
            # 402
            fba402 = fba401 + 63
            o = 63
            folder = "402"
            m = "Faculty of Business Administration Building"
            x = "Room no. 402"
            te(fba402, folder, m, x, o)
            # 403
            fba403 = fba402 + 63
            o = 63
            folder = "403"
            m = "Faculty of Business Administration Building"
            x = "Room no. 403"
            te(fba403, folder, m, x, o)
            # 404
            fba404 = fba403 + 63
            o = 63
            folder = "404"
            m = "Faculty of Business Administration Building"
            x = "Room no. 404"
            te(fba404, folder, m, x, o)
            # 405
            fba405 = fba404 + 63
            o = 63
            folder = "405"
            m = "Faculty of Business Administration Building"
            x = "Room no. 405"
            te(fba405, folder, m, x, o)
            # 406
            fba406 = fba405 + 63
            o = 63
            folder = "406"
            m = "Faculty of Business Administration Building"
            x = "Room no. 406"
            te(fba406, folder, m, x, o)
            # 501
            fba501 = fba406 + 63
            o = 63
            folder = "501"
            m = "Faculty of Business Administration Building"
            x = "Room no. 501"
            te(fba501, folder, m, x, o)
            # 502
            fba502 = fba501 + 63
            o = 63
            folder = "502"
            m = "Faculty of Business Administration Building"
            x = "Room no. 502"
            te(fba502, folder, m, x, o)
            # 503
            fba503 = fba502 + 63
            o = 63
            folder = "503"
            m = "Faculty of Business Administration Building"
            x = "Room no. 503"
            te(fba503, folder, m, x, o)
            # 504
            fba504 = fba503 + 63
            o = 63
            folder = "504"
            m = "Faculty of Business Administration Building"
            x = "Room no. 504"
            te(fba504, folder, m, x, o)
            # 505
            fba505 = fba504 + 63
            o = 63
            folder = "504"
            m = "Faculty of Business Administration Building"
            x = "Room no. 504"
            te(fba505, folder, m, x, o)
            # 506
            fba506 = fba505 + 63
            o = 63
            folder = "506"
            m = "Faculty of Business Administration Building"
            x = "Room no. 506"
            te(fba506, folder, m, x, o)
            # 601
            fba601 = fba506 + 63
            o = 63
            folder = "601"
            m = "Faculty of Business Administration Building"
            x = "Room no. 601"
            te(fba601, folder, m, x, o)
            # 602
            fba602 = fba601 + 63
            o = 63
            folder = "602"
            m = "Faculty of Business Administration Building"
            x = "Room no. 602"
            te(fba602, folder, m, x, o)
            # 603
            fba603 = fba602 + 63
            o = 63
            folder = "603"
            m = "Faculty of Business Administration Building"
            x = "Room no. 603"
            te(fba603, folder, m, x, o)
            # 604
            fba604 = fba603 + 63
            o = 63
            folder = "604"
            m = "Faculty of Business Administration Building"
            x = "Room no. 604"
            te(fba604, folder, m, x, o)
            # 605
            fba605 = fba604 + 63
            o = 63
            folder = "605"
            m = "Faculty of Business Administration Building"
            x = "Room no. 605"
            te(fba605, folder, m, x, o)
            # 606
            fba606 = fba605 + 63
            o = 63
            folder = "606"
            m = "Faculty of Business Administration Building"
            x = "Room no. 606"
            te(fba606, folder, m, x, o)
            # 607
            fba607 = fba606 + 63
            o = 63
            folder = "607"
            m = "Faculty of Business Administration Building"
            x = "Room no. 607"
            te(fba607, folder, m, x, o)
            # 701
            fba701 = fba607 + 63
            o = 63
            folder = "701"
            m = "Faculty of Business Administration Building"
            x = "Room no. 701"
            te(fba701, folder, m, x, o)
            # 702
            fba702 = fba701 + 63
            o = 63
            folder = "702"
            m = "Faculty of Business Administration Building"
            x = "Room no. 702"
            te(fba702, folder, m, x, o)
            # 703
            fba703 = fba702 + 63
            o = 63
            folder = "703"
            m = "Faculty of Business Administration Building"
            x = "Room no. 703"
            te(fba703, folder, m, x, o)
            # 704
            fba704 = fba703 + 63
            o = 63
            folder = "704"
            m = "Faculty of Business Administration Building"
            x = "Room no. 704"
            te(fba704, folder, m, x, o)
            # 706
            fba706 = fba704 + 63
            o = 63
            folder = "706"
            m = "Faculty of Business Administration Building"
            x = "Room no. 706"
            te(fba706, folder, m, x, o)
            # 801
            fba801 = fba706 + 63
            o = 63
            folder = "801"
            m = "Faculty of Business Administration Building"
            x = "Room no. 801"
            te(fba801, folder, m, x, o)
            # 802
            fba802 = fba801 + 63
            o = 63
            folder = "802"
            m = "Faculty of Business Administration Building"
            x = "Room no. 802"
            te(fba802, folder, m, x, o)
            # 803
            fba803 = fba802 + 63
            o = 63
            folder = "803"
            m = "Faculty of Business Administration Building"
            x = "Room no. 803"
            te(fba803, folder, m, x, o)
            # 804
            fba804 = fba803 + 63
            o = 63
            folder = "804"
            m = "Faculty of Business Administration Building"
            x = "Room no. 804"
            te(fba804, folder, m, x, o)
            # 805
            fba805 = fba804 + 63
            o = 63
            folder = "805"
            m = "Faculty of Business Administration Building"
            x = "Room no. 805"
            te(fba805, folder, m, x, o)
            # 806
            fba806 = fba805 + 63
            o = 63
            folder = "806"
            m = "Faculty of Business Administration Building"
            x = "Room no. 806"
            te(fba806, folder, m, x, o)
            # 901
            fba901 = fba806 + 63
            o = 63
            folder = "901"
            m = "Faculty of Business Administration Building"
            x = "Room no. 901"
            te(fba901, folder, m, x, o)
            # 902
            fba902 = fba901 + 63
            o = 63
            folder = "902"
            m = "Faculty of Business Administration Building"
            x = "Room no. 902"
            te(fba901, folder, m, x, o)
            # 903
            fba903 = fba902 + 63
            o = 63
            folder = "902"
            m = "Faculty of Business Administration Building"
            x = "Room no. 902"
            te(fba903, folder, m, x, o)
            # 904
            fba904 = fba903 + 63
            o = 63
            folder = "904"
            m = "Faculty of Business Administration Building"
            x = "Room no. 904"
            te(fba904, folder, m, x, o)
            # 905
            fba905 = fba904 + 63
            o = 63
            folder = "905"
            m = "Faculty of Business Administration Building"
            x = "Room no. 905"
            te(fba905, folder, m, x, o)
            # 906
            fba906 = fba905 + 63
            o = 63
            folder = "906"
            m = "Faculty of Business Administration Building"
            x = "Room no. 906"
            te(fba906, folder, m, x, o)
            # 1001
            fba1001 = fba906 + 63
            o = 63
            folder = "1001"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1001"
            te(fba1001, folder, m, x, o)
            # 1002
            fba1002 = fba1001 + 63
            o = 63
            folder = "1002"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1002"
            te(fba1002, folder, m, x, o)
            # 1003
            fba1003 = fba1002 + 63
            o = 63
            folder = "1003"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1003"
            te(fba1003, folder, m, x, o)
            # 1004
            fba1004 = fba1003 + 63
            o = 63
            folder = "1004"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1004"
            te(fba1004, folder, m, x, o)
            # 1005
            fba1005 = fba1004 + 63
            o = 63
            folder = "1005"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1005"
            te(fba1005, folder, m, x, o)
            # 1006
            fba1006 = fba1005 + 63
            o = 63
            folder = "1006"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1006"
            te(fba1006, folder, m, x, o)
            # 101
            fss101 = fba1006 + 63
            o = 63
            folder = "101"
            m = "Faculty of Social Science Building"
            x = "Room no. 101"
            te(fss101, folder, m, x, o)
            # 102
            fss102 = fss101 + 63
            o = 63
            folder = "102"
            m = "Faculty of Social Science Building"
            x = "Room no. 102"
            te(fss102, folder, m, x, o)
            # 103
            fss103 = fss102 + 63
            o = 63
            folder = "103"
            m = "Faculty of Social Science Building"
            x = "Room no. 103"
            te(fba103, folder, m, x, o)
            # 104
            fss104 = fss103 + 63
            o = 63
            folder = "104"
            m = "Faculty of Social Science Building"
            x = "Room no. 104"
            te(fss104, folder, m, x, o)
            # 105
            fss105 = fss104 + 63
            o = 63
            folder = "105"
            m = "Faculty of Social Science Building"
            x = "Room no. 105"
            te(fss105, folder, m, x, o)
            # 201
            fss201 = fss105 + 63
            o = 63
            folder = "201"
            m = "Faculty of Social Science Building"
            x = "Room no. 201"
            te(fss201, folder, m, x, o)
            # 202
            fss202 = fss201 + 63
            o = 63
            folder = "202"
            m = "Faculty of Social Science Building"
            x = "Room no. 202"
            te(fss202, folder, m, x, o)
            # 203
            fss203 = fss202 + 63
            o = 63
            folder = "203"
            m = "Faculty of Social Science Building"
            x = "Room no. 203"
            te(fss203, folder, m, x, o)
            # 204
            fss204 = fss203 + 63
            o = 63
            folder = "204"
            m = "Faculty of Social Science Building"
            x = "Room no. 204"
            te(fss204, folder, m, x, o)
            # 205
            fss205 = fss204 + 63
            o = 63
            folder = "205"
            m = "Faculty of Social Science Building"
            x = "Room no. 205"
            te(fss205, folder, m, x, o)
            # 301
            fss301 = fss205 + 63
            o = 63
            folder = "301"
            m = "Faculty of Social Science Building"
            x = "Room no. 301"
            te(fss301, folder, m, x, o)
            # 302
            fss302 = fss301 + 63
            o = 63
            folder = "302"
            m = "Faculty of Social Science Building"
            x = "Room no. 302"
            te(fss302, folder, m, x, o)
            # 303
            fss303 = fss302 + 63
            o = 63
            folder = "303"
            m = "Faculty of Social Science Building"
            x = "Room no. 303"
            te(fss303, folder, m, x, o)
            # 304
            fss304 = fss303 + 63
            o = 63
            folder = "304"
            m = "Faculty of Social Science Building"
            x = "Room no. 304"
            te(fss304, folder, m, x, o)
            # 306
            fss306 = fss304 + 63
            o = 63
            folder = "306"
            m = "Faculty of Social Science Building"
            x = "Room no. 306"
            te(fss306, folder, m, x, o)
            # 401
            fss401 = fss306 + 63
            o = 63
            folder = "401"
            m = "Faculty of Social Science Building"
            x = "Room no. 401"
            te(fss401, folder, m, x, o)
            # 402
            fss402 = fss401 + 63
            o = 63
            folder = "402"
            m = "Faculty of Social Science Building"
            x = "Room no. 402"
            te(fss402, folder, m, x, o)
            # 403
            fss403 = fss402 + 63
            o = 63
            folder = "403"
            m = "Faculty of Social Science Building"
            x = "Room no. 403"
            te(fss403, folder, m, x, o)
            # 404
            fss404 = fss403 + 63
            o = 63
            folder = "404"
            m = "Faculty of Social Science Building"
            x = "Room no. 404"
            te(fba404, folder, m, x, o)
            # 405
            fss405 = fss404 + 63
            o = 63
            folder = "405"
            m = "Faculty of Social Science Building"
            x = "Room no. 405"
            te(fss405, folder, m, x, o)
            # 406
            fss406 = fss405 + 63
            o = 63
            folder = "406"
            m = "Faculty of Social Science Building"
            x = "Room no. 406"
            te(fss406, folder, m, x, o)
            # 501
            fss501 = fss406 + 63
            o = 63
            folder = "501"
            m = "Faculty of Social Science Building"
            x = "Room no. 501"
            te(fss501, folder, m, x, o)
            # 502
            fss502 = fss501 + 63
            o = 63
            folder = "502"
            m = "Faculty of Social Science Building"
            x = "Room no. 502"
            te(fss502, folder, m, x, o)
            # 503
            fss503 = fss502 + 63
            o = 63
            folder = "503"
            m = "Faculty of Social Science Building"
            x = "Room no. 503"
            te(fss503, folder, m, x, o)
            # 504
            fss504 = fss503 + 63
            o = 63
            folder = "504"
            m = "Faculty of Social Science Building"
            x = "Room no. 504"
            te(fss504, folder, m, x, o)
            # 505
            fss505 = fss504 + 63
            o = 63
            folder = "505"
            m = "Faculty of Social Science Building"
            x = "Room no. 505"
            te(fss505, folder, m, x, o)
            # 601
            fss601 = fss505 + 63
            o = 63
            folder = "601"
            m = "Faculty of Social Science Building"
            x = "Room no. 601"
            te(fss601, folder, m, x, o)
            # 602
            fss602 = fss601 + 63
            o = 63
            folder = "602"
            m = "Faculty of Social Science Building"
            x = "Room no. 602"
            te(fss602, folder, m, x, o)
            # 603
            fss603 = fss602 + 63
            o = 63
            folder = "603"
            m = "Faculty of Social Science Building"
            x = "Room no. 603"
            te(fss603, folder, m, x, o)
            # 604
            fss604 = fss603 + 63
            o = 63
            folder = "604"
            m = "Faculty of Social Science Building"
            x = "Room no. 604"
            te(fss604, folder, m, x, o)
            # 605
            fss605 = fss604 + 63
            o = 63
            folder = "605"
            m = "Faculty of Social Science Building"
            x = "Room no. 605"
            te(fss605, folder, m, x, o)
            # 606
            fss606 = fss605 + 63
            o = 63
            folder = "606"
            m = "Faculty of Social Science Building"
            x = "Room no. 606"
            te(fss606, folder, m, x, o)
            # 701
            fss701 = fss606 + 63
            o = 63
            folder = "701"
            m = "Faculty of Social Science Building"
            x = "Room no. 701"
            te(fss701, folder, m, x, o)
            # 702
            fss702 = fss701 + 63
            o = 63
            folder = "702"
            m = "Faculty of Social Science Building"
            x = "Room no. 702"
            te(fss702, folder, m, x, o)
            # 703
            fss703 = fss702 + 63
            o = 63
            folder = "703"
            m = "Faculty of Social Science Building"
            x = "Room no. 703"
            te(fss703, folder, m, x, o)
            # 704
            fss704 = fss703 + 63
            o = 63
            folder = "704"
            m = "Faculty of Social Science Building"
            x = "Room no. 704"
            te(fss704, folder, m, x, o)
            # 705
            fss705 = fss704 + 63
            o = 63
            folder = "705"
            m = "Faculty of Social Science Building"
            x = "Room no. 705"
            te(fss705, folder, m, x, o)
            # 706
            fss706 = fss705 + 63
            o = 63
            folder = "706"
            m = "Faculty of Social Science Building"
            x = "Room no. 706"
            te(fss706, folder, m, x, o)
            # 801
            fss801 = fss706 + 63
            o = 63
            folder = "801"
            m = "Faculty of Social Science Building"
            x = "Room no. 801"
            te(fss801, folder, m, x, o)
            # 802
            fss802 = fss801 + 63
            o = 63
            folder = "802"
            m = "Faculty of Social Science Building"
            x = "Room no. 802"
            te(fss802, folder, m, x, o)
            # 803
            fss803 = fss802 + 63
            o = 63
            folder = "803"
            m = "Faculty of Social Science Building"
            x = "Room no. 803"
            te(fss803, folder, m, x, o)
            # 804
            fss804 = fss803 + 63
            o = 63
            folder = "804"
            m = "Faculty of Social Science Building"
            x = "Room no. 804"
            te(fss804, folder, m, x, o)
            # 805
            fss805 = fss804 + 63
            o = 63
            folder = "805"
            m = "Faculty of Social Science Building"
            x = "Room no. 805"
            te(fss805, folder, m, x, o)
            # 806
            fss806 = fss805 + 63
            o = 63
            folder = "806"
            m = "Faculty of Social Science Building"
            x = "Room no. 806"
            te(fss806, folder, m, x, o)
            # 901
            fss901 = fss806 + 63
            o = 63
            folder = "901"
            m = "Faculty of Social Science Building"
            x = "Room no. 901"
            te(fss901, folder, m, x, o)
            # 902
            fss902 = fss901 + 63
            o = 63
            folder = "902"
            m = "Faculty of Social Science Building"
            x = "Room no. 902"
            te(fss902, folder, m, x, o)
            # 903
            fss903 = fss902 + 63
            o = 63
            folder = "903"
            m = "Faculty of Social Science Building"
            x = "Room no. 903"
            te(fss903, folder, m, x, o)
            # 904
            fss904 = fss903 + 63
            o = 63
            folder = "904"
            m = "Faculty of Social Science Building"
            x = "Room no. 904"
            te(fss904, folder, m, x, o)
            # 905
            fss905 = fss904 + 63
            o = 63
            folder = "905"
            m = "Faculty of Social Science Building"
            x = "Room no. 905"
            te(fss905, folder, m, x, o)
            # 906
            fss906 = fss905 + 63
            o = 63
            folder = "906"
            m = "Faculty of Social Science Building"
            x = "Room no. 906"
            te(fss906, folder, m, x, o)
            # 1001
            fss1001 = fss906 + 63
            o = 63
            folder = "1001"
            m = "Faculty of Social Science Building"
            x = "Room no. 1001"
            te(fss1001, folder, m, x, o)
            # 1002
            fss1002 = fss1001 + 63
            o = 63
            folder = "1002"
            m = "Faculty of Social Science Building"
            x = "Room no. 1002"
            te(fss1002, folder, m, x, o)
            # 1003
            fss1003 = fss1002 + 63
            o = 63
            folder = "1003"
            m = "Faculty of Social Science Building"
            x = "Room no. 1003"
            te(fss1003, folder, m, x, o)
            # 1004
            fss1004 = fss1003 + 63
            o = 63
            folder = "1004"
            m = "Faculty of Social Science Building"
            x = "Room no. 1004"
            te(fss1004, folder, m, x, o)
            # 1005
            fss1005 = fss1004 + 63
            o = 63
            folder = "1005"
            m = "Faculty of Social Science Building"
            x = "Room no. 1005"
            te(fss1005, folder, m, x, o)
            # 1006
            fss1006 = fss1005 + 63
            o = 20
            folder = "1006"
            m = "Faculty of Social Science Building"
            x = "Room no. 1006"
            te(fss1006, folder, m, x, o)
            mylabel = Label(root, text="This file is generated", fg="Red")
            mylabel.pack()
            mylabel.place(x=720, y=550, anchor=S)
        else:
            mylabel = Label(root, text="Invalid Input!", fg="Red")
            mylabel.pack()
            mylabel.place(x=720, y=550, anchor=S)
    mylabel = Label(root, text="Individual Roll to Check Seat Plan:", fg="Black")
    mylabel.pack()
    mylabel.place(x=431, y=550)
    e3 = Entry(root, width=63)
    e3.pack()
    e3.place(relx=0.5, rely=0.73, anchor=CENTER)
    def search(m,x):
        mylabel = Label(root, text=f"The roll is in {m},{x}", fg="Red")
        mylabel.pack()
        mylabel.place(x=720, y=670, anchor=S)
    def show1():
        # 106
        p = e3.get()
        if (p.isdigit() == True):
            q = int(p)
            o = 40
            m = "Science Building"
            x = "Room no. 106"
            if (q >= rf and q <= rf + o):
                search(m, x)
            b107 = rf + 40
            o = 63
            folder = "107"
            m = "Science Building"
            x = "Room no. 107"
            if (q >= b107 and q <= b107 + o):
                search(m, x)
            # 108
            b108 = b107 + 63
            o = 63
            folder = "108"
            m = "Science Building"
            x = "Room no. 108"
            if (q >= b108 and q <= b108 + o):
                search(m, x)
            # 301
            b301 = b108 + 63
            o = 63
            folder = "301"
            m = "Science Building"
            x = "Room no. 301"
            if (q >= b301 and q <= b301 + o):
                search(m, x)
            # 302
            b302 = b301 + 63
            o = 63
            folder = "302"
            m = "Science Building"
            x = "Room no. 302"
            if (q >= b302 and q <= b302 + o):
                search(m, x)
            # 303
            b303 = b302 + 63
            o = 63
            folder = "303"
            m = "Science Building"
            x = "Room no. 303"
            if (q >= b303 and q <= b303 + o):
                search(m, x)
            # 304
            b304 = b303 + 63
            o = 63
            folder = "304"
            m = "Science Building"
            x = "Room no. 304"
            if (q >= b304 and q <= b304 + o):
                search(m, x)
            # 310
            b310 = b304 + 63
            o = 63
            folder = "310"
            m = "Science Building"
            x = "Room no. 310"
            if (q >= b310 and q <= b310 + o):
                search(m, x)
            # 418
            b418 = b310 + 63
            o = 63
            folder = "418"
            m = "Science Building"
            x = "Room no. 418"
            if (q >= b418 and q <= b418 + o):
                search(m, x)
            # 505
            b505 = b418 + 63
            o = 63
            folder = "505"
            m = "Science Building"
            x = "Room no. 303"
            if (q >= b505 and q <= b505 + o):
                search(m, x)
            # 512
            b512 = b505 + 63
            o = 63
            folder = "512"
            m = "Science Building"
            x = "Room no. 512"
            if (q >= b512 and q <= b512 + o):
                search(m, x)
            # 513
            b513 = b512 + 63
            o = 63
            folder = "513"
            m = "Science Building"
            x = "Room no. 513"
            if (q >= b513 and q <= b513 + o):
                search(m, x)
            # 515
            b515 = b513 + 63
            o = 63
            folder = "515"
            m = "Science Building"
            x = "Room no. 515"
            if (q >= b515 and q <= b515 + o):
                search(m, x)
            # 209
            ab209 = b515 + 63
            o = 63
            folder = "209"
            m = "Arts Building"
            x = "Room no. 209"
            if (q >= ab209 and q <= ab209 + o):
                search(m, x)
            # 213
            ab213 = ab209 + 63
            o = 63
            folder = "213"
            m = "Arts Building"
            x = "Room no. 213"
            if (q >= ab213 and q <= ab213 + o):
                search(m, x)
            # 214
            ab214 = ab213 + 63
            o = 63
            folder = "214"
            m = "Arts Building"
            x = "Room no. 214"
            if (q >= ab214 and q <= ab214 + o):
                search(m, x)
            # 215
            ab215 = ab214 + 63
            o = 63
            folder = "215"
            m = "Arts Building"
            x = "Room no. 215"
            if (q >= ab215 and q <= ab215 + o):
                search(m, x)
            # 306
            ab306 = ab215 + 63
            o = 48
            folder = "306"
            m = "Arts Building"
            x = "Room no. 306"
            if (q >= ab306 and q <= ab306 + o):
                search(m, x)
            # 310
            ab310 = ab306 + 48
            o = 63
            folder = "310"
            m = "Arts Building"
            x = "Room no. 310"
            if (q >= ab310 and q <= ab310 + o):
                search(m, x)
            # 415
            ab415 = ab310 + 63
            o = 63
            folder = "415"
            m = "Arts Building"
            x = "Room no. 415"
            if (q >= ab415 and q <= ab415 + o):
                search(m, x)
            # 416
            ab416 = ab415 + 63
            o = 63
            folder = "416"
            m = "Arts Building"
            x = "Room no. 416"
            if (q >= ab416 and q <= ab416 + o):
                search(m, x)
            # 417
            ab417 = ab416 + 63
            o = 63
            folder = "417"
            m = "Arts Building"
            x = "Room no. 417"
            if (q >= ab417 and q <= ab417 + o):
                search(m, x)
            # 418
            ab418 = ab417 + 63
            o = 63
            folder = "418"
            m = "Arts Building"
            x = "Room no. 418"
            if (q >= ab418 and q <= ab418 + o):
                search(m, x)
            # 511
            ab511 = ab418 + 63
            o = 40
            folder = "511"
            m = "Arts Building"
            x = "Room no. 511"
            if (q >= ab511 and q <= ab511 + o):
                search(m, x)
            # 517
            ab517 = ab511 + 40
            o = 63
            folder = "517"
            m = "Arts Building"
            x = "Room no. 517"
            if (q >= ab517 and q <= ab517 + o):
                search(m, x)
            # 101
            fba101 = ab517 + 63
            o = 63
            folder = "101"
            m = "Faculty of Business Administration Building"
            x = "Room no. 101"
            if (q >= fba101 and q <= fba101 + o):
                search(m, x)
            # 102
            fba102 = fba101 + 63
            o = 63
            folder = "102"
            m = "Faculty of Business Administration Building"
            x = "Room no. 102"
            if (q >= fba102 and q <= fba102 + o):
                search(m, x)
            # 103
            fba103 = fba102 + 63
            o = 63
            folder = "103"
            m = "Faculty of Business Administration Building"
            x = "Room no. 103"
            if (q >= fba103 and q <= fba103 + o):
                search(m, x)
            # 104
            fba104 = fba103 + 63
            o = 63
            folder = "104"
            m = "Faculty of Business Administration Building"
            x = "Room no. 104"
            if (q >= fba104 and q <= fba104 + o):
                search(m, x)
            # 105
            fba105 = fba104 + 63
            o = 63
            folder = "105"
            m = "Faculty of Business Administration Building"
            x = "Room no. 105"
            if (q >= fba105 and q <= fba105 + o):
                search(m, x)
            # 205
            fba205 = fba105 + 63
            o = 63
            folder = "205"
            m = "Faculty of Business Administration Building"
            x = "Room no. 205"
            if (q >= fba205 and q <= fba205 + o):
                search(m, x)
            # 207
            fba207 = fba205 + 63
            o = 63
            folder = "207"
            m = "Faculty of Business Administration Building"
            x = "Room no. 207"
            if (q >= fba207 and q <= fba207 + o):
                search(m, x)
            # 208
            fba208 = fba207 + 63
            o = 63
            folder = "208"
            m = "Faculty of Business Administration Building"
            x = "Room no. 208"
            if (q >= fba208 and q <= fba208 + o):
                search(m, x)
            # 209
            fba209 = fba208 + 63
            o = 63
            folder = "209"
            m = "Faculty of Business Administration Building"
            x = "Room no. 209"
            if (q >= fba209 and q <= fba209 + o):
                search(m, x)
            # 301
            fba301 = fba209 + 63
            o = 63
            folder = "301"
            m = "Faculty of Business Administration Building"
            x = "Room no. 301"
            if (q >= fba301 and q <= fba301 + o):
                search(m, x)
            # 302
            fba302 = fba301 + 63
            o = 63
            folder = "302"
            m = "Faculty of Business Administration Building"
            x = "Room no. 302"
            if (q >= fba302 and q <= fba302 + o):
                search(m, x)
            # 303
            fba303 = fba302 + 63
            o = 63
            folder = "303"
            m = "Faculty of Business Administration Building"
            x = "Room no. 303"
            if (q >= fba303 and q <= fba303 + o):
                search(m, x)
            # 304
            fba304 = fba303 + 63
            o = 63
            folder = "304"
            m = "Faculty of Business Administration Building"
            x = "Room no. 304"
            if (q >= fba304 and q <= fba304 + o):
                search(m, x)
            # 305
            fba305 = fba304 + 63
            o = 63
            folder = "305"
            m = "Faculty of Business Administration Building"
            x = "Room no. 305"
            if (q >= fba305 and q <= fba305 + o):
                search(m, x)
            # 401
            fba401 = fba305 + 63
            o = 63
            folder = "401"
            m = "Faculty of Business Administration Building"
            x = "Room no. 401"
            if (q >= fba401 and q <= fba401 + o):
                search(m, x)
            # 402
            fba402 = fba401 + 63
            o = 63
            folder = "402"
            m = "Faculty of Business Administration Building"
            x = "Room no. 402"
            if (q >= fba402 and q <= fba402 + o):
                search(m, x)
            # 403
            fba403 = fba402 + 63
            o = 63
            folder = "403"
            m = "Faculty of Business Administration Building"
            x = "Room no. 403"
            if (q >= fba403 and q <= fba403 + o):
                search(m, x)
            # 404
            fba404 = fba403 + 63
            o = 63
            folder = "404"
            m = "Faculty of Business Administration Building"
            x = "Room no. 404"
            if (q >= fba404 and q <= fba404 + o):
                search(m, x)
            # 405
            fba405 = fba404 + 63
            o = 63
            folder = "405"
            m = "Faculty of Business Administration Building"
            x = "Room no. 405"
            if (q >= fba405 and q <= fba405 + o):
                search(m, x)
            # 406
            fba406 = fba405 + 63
            o = 63
            folder = "406"
            m = "Faculty of Business Administration Building"
            x = "Room no. 406"
            if (q >= fba406 and q <= fba406 + o):
                search(m, x)
            # 501
            fba501 = fba406 + 63
            o = 63
            folder = "501"
            m = "Faculty of Business Administration Building"
            x = "Room no. 501"
            if (q >= fba501 and q <= fba501 + o):
                search(m, x)
            # 502
            fba502 = fba501 + 63
            o = 63
            folder = "502"
            m = "Faculty of Business Administration Building"
            x = "Room no. 502"
            if (q >= fba502 and q <= fba502 + o):
                search(m, x)
            # 503
            fba503 = fba502 + 63
            o = 63
            folder = "503"
            m = "Faculty of Business Administration Building"
            x = "Room no. 503"
            if (q >= fba503 and q <= fba503 + o):
                search(m, x)
            # 504
            fba504 = fba503 + 63
            o = 63
            folder = "504"
            m = "Faculty of Business Administration Building"
            x = "Room no. 504"
            if (q >= fba504 and q <= fba504 + o):
                search(m, x)
            # 505
            fba505 = fba504 + 63
            o = 63
            folder = "504"
            m = "Faculty of Business Administration Building"
            x = "Room no. 504"
            if (q >= fba505 and q <= fba505 + o):
                search(m, x)
            # 506
            fba506 = fba505 + 63
            o = 63
            folder = "506"
            m = "Faculty of Business Administration Building"
            x = "Room no. 506"
            if (q >= fba506 and q <= fba506 + o):
                search(m, x)
            # 601
            fba601 = fba506 + 63
            o = 63
            folder = "601"
            m = "Faculty of Business Administration Building"
            x = "Room no. 601"
            if (q >= fba601 and q <= fba601 + o):
                search(m, x)
            # 602
            fba602 = fba601 + 63
            o = 63
            folder = "602"
            m = "Faculty of Business Administration Building"
            x = "Room no. 602"
            if (q >= fba602 and q <= fba602 + o):
                search(m, x)
            # 603
            fba603 = fba602 + 63
            o = 63
            folder = "603"
            m = "Faculty of Business Administration Building"
            x = "Room no. 603"
            if (q >= fba603 and q <= fba603 + o):
                search(m, x)
            # 604
            fba604 = fba603 + 63
            o = 63
            folder = "604"
            m = "Faculty of Business Administration Building"
            x = "Room no. 604"
            if (q >= fba604 and q <= fba604 + o):
                search(m, x)
            # 605
            fba605 = fba604 + 63
            o = 63
            folder = "605"
            m = "Faculty of Business Administration Building"
            x = "Room no. 605"
            if (q >= fba605 and q <= fba605 + o):
                search(m, x)
            # 606
            fba606 = fba605 + 63
            o = 63
            folder = "606"
            m = "Faculty of Business Administration Building"
            x = "Room no. 606"
            if (q >= fba606 and q <= fba606 + o):
                search(m, x)
            # 607
            fba607 = fba606 + 63
            o = 63
            folder = "607"
            m = "Faculty of Business Administration Building"
            x = "Room no. 607"
            if (q >= fba607 and q <= fba607 + o):
                search(m, x)
            # 701
            fba701 = fba607 + 63
            o = 63
            folder = "701"
            m = "Faculty of Business Administration Building"
            x = "Room no. 701"
            if (q >= fba701 and q <= fba701 + o):
                search(m, x)
            # 702
            fba702 = fba701 + 63
            o = 63
            folder = "702"
            m = "Faculty of Business Administration Building"
            x = "Room no. 702"
            if (q >= fba702 and q <= fba702 + o):
                search(m, x)
            # 703
            fba703 = fba702 + 63
            o = 63
            folder = "703"
            m = "Faculty of Business Administration Building"
            x = "Room no. 703"
            if (q >= fba703 and q <= fba703 + o):
                search(m, x)
            # 704
            fba704 = fba703 + 63
            o = 63
            folder = "704"
            m = "Faculty of Business Administration Building"
            x = "Room no. 704"
            if (q >= fba704 and q <= fba704 + o):
                search(m, x)
            # 706
            fba706 = fba704 + 63
            o = 63
            folder = "706"
            m = "Faculty of Business Administration Building"
            x = "Room no. 706"
            if (q >= fba706 and q <= fba706 + o):
                search(m, x)
            # 801
            fba801 = fba706 + 63
            o = 63
            folder = "801"
            m = "Faculty of Business Administration Building"
            x = "Room no. 801"
            if (q >= fba801 and q <= fba801 + o):
                search(m, x)
            # 802
            fba802 = fba801 + 63
            o = 63
            folder = "802"
            m = "Faculty of Business Administration Building"
            x = "Room no. 802"
            if (q >= fba802 and q <= fba802 + o):
                search(m, x)
            # 803
            fba803 = fba802 + 63
            o = 63
            folder = "803"
            m = "Faculty of Business Administration Building"
            x = "Room no. 803"
            if (q >= fba803 and q <= fba803 + o):
                search(m, x)
            # 804
            fba804 = fba803 + 63
            o = 63
            folder = "804"
            m = "Faculty of Business Administration Building"
            x = "Room no. 804"
            if (q >= fba804 and q <= fba804 + o):
                search(m, x)
            # 805
            fba805 = fba804 + 63
            o = 63
            folder = "805"
            m = "Faculty of Business Administration Building"
            x = "Room no. 805"
            if (q >= fba805 and q <= fba805 + o):
                search(m, x)
            # 806
            fba806 = fba805 + 63
            o = 63
            folder = "806"
            m = "Faculty of Business Administration Building"
            x = "Room no. 806"
            if (q >= fba806 and q <= fba806 + o):
                search(m, x)
            # 901
            fba901 = fba806 + 63
            o = 63
            folder = "901"
            m = "Faculty of Business Administration Building"
            x = "Room no. 901"
            if (q >= fba901 and q <= fba901 + o):
                search(m, x)
            # 902
            fba902 = fba901 + 63
            o = 63
            folder = "902"
            m = "Faculty of Business Administration Building"
            x = "Room no. 902"
            if (q >= fba902 and q <= fba902 + o):
                search(m, x)
            # 903
            fba903 = fba902 + 63
            o = 63
            folder = "902"
            m = "Faculty of Business Administration Building"
            x = "Room no. 902"
            if (q >= fba903 and q <= fba903 + o):
                search(m, x)
            # 904
            fba904 = fba903 + 63
            o = 63
            folder = "904"
            m = "Faculty of Business Administration Building"
            x = "Room no. 904"
            if (q >= fba904 and q <= fba904 + o):
                search(m, x)
            # 905
            fba905 = fba904 + 63
            o = 63
            folder = "905"
            m = "Faculty of Business Administration Building"
            x = "Room no. 905"
            if (q >= fba905 and q <= fba905 + o):
                search(m, x)
            # 906
            fba906 = fba905 + 63
            o = 63
            folder = "906"
            m = "Faculty of Business Administration Building"
            x = "Room no. 906"
            if (q >= fba906 and q <= fba906 + o):
                search(m, x)
            # 1001
            fba1001 = fba906 + 63
            o = 63
            folder = "1001"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1001"
            if (q >= fba1001 and q <= fba1001 + o):
                search(m, x)
            # 1002
            fba1002 = fba1001 + 63
            o = 63
            folder = "1002"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1002"
            if (q >= fba1002 and q <= fba1002 + o):
                search(m, x)
            # 1003
            fba1003 = fba1002 + 63
            o = 63
            folder = "1003"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1003"
            if (q >= fba1003 and q <= fba1003 + o):
                search(m, x)
            # 1004
            fba1004 = fba1003 + 63
            o = 63
            folder = "1004"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1004"
            if (q >= fba1004 and q <= fba1004 + o):
                search(m, x)
            # 1005
            fba1005 = fba1004 + 63
            o = 63
            folder = "1005"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1005"
            if (q >= fba1005 and q <= fba1005 + o):
                search(m, x)
            # 1006
            fba1006 = fba1005 + 63
            o = 63
            folder = "1006"
            m = "Faculty of Business Administration Building"
            x = "Room no. 1006"
            if (q >= fba1006 and q <= fba1006 + o):
                search(m, x)
            # 101
            fss101 = fba1006 + 63
            o = 63
            folder = "101"
            m = "Faculty of Social Science Building"
            x = "Room no. 101"
            if (q >= fss101 and q <= fss101 + o):
                search(m, x)
            # 102
            fss102 = fss101 + 63
            o = 63
            folder = "102"
            m = "Faculty of Social Science Building"
            x = "Room no. 102"
            if (q >= fss102 and q <= fss102 + o):
                search(m, x)
            # 103
            fss103 = fss102 + 63
            o = 63
            folder = "103"
            m = "Faculty of Social Science Building"
            x = "Room no. 103"
            if (q >= fss103 and q <= fss103 + o):
                search(m, x)
            # 104
            fss104 = fss103 + 63
            o = 63
            folder = "104"
            m = "Faculty of Social Science Building"
            x = "Room no. 104"
            if (q >= fss104 and q <= fss104 + o):
                search(m, x)
            # 105
            fss105 = fss104 + 63
            o = 63
            folder = "105"
            m = "Faculty of Social Science Building"
            x = "Room no. 105"
            if (q >= fss105 and q <= fss105 + o):
                search(m, x)
            # 201
            fss201 = fss105 + 63
            o = 63
            folder = "201"
            m = "Faculty of Social Science Building"
            x = "Room no. 201"
            if (q >= fss201 and q <= fss201 + o):
                search(m, x)
            # 202
            fss202 = fss201 + 63
            o = 63
            folder = "202"
            m = "Faculty of Social Science Building"
            x = "Room no. 202"
            if (q >= fss202 and q <= fss202 + o):
                search(m, x)
            # 203
            fss203 = fss202 + 63
            o = 63
            folder = "203"
            m = "Faculty of Social Science Building"
            x = "Room no. 203"
            if (q >= fss203 and q <= fss203 + o):
                search(m, x)
            # 204
            fss204 = fss203 + 63
            o = 63
            folder = "204"
            m = "Faculty of Social Science Building"
            x = "Room no. 204"
            if (q >= fss204 and q <= fss204 + o):
                search(m, x)
            # 205
            fss205 = fss204 + 63
            o = 63
            folder = "205"
            m = "Faculty of Social Science Building"
            x = "Room no. 205"
            if (q >= fss205 and q <= fss205 + o):
                search(m, x)
            # 301
            fss301 = fss205 + 63
            o = 63
            folder = "301"
            m = "Faculty of Social Science Building"
            x = "Room no. 301"
            if (q >= fss301 and q <= fss301 + o):
                search(m, x)
            # 302
            fss302 = fss301 + 63
            o = 63
            folder = "302"
            m = "Faculty of Social Science Building"
            x = "Room no. 302"
            if (q >= fss302 and q <= fss302 + o):
                search(m, x)
            # 303
            fss303 = fss302 + 63
            o = 63
            folder = "303"
            m = "Faculty of Social Science Building"
            x = "Room no. 303"
            if (q >= fss303 and q <= fss303 + o):
                search(m, x)
            # 304
            fss304 = fss303 + 63
            o = 63
            folder = "304"
            m = "Faculty of Social Science Building"
            x = "Room no. 304"
            if (q >= fss304 and q <= fss304 + o):
                search(m, x)
            # 306
            fss306 = fss304 + 63
            o = 63
            folder = "306"
            m = "Faculty of Social Science Building"
            x = "Room no. 306"
            if (q >= fss306 and q <= fss306 + o):
                search(m, x)
            # 401
            fss401 = fss306 + 63
            o = 63
            folder = "401"
            m = "Faculty of Social Science Building"
            x = "Room no. 401"
            if (q >= fss401 and q <= fss401 + o):
                search(m, x)
            # 402
            fss402 = fss401 + 63
            o = 63
            folder = "402"
            m = "Faculty of Social Science Building"
            x = "Room no. 402"
            if (q >= fss402 and q <= fss402 + o):
                search(m, x)
            # 403
            fss403 = fss402 + 63
            o = 63
            folder = "403"
            m = "Faculty of Social Science Building"
            x = "Room no. 403"
            if (q >= fss403 and q <= fss403 + o):
                search(m, x)
            # 404
            fss404 = fss403 + 63
            o = 63
            folder = "404"
            m = "Faculty of Social Science Building"
            x = "Room no. 404"
            if (q >= fss404 and q <= fss404 + o):
                search(m, x)
            # 405
            fss405 = fss404 + 63
            o = 63
            folder = "405"
            m = "Faculty of Social Science Building"
            x = "Room no. 405"
            if (q >= fss405 and q <= fss405 + o):
                search(m, x)
            # 406
            fss406 = fss405 + 63
            o = 63
            folder = "406"
            m = "Faculty of Social Science Building"
            x = "Room no. 406"
            if (q >= fss406 and q <= fss406 + o):
                search(m, x)
            # 501
            fss501 = fss406 + 63
            o = 63
            folder = "501"
            m = "Faculty of Social Science Building"
            x = "Room no. 501"
            if (q >= fss501 and q <= fss501 + o):
                search(m, x)
            # 502
            fss502 = fss501 + 63
            o = 63
            folder = "502"
            m = "Faculty of Social Science Building"
            x = "Room no. 502"
            if (q >= fss502 and q <= fss502 + o):
                search(m, x)
            # 503
            fss503 = fss502 + 63
            o = 63
            folder = "503"
            m = "Faculty of Social Science Building"
            x = "Room no. 503"
            if (q >= fss503 and q <= fss503 + o):
                search(m, x)
            # 504
            fss504 = fss503 + 63
            o = 63
            folder = "504"
            m = "Faculty of Social Science Building"
            x = "Room no. 504"
            if (q >= fss504 and q <= fss504 + o):
                search(m, x)
            # 505
            fss505 = fss504 + 63
            o = 63
            folder = "505"
            m = "Faculty of Social Science Building"
            x = "Room no. 505"
            if (q >= fss505 and q <= fss505 + o):
                search(m, x)
            # 601
            fss601 = fss505 + 63
            o = 63
            folder = "601"
            m = "Faculty of Social Science Building"
            x = "Room no. 601"
            if (q >= fss601 and q <= fss601 + o):
                search(m, x)
            # 602
            fss602 = fss601 + 63
            o = 63
            folder = "602"
            m = "Faculty of Social Science Building"
            x = "Room no. 602"
            if (q >= fss602 and q <= fss602 + o):
                search(m, x)
            # 603
            fss603 = fss602 + 63
            o = 63
            folder = "603"
            m = "Faculty of Social Science Building"
            x = "Room no. 603"
            if (q >= fss603 and q <= fss603 + o):
                search(m, x)
            # 604
            fss604 = fss603 + 63
            o = 63
            folder = "604"
            m = "Faculty of Social Science Building"
            x = "Room no. 604"
            if (q >= fss604 and q <= fss604 + o):
                search(m, x)
            # 605
            fss605 = fss604 + 63
            o = 63
            folder = "605"
            m = "Faculty of Social Science Building"
            x = "Room no. 605"
            if (q >= fss605 and q <= fss605 + o):
                search(m, x)
            # 606
            fss606 = fss605 + 63
            o = 63
            folder = "606"
            m = "Faculty of Social Science Building"
            x = "Room no. 606"
            if (q >= fss606 and q <= fss606 + o):
                search(m, x)
            # 701
            fss701 = fss606 + 63
            o = 63
            folder = "701"
            m = "Faculty of Social Science Building"
            x = "Room no. 701"
            if (q >= fss701 and q <= fss701 + o):
                search(m, x)
            # 702
            fss702 = fss701 + 63
            o = 63
            folder = "702"
            m = "Faculty of Social Science Building"
            x = "Room no. 702"
            if (q >= fss702 and q <= fss702 + o):
                search(m, x)
            # 703
            fss703 = fss702 + 63
            o = 63
            folder = "703"
            m = "Faculty of Social Science Building"
            x = "Room no. 703"
            if (q >= fss703 and q <= fss703 + o):
                search(m, x)
            # 704
            fss704 = fss703 + 63
            o = 63
            folder = "704"
            m = "Faculty of Social Science Building"
            x = "Room no. 704"
            if (q >= fss704 and q <= fss704 + o):
                search(m, x)
            # 705
            fss705 = fss704 + 63
            o = 63
            folder = "705"
            m = "Faculty of Social Science Building"
            x = "Room no. 705"
            if (q >= fss705 and q <= fss705 + o):
                search(m, x)
            # 706
            fss706 = fss705 + 63
            o = 63
            folder = "706"
            m = "Faculty of Social Science Building"
            x = "Room no. 706"
            if (q >= fss706 and q <= fss706 + o):
                search(m, x)
            # 801
            fss801 = fss706 + 63
            o = 63
            folder = "801"
            m = "Faculty of Social Science Building"
            x = "Room no. 801"
            if (q >= fss801 and q <= fss801 + o):
                search(m, x)
            # 802
            fss802 = fss801 + 63
            o = 63
            folder = "802"
            m = "Faculty of Social Science Building"
            x = "Room no. 802"
            if (q >= fss802 and q <= fss802 + o):
                search(m, x)
            # 803
            fss803 = fss802 + 63
            o = 63
            folder = "803"
            m = "Faculty of Social Science Building"
            x = "Room no. 803"
            if (q >= fss803 and q <= fss803 + o):
                search(m, x)
            # 804
            fss804 = fss803 + 63
            o = 63
            folder = "804"
            m = "Faculty of Social Science Building"
            x = "Room no. 804"
            if (q >= fss804 and q <= fss804 + o):
                search(m, x)
            # 805
            fss805 = fss804 + 63
            o = 63
            folder = "805"
            m = "Faculty of Social Science Building"
            x = "Room no. 805"
            if (q >= fss805 and q <= fss805 + o):
                search(m, x)
            # 806
            fss806 = fss805 + 63
            o = 63
            folder = "806"
            m = "Faculty of Social Science Building"
            x = "Room no. 806"
            if (q >= fss806 and q <= fss806 + o):
                search(m, x)
            # 901
            fss901 = fss806 + 63
            o = 63
            folder = "901"
            m = "Faculty of Social Science Building"
            x = "Room no. 901"
            if (q >= fss901 and q <= fss901 + o):
                search(m, x)
            # 902
            fss902 = fss901 + 63
            o = 63
            folder = "902"
            m = "Faculty of Social Science Building"
            x = "Room no. 902"
            if (q >= fss902 and q <= fss902 + o):
                search(m, x)
            # 903
            fss903 = fss902 + 63
            o = 63
            folder = "903"
            m = "Faculty of Social Science Building"
            x = "Room no. 903"
            if (q >= fss903 and q <= fss903 + o):
                search(m, x)
            # 904
            fss904 = fss903 + 63
            o = 63
            folder = "904"
            m = "Faculty of Social Science Building"
            x = "Room no. 904"
            if (q >= fss904 and q <= fss904 + o):
                search(m, x)
            # 905
            fss905 = fss904 + 63
            o = 63
            folder = "905"
            m = "Faculty of Social Science Building"
            x = "Room no. 905"
            if (q >= fss905 and q <= fss905 + o):
                search(m, x)
            # 906
            fss906 = fss905 + 63
            o = 63
            folder = "906"
            m = "Faculty of Social Science Building"
            x = "Room no. 906"
            if (q >= fss906 and q <= fss906 + o):
                search(m, x)
            # 1001
            fss1001 = fss906 + 63
            o = 63
            folder = "1001"
            m = "Faculty of Social Science Building"
            x = "Room no. 1001"
            if (q >= fss1001 and q <= fss1001 + o):
                search(m, x)
            # 1002
            fss1002 = fss1001 + 63
            o = 63
            folder = "1002"
            m = "Faculty of Social Science Building"
            x = "Room no. 1002"
            if (q >= fss1002 and q <= fss1002 + o):
                search(m, x)
            # 1003
            fss1003 = fss1002 + 63
            o = 63
            folder = "1003"
            m = "Faculty of Social Science Building"
            x = "Room no. 1003"
            if (q >= fss1003 and q <= fss1003 + o):
                search(m, x)
            # 1004
            fss1004 = fss1003 + 63
            o = 63
            folder = "1004"
            m = "Faculty of Social Science Building"
            x = "Room no. 1004"
            if (q >= fss1004 and q <= fss1004 + o):
                search(m, x)
            # 1005
            fss1005 = fss1004 + 63
            o = 63
            folder = "1005"
            m = "Faculty of Social Science Building"
            x = "Room no. 1005"
            if (q >= fss1005 and q <= fss1005 + o):
                search(m, x)
            # 1006
            fss1006 = fss1005 + 63
            o = 20
            folder = "1006"
            m = "Faculty of Social Science Building"
            x = "Room no. 1006"
            if (q >= fss1006 and q <= fss1006 + o):
                search(m, x)
        else :
            mylabel = Label(root, text="Invalid Input!", fg="Red")
            mylabel.pack()
            mylabel.place(x=720, y=670, anchor=S)
    mb = Button(root, text="submit", command=show1)
    mb.pack()
    mb.place(relx=0.5, rely=0.78, anchor=CENTER)
mb = Button(root, text="submit", command=show)
mb.pack()
mb.place(relx=0.5, rely=0.63, anchor=CENTER)
root.mainloop()
