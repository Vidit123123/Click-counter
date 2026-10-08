import customtkinter as ctk
import json
from tkinter import messagebox
def getClicks():
	try:
		with open("clicks.json","r") as cl:
			clicks = json.load(cl).get("clicks",0)
	except FileNotFoundError:
		clicks = 0
	return clicks
ctk.set_appearance_mode("dark")
class app(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Click")
		self.total = getClicks()
		self.geometry("250x150")
		self.lab = ctk.CTkLabel(self,text=self.total)
		self.lab.pack()
		self.nextChallange = ctk.CTkLabel(self,text="Click 100 times")
		self.nextChallange.pack()
		self.button = ctk.CTkButton(self,command=self.increase,text="Click",fg_color="#1900ff")
		self.button.pack(padx=5,pady=5)
		self.resetBtn = ctk.CTkButton(self,command=self.reset,text="Reset",text_color="red",fg_color="#1900ff")
		self.resetBtn.pack(padx=5,pady=5)
	def increase(self):
		clicks = getClicks()

		newCount = clicks+1
		self.lab.configure(text=clicks+1)
		if clicks < 100:
			self.nextChallange.configure(text="Click 100 times")
		elif clicks >= 100 and clicks < 250:
			if clicks == 100:
				messagebox.showinfo("Congrats","You have Clicked 100 times")
			self.nextChallange.configure(text="Click 250 times")
		elif clicks >= 250 and clicks < 500:
			if clicks == 250:
				messagebox.showinfo("Congrats","You have Clicked 250 times")
			self.nextChallange.configure(text="Click 500 times",text_color="#00ff00")
		elif clicks >= 500 and clicks < 1000:
			if clicks == 500:
				messagebox.showinfo("Congrats","You have Clicked 500 times")
			self.nextChallange.configure(text="Click 1000 times")
		else:
			self.nextChallange.configure(text="You are legendary")
		with open("clicks.json","w") as cl:
			json.dump({"clicks": newCount},cl)
	def reset(self):
		if messagebox.askokcancel("Reset","Are you sure you want to delete all your clicks"):
			with open("clicks.json","w") as cl:
				json.dump({"clicks": 0},cl)
			self.lab.configure(text=0)
if __name__ == "__main__":
	appp = app()
	appp.mainloop()
