import cv2
import time
from keys import *
from handTracker import *
import mysql.connector

mey_database = mysql.connector.connect(
    host="localhost", user="root", password="159753123Aa", database="kullanicilar")
mey_cursor = mey_database.cursor()

# bakiyem


w, h = 80, 70
startX, startY = 450, 440
textBox = Key(startX, startY - h - 25, 4 * w + 50, h, '')
currentScreen = "login"

# para gonder ekranı degiskeni
gonderilenMiktar = 0
IBAN = ""

# keys
sifreGirKey = Key(450, 250, 400, 100, "Sifrenizi Giriniz")
numGirKey = Key(450, 250, 400, 100, "Kart Numarasini Giriniz")
miktarGirKey = Key(430, 250, 400, 100, "Cekmek Istediginiz Tutari Giriniz")
hataliGirKey = Key(430, 250, 400, 100, " Bakiyeniz Yetersiz!!!")
bakiyeTextKey = Key(450, 100, 400, 100, "bakiye")
paraCekBakiye = Key(430, 200, 400, 100, "bakiye")
numaraTextKey = Key(450, 150, 400, 100, "numara")
ibanTextKey = Key(450, 200, 400, 100, "iban")

# title keys
loginTitleKey = Key(450, 10, 400, 150, "Giris Yap")
mainTitleKey = Key(430, 10, 400, 150, "Ana Menu")
paracekTitleKey = Key(430, 10, 400, 150, "Para Cek")
parayatirTitleKey = Key(450, 10, 400, 150, "Para Yatir")
paragonderTitleKey = Key(450, 10, 400, 150, "Para Gonder")
hesapBilgilerimTitleKey = Key(450, 10, 400, 150, "Hesap Bilgilerim")

# main menu buttons
paracekKey = Key(200, 100, 200, 150, "Para Cek")
parayatirKey = Key(200, 270, 200, 150, "Para Yatir")
paragonderKey = Key(200, 440, 200, 150, "Para Gonder")
bakiyeKey = Key(200, 610, 200, 150, "Hesap Bilgilerim")



def getMousPos(event, x, y, flags, param):
    global clickedX, clickedY
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONUP:
        # print(x,y)
        clickedX, clickedY = x, y
    if event == cv2.EVENT_MOUSEMOVE:
        #     print(x,y)
        mouseX, mouseY = x, y


def calculateIntDidtance(pt1, pt2):
    return int(((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5)


def showMainMenu(frame):
    sifreGirKey.text = ""
    loginTitleKey.text = ""
    mainTitleKey.text = "Ana Menu"
    mainTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)

    paracekKey.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.5, fontScale=0.5)
    parayatirKey.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.5, fontScale=0.5)
    paragonderKey.drawKey(frame, (255, 255, 255),
                          (0, 0, 0), 0.5, fontScale=0.5)
    bakiyeKey.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.5, fontScale=0.5)


def showLoginScreen(frame):
    loginTitleKey.text = "Giris Yap"
    numGirKey.drawKey(frame, alpha=1)
    loginTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)
def showLogimScreem1(frame):
    loginTitleKey.text = "Giris Yap"
    sifreGirKey.drawKey(frame, alpha=1)
    loginTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)

def showParaCekScreen(frame):
    mainTitleKey.text = ""
    paracekTitleKey.text = "Para Cek"
    paracekTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)

    miktarGirKey.drawKey(frame, alpha=1)
    miktarGirKey.text = "Cekmek Istediginiz Tutari Giriniz"
    paraCekBakiye.drawKey(frame, alpha=1)
    # bakiye goster
    numara: int
    with open("numara.txt", "r") as file:
        numara = int(file.read())

    mey_cursor.execute(
        "SELECT para,kartnumarası,iban FROM users WHERE kartnumarası=" + str(numara))
    bilgiler = mey_cursor.fetchall()
    paraCekBakiye.text = "Bakiye: " + str(bilgiler[0][0])

def showParaCekScreen1(frame):
    mainTitleKey.text = ""
    paracekTitleKey.text = "Para Cek"
    paracekTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)
    hataliGirKey.drawKey(frame, alpha=1)
    hataliGirKey.text = "Bakiyeniz Yetersiz!!!"
    paraCekBakiye.drawKey(frame, alpha=1)
    # bakiye goster
    numara: int
    with open("numara.txt", "r") as file:
        numara = int(file.read())

    mey_cursor.execute(
        "SELECT para,kartnumarası,iban FROM users WHERE kartnumarası=" + str(numara))
    bilgiler = mey_cursor.fetchall()
    paraCekBakiye.text = "Bakiye: " + str(bilgiler[0][0])


def showParaYatirKey(frame):
    parayatirTitleKey.text = "Para Yatir"
    parayatirTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)

    miktarGirKey.drawKey(frame, alpha=1)
    miktarGirKey.text = "Yatirmak Istediginiz Miktari Giriniz"


def showParaGonderKey(frame):
    paragonderTitleKey.text = "Para Gonder"
    paragonderTitleKey.drawKey(frame, alpha=1, fontScale=1.5, thickness=3)

    miktarGirKey.drawKey(frame, alpha=1)
    miktarGirKey.text = "Gondermek Istediginiz IBAN ile Miktar Arasinda Bosluk Birakarak Giriniz"


def showBakiyeScreen(frame):
    miktarGirKey.text = ""
    bakiyeTextKey.drawKey(frame, alpha=1)
    numaraTextKey.drawKey(frame,alpha=1)
    ibanTextKey.drawKey(frame, alpha=1)
    hesapBilgilerimTitleKey.drawKey(frame,alpha=1)
    # bakiye goster
    numara: int
    with open("numara.txt", "r") as file:
        numara = int(file.read())

    mey_cursor.execute(
        "SELECT para,kartnumarası,iban FROM users WHERE kartnumarası=" + str(numara))
    bilgiler = mey_cursor.fetchall()
    bakiyeTextKey.text = "Bakiye: " + str(bilgiler[0][0])
    numaraTextKey.text="Kart Numarasi: "+str(bilgiler[0][1])
    ibanTextKey.text="Iban: "+str(bilgiler[0][2])


def girisButtonIslemi(screen, gonderilenMiktar):
    currentScreen = ""

    if screen == "login":
        # ana menuye git
        mey_cursor.execute("SELECT kartnumarası,sifre FROM users")
        numaralar = mey_cursor.fetchall()

        for i in numaralar:
            if textBox.text == str(i[0]):
                currentScreen = "login1"


    elif screen=="login1":
        mey_cursor.execute("SELECT kartnumarası,sifre FROM users")
        numaralar = mey_cursor.fetchall()

        for i in numaralar:
            if textBox.text == str(i[1]):
                with open("numara.txt", "w") as file:
                    file.write(str(i[0]))

                currentScreen = "main"

    elif screen == "paracek":
        # para cek
        numara: int
        with open("numara.txt", "r") as file:
            numara = int(file.read())

        mey_cursor.execute(
            "SELECT para FROM users WHERE kartnumarası=" + str(numara))
        paralar = mey_cursor.fetchall()
        yenipara: int
        if len(textBox.text) > 0:
            if( int(paralar[0][0]) - int(textBox.text)<0):
                currentScreen="paracek1"
            else:

                yenipara = int(paralar[0][0]) - int(textBox.text)
                update = "UPDATE users SET para=" + \
                         str(yenipara) + " WHERE kartnumarası=" + str(numara)
                mey_cursor.execute(update)
                mey_database.commit()

                currentScreen = "main"
    elif screen=="paracek1":
        # para cek
        numara: int
        with open("numara.txt", "r") as file:
            numara = int(file.read())

        mey_cursor.execute(
            "SELECT para FROM users WHERE kartnumarası=" + str(numara))
        paralar = mey_cursor.fetchall()
        yenipara: int
        if len(textBox.text) > 0:
            if( int(paralar[0][0]) - int(textBox.text)<0):
                currentScreen="paracek1"
            else:

                yenipara = int(paralar[0][0]) - int(textBox.text)
                update = "UPDATE users SET para=" + \
                         str(yenipara) + " WHERE kartnumarası=" + str(numara)
                mey_cursor.execute(update)
                mey_database.commit()

                currentScreen = "main"


    elif screen == "parayatir":
        # para yatir
        numara: int
        with open("numara.txt", "r") as file:
            numara = int(file.read())

        mey_cursor.execute(
            "SELECT para FROM users WHERE kartnumarası=" + str(numara))
        paralar = mey_cursor.fetchall()
        yenipara: int
        if len(textBox.text) > 0:
            yenipara = int(paralar[0][0]) + int(textBox.text)
        update = "UPDATE users SET para=" + \
                 str(yenipara) + " WHERE kartnumarası=" + str(numara)
        mey_cursor.execute(update)
        mey_database.commit()

        currentScreen = "main"

    elif screen == "paragonder":
        # para gonder
        numara: int
        with open("numara.txt", "r") as file:
            numara = int(file.read())

        gonderimBilgiler = []
        if len(textBox.text) > 0:
            gonderimBilgiler = textBox.text.split(" ")

        mey_cursor.execute("SELECT para FROM users WHERE kartnumarası=" + str(numara))
        paralar = mey_cursor.fetchall()

        yenipara: int

        if len(textBox.text) > 0:
            yenipara = int(paralar[0][0]) - int(gonderimBilgiler[1])

        update = "UPDATE users SET para=" + \
                 str(yenipara) + " WHERE kartnumarası=" + str(numara)

        mey_cursor.execute(update)
        mey_database.commit()

        mey_cursor.execute("SELECT para FROM users WHERE iban=" + gonderimBilgiler[0])
        paralar2 = mey_cursor.fetchall()

        yeniPara2 = int(gonderimBilgiler[1]) + int(paralar2[0][0])

        update2 = "UPDATE users SET para=" + str(yeniPara2) + " WHERE iban=" + gonderimBilgiler[0]
        mey_cursor.execute(update2)
        mey_database.commit()

        currentScreen = "main"

    elif screen == "bakiye":

        currentScreen = "main"

    return currentScreen


# Creating keys
keys = []
letters = ["1", "2", "3", "4", "5", "6", "7",
           "8", "9", "0", "Bosluk", "Sil", "Iptal", "Giris", "Cikis"]
for i, l in enumerate(letters):
    if i < 3:
        keys.append(Key(startX + i * w + i * 5, startY, w, h, l))
    elif i < 6:
        keys.append(Key(startX + (i - 3) * w + (i - 3)
                        * 5, startY + h + 5, w, h, l))
    elif i < 9:
        keys.append(Key(startX + (i - 6) * w + (i - 6) *
                        5, startY + 2 * h + 10, w, h, l))
    elif i < 10:
        keys.append(Key(startX + (i - 9) * w + (i - 9) *
                        5, startY + 3 * h + 15, w, h, l))
    elif i < 11:
        keys.append(Key(startX + (i - 9) * w + (i - 9) *
                        5, startY + 3 * h + 15, 2 * w + 5, h, l))
    elif i < 12:
        keys.append(Key(startX + (i - 8) * w + (i - 8)
                        * 5 + 10, startY, w + 25, h, l))
    elif i < 13:
        keys.append(Key(startX + (i - 9) * w + (i - 9) *
                        5 + 10, startY + h + 5, w + 25, h, l))
    elif i < 14:
        keys.append(Key(startX + (i - 10) * w + (i - 10) * 5 +
                        10, startY + 2 * h + 10, w + 25, h, l))
    elif i < 15:
        keys.append(Key(startX + (i - 11) * w + (i - 11) * 5 +
                        10, startY + 3 * h + 15, w + 25, h, l))

showKey = Key(1000, 65, 80, 50, 'Show')
exitKey = Key(1000, 5, 80, 50, 'Exit')

cap = cv2.VideoCapture(0)
ptime = 0

# initiating the hand tracker
tracker = HandTracker(detectionCon=1)

# getting frame's height and width
frameHeight, frameWidth, _ = cap.read()[1].shape
showKey.x = int(frameWidth * 1.5) - 85
exitKey.x = int(frameWidth * 1.5) - 85
# print(showKey.x)

clickedX, clickedY = 0, 0
mousX, mousY = 0, 0

show = False
cv2.namedWindow('video')
counter = 0
previousClick = 0
while True:
    if counter > 0:
        counter -= 1

    signTipX = 0
    signTipY = 0

    thumbTipX = 0
    thumbTipY = 0

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (int(frameWidth * 2), int(frameHeight * 2)))
    frame = cv2.flip(frame, 1)

    # show login page
    if currentScreen == "login":
        showLoginScreen(frame)

    elif currentScreen == "main":
        showMainMenu(frame)

    elif currentScreen == "paracek":
        showParaCekScreen(frame)

    elif currentScreen=="paracek1":
        showParaCekScreen1(frame)

    elif currentScreen == "parayatir":
        showParaYatirKey(frame)

    elif currentScreen == "paragonder":
        showParaGonderKey(frame)

    elif currentScreen== "login1":
        showLogimScreem1(frame)


    elif currentScreen == "bakiye":
        showBakiyeScreen(frame)

    # find hands
    frame = tracker.findHands(frame)
    lmList = tracker.getPostion(frame, draw=False)
    if lmList:
        signTipX, signTipY = lmList[8][1], lmList[8][2]
        thumbTipX, thumbTipY = lmList[12][1], lmList[12][2]
        if calculateIntDidtance((signTipX, signTipY), (thumbTipX, thumbTipY)) < 70:
            centerX = int((signTipX + thumbTipX) / 2)
            centerY = int((signTipY + thumbTipY) / 2)
            cv2.line(frame, (signTipX, signTipY),
                     (thumbTipX, thumbTipY), (0, 255, 0), 2)
            cv2.circle(frame, (centerX, centerY), 5, (0, 255, 0), cv2.FILLED)

    ctime = time.time()
    fps = int(1 / (ctime - ptime))

    cv2.putText(frame, str(fps) + " FPS", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    showKey.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.1, fontScale=0.5)
    exitKey.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.1, fontScale=0.5)
    cv2.setMouseCallback('video', getMousPos)

    if showKey.isOver(clickedX, clickedY):
        show = not show
        showKey.text = "Hide" if show else "Show"
        clickedX, clickedY = 0, 0

    if exitKey.isOver(clickedX, clickedY):
        # break
        exit()

    if showKey.isOver(thumbTipX, thumbTipY):
        show = not show
        showKey.text = "Hide" if show else "Show"
        clickedX, clickedY = 0, 0

    if exitKey.isOver(thumbTipX, thumbTipY):
        # break
        exit()

    # checking if sign finger is over a key and if click happens
    alpha = 0.5
    if show:
        textBox.drawKey(frame, (255, 255, 255), (0, 0, 0), 0.3)
        for k in keys:
            if k.isOver(mouseX, mouseY) or k.isOver(signTipX, signTipY):
                alpha = 0.1
                # writing using mouse right click
                if k.isOver(clickedX, clickedY):
                    if k.text == 'Sil':
                        textBox.text = textBox.text[:-1]
                    elif k.text == 'Iptal' and currentScreen=="paragonder":
                        currentScreen = "main"
                    elif k.text == 'Iptal' and currentScreen=="parayatir":
                        currentScreen = "main"
                    elif k.text == 'Iptal' and currentScreen=="paracek":
                        currentScreen = "main"
                    elif k.text == 'Iptal' and currentScreen=="bakiye":
                        currentScreen = "main"
                    elif k.text=='Iptal':
                        textBox.text=''
                    elif k.text == 'Bosluk':
                        textBox.text += " "
                    elif k.text == 'Cikis':
                        currentScreen = "login"
                    elif k.text == 'Giris' and currentScreen == 'main':
                        currentScreen == 'main'
                    elif k.text == 'Giris':
                        currentScreen = girisButtonIslemi(
                            currentScreen, gonderilenMiktar)
                        textBox.text = ""
                    else:
                        textBox.text += k.text

                # writing using fingers
                if (k.isOver(thumbTipX, thumbTipY)):
                    clickTime = time.time()
                    if clickTime - previousClick > 1:
                        if k.text == 'Sil':
                            textBox.text = textBox.text[:-1]
                        elif k.text == 'Iptal' and currentScreen=="paragonder":
                            currentScreen = "main"
                        elif k.text == 'Iptal' and currentScreen=="parayatir":
                            currentScreen = "main"
                        elif k.text == 'Iptal' and currentScreen=="paracek":
                            currentScreen = "main"
                        elif k.text == 'Iptal' and currentScreen=="bakiye":
                            currentScreen = "main"
                        elif k.text == 'Iptal':
                            textBox.text = ''
                        elif k.text == 'Bosluk':
                            textBox.text += " "
                        elif k.text == 'Cikis':
                            currentScreen = "login"
                        elif k.text=='Giris' and currentScreen=='main':
                            currentScreen=='main'

                        elif len(textBox.text) < 30:
                            if k.text == 'Giris':
                                currentScreen = girisButtonIslemi(
                                    currentScreen, gonderilenMiktar)
                                textBox.text = ""
                            else:
                                textBox.text += k.text

                        previousClick = clickTime

            k.drawKey(frame, (255, 255, 255), (0, 0, 0), alpha=alpha)
            alpha = 0.5

        # diger butonların tıklanma olayları
        if paracekKey.isOver(mouseX, mouseY) or paracekKey.isOver(signTipX, signTipY):
            if paracekKey.isOver(clickedX, clickedY):
                currentScreen = "paracek"

        if parayatirKey.isOver(mouseX, mouseY) or parayatirKey.isOver(signTipX, signTipY):
            if parayatirKey.isOver(clickedX, clickedY):
                currentScreen = "parayatir"

        if paragonderKey.isOver(mouseX, mouseY) or paragonderKey.isOver(signTipX, signTipY):
            if paragonderKey.isOver(clickedX, clickedY):
                currentScreen = "paragonder"

        if bakiyeKey.isOver(mouseX, mouseY) or bakiyeKey.isOver(signTipX, signTipY):
            if bakiyeKey.isOver(clickedX, clickedY):
                currentScreen = "bakiye"

        if paracekKey.isOver(mouseX, mouseY) or paracekKey.isOver(signTipX, signTipY):
            if paracekKey.isOver(thumbTipX, thumbTipY):
                currentScreen = "paracek"

        if parayatirKey.isOver(mouseX, mouseY) or parayatirKey.isOver(signTipX, signTipY):
            if parayatirKey.isOver(thumbTipX, thumbTipY):
                currentScreen = "parayatir"

        if paragonderKey.isOver(mouseX, mouseY) or paragonderKey.isOver(signTipX, signTipY):
            if paragonderKey.isOver(thumbTipX, thumbTipY):
                currentScreen = "paragonder"

        if bakiyeKey.isOver(mouseX, mouseY) or bakiyeKey.isOver(signTipX, signTipY):
            if bakiyeKey.isOver(thumbTipX, thumbTipY):
                currentScreen = "bakiye"

        clickedX, clickedY = 0, 0
    ptime = ctime
    cv2.imshow('video', frame)

    ## stop the video when 'q' is pressed
    pressedKey = cv2.waitKey(1)
    if pressedKey == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
