import datetime
import tkinter as tk

class ParkingLot:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.spots = [None] * capacity
        self.waiting_list = []
        self.records = {}

    def park(self, car):
        if None in self.spots:
            spot_num = self.spots.index(None)
            self.spots[spot_num] = car
            self.records[car] = datetime.datetime.now()
            print(f"Car {car} is parked in spot {spot_num+1}.")
            return f"Car {car} is parked in spot {spot_num+1}."
        else:
            self.waiting_list.append(car)
            print(f"Parking lot is full. Car {car} added to waiting list.")
            return f"Parking lot is full. Car {car} added to waiting list."

    def unpark(self, car):
        if car in self.spots:
            spot_num = self.spots.index(car)
            self.spots[spot_num] = None
            start_time = self.records.pop(car)
            end_time = datetime.datetime.now()
            duration = end_time - start_time
            cost = duration.total_seconds() / 3600 * self.rate
            print(f"Car {car} has left the parking spot {spot_num+1}.")
            print(f"Duration: {duration.total_seconds()/60:.2f} minutes, cost: ${cost:.2f}")
            self._check_waiting_list()
            return f"Car {car} has left the parking spot {spot_num+1}.\nDuration: {duration.total_seconds()/60:.2f} minutes, cost: ${cost:.2f}"
        else:
            print(f"Car {car} is not parked in this parking lot.")
            return f"Car {car} is not parked in this parking lot."

    def _check_waiting_list(self):
        if self.waiting_list and None in self.spots:
            car = self.waiting_list.pop(0)
            self.park(car)

    def get_status(self):
        status = f"Parking lot status: {self.spots}"
        print(status)
        return status

    def get_records(self):
        records = ""
        for car, start_time in self.records.items():
            records += f"Car {car} is parked since {start_time}\n"
        print(records)
        return records

    def search_record(self, car):
        if car in self.records:
            start_time = self.records[car]
            record = f"Car {car} is parked since {start_time}"
            print(record)
            return record
        else:
            print(f"Car {car} is not parked in this parking lot.")
            return f"Car {car} is not parked in this parking lot."

    def clear_records(self, days):
        now = datetime.datetime.now()
        for car, start_time in list(self.records.items()):
            if (now - start_time).days >= days:
                self.records.pop(car)
        msg = f"Records older than {days} days have been cleared."
        print(msg)
        return msg

