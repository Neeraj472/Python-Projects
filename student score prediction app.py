import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

r=tk.Tk()
r.title("prediction app")
r.geometry("400x300")
r.config(bg="#FAD671")

df =pd.read_csv("C:\\Users\\LENOVO\\Desktop\\Javascript\\machinelearning\\student.csv")
X =df[["hours","sleep","attendance"]] #feature
y =df["score"] #target

X_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2,random_state=42)
model =LinearRegression()
model.fit(X_train,y_train)
y_pred =model.predict(X_test)
print("acutal:",y_pred,"predict :",y_pred)

mae =mean_absolute_error(y_test,y_pred)
mse =mean_squared_error(y_test,y_pred)
r2 =r2_score(y_test,y_pred)

print("mean absolute error :",mae)
print("mean square error",mse)
print(" r2 score",r2)

def predict():
    if hours_entry.get()=="":
        messagebox.showerror(title="INVALID VALUE",message="Please fill the value in Hours box")
        
    hours =float(hours_entry.get())
    
    if sleep_entry.get()=="":
        messagebox.showerror(title="INVALID VALUE",message="Please fill the value in Sleep box")
        
    sleep =float(sleep_entry.get())
    
    if attendance_entry.get()=="":
        messagebox.showerror(title="INVALID VALUE",message="Please fill the value in attendance box")
        
    attendance =float(attendance_entry.get())
    
    result =model.predict([[hours,sleep,attendance]])[0]
    messagebox.showinfo(title="predicted score",message=result)
    hours_entry.delete(0,tk.END)
    sleep_entry.delete(0,tk.END)
    attendance_entry.delete(0,tk.END)
    return

label =tk.Label(r,text="Score Prediction Model",font=("Arial",20),fg="blue",bg="#FAD671")
label.grid(row=0,column=3)

hours_label =tk.Label(r,text ="Hours :",font=("Arial",10),fg="black",bg="#FAD671")
hours_label.grid(row=3,column=2)
hours_entry =tk.Entry(r)
hours_entry.grid(row=3,column=3)

sleep_label =tk.Label(r,text ="Sleep :",font=("Arial",10),fg="black",bg="#FAD671")
sleep_label.grid(row=4,column=2)
sleep_entry =tk.Entry(r)
sleep_entry.grid(row=4,column=3)

attendance_label =tk.Label(r,text="Attendance",font=("Arial",10),fg="black",bg="#FAD671")
attendance_label.grid(row=5,column=2)
attendance_entry =tk.Entry(r)
attendance_entry.grid(row=5,column=3)

predict_button =tk.Button(r,text="Predict",font=("Arial",15),fg="black",bg="#FAD671",command=predict)
predict_button.grid(row=6,column=3,pady =10)

r.mainloop()