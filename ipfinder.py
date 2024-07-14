import tkinter as tk
from tkinter import messagebox
import requests

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data['status'] == 'fail':
            return "Invalid IP address or API limit reached."
        return f"""
        IP: {data['query']}
        Country: {data['country']}
        Region: {data['regionName']}
        City: {data['city']}
        ISP: {data['isp']}
        Latitude: {data['lat']}
        Longitude: {data['lon']}
        """
    except requests.RequestException:
        return "Error fetching IP information. Check your internet connection."

def display_ip_info():
    ip_address = entry_ip.get()
    if ip_address:
        info = get_ip_info(ip_address)
        label_info.config(text=info)
    else:
        messagebox.showerror("Input Error", "Please enter a valid IP address.")


root = tk.Tk()
root.title("IP Information")


tk.Label(root, text="Enter IP Address:").pack(pady=5)
entry_ip = tk.Entry(root)
entry_ip.pack(pady=5)

tk.Button(root, text="Get Info", command=display_ip_info).pack(pady=5)

label_info = tk.Label(root, text="", justify="left", font=("Helvetica", 12))
label_info.pack(pady=20)

root.mainloop()
