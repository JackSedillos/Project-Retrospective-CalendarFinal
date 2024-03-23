import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")

        self.main_frame = tk.Frame(self.master, bg="Green")
        self.main_frame.pack(padx=20, pady=20)

        self.calendar_frame = tk.Frame(self.main_frame, bg="lightgray")
        self.calendar_frame.pack(padx=10, pady=10)

        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Add Labels for each day of the week in self.days in the grid starting at index 1 (Column Labels)
        for i, day in enumerate(self.days):
            tk.Label(self.calendar_frame, text=day, width=10, borderwidth=2, relief="ridge").grid(row=0, column=i+1)

        self.hours = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM",
                      "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM",
                      "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]

        # Add labels for each time of the day in self.hours in the grid starting at index 1 (Row Labels)
        for i, hour in enumerate(self.hours):
            tk.Label(self.calendar_frame, text=hour, width=10, borderwidth=2, relief="ridge").grid(row=i + 1, column=0)

        # Create Hours X Days table with empty event slots
        self.event_slots = []
        for i in range(len(self.hours)):
            row = []
            for j in range(len(self.days)):
                label = tk.Label(self.calendar_frame, text="", width=20, height=2, borderwidth=1, relief="solid")
                label.grid(row=i + 1, column=j + 1)
                row.append(label)
            self.event_slots.append(row)

        self.event_frame = tk.Frame(self.main_frame)
        self.event_frame.pack(padx=10, pady=5)

        # Create a Day Label and entry point
        self.day_label = tk.Label(self.event_frame, text="Day:")
        self.day_label.grid(row=0, column=0, padx=5, pady=5)

        self.day_entry = tk.Entry(self.event_frame)
        self.day_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a Time Label and entry point
        self.time_label = tk.Label(self.event_frame, text="Time:")
        self.time_label.grid(row=0, column=2, padx=5, pady=5)

        self.time_entry = tk.Entry(self.event_frame)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Create a Description Label and entry point
        self.desc_label = tk.Label(self.event_frame, text="Description:")
        self.desc_label.grid(row=0, column=4, padx=5, pady=5)

        self.desc_entry = tk.Entry(self.event_frame)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)

        # buttom styles using ttk
        self.style = ttk.Style()
        self.style.configure('TButton', background='Green', font=('Times New Roman', 10))

        # Create an "Add Event" button to the right of all text entries, and calling ttk to use customized buttom layout
        self.add_event_button = ttk.Button(self.event_frame, text="Add Event", command=self.add_event)
        self.add_event_button.grid(row=0, column=6, padx=5, pady=5)

        # Create a "Delete Event" button to the right of add event button
        self.delete_event_button = ttk.Button(self.event_frame, text="Delete Event", command=self.delete_event)
        self.delete_event_button.grid(row=0, column=7, padx=5, pady=5)

    def add_event(self):
        # store results from text entries
        day = self.day_entry.get()
        time = self.time_entry.get()
        desc = self.desc_entry.get()
        # Return a pop-up error message using messagebox if there is an invalid day or time or if desc doesn't exist
        if day in self.days and time in self.hours and desc:
            day_index = self.days.index(day)
            time_index = self.hours.index(time)
            self.event_slots[time_index][day_index].config(text=desc)
            self.day_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error Message", "There was an error in your entry, Please re-enter a valid Day, Time, and Description")

    def delete_event(self):
        # Retreiving the results of day and time text entries
        day = self.day_entry.get()
        time = self.time_entry.get()
        # Clear the entry fields after retrieving values
        self.day_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        # Check if the day and time are valid
        if day in self.days and time in self.hours:
            day_index = self.days.index(day)
            time_index = self.hours.index(time)
            # Clear the event slot
            self.event_slots[time_index][day_index].config(text="")
        else:
            messagebox.showerror("Error Message", "There was an error in your entry, Please re-enter a valid Day and Time")


def main():
    # Create a blank GUI
    root = tk.Tk()
    # Populate GUI by running it through CalendarApp class
    CalendarApp(root)
    # Run GUI and make it interactive
    root.mainloop()


if __name__ == "__main__":
    main()