import tkinter as tk
from tkinter import ttk


class convert():
    def __init__(self, u_input):
        self.u_input = u_input

    # ---------- Temperature ----------
    class temp():
        @staticmethod
        def fromcelciustofahrenheit(value):
            return value * 1.8 + 32

        @staticmethod
        def fromfahrenheittocelcius(value):
            return (value - 32) * 5 / 9

    # ---------- Data ----------
    class data():
        @staticmethod
        def fromkbtomb(value):
            return value / 1024

        @staticmethod
        def frommbtokb(value):
            return value * 1024

        @staticmethod
        def frommbtogb(value):
            return value / 1024

        @staticmethod
        def fromgbtomb(value):
            return value * 1024

        @staticmethod
        def fromgbtokb(value):
            return value * 1024 * 1024

        @staticmethod
        def fromkbtob(value):
            return value * 1024

    # ---------- Distance ----------
    class distance():
        @staticmethod
        def frommmtocm(value):
            return value / 10

        @staticmethod
        def fromcmtom(value):
            return value / 100

        @staticmethod
        def frommtokm(value):
            return value / 1000

        @staticmethod
        def fromkmtom(value):
            return value * 1000

        @staticmethod
        def frommtocm(value):
            return value * 100

        @staticmethod
        def fromcmtomm(value):
            return value * 10


# ---------------- GUI ----------------

CONVERTERS = {
    "Temperature": {
        "Celcius -> Fahrenheit": (convert.temp.fromcelciustofahrenheit, "°C", "°F"),
        "Fahrenheit -> Celcius": (convert.temp.fromfahrenheittocelcius, "°F", "°C"),
    },
    "Data": {
        "Kilobyte -> Megabyte": (convert.data.fromkbtomb, "KB", "MB"),
        "Megabyte -> Kilobyte": (convert.data.frommbtokb, "MB", "KB"),
        "Megabyte -> Gigabyte": (convert.data.frommbtogb, "MB", "GB"),
        "Gigabyte -> Megabyte": (convert.data.fromgbtomb, "GB", "MB"),
        "Gigabyte -> Kilobyte": (convert.data.fromgbtokb, "GB", "KB"),
        "Kilobyte -> Byte":     (convert.data.fromkbtob, "KB", "B"),
    },
    "Distance": {
        "Millimeter -> Centimeter": (convert.distance.frommmtocm, "mm", "cm"),
        "Centimeter -> Meter":      (convert.distance.fromcmtom, "cm", "m"),
        "Meter -> Kilometer":       (convert.distance.frommtokm, "m", "km"),
        "Kilometer -> Meter":       (convert.distance.fromkmtom, "km", "m"),
        "Meter -> Centimeter":      (convert.distance.frommtocm, "m", "cm"),
        "Centimeter -> Millimeter": (convert.distance.fromcmtomm, "cm", "mm"),
    },
}


class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Converter")
        self.geometry("420x320")
        self.resizable(False, False)

        self.category_var = tk.StringVar(value="Temperature")
        self.conversion_var = tk.StringVar()
        self.input_var = tk.StringVar()
        self.result_var = tk.StringVar(value="—")

        self._build_ui()
        self._on_category_change()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 6}

        # Category
        ttk.Label(self, text="Category:").grid(row=0, column=0, sticky="w", **pad)
        cat_menu = ttk.Combobox(
            self, textvariable=self.category_var,
            values=list(CONVERTERS.keys()), state="readonly", width=25
        )
        cat_menu.grid(row=0, column=1, **pad)
        cat_menu.bind("<<ComboboxSelected>>", lambda e: self._on_category_change())

        # Conversion
        ttk.Label(self, text="Conversion:").grid(row=1, column=0, sticky="w", **pad)
        self.conv_menu = ttk.Combobox(
            self, textvariable=self.conversion_var,
            state="readonly", width=25
        )
        self.conv_menu.grid(row=1, column=1, **pad)
        self.conv_menu.bind("<<ComboboxSelected>>", lambda e: self._update_units())

        # Input
        ttk.Label(self, text="Value:").grid(row=2, column=0, sticky="w", **pad)
        self.entry = ttk.Entry(self, textvariable=self.input_var, width=27)
        self.entry.grid(row=2, column=1, **pad)
        self.entry.bind("<Return>", lambda e: self._convert())

        # Unit label
        self.unit_label = ttk.Label(self, text="")
        self.unit_label.grid(row=2, column=2, sticky="w", **pad)

        # Convert button
        ttk.Button(self, text="Convert", command=self._convert).grid(
            row=3, column=0, columnspan=3, pady=12
        )

        # Result
        ttk.Label(self, text="Result:").grid(row=4, column=0, sticky="w", **pad)
        self.result_label = ttk.Label(
            self, textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"), foreground="#1a7f37"
        )
        self.result_label.grid(row=4, column=1, columnspan=2, sticky="w", **pad)

        # Status
        self.status = ttk.Label(self, text="", foreground="red")
        self.status.grid(row=5, column=0, columnspan=3, **pad)

    def _on_category_change(self):
        convs = list(CONVERTERS[self.category_var.get()].keys())
        self.conv_menu["values"] = convs
        self.conversion_var.set(convs[0])
        self._update_units()
        self._clear()

    def _update_units(self):
        _, from_u, _ = self._current()
        self.unit_label.config(text=from_u)

    def _current(self):
        return CONVERTERS[self.category_var.get()][self.conversion_var.get()]

    def _clear(self):
        self.input_var.set("")
        self.result_var.set("—")
        self.status.config(text="")

    def _convert(self):
        self.status.config(text="")
        raw = self.input_var.get().strip()
        if not raw:
            self.status.config(text="please enter a number")
            return
        try:
            value = float(raw)
        except ValueError:
            self.status.config(text="please enter a number")
            return

        func, from_u, to_u = self._current()
        result = func(value)

        # show integer when it's clean, else round to 4 decimals
        if result == int(result):
            shown = int(result)
        else:
            shown = round(result, 4)

        self.result_var.set(f"{value} {from_u} = {shown} {to_u}")


if __name__ == "__main__":
    ConverterApp().mainloop()