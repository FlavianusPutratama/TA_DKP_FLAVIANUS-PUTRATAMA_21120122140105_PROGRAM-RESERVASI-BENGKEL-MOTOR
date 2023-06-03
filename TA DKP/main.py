from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry       

class ReservationApp:
    def __init__(self, master):
        self.master = master
        master.title("Reservasi Bengkel")

        self.label_name = tk.Label(master, text="Nama Pelanggan:", font=("Bahnschrift SemiBold", 15))
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()

        self.label_motor = tk.Label(master, text="Jenis Motor:", font=("Bahnschrift SemiBold", 15))
        self.label_motor.pack()
        self.selected_motor = tk.StringVar()
        self.dropdown_motor = ttk.Combobox(master, textvariable=self.selected_motor, values=["Matic", "Bebek", "Sport", "2 Stroke"])
        self.dropdown_motor.pack()

        self.label_cc = tk.Label(master, text="CC Motor:", font=("Bahnschrift SemiBold", 15))
        self.label_cc.pack()
        self.selected_cc = tk.StringVar()
        self.dropdown_cc = ttk.Combobox(master, textvariable=self.selected_cc, values=["100-125 CC", "125-150 CC", "150-200 CC", "200-250 CC", "250 Keatas"])
        self.dropdown_cc.pack()

        self.label_service = tk.Label(master, text="Jenis Servis:", font=("Bahnschrift SemiBold", 15))
        self.label_service.pack()
        self.selected_service = tk.StringVar()
        self.dropdown_service = ttk.Combobox(master, textvariable=self.selected_service, values=["Servis Pengereman", "Servis Ringan", "Servis Besar", "Servis Kelistrikan", "Ganti Oli"])
        self.dropdown_service.pack()

        self.label_date = tk.Label(master, text="Tanggal Reservasi:", font=("Bahnschrift SemiBold", 15))
        self.label_date.pack()
        self.entry_date = DateEntry(master, width=12, background='green', foreground='lightgreen', font=('Bahnschrift Light', 13))
        self.entry_date.pack()

        self.reserve_button = tk.Button(master, width=17, background='lightgreen', text="Reservasi", command=self.reserve, font=("Bahnschrift SemiBold", 19))
        self.reserve_button.pack()

    def get_price(self, motor, cc, service):            # Fungsi untuk menentukan estimasi harga berdasarkan jenis motor, cc motor, dan jenis servis
        if motor == "Matic":
            if cc == "100-125 CC":
                if service == "Servis Pengereman":
                    return "30.000"
                elif service == "Servis Ringan":
                    return "100.000"
                elif service == "Servis Besar":
                    return "200.000"
                elif service == "Servis Kelistrikan":
                    return "125.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "125-150 CC":
                if service == "Servis Pengereman":
                    return "40.000"
                elif service == "Servis Ringan":
                    return "150.000"
                elif service == "Servis Besar":
                    return "250.000"
                elif service == "Servis Kelistrikan":
                    return "130.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "150-200 CC":
                if service == "Servis Pengereman":
                    return "50.000"
                elif service == "Servis Ringan":
                    return "170.000"
                elif service == "Servis Besar":
                    return "270.000"
                elif service == "Servis Kelistrikan":
                    return "200.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "250 Keatas":
                if service == "Servis Pengereman":
                    return "60.000"
                elif service == "Servis Ringan":
                    return "350.000"
                elif service == "Servis Besar":
                    return "450.000"
                elif service == "Servis Kelistrikan":
                    return "300.000"
                elif service == "Ganti Oli":
                    return "20.000"

        elif motor == "Bebek":
            if cc == "100-125 CC":
                if service == "Servis Pengereman":
                    return "30.000"
                elif service == "Servis Ringan":
                    return "100.000"
                elif service == "Servis Besar":
                    return "180.000"
                elif service == "Servis Kelistrikan":
                    return "115.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "125-150 CC":
                if service == "Servis Pengereman":
                    return "40.000"
                elif service == "Servis Ringan":
                    return "150.000"
                elif service == "Servis Besar":
                    return "250.000"
                elif service == "Servis Kelistrikan":
                    return "150.000"
                elif service == "Ganti Oli":
                    return "20.000"

        elif motor == "Sport":
            if cc == "150-200 CC":
                if service == "Servis Pengereman":
                    return "50.000"
                elif service == "Servis Ringan":
                    return "150.000"
                elif service == "Servis Besar":
                    return "250.000"
                elif service == "Servis Kelistrikan":
                    return "175.000"
                elif service == "Ganti Oli":
                    return "20.000"
            if cc == "200-250 CC":
                if service == "Servis Pengereman":
                    return "50.000"
                elif service == "Servis Ringan":
                    return "150.000"
                elif service == "Servis Besar":
                    return "300.000"
                elif service == "Servis Kelistrikan":
                    return "200.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "250 Keatas":
                if service == "Servis Pengereman":
                    return "60.000"
                elif service == "Servis Ringan":
                    return "750.000"
                elif service == "Servis Besar":
                    return "350.000"
                elif service == "Servis Kelistrikan":
                    return "250.000"
                elif service == "Ganti Oli":
                    return "20.000"
        elif motor == "2 Stroke":
            if cc == "100-125 CC":
                if service == "Servis Pengereman":
                    return "30.000"
                elif service == "Servis Ringan":
                    return "100.000"
                elif service == "Servis Besar":
                    return "180.000"
                elif service == "Servis Kelistrikan":
                    return "115.000"
                elif service == "Ganti Oli":
                    return "20.000"
            elif cc == "125-150 CC":
                if service == "Servis Pengereman":
                    return "40.000"
                elif service == "Servis Ringan":
                    return "150.000"
                elif service == "Servis Besar":
                    return "250.000"
                elif service == "Servis Kelistrikan":
                    return "150.000"
                elif service == "Ganti Oli":
                    return "20.000"
        
        # Pengkondisian jika tidak ada kombinasi yang cocok
        return "Harga tidak tersedia"


    def reserve(self):
        name = self.entry_name.get()
        date = self.entry_date.get()
        motor = self.selected_motor.get()
        cc = self.selected_cc.get()
        service = self.selected_service.get()

        if name == '' or date == '' or motor == '' or cc == '' or service == '':
            messagebox.showwarning("Peringatan", "Harap isi semua field!")
        else:
            price = self.get_price(motor, cc, service)
            message = f"Reservasi sukses!\n\nNama: {name}\nTanggal: {date}\nJenis Motor: {motor}\nCC Motor: {cc}\nJenis Servis: {service}\nEstimasi Harga: {price} IDR"
            messagebox.showinfo("Reservasi Bengkel", message)

            with open("reservasi.txt", "a") as file:
                file.write(f"Nama: {name}\nTanggal: {date}\nJenis Motor: {motor}\nCC Motor: {cc}\nJenis Servis: {service}\nEstimasi Harga: {price} IDR\n\n")

            self.entry_name.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.selected_motor.set("")
            self.selected_cc.set("")
            self.selected_service.set("")

        response = messagebox.askquestion("Reservasi Bengkel", "Apakah Anda ingin melakukan reservasi lain?")
        while response == 'no':
            self.master.destroy()
            break


if __name__ == "__main__":
    window = tk.Tk()
    app = ReservationApp(window)
    window.mainloop()