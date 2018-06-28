import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import random
from kafka import KafkaConsumer, KafkaProducer
import Request

queue = deque()
x_queue = deque()

fig = plt.figure(figsize=(5, 2), dpi=100)
ax = fig.add_subplot(2, 2, 1, )
ax.get_xaxis().set_visible(False)

for i in range(100):
    queue.append(i)
    x_queue.append(i)

consumer = KafkaConsumer('queue')

for msg in consumer:
    print(msg)
    queue.append(int(msg.value))
    queue.popleft()
    def animate(i):     
            ax.clear()
            ax.plot(x_queue, queue, color='g', label='Data value', linewidth='1')
            plt.pause(0.01)
    ani = animation.FuncAnimation(fig, animate, interval=100)
    plt.show()