import tkinter as tk
import time

window = tk.Tk()
window.geometry("250x250")

#message = tk.Message(window, text="this is a message", width=50)
#message.pack

def count_down():
	timer = 10
	while timer >= 0:
		label.configure(text=timer)
		time.sleep(1)
		timer -= 1
	time.sleep(1)
	label.configure(text="Ka-Boom!")

#def configure_label():
	#label.configure(text="Button clicked!")

text = tk.Text(window, height=2, width=30)
text.insert(tk.INSERT, "To be or not to be that is the question")
text.insert(tk.END, "Bye")
text.pack

label = tk.Label(window, text="Don't click that button!", width=200)
label.pack()

button = tk.Button(window, text="Start" , command=count_down)
button.pack()

window.mainloop()