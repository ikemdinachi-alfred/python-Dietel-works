def nokia_phone():
    menu = (input("""
                        NOKIA PHONE MAIN MANU
                    **************************************           
                            1-> Phone book              
                            2-> Messages                
                            3-> Chat                    
                            4-> Call Register           
                            5-> Tones                   
                            6-> Settings               
                            7-> Call Divert             
                            8-> Games                   
                            9-> Calculator             
                            10-> Reminders              
                            11-> Clock                  
                            12-> Profiles               
                            13-> SIM services           
                    **************************************          
                    select options: """))
    match menu:
        case '1':
            print(phone_book())
        case '2':
            print(message())
        case '3':
            print(chart())
        case '4':
            print(call_register())
        case '5':
            print(tone())
        case '6':
            print(setting())
        case '7':
            print(cal_divert())
        case '8':
            print(Games())
        case '9':
            print(calculator())
        case '10':
            print(reminder())
        case '11':
            print(clock())
        case '12':
            print(profiles())
        case '13':
            print(Sim_services())
        case _:
            print(main_menu())


def phone_book():
    phone_book_menu = (input("""
       Phone Book:
********************************* 
        1-> Search
        2-> Service Nos.
        3-> Add name
        4-> Erase
        5-> Edit
        6-> Assign tone
        7-> Send b'card
        8-> Option
        9-> Speed dials
        10-> Voice tags  
*********************************    
        select option """))
    match phone_book_menu:
        case '1':
            print(' Search Activated'), print(main_menu())
        case '2':
            print(" Service Nos Activate"), print(main_menu())
        case '3':
            print(" Add name Activated"), print(main_menu())
        case '4':
            print(" Erase Activated "), print(main_menu())
        case '5':
            print(" Edit Activated "), print(main_menu())
        case '6':
            print(" Assign tone Activated "), print(main_menu())
        case '7':
            print(" end b'card is Activated "), print(main_menu())
        case '9':
            print(" Speed dail activated "), print(main_menu())
        case '10':
            print("voice tag activated"), print(main_menu())
        case '8':
            print(options())


def options():
    option_menu = (input("""
             Option Activated                  
            1-> Type of view
            2-> Memory Status 
            Select Option """))
    match option_menu:
        case '1':
            print("Type of view Activated"), print(main_menu())
        case '2':
            print("Memory Status Activated"), print(main_menu())
        case _:
            print(options())


def main_menu():
    going_back = (input(" press 1 to go back to main menu:  "))
    if going_back == '1': print(nokia_phone())


def message():
    message_menu = (input("""
                                Message    
                 **************************************                      
                            1-> Write messages
                            2-> Inbox
                            3-> Outbox
                            4-> Picture messages
                            5-> Templates
                            6-> Smileys
                            7-> Message settings
                            8-> info service
                            9-> Voice mailbox number
                            10. Service command editor
                 **************************************                                    
                            Select option:  """))
    match message_menu:
        case '1':
            print("Write message..."), print(main_menu())
        case '2':
            print(" welcome to inbox "), print(main_menu())
        case '3':
            print("Outbox Activated "), print(main_menu())
        case '4':
            print("picture message activated."), print(main_menu())
        case '5':
            print("Templates mode is active "), print(main_menu())
        case '6':
            print("smileys activated "), print(main_menu())
        case '8':
            print("info Service Activated "), print(main_menu())
        case '9':
            print("Voice mailbox number Activated"), print(main_menu())
        case '10':
            print("Service command editor Activated "), print(main_menu())
        case '7':
            print(message_setting())


def message_setting():
    message_setting_menu = (input("""
     Message setting
          1-> Set
          2-> Common
          select option:  """))
    match message_setting_menu:
        case '1':
            print(set())
        case '2':
            print(common())
        case _:
            print("Wrong input, try again "), print(main_menu())


def set():
    set_menu = (input("""
            Set1
        1-> Message Centre number
        2-> Message sent as
        3-> Message validity
        select option: """))
    match set_menu:
        case '1':
            print("Message Centre number"), print(main_menu())
        case '2':
            print("Message sent as ..."), print(main_menu())
        case '3':
            print("Message validity.."), print(main_menu())
        case _:
            print(" wrong entry try agan"), print(main_menu())


def common():
    common_menu = (input("""
     Common 
     1-> Delivery report
     2-> Reply via same centre
     3-> Character Support
       select Option:    """))
    match common_menu:
        case '1':
            print(" Delivery report..Activated"), print(main_menu())
        case '2':
            print(" Reply via same centre..Activated"), print(main_menu())
        case '3':
            print(" Character Support.. Activated"), print(main_menu())
        case _:
            print(main_menu())


def chart():
    print("chart"), print(main_menu())


def call_register():
    chart_menu = input("""
************************************** 
     Call register    
        1-> Missed calls
        2-> Received Calls
        3-> Dialled numbers
        4-> Erase recent call lists
        5-> Show call duration
        6-> Show call cost
        7-> Call cost settings
        8-> prepaid credit   
 **************************************                                    
        select options:  """)
    match chart_menu:
        case '1':
            print(" Missed calls"), print(main_menu())
        case '2':
            print(" Received calls"), print(main_menu())
        case '3':
            print(" Dialled numbers"), print(main_menu())
        case '4':
            print("Erase recent call list"), print(main_menu())
        case '5':
            print(show_call_duration())
        case '6':
            print(show_call_cost())
        case '7':
            print(call_cost_setting())
        case '8':
            print(" prepaid credit"), print(main_menu())
        case _:
            print(print(main_menu()))


def call_cost_setting():
    call_cost_setting_menu = input("""
    Call cost Settings
                                                                    
        1->call cost limit
        2-> Show  costs in
        select option:  """)
    match call_cost_setting_menu:
        case '1':
            print(" calls cost limit"), print(main_menu())
        case '2':
            print(" show costs in "), print(main_menu())
        case _:
            print(main_menu())


def show_call_duration():
    show_call_duration_menu = input("""
     **********************************
        Show call duration                               
         1-> last call duration
         2-> All call's duration
         3-> Received call's duration
         4-> Dialled calls duration
         5-> Clear timers
     **********************************
            select options:  """)
    match show_call_duration_menu:
        case '1':
            print(" last call duration"), print(main_menu())
        case '2':
            print(" All call's duration "), print(main_menu())
        case '3':
            print(" Received call's duration"), print(main_menu())
        case '4':
            print(" Dialled calls duration"), print(main_menu())
        case '5':
            print("Clear timers"), print(main_menu())
        case _:
            print(main_menu())


def show_call_cost():
    show_call_cost_menu = input("""
     Show call cost
        1-> Last call cost
        2-> All call's cost
        3-> Clear counters
        select option:  """)
    match show_call_cost_menu:
        case '1':
            print(" Last calls cost"), print(main_menu())
        case '2':
            print(" All call's cost"), print(main_menu())
        case '3':
            print(" Clear counters"), print(main_menu())
        case _:
            print(main_menu())


def tone():
    tone_menu = input("""
    
    Tones
      1->Ringing tone
      2->Ringing Volume
      3-> Incoming call alert
      4-> Composer
      5-> Message alert tone
      6-> Keypad tones
      7-> Warning and game tones
      8-> Vibrating alert
      9-> Screen saver
       select options: """)
    match tone_menu:
        case '1':
            print(" Ringing tone"), print(main_menu())
        case '2':
            print(" Ringing Volume"), print(main_menu())
        case '3':
            print("Incoming call alert"), print(main_menu())
        case '4':
            print(" composer "), print(main_menu())
        case '5':
            print("Message Message alert tone"), print(main_menu())
        case '6':
            print("Keypad tones"), print(main_menu())
        case '7':
            print(" Warning and game  tones"), print(main_menu())
        case '8':
            print("Vibrating alert"), print(main_menu())
        case '9':
            print("Screen saver"), print(main_menu())
        case _:
            print(main_menu())


def setting():
    setting_menu = input("""
    Setting
    1-> Call setting
    2-> Phone setting
    3-> security setting
    4-> Restore factory settings
       select option: """)
    match setting_menu:
        case '1':
            print(call_setting())
        case '2':
            print(phone_setting())
        case '3':
            print(setting())
        case '4':
            print("Restore factory setting"), print(main_menu())


def call_setting():
    call_setting_menu = input("""
    Call setting
    1-> Automatic redial
    2-> Speed dialling
    3-> Call waiting options
    4-> Own number sending
    5-> Phone line in use
    6-> Automatic answer
    select option: """)
    match call_setting_menu:
        case 1:
            print(" Automatic redial"), print(main_menu())
        case 2:
            print(" speed dialling"), print(main_menu())
        case 3:
            print(" Call waiting option"), print(main_menu())
        case 4:
            print("Own number sending"), print(main_menu())
        case 5:
            print("Phone line in use"), print(main_menu())
        case 6:
            print("Automatic answer"), print(main_menu())
        case _:
            print(main_menu())


def phone_setting():
    phone_setting_menu = input("""
    Phone Setting:
    1-> Language
    2-> Cell info display
    3-> Welcome note
    4-> Network selection
    5-> Lights
    6-> Confirm SIM service action
    select Option:  """)
    match phone_setting_menu:
        case '1':
            print("language Active"), print(main_menu())
        case '2':
            print("cell info display"), print(main_menu())
        case '3':
            print("welcome"), print(main_menu())
        case '4':
            print("Network selection"), print(main_menu())
        case '5':
            print("Welcome to Lights"), print(main_menu())
        case '6':
            print("Confirm SIM service action"), print(main_menu())
        case _:
            print(main_menu())


def security_setting():
    security_setting_menu = input("""
        Security setting:
         1-> PIN code request
         2-> Call barring service
         3-> Fixed dialling
         4-> Closed user group
         5-> Phone Security
         6-> Change access codes    
    
        select option:   """)
    match security_setting_menu:
        case '1':
            print(" PIN code request Active"), print(main_menu())
        case '2':
            print("Call barring service"), print(main_menu())
        case '3':
            print("Fixed dialling active"), print(main_menu())
        case '4':
            print("Closed user group"), print(main_menu())
        case '5':
            print("Phone security"), print(main_menu())
        case '6':
            print("Change access code"), print(main_menu())
        case _:
            print(main_menu())


def cal_divert():
    print("call divert activated"), print(main_menu())


def Games():
    print("enjoy wonderful games next time we come your way"), print(main_menu())


def addition():
    number1 = int(input("Enter first Number: "))
    number2 = int(input("Enter second Number: "))
    add = (number1 + number2)
    print(f'The result is = {add}')


def subtraction():
    number1 = int(input("Enter first Number: "))
    number2 = int(input("Enter second Number: "))
    answer = number1 - number2
    print(f'The result is = {answer}')


def multiplication():
    number1 = int(input("Enter first Number: "))
    number2 = int(input("Enter second Number: "))
    result = number1 * number2
    print(f'The result is = {result}')


def square_root():
    number1 = int(input("Enter Number: "))
    square = number1 * number1
    print(f'The square of {number1} is = {square}')



def calculator():
    calculator_menu = input("""
   1-> Addition
   2-> subtraction
   3-> multiplication
   4-> square root
   5-> others
   select option:   """)

    match calculator_menu:
        case '1':
            print(addition()), print(main_menu())
        case '2':
            print(subtraction()), print(main_menu())
        case '3':
            print(multiplication()), print(main_menu())
        case '4':
            print(square_root()), print(main_menu())
        case '5':
            print("other options are being updated 89%..... check again"), print(main_menu())
        case _:
            print("invalid input"), print(main_menu())


def reminder():
    print("welcome to reminder"), print(main_menu())


def clock():
    clock_menu = input("""
     Clock:
    1-> Alarm clock
    2-> Clock setting
    3-> Date setting
    4-> Stopwatch
    5-> Countdown timer
    6-> Auto update of date and time
    select option:   """)

    match clock_menu:
        case '1':
            print("Alarm clock"), print(main_menu())
        case '2':
            print("Clock setting"), print(main_menu())
        case '3':
            print("Date setting"), print(main_menu())
        case '4':
            print("Stopwatch"), print(main_menu())
        case '5':
            print("Countdown timer"), print(main_menu())
        case '6':
            print("Auto update of date and time"), print(main_menu())
        case _:
            print(main_menu())


def profiles():
    print("profiles being updated "), print(main_menu())


def Sim_services():
    print("sim services activated"), print(main_menu())


print(nokia_phone())
