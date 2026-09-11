import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class convert():
    def __init__(self, u_input):
        self.u_input = u_input
    
    def show_temp_converters():
        while True:
            clear()
            print("1. from celcius to fahrenheit")
            print("2. from fahrenheit to celcius")
            print("0. back")
            user_choice = input("enter a choice: ")
            match user_choice:
                case "1":
                    clear()
                    convert.temp.fromcelciustofahrenheit()
                case "2":
                    clear()
                    convert.temp.fromfahrenheittocelcius()
                case "0":
                    clear()
                    break
                case _:
                    clear()
                    print("invalid option")
                    time.sleep(1.5)
                    clear()
                    continue

    def show_distance_converters():
        clear()
        while True:
             print("1. from millimeter to centimeter")
             print("2. from centimeter to meter")
             print("3. from meter to kilometer")
             print("4. from kilometer to meter")
             print("5. from meter to centimeter")
             print("6. from centimeter to millimeter")
             print("0. back")
             user_choice = input("enter a choice: ")
             match user_choice:
                 case "1":
                     clear()
                     convert.distance.frommmtocm()
                 case "2":
                     clear()
                     convert.distance.fromcmtom()
                 case "3":
                     clear()
                     convert.distance.frommtokm()
                 case "4":
                     clear()
                     convert.distance.fromkmtom()
                 case "5":
                     clear()
                     convert.distance.frommtocm()
                 case "6":
                     clear()
                     convert.distance.fromcmtomm()
                 case "0":
                     clear()
                     break
                 case _:
                     clear()
                     print("invalid option")
                     time.sleep(1.5)
                     clear()
                     continue

    def show_data_converters():
        while True:
             clear()
             print("1. from kilobyte to megabyte")
             print("2. from megabyte to kilobyte")
             print("3. from megabyte to gigabyte")
             print("4. from gigabyte to megabyte")
             print("5. from gigabyte to kilobyte")
             print("6. from kilobyte to byte")
             print("0. back")
             user_choice = input("enter a choice: ")
             match user_choice:
                 case "1":
                     clear()
                     convert.data.fromkbtomb()
                 case "2":
                     clear()
                     convert.data.frommbtokb()
                 case "3":
                     clear()
                     convert.data.frommbtogb()
                 case "4":
                     clear()
                     convert.data.fromgbtomb()
                 case "5":
                     clear()
                     convert.data.fromgbtokb()
                 case "6":
                     clear()
                     convert.data.fromkbtob()
                 case "0":
                     clear()
                     break
                 case _:
                     clear()
                     print("invalid option")
                     time.sleep(1.5)
                     clear()
                     continue

    def print_converters():
        while True:
            clear()
            print("welcome to converter app")
            print("1. Temperatures")
            print("2. Data")
            print("3. distance")
            print("4. exit")
            user_choice = input("enter a choice: ")
            match user_choice:
                case "1":
                    clear()
                    convert.show_temp_converters()
                case "2":
                    clear()
                    convert.show_data_converters()
                case "3":
                    clear()
                    convert.show_distance_converters()
                case "4":
                    clear()
                    print("goodbye")
                    time.sleep(1.5)
                    clear()
                    break
                case _:
                    clear()
                    print("invalid option")
                    time.sleep(1.5)
                    clear()
                    continue

    class temp(): 
     @staticmethod
     def fromcelciustofahrenheit():
        while True: 
         try: 
             clear()
             u_input = int(input("enter degree in celcius: "))
         except ValueError:
             clear()
             print("please enter a number")
             time.sleep(1.5)
             continue    
         result = u_input * 1.8 + 32
         print(f"{u_input} degress celcius equals {round(result)} fahrenheit")
         time.sleep(2)
         break
     @staticmethod
     def fromfahrenheittocelcius():
        while True: 
             try:
              clear()
              u_input = int(input("enter degree in fahrenheit: "))
             except ValueError:
              clear()
              print("please enter a number")
              time.sleep(1.5)
              continue
             result = (u_input - 32) * 5 / 9
             print(f"{u_input} degrees in fahrenheit equals {round(result)} degress in celcius")
             time.sleep(2)
             break

    class data():
        def fromkbtomb():
           while True: 
             try:
                 clear()
                 u_input = int(input("enter kilobyte: "))
             except ValueError:
                 clear()
                 print("please enter a number")
                 time.sleep(1.5)
                 continue
             result = u_input / 1024
             print(f"{u_input} KB in megabytes are {result} MB")
             time.sleep(2)
             break
        def frommbtokb():
           while True: 
             try:
                 clear()
                 u_input = int(input("enter megabytes: "))
             except ValueError:
                 clear()
                 print("please enter a number")
                 time.sleep(1.5)
                 continue
             result = u_input * 1024
             print(f"{u_input} MB equals {result} KB")
             time.sleep(2)
             break
        def frommbtogb():
            while True:
                try:
                    clear()
                    u_input = int(input("enter megabytes: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input / 1024
                print(f"{u_input} MB equals {result} GB ")
                time.sleep(2)
                break

        def fromgbtomb():
            while True:
                try:
                    clear()
                    u_input = int(input("enter gigabytes: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input * 1024
                print(f"{u_input} GB equals {result} MB")
                time.sleep(2)
                break

        def fromgbtokb():
            while True:
                try:
                    clear()
                    u_input = int(input("enter gigabytes: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input * 1024 * 1024
                print(f"{u_input} GB equals {result} KB")
                time.sleep(2)
                break

        def fromkbtob():
            while True:
                try:
                    clear()
                    u_input = int(input("enter kilobytes: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input * 1024
                print(f"{u_input} KB equals {result} bytes")
                time.sleep(2)
                break    

    class distance():
        def frommmtocm():
            while True:
                try:
                    clear()
                    u_input = int(input("enter millimeter:  "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input / 10
                print(f"{u_input} millimeter equals {result} cm")
                time.sleep(2)
                break
        def fromcmtom():
            while True:
                try:
                    clear()
                    u_input = int(input("enter centimeter: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input / 100
                print(f"{u_input} centimeters equals {result} meter")
                time.sleep(2)
                break
        def frommtokm():
            while True:
                try:
                    clear()
                    u_input = int(input("enter meter: "))
                except ValueError:
                    clear()
                    print("please enter a number")
                    time.sleep(1.5)
                    continue
                result = u_input / 1000
                print(f"{u_input} meters equals {result} km")
                time.sleep(2)
                break                                            
        def fromkmtom():
         while True:
             try:
                 clear()
                 u_input = int(input("enter kilometer:  "))
             except ValueError:
                 clear()
                 print("please enter a number")
                 time.sleep(1.5)
                 continue
             result = u_input * 1000
             print(f"{u_input} kilometers equals {result} meters")
             time.sleep(2)
             break

        def frommtocm():
         while True:
             try:
                 clear()
                 u_input = int(input("enter meter:  "))
             except ValueError:
                 clear()
                 print("please enter a number")
                 time.sleep(1.5)
                 continue
             result = u_input * 100
             print(f"{u_input} meters equals {result} cm")
             time.sleep(2)
             break

        def fromcmtomm():
         while True:
             try:
                 clear()
                 u_input = int(input("enter centimeter:  "))
             except ValueError:
                 clear()
                 print("please enter a number")
                 time.sleep(1.5)
                 continue
             result = u_input * 10
             print(f"{u_input} centimeters equals {result} mm")
             time.sleep(2)
             break


if __name__ == "__main__":
    convert.print_converters()