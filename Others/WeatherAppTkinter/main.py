# Himanshu Tripathi


import tkinter as tk
# from PIL import ImageTk, Image
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = f'City: {name} \n Description: {desc} \n Temperature: {str(temp)}'
		
	except:
		final_str = 'Sorry No Data Found'
	
	return final_str
	


# *********************************** key

# button
def get_weather(city):
# 	you need to add your own key
	weather_key = '*********************'
	# url = 'https://api.openweathermap.org/data/2.5/forecast'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key,'q':city, 'units':'Imperial'}
	response = requests.get(url,params=params)
	# print(response.json())
	weather = response.json()
	label['text'] = format_response(weather)
	
	# print(name,condition,temp)

root = tk.Tk()

# make a window
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='image.png')
background_label = tk.Label(root,image = background_image)
background_label.place(relheight=1,relwidth=1)

# upper frame
# for making frame
frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

# for input 
entry = tk.Entry(frame, font=('Californian FB',20))
entry.place(relwidth=0.65, relheight=1)

# for button
# for button to clikable using command and then pass functionName

button = tk.Button(frame, text = "Get Weather" ,font=('Californian FB',15) , command =lambda:get_weather(entry.get()) )
button.place(relx = 0.7,relwidth = 0.3,relheight=1)

# lower frame
lower_frame = tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relheight=0.6,relwidth=0.75,anchor='n')

# lable field
label = tk.Label(lower_frame,font=('Californian FB',20))
label.place(relheight=1,relwidth=1)

# print(tk.font.families())
root.mainloop()
