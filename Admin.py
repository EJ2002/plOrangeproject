try:
    event = {}
    employee = {'Linda', 'John', 'Lester', 'Blake'}
    emp_gross = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
    emp_total_deduct = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}
    emp_net_pay = {'Linda': '', 'John': '', 'Lester': '', 'Blake': ''}


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
            print_payroll()


    def events_menu():
        print("Events Command List"
              "\nView"
              "\nCreate")


    def payroll():
        while True:
            print(employee)
            emp_type = input("Type in the name of the selected employee or\nType |Back| to return to menu: ")
            if emp_type in employee:
                pass
                num_hrs = float(input("Number of hrs. worked: "))
                rate_hr = float(input("Rate per hour: "))
                overtime = float(input("Overtime(hrs.): "))

                gross_pay = (num_hrs * rate_hr) + (overtime * rate_hr * 1.25)
                SSS = float(gross_pay * 0.033)
                PhilHealth = float(gross_pay * 0.02)
                total_deduct = float(SSS + PhilHealth)
                net_pay = float(gross_pay - total_deduct)
                emp_gross[emp_type] = gross_pay
                emp_total_deduct[emp_type] = total_deduct
                emp_net_pay[emp_type] = net_pay
            elif emp_type == 'Back':
                admin_menu()
            else:
                print("Incorrect command.")


    def print_payroll():
        emp_select = input("Name of Employee: ")
        if emp_select in employee:
            print(emp_select, "'s", 'expected salary')
            print('Gross pay:', emp_gross[emp_select], 'pesos')
            print('Deductions:', emp_total_deduct[emp_select], 'pesos')
            print('Net pay:', emp_net_pay[emp_select], 'pesos')


    admin_menu()
    print_payroll()
    events_menu()
    payroll()
except ValueError:
    print("Input Invalid.")

except OSError:
    print("Error in system.")

except NameError:
    print("Variable not found.")
