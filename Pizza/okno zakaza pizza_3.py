import tkinter
import tkinter.ttk
from PIL import Image, ImageTk

def zakaz(qw):
    #zkz={{label10:{label11:label12}, label20:{label21:label22}, label30:{label31:label32}}
    #zkz={list(pizza)[0]:{size[0].get():kolvo[0].get()}, list(pizza)[1]:{size[1].get():kolvo[1].get()}, list(pizza)[2]:{size[2].get():kolvo[2].get()}}
    #print(zkz)
    #print('date.get() ', label71.get(), type( label71.get()  ) )

    D=dict()
    kolvo_all=sum([i.get() for i in kolvo]) #общее кол-во
    #print('kolvo_all', kolvo_all)
    prices=[]
    pr1=[]
    for i in range(len(size)):  #для размеров
        if size[i].get()!='':  #обходим в словаре пустые элемнты
            priceofP=int(pizza[list(pizza)[i]]['size'][size[i].get()])  #цена одной единсвтенной из словаря
            #print("priceofP",priceofP)
            #D[list(pizza)[i]]={priceofP}
            D[list(pizza)[i]] = {size[i].get():kolvo[i].get()}
            pr1.append(priceofP)
        else:
            priceofP=0
            pr1.append(100000)
        prices.append(priceofP)  # строка всех цен

    try:
        minP=prices.index(min(pr1)) #ищем мин цену для акции
    except:
        print("Выберите пиццу и укажите количество")

    #print('prices', prices)
    sums=[]
    try:
        if label81.get() == 'Сегодня': # учитываем вторую акцию
            #print('проверка пройдена')
            for i in range(len(prices)): # все цены
                if kolvo_all < 3:
                    sums.append(prices[i]*kolvo[i].get())
                else:
                    if i!=minP:
                        sums.append(prices[i]*kolvo[i].get())
                    else:
                        sums.append(prices[i]*(kolvo[i].get()-1))
                        print("При заказе от трёх пицц самая дешёвая пицца - бесплатно!")
            sumZ=sum(sums)
        if label81.get() == 'Завтра':
            for i in range(len(prices)):
                sums.append(prices[i]*kolvo[i].get())
            sumZ=sum(sums)*0.95
            print("Скидка 5% при заказе доставки на завтра.")

        #print('проверка пройдена 3')
        orderS=tkinter.IntVar()
        orderS.set(sumZ)

        label101=tkinter.Label(window, textvariable = orderS).grid(row=10,column=1)
        #label91.config( text = orderS)
    except:
        print("Выберите день доставки.")

    D['Время']={label60.get()}
    D['Адрес']={label61.get()}
    D['Телефон']={label62.get()}
    if qw=='cost':
        qw=0
    if qw=='end':
        print('\nЗаказ сформирован!\n')
        print(D)

    #print('label12', kolvo[0].get(), type( kolvo[0].get() ))
    #d*8


pizza = {
    'ПЕППЕРОНИ': {'sostav': 'Пепперони, моцарелла, томатный соус', 'size': {'S': 100, 'M': 200}},
    'МАРГАРИТА': {'sostav': 'Томаты, моцарелла, томатный соус', 'size': {'S': 150, 'M': 300}},
    'ГАВАЙСКАЯ': {'sostav': 'Курица, ветчина, ананас, моцарелла, томатный соус', 'size': {'S': 200, 'M': 400}}
    }

window = tkinter.Tk()
window.title('Заказ пиццы')

width = 200
imgg=[]
img = [ Image.open(f'piz{i}.jpg') for i in range(3)]
for i in img:
    ratio = (width / float(i.size[0]))
    height = int((float(i.size[1]) * float(ratio)))
    imgg.append(i.resize((width, height)))

render = [ ImageTk.PhotoImage(imgg[i]) for i in range(3) ]
for i in range(3):
    tkinter.Label(window, image=render[i]).grid(row=0,column=i)


label10 = tkinter.Label(window, text='Выберите пиццы ', font=('Courier', 12, 'bold italic'))
label10.grid(row=1,column=0)
label11 = tkinter.Label(window, text='Выберите размер ', font=('Courier', 12, 'bold italic'))
label11.grid(row=1,column=1)
label12 = tkinter.Label(window, text='Укажите количество ', font=('Courier', 12, 'bold italic'))
label12.grid(row=1,column=2)

label20 = tkinter.Label(window, text='ПЕППЕРОНИ ', font=('Courier', 12, 'bold italic'))
label20.grid(row=2,column=0)
label30 = tkinter.Label(window, text='МАРГАРИТА ', font=('Courier', 12, 'bold italic'))
label30.grid(row=3,column=0)
label40 = tkinter.Label(window, text='ГАВАЙСКАЯ ', font=('Courier', 12, 'bold italic'))
label40.grid(row=4,column=0)

label50 = tkinter.Label(window, text='Введите время заказа ', font=('Courier', 10, 'bold italic'))
label50.grid(row=5,column=0)
label51 = tkinter.Label(window, text='Введите адрес заказа ', font=('Courier', 10, 'bold italic'))
label51.grid(row=5,column=1)
label52 = tkinter.Label(window, text='Введите номер телефона ', font=('Courier', 10, 'bold italic'))
label52.grid(row=5,column=2)
label71 = tkinter.Label(window, text='Выберите день заказа: ', font=('Courier', 10, 'bold italic')).grid(row=7,column=1)
label91 = tkinter.Label(window, text='Сумма заказа со скидкой: ', font=('Courier', 10, 'bold italic')).grid(row=9,column=1)

#for r in range(1, 4):
#   for c in range(1, 2):
#      tkinter.ttk.Combobox(window, values = [u"S",u"M"]).grid(row=r,column=c)

#for r in range(1, 4):
#   for c in range(2, 3):
 #     tkinter.ttk.Spinbox(window, from_=0, to=30).grid(row=r,column=c)


size = [tkinter.StringVar() for i in range(0,3)]
label21 = tkinter.ttk.Combobox(window, values = ["S","M"], textvariable=size[0]).grid(row=2,column=1)
label31 = tkinter.ttk.Combobox(window, values = ["S","M"],textvariable=size[1]).grid(row=3,column=1)
label41 = tkinter.ttk.Combobox(window, values = ["S","M"], textvariable=size[2]).grid(row=4,column=1)

kolvo = [tkinter.IntVar() for i in range(0,3)]
label22 = tkinter.ttk.Spinbox(window, from_=0, to=30, textvariable=kolvo[0]).grid(row=2,column=2)
label32 = tkinter.ttk.Spinbox(window, from_=0, to=30, textvariable=kolvo[1] ).grid(row=3,column=2)
label42 = tkinter.ttk.Spinbox(window, from_=0, to=30, textvariable=kolvo[2] ).grid(row=4,column=2)


label81=tkinter.ttk.Combobox(window, values = ['Сегодня','Завтра'], textvariable= tkinter.StringVar() )
label81.grid(row=8,column=1)
label60=tkinter.Entry(window)
label60.grid(row=6,column=0)
label61=tkinter.Entry(window)
label61.grid(row=6,column=1)
label62=tkinter.Entry(window)
label62.grid(row=6,column=2)

label101=tkinter.Label(window).grid(row=10,column=1)

button1 = tkinter.Button(window, text='Стоимость', command=lambda: zakaz('cost')).grid(row=11,column=1)
button1 = tkinter.Button(window, text='Заказать', command=lambda: zakaz('end')).grid(row=12,column=1)
button2 = tkinter.Button(window, text='Выход', command=window.destroy).grid(row=13,column=1)


window.mainloop()


