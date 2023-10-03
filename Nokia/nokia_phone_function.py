
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
        case '1': print(phone_book())
        case '2': print(message())
        case _: print(main_menu())
def phone_book():
    phone_book_menu = (input("""
       Phone Book:
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
    
        select option """))
    match phone_book_menu:
            case '1': print(' Search Activated'), print(main_menu())
            case '2': print(" Service Nos Activate"), print(main_menu())
            case '3': print(" Add name Activated"), print(main_menu())
            case '4': print(" Erase Activated "), print(main_menu())
            case '5': print(" Edit Activated "), print(main_menu())
            case '6': print(" Assign tone Activated "), print(main_menu())
            case '7': print(" end b'card is Activated "), print(main_menu())
            case '9': print(" Speed dail activated "), print(main_menu())
            case '10': print("voice tag activated"), print(main_menu())
            case '8': print(options())
def options():
    option_menu = (input("""
             Option Activated                  
                  1-> Type of view
                  2-> Memory Status 
                    Select Option """))
    match option_menu:
        case '1': print("Type of view Activated"), print(main_menu())
        case '2': print("Memory Status Activated"), print(main_menu())
        case _: print(options()), print(main_menu())


def main_menu():
    going_back = (input(" press 1 to go back to main menu:  "))
    if going_back == '1': print(nokia_phone())

def message():
    message_menu = int(input("""
                                Message                         
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
                                                    
                            Select option:  """))
    match message_menu:
        case '1': print("Write message..."), print(main_menu())
        case '2': print(" welcome to inbox "), print(main_menu())
        case '3': print("Outbox Activated "), print(main_menu())
        case '4': print("picture message activated."), print(main_menu())
        case '5': print("Templates mode is active "), print(main_menu())
        case '6': print("smileys activated "), print(main_menu())
        case '8': print("info Service Activated "), print(main_menu())
        case '9': print("Voice mailbox number Activated"), print(main_menu())
        case '10': print("Service command editor Activated "), print(main_menu())
        case '7': print(message_setting())
def message_setting():
    message_setting_menu = (input("""
     Message setting
          1-> Set
          2-> Common
          select option:  """))
    match message_setting_menu:
       case '1': print(set())
       case '2': print(common())
       case _: print("Wrong input, try again "), print(main_menu())

def set():
    set_menu = (input("""
            Set1
        1-> Message Centre number
        2-> Message sent as
        3-> Message validity
        select option: """))
    match set_menu:
        case '1': print("Message Centre number"), print(main_menu())
        case '2': print("Message sent as ..."), print(main_menu())
        case '3': print("Message validity.."), print(main_menu())
        case _: print(" wrong entry try agan"), print(main_menu())
def common():
    common_menu = (input("""
     Common 
     1-> Delivery report
     2-> Reply via same centre
     3-> Character Support
       select Option:    """))
    match common_menu:
        case '1': print(" Delivery report..Activated"), print(main_menu())
        case '2': print(" Reply via same centre..Activated"), print(main_menu())
        case '3': print(" Character Support.. Activated"), print(main_menu())
        case _:  print(main_menu())

print(nokia_phone())



    
    
    
    
