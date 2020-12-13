event ={}
employee = {'Linda', 'John', 'Lester', 'Blake'}
emp_gross = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
emp_total_deduct = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
emp_net_pay = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}

try:
    def admin_menu():
        print("Command List:"
              " 'Payroll',",
              " 'Events' ",
              " 'Print' ")

        admin_option = input("Enter command:")
        if admin_option == 'Events':
            print("EVENTS")
            events_menu()
        elif admin_option == 'Payroll':
            payroll()
        elif admin_option == 'Print':
            print_pay()
        else:
            print("Invalid Command.")


    def events_menu():
        while True:
            event_name = str(input("Enter an Event: "))
            event_time = str(input("Input Time: "))
            event_place = str(input("Input Place:"))
            event.setdefault(event_name, [])
            event[event_name].append(event_time)
            event[event_name].append(event_place)
            for k, v in event.items():
                print(k, v)

    def payroll():
        while True:
            emp_type = input("Type in employee name or\nType |Back| to return to menu: ")
            if emp_type == 'Back':
                admin_menu()
            else:
                num_hrs = float(input("Number of hrs. worked: "))
                print("Rate per hour: 80")
                overtime = float(input("Overtime(hrs.): "))
                gross_pay = (num_hrs * 80) + (overtime * 80 * 1.25)
                if gross_pay < 2250:
                    SSS = float(gross_pay - 80)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2250 and gross_pay <= 2749:
                    SSS = float(gross_pay - 100)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2750 and gross_pay <= 3249:
                    SSS = float(gross_pay - 120)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3250 and gross_pay <= 3749:
                    SSS = float(gross_pay - 140)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3750 and gross_pay <= 4249:
                    SSS = float(gross_pay - 160)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4250 and gross_pay <= 4749:
                    SSS = float(gross_pay - 180)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4750 and gross_pay <= 5249:
                    SSS = float(gross_pay - 200)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5250 and gross_pay <= 5749:
                    SSS = float(gross_pay - 220)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5750 and gross_pay <= 6249:
                    SSS = float(gross_pay - 240)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6250 and gross_pay <= 6749:
                    SSS = float(gross_pay - 260)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6750 and gross_pay <= 7249:
                    SSS = float(gross_pay - 280)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 7250 and gross_pay <= 7749:
                    SSS = float(gross_pay - 300)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 7750 and gross_pay <= 8249:
                    SSS = float(gross_pay - 320)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8250 and gross_pay <= 8749:
                    SSS = float(gross_pay - 340)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8750 and gross_pay <= 9249:
                    SSS = float(gross_pay - 360)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9250 and gross_pay <= 9749:
                    SSS = float(gross_pay - 380)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9750 and gross_pay <= 10249:
                    SSS = float(gross_pay - 400)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10250 and gross_pay <= 10749:
                    SSS = float(gross_pay - 420)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10750 and gross_pay <= 11249:
                    SSS = float(gross_pay - 440)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11250 and gross_pay <= 11749:
                    SSS = float(gross_pay - 460)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11750 and gross_pay <= 12249:
                    SSS = float(gross_pay - 480)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12250 and gross_pay <= 12749:
                    SSS = float(gross_pay - 500)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12750 and gross_pay <= 13249:
                    SSS = float(gross_pay - 520)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13250 and gross_pay <= 13749:
                    SSS = float(gross_pay - 540)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13750 and gross_pay <= 14249:
                    SSS = float(gross_pay - 560)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14250 and gross_pay <= 14749:
                    SSS = float(gross_pay - 580)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14750 and gross_pay <= 15249:
                    SSS = float(gross_pay - 600)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15250 and gross_pay <= 15749:
                    SSS = float(gross_pay - 620)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15750 and gross_pay <= 16249:
                    SSS = float(gross_pay - 640)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16250 and gross_pay <= 16749:
                    SSS = float(gross_pay - 660)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16750 and gross_pay <= 17249:
                    SSS = float(gross_pay - 680)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17250 and gross_pay <= 17749:
                    SSS = float(gross_pay - 700)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17750 and gross_pay <= 18249:
                    SSS = float(gross_pay - 720)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18250 and gross_pay <= 18749:
                    SSS = float(gross_pay - 740)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18750 and gross_pay <= 19249:
                    SSS = float(gross_pay - 760)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 19250 and gross_pay <= 19749:
                    SSS = float(gross_pay - 780)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                else:
                    SSS = float(gross_pay - 800)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

    def print_pay():
        emp_name = input("Type in name or\nType |Back| to return to menu: ")
        if emp_name in employee:
            print(emp_name, "salary" )
            print('Gross pay:', emp_gross[emp_name], "pesos")
            print('Deductions:', emp_total_deduct[emp_name], "pesos")
            print('Net pay:', emp_net_pay[emp_name], "pesos")
    admin_menu()
    events_menu()
    payroll()
    print_pay()
except ValueError:
    print("Input Invalid.")

except OSError:
    print("Error in system.")

except NameError:
    print("Variable not found.")

