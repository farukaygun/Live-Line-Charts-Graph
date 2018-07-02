import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import json
from kafka import KafkaConsumer, KafkaProducer
from multiprocessing import Process,Manager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import tkinter as Tk

id1 = '1'
id2 = '2'

root = Tk.Tk()
root.geometry('500x260')
root.title("Performans")
root.resizable(width=False, height=False)

queue = Manager().list()
x_queue = Manager().list()

queue2 = Manager().list()
x_queue2 = Manager().list()

fig = plt.figure(figsize=(5, 2), dpi=100)
ax = fig.add_subplot(1, 1, 1 )
ax.get_xaxis().set_visible(False)

def aaa():

    if abc.get() == id1:
        ax.plot(x_queue, queue, color='g', label='Data value', linewidth='1')
    elif abc.get() == id2:
        ax.plot(x_queue2, queue2, color='g', label='Data value', linewidth='1')

id_label = Tk.Label(master=root, text="Id: ")
id_label.pack()
abc = Tk.Entry(master=root, font=30)
abc.pack()

id_label.config(font=30)
abc.place(x=30, y=3)
id_label.place(x=10, y=3)

for i in range(100):
    queue.append(0)
    x_queue.append(i)
    queue2.append(0)
    x_queue2.append(i)

def readMessagesFromKafka():
    consumer = KafkaConsumer('queue')

    global queue
    global queue2
    for msg in consumer:
        queue.append(int(msg.value))
        queue.pop(0) 
        queue2.append(int(msg.value))
        queue2.pop(0)

def drawPlot():
    global queue
    global queue2
    global x_queue
    global x_queue2

    def animate(i):
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        randomData2 = random.randint(1, 100)
        randomData = random.randint(1, 100)
        
        if abc.get() == id1:
            print(randomData)
            producer.send('queue', json.dumps(randomData).encode('utf-8'))
            ax.clear()

        elif abc.get() == id2:
            print(randomData2)
            producer.send('queue', json.dumps(randomData2).encode('utf-8'))
            ax.clear()

        aaa()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.BOTTOM, expand=True)
    
    ani = animation.FuncAnimation(fig, animate, interval=1)
    Tk.mainloop()

if __name__ == '__main__':
    p1 = Process(target=readMessagesFromKafka)
    p1.start()
    p2 = Process(target=drawPlot)
    p2.start()
    p1.join()
    p2.join()
