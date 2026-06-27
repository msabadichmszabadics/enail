import tkinter as tk

root = tk.Tk()
root.title("Fusebox")
root.geometry("700x500")
root.configure(bg="#202020")

canvas = tk.Canvas(root, width=700, height=500, bg="#202020", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ======================
# FUSEBOX
# ======================

canvas.create_rectangle(40, 70, 220, 330, fill="#8a8a8a", outline="black", width=3)
canvas.create_text(130, 95, text="FUSEBOX", fill="black",
                   font=("Arial", 16, "bold"))

canvas.create_rectangle(90, 140, 170, 260, fill="#404040", outline="black")

lever = canvas.create_rectangle(100, 150, 160, 200,
                                fill="red", outline="black")

canvas.create_text(130, 285, text="OFF", fill="white",
                   font=("Arial", 14, "bold"))

# ======================
# SZEMPÁR
# ======================

canvas.create_oval(350, 150, 450, 220, fill="white")
canvas.create_oval(480, 150, 580, 220, fill="white")

left_eye = canvas.create_oval(388, 173, 412, 197, fill="#222")
right_eye = canvas.create_oval(518, 173, 542, 197, fill="#222")

glow_left = canvas.create_oval(370,155,430,215,outline="",fill="")
glow_right = canvas.create_oval(500,155,560,215,outline="",fill="")

on = False

def toggle(event=None):
    global on

    on = not on

    if on:
        canvas.coords(lever, 100, 200, 160, 250)
        canvas.itemconfig(lever, fill="lime")
        canvas.itemconfig(left_eye, fill="yellow")
        canvas.itemconfig(right_eye, fill="yellow")
        canvas.itemconfig(glow_left, fill="#ffff66")
        canvas.itemconfig(glow_right, fill="#ffff66")
        canvas.itemconfig(6, text="ON")
    else:
        canvas.coords(lever, 100, 150, 160, 200)
        canvas.itemconfig(lever, fill="red")
        canvas.itemconfig(left_eye, fill="#222")
        canvas.itemconfig(right_eye, fill="#222")
        canvas.itemconfig(glow_left, fill="")
        canvas.itemconfig(glow_right, fill="")
        canvas.itemconfig(6, text="OFF")

canvas.tag_bind(lever, "<Button-1>", toggle)

root.mainloop()