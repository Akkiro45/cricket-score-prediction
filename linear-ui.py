from tkinter import *
import tkinter
from tkinter import messagebox

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy as np


dataset = pd.read_csv('data/ipl.csv')
X = dataset.iloc[:,[3,4,7,8,9,12,13]].values
y = dataset.iloc[:, 14].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

lin = LinearRegression()
lin.fit(X_train,y_train)

y_pred = lin.predict(X_test)
score = lin.score(X_test,y_test)*100
print("R square value:" , score)

root = Tk()
topframe = Frame(root, bg='#2874FF')
root.title('Score Prediction')
root.geometry("260x220")
topframe.place(bordermode=OUTSIDE, height=500, width=500)

Label(topframe, text='Batting Team', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=0) 
Label(topframe, text='Balling Team', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=1)
Label(topframe, text='Current Score', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=2) 
Label(topframe, text='Current Wicktes', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=3)
Label(topframe, text='Current Over', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=4)
Label(topframe, text='Strikers Runs', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=5)
Label(topframe, text='Non-Strikers Runs', bg='#2874FF', fg='#FFF', font=("bold", 11)).grid(row=6)
batTeam = Entry(topframe) 
ballTeam = Entry(topframe)
score = Entry(topframe)
wikts = Entry(topframe)
over = Entry(topframe)
strikersRuns = Entry(topframe)
nonStrikersRuns = Entry(topframe) 
batTeam.grid(row=0, column=1) 
ballTeam.grid(row=1, column=1)
score.grid(row=2, column=1) 
wikts.grid(row=3, column=1)
over.grid(row=4, column=1) 
strikersRuns.grid(row=5, column=1)
nonStrikersRuns.grid(row=6, column=1)

def predict():
	new_prediction = lin.predict(sc.transform(np.array([[int(batTeam.get()),int(ballTeam.get()),int(score.get()),int(wikts.get()),int(over.get()),int(strikersRuns.get()),int(nonStrikersRuns.get())]])))
	messagebox.showinfo("Prediction",new_prediction)
button = tkinter.Button(root, text='Predict', width=20, command=predict, font=("bold", 11), bg='#00D348', fg='#FFF') 
button.place(x=25, y=180)

root.mainloop()








