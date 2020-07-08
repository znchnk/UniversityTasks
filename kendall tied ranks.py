import tkinter
import tkinter.ttk
import numpy as np

print('Введите кол-во экспертов')
exp=int(input())
print('Введите кол-во факторов')
fac=int(input())


def kend(ocenki):
    data=[[znach[i][j].get() for j in range(len(znach[0]))] for i in range(len(znach)) ]
    #print(data)
    
    znam = exp**2*(fac**3-fac)
    ocenkiSums = np.sum(data, axis=0)
    koef= 0.5*exp*(fac+1)
    S=sum((ocenkiSums-koef)**2)
    otv = 12*S/znam
    #print(otv)

    otvS=tkinter.IntVar()
    otvS.set(round(otv,2))
    label101=tkinter.Label(window, textvariable = otvS).grid(row=exp+3,column=2)

# пользовательское окно 
window = tkinter.Tk()
window.title('К-т конкордации Кендалла')

expName = [ (f'эксперт{i}') for i in range(exp)]
facName = [ (f'ф{i}') for i in range(fac)]

for i in range(exp):
    tkinter.Label(window, text=expName[i], font=('Courier', 10, 'bold italic')).grid(row=i+2,column=0)

for i in range(fac):
    tkinter.Label(window, text=facName[i], font=('Courier', 10, 'bold italic')).grid(row=1,column=i+1)
    

znach= [[tkinter.IntVar() for i in range(fac)] for j in range(exp)]
for i in range(fac):
   for j in range(exp):
       tkinter.ttk.Spinbox(window, from_=0, to=30, textvariable=znach[j][i]).grid(row=j+2,column=i+1)


label91 = tkinter.Label(window, text='К-т конкордации Кендалла: ', font=('Courier', 10, 'bold italic')).grid(row=exp+3,column=1)

button1 = tkinter.Button(window, text='Рассчитать', command=lambda: kend(2)).grid(row=exp+4,column=1)
button2 = tkinter.Button(window, text='Выход', command=window.destroy).grid(row=exp+5,column=1)


window.mainloop()


