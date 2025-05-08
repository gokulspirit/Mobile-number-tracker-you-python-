import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, region_code_for_number
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser

# FREE OpenCage API Key (rate limited – 2,500 requests/month)
API_KEY = "e6c4a2f59e88494e9d4e62fa4b7d6c8b"

def track_location():
    number = entry.get()
    try:
        # Parse number
        phoneNumber = phonenumbers.parse(number)
        
        # Get info
        location = geocoder.description_for_number(phoneNumber, "en")
        provider = carrier.name_for_number(phoneNumber, "en")
        time_zones = timezone.time_zones_for_number(phoneNumber)
        region = region_code_for_number(phoneNumber)
        
        # Geocode using OpenCage
        geocoder_oc = OpenCageGeocode(API_KEY)
        results = geocoder_oc.geocode(location)
        
        if results:
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']

            # Generate map
            mapObj = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(mapObj)
            mapObj.save("Location.html")

            # Open in browser
            webbrowser.open("Location.html")

            # Show info
            info = (
                f"Location: {location}\n"
                f"Service Provider: {provider}\n"
                f"Time Zone(s): {', '.join(time_zones)}\n"
                f"Region Code: {region}\n"
                f"Map saved and opened in browser."
            )
            messagebox.showinfo("Tracking Successful", info)
        else:
            messagebox.showwarning("Error", "Could not geocode location.")

    except Exception as e:
        messagebox.showerror("Invalid Input", str(e))


# GUI Setup
root = tk.Tk()
root.title("Phone Number Tracker")
root.geometry("400x250")

tk.Label(root, text="Enter Phone Number (+CountryCode):", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

tk.Button(root, text="Track Location", command=track_location, font=("Arial", 12)).pack(pady=20)

root.mainloop()
