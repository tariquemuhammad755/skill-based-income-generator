import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Data used for mapping skills with income details
# This can be expanded later if required

skills_info = {
    "Python": {
        "jobs": ["Python Developer", "Backend Developer", "Automation Engineer"],
        "sites": ["Upwork", "Freelancer"],
        "pay": {
            "Beginner": "Rs. 20,000 - Rs. 40,000 per month",
            "Intermediate": "Rs. 40,000 - Rs. 80,000 per month",
            "Expert": "Rs. 80,000 - Rs. 1,50,000 per month"
        }
    },

    "Data Analysis": {
        "jobs": ["Data Analyst", "Power BI Developer"],
        "sites": ["LinkedIn", "Upwork", "Kaggle"],
        "pay": {
            "Beginner": "Rs. 25,000 - Rs. 45,000 per month",
            "Intermediate": "Rs. 50,000 - Rs. 90,000 per month",
            "Expert": "Rs. 1,00,000 - Rs. 1,80,000 per month"
        }
    },

    "Web Development": {
        "jobs": ["Frontend Developer", "Full Stack Developer"],
        "sites": ["Fiverr", "Upwork", "Internshala"],
        "pay": {
            "Beginner": "Rs. 20,000 - Rs. 40,000 per month",
            "Intermediate": "Rs. 45,000 - Rs. 85,000 per month",
            "Expert": "Rs. 90,000 - Rs. 1,60,000 per month"
        }
    }
}


def show_result():
    user_name = name_box.get().strip()
    chosen_skill = skill_box.get()
    skill_level = level_box.get()

    if user_name == "" or chosen_skill == "" or skill_level == "":
        messagebox.showwarning("Input Error", "Please fill all the details")
        return

    details = skills_info[chosen_skill]

    text = "Name: " + user_name + "\n\n"

    text += "Recommended Job Roles:\n"
    for j in details["jobs"]:
        text += "- " + j + "\n"

    text += "\nPlatforms to apply or freelance:\n"
    for s in details["sites"]:
        text += "- " + s + "\n"

    text += "\nExpected Monthly Income (" + skill_level + "):\n"
    text += details["pay"][skill_level]

    output_lbl.config(text=text)
#adding ckear button
def clear_fields():
    name_box.delete(0, tk.END)
    skill_box.current(0)
    level_box.current(0)
    output_lbl.config(text="")

# Creating main window
root = tk.Tk()
root.title("Skill Based Income Generator")
root.geometry("480x520")
root.resizable(False, False)

# Heading
head = tk.Label(root, text="Skill Based Income Generator",
                font=("Arial", 15, "bold"))
head.pack(pady=10)

# Name input
tk.Label(root, text="Your Name").pack()
name_box = tk.Entry(root, width=30)
name_box.pack(pady=5)

# Skill selection
tk.Label(root, text="Select Your Skill").pack()
skill_box = ttk.Combobox(root, state="readonly",
                          values=list(skills_info.keys()))
skill_box.pack(pady=5)
skill_box.current(0)      # default skill selected

# Skill level
tk.Label(root, text="Skill Level").pack()
level_box = ttk.Combobox(root, state="readonly",
                         values=["Beginner", "Intermediate", "Expert"])
level_box.pack(pady=5)
level_box.current(0)  #default level selected

# Button
btn = tk.Button(root, text="Generate Income Details",
                command=show_result)
btn.pack(pady=15)
clear_btn = tk.Button(root, text="Clear",
                      command=clear_fields)
clear_btn.pack(pady=5)

# Output section
output_lbl = tk.Label(root, justify="left",
                      wraplength=440,
                      font=("Arial", 10))
output_lbl.pack(padx=10, pady=10)

root.mainloop()