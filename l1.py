import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("test.jpg")
fig, ax = plt.subplots()
ax = plt.imshow(img)


def onclick(event):
    x, y = event.xdata, event.ydata
    print(f"Point at X={x:.2f} and Y={y:.2f} set")
    plt.plot(x, y, 'ro', alpha=0.5)
    fig.canvas.draw()


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
