import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

def check_password_strength(password):
    # Define the criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "digits": re.search(r"\d", password) is not None,
        "special": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    }
    
    # Evaluate the criteria
    score = sum(criteria.values())
    strength = "Weak"
    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"

    # Provide detailed feedback
    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not criteria["digits"]:
        feedback.append("Password should contain at least one digit.")
    if not criteria["special"]:
        feedback.append("Password should contain at least one special character.")
    
    return strength, feedback

def on_check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    
    result_text = f"Password Strength: {strength}\n"
    if feedback:
        result_text += "Feedback:\n" + "\n".join(f" - {f}" for f in feedback)
    
    result_label.config(text=result_text)

def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        eye_button.config(image=eye_closed_image)
    else:
        password_entry.config(show='')
        eye_button.config(image=eye_open_image)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

# Create and place the password entry widget
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)
password_frame = tk.Frame(root)
password_frame.pack(pady=10)
password_entry = tk.Entry(password_frame, show="*", width=30)
password_entry.pack(side=tk.LEFT, padx=(0, 10))

# Load images for the eye button
eye_open_image = ImageTk.PhotoImage(Image.open("eye_open.png").resize((20, 20)))
eye_closed_image = ImageTk.PhotoImage(Image.open("eye_closed.png").resize((20, 20)))

# Create and place the eye button
eye_button = tk.Button(password_frame, image=eye_closed_image, command=toggle_password_visibility)
eye_button.pack(side=tk.LEFT)

# Create and place the check button
check_button = tk.Button(root, text="Check Password Strength", command=on_check_password)
check_button.pack(pady=20)

# Create and place the result label
result_label = tk.Label(root, text="", wraplength=350, justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
