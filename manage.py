from registr import login, registr_user
from database import *
from kurs import *
from yozilganlar import*

print('\tHello 🙌')
def start():
    while True:
        print('1.Registr\t2.Login')
        choise=int(input('<<< '))
        try:
            if choise==1:
                registr_user()
                while True:
                        print('/t1.Aktiv kurslar royhatini korish\t2.Aktiv kurslarni korish\t3.Yozilgan kurslarni korish\t4.exit')
                        tanlash=int(input('<<< '))
                        if tanlash==1:
                            pass
                        elif tanlash==2:
                            pass
                        elif tanlash==3:
                            yozilgankurs(a[1])
                        else:
                            return
            elif choise==2:
                a=login()
                if a=='admin':
                    while True:
                        show_kurs()
                        print('\t1.Kurs qoshish\t2.Kursga yozilgan oquvchilarni korish\3.Exit')
                        tanlash=int(input('<<< '))
                        if tanlash==1:
                            insert_kurs()
                        elif tanlash==2:
                            show_yozilganlar()
                        else:
                            return
                elif a[0]==True:
                    while True:
                        print('/t1.Aktiv kurslar royhatini korish\t2.Aktiv kurslarni korish\t3.Yozilgan kurslarni korish\t4.exit')
                        tanlash=int(input('<<< '))
                        if tanlash==1:
                            pass
                        elif tanlash==2:
                            pass
                        elif tanlash==3:
                            yozilgankurs(a[1])
                        else:
                            return

        except:
            raise IndentationError('Dasturni qayta ishga tushiring!!!😔')
        
start()