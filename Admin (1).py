event = {}
non_working_rate = {}
holiday_rate = 120
employee = {'Linda', 'John', 'Lester', 'Blake'}
overtime_hrs = {'Linda':'3', 'John':'5', 'Lester': '3', 'Blake': '2'}
emp_gross = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
emp_total_deduct = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
emp_net_pay = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
sss_contrib = {'below 2000': 80,
               '2250-2749': 100,
               '2750-3249': 120,
               '3250-3749': 140,
               '3750-4249': 160,
               '4250-4749': 180,
               '4750-5249': 200,
               '5250-5749': 220,
               '5750-6249': 240,
               '6250-6749': 260,
               '6750-7249': 280,
               '7250-7749': 300,
               '7750-8249': 320,
               '8250-8749': 340,
               '8750-9249': 360,
               '9250-9749': 380,
               '9750-10249': 400,
               '10250-10749': 420,
               '10750-11249': 440,
               '11250-11749': 460,
               '11750-12249': 480,
               '12250-12749': 500,
               '12750-13249': 520,
               '13250-13749': 540,
               '13750-14249': 560,
               '14250-14749': 580, 
               '14750-15249': 600,
               '15250-15749': 620,
               '15750-16249': 640,
               '16250-16749': 660,
               '16750-17249': 680,
               '17250-17749': 700,
               '17750-18249': 720,
               '18250-18749': 740,
               '18750-19249': 760,
               '19250-19749': 780,
               '19750 and above': 800,
               }

try:
    def admin_menu():
        print("Command List:"
              " 'Payroll' ",
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
            event_guest = input("Employee Invited:")
            event[event_name].append(event_guest)
            if event_guest in event:
                non_working_rate.setdefault(event_guest, [])
                non_working_rate[event_guest].append(holiday_rate)
                for k, v in event.items():
                    print(k, v)


    def payroll():
        while True:
            emp_type = input("Type in employee name or\nType |Back| to return to menu: ")
            if emp_type == 'Back':
                admin_menu()
            elif emp_type in non_working_rate :
                num_hrs = float(input("Number of hrs. worked: "))
                print("Rate per hour: 80")
                overtime = float(overtime_hrs[emp_type])
                gross_pay = (num_hrs * 80) + (overtime * 80 * 1.25)
                if gross_pay < 2250:
                    contrib = float(sss_contrib['below 2000'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2250 and gross_pay <= 2749:
                    contrib = float(sss_contrib['2250-2749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2750 and gross_pay <= 3249:
                    contrib = float(sss_contrib['2750-3249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3250 and gross_pay <= 3749:
                    contrib = float(sss_contrib['3250-3749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3750 and gross_pay <= 4249:
                    contrib = float(sss_contrib['3750-4249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4250 and gross_pay <= 4749:
                    contrib = float(sss_contrib['4250-4749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4750 and gross_pay <= 5249:
                    contrib = float(sss_contrib['4750-5249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5250 and gross_pay <= 5749:
                    contrib = float(sss_contrib['5250-5749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5750 and gross_pay <= 6249:
                    contrib = float(sss_contrib['5750-6249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6250 and gross_pay <= 6749:
                    contrib = float(sss_contrib['6250-6749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6750 and gross_pay <= 7249:
                    contrib = float(sss_contrib['6750-7249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 7250 and gross_pay <= 7749:
                    contrib = float(sss_contrib['7250-7749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay


                elif gross_pay >= 7750 and gross_pay <= 8249:
                    contrib = float(sss_contrib['7750-8249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8250 and gross_pay <= 8749:
                    contrib = float(sss_contrib['8250-8749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8750 and gross_pay <= 9249:
                    contrib = float(sss_contrib['8750-9249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9250 and gross_pay <= 9749:
                    contrib = float(sss_contrib['9250-9749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9750 and gross_pay <= 10249:
                    contrib = float(sss_contrib['9750-10249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10250 and gross_pay <= 10749:
                    contrib = float(sss_contrib['10250-10749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10750 and gross_pay <= 11249:
                    contrib = float(sss_contrib['10750-11249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11250 and gross_pay <= 11749:
                    contrib = float(sss_contrib['11250-11749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11750 and gross_pay <= 12249:
                    contrib = float(sss_contrib['11750-12249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12250 and gross_pay <= 12749:
                    contrib = float(sss_contrib['12250-12749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12750 and gross_pay <= 13249:
                    contrib = float(sss_contrib['12750-13249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13250 and gross_pay <= 13749:
                    contrib = float(sss_contrib['13250-13749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13750 and gross_pay <= 14249:
                    contrib = float(sss_contrib['13750-14249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14250 and gross_pay <= 14749:
                    contrib = float(sss_contrib['14250-14749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14750 and gross_pay <= 15249:
                    contrib = float(sss_contrib['14750-15249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15250 and gross_pay <= 15749:
                    contrib = float(sss_contrib['15250-15749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15750 and gross_pay <= 16249:
                    contrib = float(sss_contrib['15750-16249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16250 and gross_pay <= 16749:
                    contrib = float(sss_contrib['16250-16749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16750 and gross_pay <= 17249:
                    contrib = float(sss_contrib['16750-17249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17250 and gross_pay <= 17749:
                    contrib = float(sss_contrib['17250-17749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17750 and gross_pay <= 18249:
                    contrib = float(sss_contrib['17750-18249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18250 and gross_pay <= 18749:
                    contrib = float(sss_contrib['18250-18749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18750 and gross_pay <= 19249:
                    contrib = float(sss_contrib['18750-19249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 19250 and gross_pay <= 19749:
                    contrib = float(sss_contrib['19250-19749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                else:
                    contrib = float(sss_contrib['19750 and above'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay
            else:
                num_hrs = float(input("Number of hrs. worked: "))
                print("Rate per hour: 80")
                overtime = float(overtime_hrs[emp_type])
                gross_pay = (num_hrs * 80) + (overtime * 80 * 1.25)
                if gross_pay < 2250:
                    contrib = float(sss_contrib['below 2000'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2250 and gross_pay <= 2749:
                    contrib = float(sss_contrib['2250-2749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 2750 and gross_pay <= 3249:
                    contrib = float(sss_contrib['2750-3249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3250 and gross_pay <= 3749:
                    contrib = float(sss_contrib['3250-3749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 3750 and gross_pay <= 4249:
                    contrib = float(sss_contrib['3750-4249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4250 and gross_pay <= 4749:
                    contrib = float(sss_contrib['4250-4749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 4750 and gross_pay <= 5249:
                    contrib = float(sss_contrib['4750-5249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5250 and gross_pay <= 5749:
                    contrib = float(sss_contrib['5250-5749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 5750 and gross_pay <= 6249:
                    contrib = float(sss_contrib['5750-6249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6250 and gross_pay <= 6749:
                    contrib = float(sss_contrib['6250-6749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 6750 and gross_pay <= 7249:
                    contrib = float(sss_contrib['6750-7249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 7250 and gross_pay <= 7749:
                    contrib = float(sss_contrib['7250-7749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay


                elif gross_pay >= 7750 and gross_pay <= 8249:
                    contrib = float(sss_contrib['7750-8249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8250 and gross_pay <= 8749:
                    contrib = float(sss_contrib['8250-8749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 8750 and gross_pay <= 9249:
                    contrib = float(sss_contrib['8750-9249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9250 and gross_pay <= 9749:
                    contrib = float(sss_contrib['9250-9749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 9750 and gross_pay <= 10249:
                    contrib = float(sss_contrib['9750-10249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10250 and gross_pay <= 10749:
                    contrib = float(sss_contrib['10250-10749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 10750 and gross_pay <= 11249:
                    contrib = float(sss_contrib['10750-11249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11250 and gross_pay <= 11749:
                    contrib = float(sss_contrib['11250-11749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 11750 and gross_pay <= 12249:
                    contrib = float(sss_contrib['11750-12249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12250 and gross_pay <= 12749:
                    contrib = float(sss_contrib['12250-12749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 12750 and gross_pay <= 13249:
                    contrib = float(sss_contrib['12750-13249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13250 and gross_pay <= 13749:
                    contrib = float(sss_contrib['13250-13749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 13750 and gross_pay <= 14249:
                    contrib = float(sss_contrib['13750-14249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14250 and gross_pay <= 14749:
                    contrib = float(sss_contrib['14250-14749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 14750 and gross_pay <= 15249:
                    contrib = float(sss_contrib['14750-15249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15250 and gross_pay <= 15749:
                    contrib = float(sss_contrib['15250-15749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 15750 and gross_pay <= 16249:
                    contrib = float(sss_contrib['15750-16249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16250 and gross_pay <= 16749:
                    contrib = float(sss_contrib['16250-16749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 16750 and gross_pay <= 17249:
                    contrib = float(sss_contrib['16750-17249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17250 and gross_pay <= 17749:
                    contrib = float(sss_contrib['17250-17749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 17750 and gross_pay <= 18249:
                    contrib = float(sss_contrib['17750-18249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18250 and gross_pay <= 18749:
                    contrib = float(sss_contrib['18250-18749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 18750 and gross_pay <= 19249:
                    contrib = float(sss_contrib['18750-19249'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                elif gross_pay >= 19250 and gross_pay <= 19749:
                    contrib = float(sss_contrib['19250-19749'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay

                else:
                    contrib = float(sss_contrib['19750 and above'])
                    SSS = float(gross_pay - contrib)
                    PhilHealth = float(gross_pay * 0.02)
                    total_deduct = float(SSS + PhilHealth)
                    net_pay = float(gross_pay - total_deduct)
                    emp_gross[emp_type] = gross_pay
                    emp_total_deduct[emp_type] = total_deduct
                    emp_net_pay[emp_type] = net_pay


    def print_pay():
        emp_name = input("Type in name or\nType |Back| to return to menu: ")
        if emp_name in employee:
            conv_gross = float(emp_gross[emp_name])
            conv_tdeduct = float(emp_total_deduct[emp_name])
            conv_netpay = float(emp_net_pay[emp_name])
            print('Employee Name: {}'.format(emp_name))
            print('Gross Pay: {:.2f}'.format(conv_gross))
            print('Total Deductions: {:.2f}'.format(conv_tdeduct))
            print('Net Pay: {:.2f}'.format(conv_netpay))


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

