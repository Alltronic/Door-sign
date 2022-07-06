import tkinter as tk
import time
   
main = tk.Tk()
# get screen width and height
ws = main.winfo_screenwidth() 
hs = main.winfo_screenheight()
main.geometry("%dx%d+0+0" % (ws,hs))
main["background"]="black"
main.wait_visibility()

current_time = time.localtime(time.time())
myText = tk.StringVar()
print(current_time.tm_hour)

if current_time.tm_hour > 17:
    myText.set("Closed")
else:
    myText.set("Open")

theLabel = tk.Label(main, textvariable=myText, fg="yellow", bg="black", font=("Arial", 96))
theLabel.place(relx = 0.5, rely=0.5, anchor = "center")

main.mainloop()
