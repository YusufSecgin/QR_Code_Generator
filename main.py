import qrcode
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
import webbrowser

# Function to generate QR code
def generate_qr():
    url = url_entry.get()
    if url == "":
        messagebox.showwarning("Warning", "Please enter a URL")
        return
    if not url.startswith("http"):
        messagebox.showwarning("Invalid URL", "Please enter a valid URL")
        return

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate QR code image with transparent background
    global qr_img  # Define as a global variable
    qr_img = qr.make_image(fill="#0A4A3A", back_color=(255, 255, 255, 0)).convert('RGBA')  # Use Rolex green for fill

    # Resize image for Tkinter
    img = qr_img.resize((200, 200), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    # Display image in the interface
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep a reference to avoid garbage collection

    messagebox.showinfo("Success", "QR code generated successfully.")

# Function to save QR code
def save_qr():
    if 'qr_img' not in globals():
        messagebox.showwarning("Warning", "You must generate a QR code first.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("SVG files", "*.svg")])
    if file_path:
        # Save with transparent background
        qr_img.save(file_path, format="PNG")  # No need to specify transparency
        messagebox.showinfo("Success", f"QR code saved as {file_path}.")

# Function to open URL in the browser
def open_in_browser():
    url = url_entry.get()
    if url == "":
        messagebox.showwarning("Warning", "Please enter a URL")
        return
    webbrowser.open(url)

# Create the GUI
root = Tk()
root.title("QR Code Generator")

# Rolex colors
bg_color = "#0A4A3A"  # Rolex green
fg_color = "#D4AF37"  # Rolex gold
button_color = "#D4AF37"

# Set window size
root.geometry("400x600")
root.config(bg=bg_color)

# Title label
title_label = Label(root, text="QR Code Generator", font=("Helvetica Neue", 20, "bold"), bg=bg_color, fg=fg_color)
title_label.pack(pady=20)

# URL entry field
url_entry = Entry(root, width=40, font=("Helvetica Neue", 14), borderwidth=2)
url_entry.insert(0, "Enter URL to generate QR code")
url_entry.bind("<FocusIn>", lambda e: url_entry.delete(0, "end") if url_entry.get() == "Enter URL to generate QR code" else None)
url_entry.pack(pady=10)

# Button frame
button_frame = Frame(root, bg=bg_color)
button_frame.pack(pady=20)

# Button to generate QR code
generate_btn = ttk.Button(button_frame, text="Generate QR Code", command=generate_qr, style="TButton")
generate_btn.pack(side=LEFT, padx=5)

# Button to save QR code
save_btn = ttk.Button(button_frame, text="Save", command=save_qr, style="TButton")
save_btn.pack(side=LEFT, padx=5)

# Button to open URL in browser
browser_btn = ttk.Button(button_frame, text="Open in Browser", command=open_in_browser, style="TButton")
browser_btn.pack(side=LEFT, padx=5)

# Label to display QR code
qr_label = Label(root, bg=bg_color)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
