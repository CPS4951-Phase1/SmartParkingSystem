from main import ParkingLot
import tkinter as tk

class ParkingLotGUI:
    def __init__(self, capacity, rate):
        self.parking_lot = ParkingLot(capacity, rate)
        self.window = tk.Tk()
        self.window.title("Parking Lot")

        # 停车功能
        tk.Label(self.window, text="Enter car number:").grid(row=0, column=0)
        self.car_number_entry = tk.Entry(self.window)
        self.car_number_entry.grid(row=0, column=1)
        tk.Button(self.window, text="Park", command=self.park_car).grid(row=0, column=2)
        self.parking_result = tk.StringVar()
        tk.Label(self.window, textvariable=self.parking_result).grid(row=1, column=0, columnspan=3)

        # 取车功能
        tk.Label(self.window, text="Enter car number:").grid(row=2, column=0)
        self.unpark_entry = tk.Entry(self.window)
        self.unpark_entry.grid(row=2, column=1)
        tk.Button(self.window, text="Unpark", command=self.unpark_car).grid(row=2, column=2)
        self.unpark_result = tk.StringVar()
        tk.Label(self.window, textvariable=self.unpark_result).grid(row=3, column=0, columnspan=3)

        # 停车场状态功能
        tk.Button(self.window, text="Parking Lot Status", command=self.show_parking_lot_status).grid(row=4, column=0)
        self.parking_lot_status = tk.StringVar()
        tk.Label(self.window, textvariable=self.parking_lot_status).grid(row=5, column=0, columnspan=3)

        # 停车记录功能
        tk.Button(self.window, text="Parking Records", command=self.show_parking_records).grid(row=6, column=0)
        self.parking_records = tk.StringVar()
        tk.Label(self.window, textvariable=self.parking_records).grid(row=7, column=0, columnspan=3)

        # 查找记录功能
        tk.Label(self.window, text="Enter car number:").grid(row=8, column=0)
        self.search_record_entry = tk.Entry(self.window)
        self.search_record_entry.grid(row=8, column=1)
        tk.Button(self.window, text="Search Record", command=self.search_record).grid(row=8, column=2)
        self.search_record_result = tk.StringVar()
        tk.Label(self.window, textvariable=self.search_record_result).grid(row=9, column=0, columnspan=3)

        # 清理记录功能
        tk.Label(self.window, text="Enter days:").grid(row=10, column=0)
        self.clear_days_entry = tk.Entry(self.window)
        self.clear_days_entry.grid(row=10, column=1)
        tk.Button(self.window, text="Clear Records", command=self.clear_records).grid(row=10, column=2)
        self.clear_records_result = tk.StringVar()
        tk.Label(self.window, textvariable=self.clear_records_result).grid(row=11, column=0, columnspan=3)

    def park_car(self):
        car_number = self.car_number_entry.get()
        result = self.parking_lot.park(car_number)
        self.parking_result.set(result)

    def unpark_car(self):
        car_number = self.unpark_entry.get()
        result = self.parking_lot.unpark(car_number)
        self.unpark_result.set(result)

    def show_parking_lot_status(self):
        status = self.parking_lot.get_status()
        self.parking_lot_status.set(status)

    def show_parking_records(self):
        records = self.parking_lot.get_records()
        self.parking_records.set(records)

    def search_record(self):
        car_number = self.search_record_entry.get()
        result = self.parking_lot.search_record(car_number)
        self.search_record_result.set(result)

    def clear_records(self):
        days = int(self.clear_days_entry.get())
        result = self.parking_lot.clear_records(days)
        self.clear_records_result.set(result)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    capacity = 10
    rate = 1.0
    gui = ParkingLotGUI(capacity, rate)
    gui.run()