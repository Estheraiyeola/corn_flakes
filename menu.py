print(f'''
================================
    Menu Options
===============================
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
''')
userOption = input('Pick a number to proceed: ')


def main_menu():
    print(f'''
    ================================
        Menu Options
    ===============================
    1. Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    elif user_option == '2':
        messages()
    elif user_option == '3':
        chat()
    elif user_option == '4':
        call_register()
    elif user_option == '5':
        tones()
    elif user_option == '6':
        settings()
    elif user_option == '7':
        call_divert()
    elif user_option == '8':
        games()
    elif user_option == '9':
        calculator()
    elif user_option == '10':
        reminders()
    elif user_option == '11':
        clock()
    elif user_option == '12':
        profiles()
    elif user_option == '13':
        sim_services()
    else:
        print('Invalid option.')


def search():
    print(f'''
    ==================================
                Search
    ==================================
    1. Back
''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def service_nos():
    print(f'''
        ==================================
                    Service Nos
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def add_name():
    print(f'''
        ==================================
                    Add name
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def erase():
    print(f'''
        ==================================
                    Erase
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def edit():
    print(f'''
        ==================================
                    Edit
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def assign_tone():
    print(f'''
        ==================================
                    Assign tone
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def send_bcard():
    print(f'''
        ==================================
                    Send b'card
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def type_of_view():
    print(f'''
        ==================================
                    Type of view
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        options()
    else:
        print('Invalid option.')


def memory_status():
    print(f'''
        ==================================
                    Memory status
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        options()
    else:
        print('Invalid option.')


def options():
    print(f'''
        ==================================
                    Options
        ==================================
        1. Type of view
        2. Memory status
        3. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        type_of_view()
    elif user_option == '2':
        memory_status()
    elif user_option == '3':
        phone_book()
    else:
        print('Invalid option.')


def speed_dials():
    print(f'''
        ==================================
                    Speed dials
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def voice_tags():
    print(f'''
        ==================================
                    Voice tags
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_book()
    else:
        print('Invalid option.')


def phone_book():
    print(f'''
    =========================================
                Phone book
    =========================================
    1. Search
    2. Service Nos
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
    9. Speed dials
    10. Voice tags
    11. Back
''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        search()
    elif user_option == '2':
        service_nos()
    elif user_option == '3':
        add_name()
    elif user_option == '4':
        erase()
    elif user_option == '5':
        edit()
    elif user_option == '6':
        assign_tone()
    elif user_option == '7':
        send_bcard()
    elif user_option == '8':
        options()
    elif user_option == '9':
        speed_dials()
    elif user_option == '10':
        voice_tags()
    elif user_option == '11':
        main_menu()


def write_messages():
    print(f'''
        ==================================
                    Write messages
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def inbox():
    print(f'''
            ==================================
                        Inbox
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def outbox():
    print(f'''
            ==================================
                        Outbox
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def picture_messages():
    print(f'''
            ==================================
                    Picture messages
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def templates():
    print(f'''
            ==================================
                        Templates
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def smileys():
    print(f'''
            ==================================
                        Smileys
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def message_centre_number():
    print(f'''
            ==================================
                    Message centre number
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        set_()
    else:
        print('Invalid option.')


def message_sent_as():
    print(f'''
                ==================================
                        Message sent as
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        set_()
    else:
        print('Invalid option.')


def message_validity():
    print(f'''
                ==================================
                        Message validity
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        set_()
    else:
        print('Invalid option.')


def set_():
    print(f'''
            ==================================
                        Set
            ==================================
            1. Message centre number
            2. Message sent as
            3. Message validity
            4. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        message_centre_number()
    elif user_option == '2':
        message_sent_as()
    elif user_option == '3':
        message_validity()
    elif user_option == '4':
        message_settings()
    else:
        print('Invalid option.')


def delivery_reports():
    print(f'''
                ==================================
                        Delivery reports
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        common()
    else:
        print('Invalid option.')


def reply_via_same_centre():
    print(f'''
                    ==================================
                            Reply via same centre
                    ==================================
                    1. Back
                ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        common()
    else:
        print('Invalid option.')


def character_support():
    print(f'''
                    ==================================
                            Character support
                    ==================================
                    1. Back
                ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        common()
    else:
        print('Invalid option.')


def common():
    print(f'''
                ==================================
                            Common
                ==================================
                1. Delivery reports
                2. Reply via same centre
                3. Character support
                4. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        delivery_reports()
    elif user_option == '2':
        reply_via_same_centre()
    elif user_option == '3':
        character_support()
    elif user_option == '4':
        set_()
    else:
        print('Invalid option.')


def message_settings():
    print(f'''
            ==================================
                    Message settings
            ==================================
            1. Set
            2. Common
            3. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        set_()
    elif user_option == '2':
        common()
    elif user_option == '3':
        messages()
    else:
        print('Invalid option.')


def info_service():
    print(f'''
            ==================================
                        Info service
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def voice_mailbox_number():
    print(f'''
            ==================================
                    Voice mailbox number
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def service_command_editor():
    print(f'''
            ==================================
                Service command editor
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        messages()
    else:
        print('Invalid option.')


def messages():
    print(f'''
        ==================================
                    Messages
        ==================================
        1. Write messages
        2. Inbox
        3. Outbox
        4. Picture messages
        5. Templates
        6. Smileys
        7. Message settings
        8. Info service
        9. Voice mailbox number
        10. Service command editor
        11. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        write_messages()
    elif user_option == '2':
        inbox()
    elif user_option == '3':
        outbox()
    elif user_option == '4':
        picture_messages()
    elif user_option == '5':
        templates()
    elif user_option == '6':
        smileys()
    elif user_option == '7':
        message_settings()
    elif user_option == '8':
        info_service()
    elif user_option == '9':
        voice_mailbox_number()
    elif user_option == '10':
        service_command_editor()
    elif user_option == '11':
        main_menu()
    else:
        print('Invalid option.')


def chat():
    print(f'''
        ==================================
                    Chat
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def missed_calls():
    print(f'''
        ==================================
                    Missed calls
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_register()
    else:
        print('Invalid option.')


def received_calls():
    print(f'''
            ==================================
                    Received calls
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_register()
    else:
        print('Invalid option.')


def dialled_numbers():
    print(f'''
            ==================================
                    Dialled numbers
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_register()
    else:
        print('Invalid option.')


def erase_recent_call_lists():
    print(f'''
            ==================================
                Erase recent call lists
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_register()
    else:
        print('Invalid option.')


def last_call_duration():
    print(f'''
                ==================================
                        Last call duration
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_duration()
    else:
        print('Invalid option.')


def all_calls_duration():
    print(f'''
                ==================================
                        All calls' duration
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_duration()
    else:
        print('Invalid option.')


def received_calls_duration():
    print(f'''
                ==================================
                    Received calls' duration
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_duration()
    else:
        print('Invalid option.')


def dialled_calls_duration():
    print(f'''
                ==================================
                    Dialled calls' duration
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_duration()
    else:
        print('Invalid option.')


def clear_timers():
    print(f'''
                ==================================
                        Clear timers
                ==================================
                1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_duration()
    else:
        print('Invalid option.')


def show_call_duration():
    print(f'''
            ==================================
                    Show call duration
            ==================================
            1. Last call duration
            2. All call's duration
            3. Received calls' duration
            4. Dialled calls' duration
            5. Clear timers
            6. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        last_call_duration()
    elif user_option == '2':
        all_calls_duration()
    elif user_option == '3':
        received_calls_duration()
    elif user_option == '4':
        dialled_calls_duration()
    elif user_option == '5':
        clear_timers()
    elif user_option == '6':
        call_register()
    else:
        print('Invalid option.')


def last_call_cost():
    print(f'''
            ==================================
                    Last call cost
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_costs()
    else:
        print('Invalid option.')


def all_calls_cost():
    print(f'''
            ==================================
                    All calls' cost
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_costs()
    else:
        print('Invalid option.')


def clear_counters():
    print(f'''
            ==================================
                    Clear counters
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        show_call_costs()
    else:
        print('Invalid option.')


def show_call_costs():
    print(f'''
            ==================================
                    Show call costs
            ==================================
            1. Last call cost
            2. All calls' cost
            3. Clear counters
            4. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        last_call_cost()
    elif user_option == '2':
        all_calls_cost()
    elif user_option == '3':
        clear_counters()
    elif user_option == '4':
        call_register()
    else:
        print('Invalid option.')


def call_cost_limit():
    print(f'''
            ==================================
                    Call cost limit
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_cost_settings()
    else:
        print('Invalid option.')


def show_costs_in():
    print(f'''
            ==================================
                    Show costs in
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_cost_settings()
    else:
        print('Invalid option.')


def call_cost_settings():
    print(f'''
            ==================================
                    Call cost settings
            ==================================
            1. Call cost limit
            2. Show costs in
            3. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_cost_limit()
    elif user_option == '2':
        show_costs_in()
    elif user_option == '3':
        show_call_costs()
    else:
        print('Invalid option.')


def prepaid_credit():
    print(f'''
            ==================================
                    Prepaid credit
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_register()
    else:
        print('Invalid option.')


def call_register():
    print(f'''
        ==================================
                Call register
        ==================================
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
        9. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        missed_calls()
    elif user_option == '2':
        received_calls()
    elif user_option == '3':
        dialled_numbers()
    elif user_option == '4':
        erase_recent_call_lists()
    elif user_option == '5':
        show_call_duration()
    elif user_option == '6':
        show_call_costs()
    elif user_option == '7':
        call_cost_settings()
    elif user_option == '8':
        prepaid_credit()
    elif user_option == '9':
        main_menu()
    else:
        print('Invalid option.')


def ringing_tone():
    print(f'''
        ==================================
                    Ringing tone
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def ringing_volume():
    print(f'''
        ==================================
                Ringing volume
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def incoming_call_alert():
    print(f'''
            ==================================
                    Incoming call alert
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def composer():
    print(f'''
        ==================================
                    Composer
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def message_alert_tone():
    print(f'''
        ==================================
                Message alert tone
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def keypad_tones():
    print(f'''
        ==================================
                Keypad tones
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def warning_and_game_tones():
    print(f'''
        ==================================
            Warning and game tones
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def vibrating_alert():
    print(f'''
        ==================================
                Vibrating alert
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def screen_saver():
    print(f'''
        ==================================
                    Screen saver
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        tones()
    else:
        print('Invalid option.')


def tones():
    print(f'''
        ==================================
                    Tones
        ==================================
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypad tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        10. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        ringing_tone()
    elif user_option == '2':
        ringing_volume()
    elif user_option == '3':
        incoming_call_alert()
    elif user_option == '4':
        composer()
    elif user_option == '5':
        message_alert_tone()
    elif user_option == '6':
        keypad_tones()
    elif user_option == '7':
        warning_and_game_tones()
    elif user_option == '8':
        vibrating_alert()
    elif user_option == '9':
        screen_saver()
    elif user_option == '10':
        main_menu()
    else:
        print('Invalid option.')


def automatic_redial():
    print(f'''
            ==================================
                    Automatic redial
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def speed_dialling():
    print(f'''
            ==================================
                    Speed dialling
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def call_waiting_options():
    print(f'''
            ==================================
                    Call waiting options
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def own_number_sending():
    print(f'''
            ==================================
                    Own number sending
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def phone_line_in_use():
    print(f'''
            ==================================
                    Phone line in use
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def automatic_answer():
    print(f'''
            ==================================
                    Automatic answer
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    else:
        print('Invalid option.')


def call_settings():
    print(f'''
            ==================================
                    Call settings
            ==================================
            1. Automatic redial
            2. Speed dialling
            3. Call waiting options
            4. Own number sending
            5. Phone line in use
            6. Automatic answer
            7. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        automatic_redial()
    elif user_option == '2':
        speed_dialling()
    elif user_option == '3':
        call_waiting_options()
    elif user_option == '4':
        own_number_sending()
    elif user_option == '5':
        phone_line_in_use()
    elif user_option == '6':
        automatic_answer()
    elif user_option == '7':
        settings()
    else:
        print('Invalid option.')


def language():
    print(f'''
            ==================================
                        Language
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def cell_info_display():
    print(f'''
            ==================================
                    Cell info display
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def welcome_note():
    print(f'''
            ==================================
                        Welcome note
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def network_selection():
    print(f'''
            ==================================
                    Network selection
            ==================================
            1. Back
            ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def lights():
    print(f'''
            ==================================
                        Lights
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def confirm_sim_service_access():
    print(f'''
            ==================================
                Confirm SIM service access
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        phone_settings()
    else:
        print('Invalid option.')


def phone_settings():
    print(f'''
            ==================================
                    Phone settings
            ==================================
            1. Language
            2. Cell info display
            3. Welcome note
            4. Network selection
            5. Lights
            6. confirm SIM service access
            7. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        language()
    elif user_option == '2':
        cell_info_display()
    elif user_option == '3':
        welcome_note()
    elif user_option == '4':
        network_selection()
    elif user_option == '5':
        lights()
    elif user_option == '6':
        confirm_sim_service_access()
    elif user_option == '7':
        phone_settings()
    else:
        print('Invalid option.')


def pin_code_request():
    print(f'''
            ==================================
                    PIN code request
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def call_barring_service():
    print(f'''
            ==================================
                    Call barring service
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def fixed_dialling():
    print(f'''
            ==================================
                    Fixed dialling
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def closed_user_group():
    print(f'''
            ==================================
                    Closed user group
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def phone_security():
    print(f'''
            ==================================
                    Phone security
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def change_access_code():
    print(f'''
        ==================================
                Change access code
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        security_settings()
    else:
        print('Invalid option.')


def security_settings():
    print(f'''
            ==================================
                    Security settings
            ==================================
            1. PIN code request
            2. Call barring service
            3. Fixed dialling
            4. Closed user group
            5. Phone security
            6. Change access code
            7. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        pin_code_request()
    elif user_option == '2':
        call_barring_service()
    elif user_option == '3':
        fixed_dialling()
    elif user_option == '4':
        closed_user_group()
    elif user_option == '5':
        phone_security()
    elif user_option == '6':
        change_access_code()
    elif user_option == '7':
        settings()
    else:
        print('Invalid option.')


def restore_factory_settings():
    print(f'''
            ==================================
                Restore factory settings
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        settings()
    else:
        print('Invalid option.')


def settings():
    print(f'''
            ==================================
                        Settings
            ==================================
            1. Call settings
            2. Phone settings
            3. Security settings
            4. Restore factory settings
            5. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        call_settings()
    elif user_option == '2':
        phone_settings()
    elif user_option == '3':
        security_settings()
    elif user_option == '4':
        restore_factory_settings()
    elif user_option == '5':
        main_menu()
    else:
        print('Invalid option.')


def call_divert():
    print(f'''
        ==================================
                    Call divert
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def games():
    print(f'''
        ==================================
                    Games
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def calculator():
    print(f'''
        ==================================
                    Calculator
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def reminders():
    print(f'''
        ==================================
                    Reminders
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def alarm_clock():
    print(f'''
        ==================================
                    Alarm clock
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def clock_settings():
    print(f'''
        ==================================
                    Clock settings
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def date_settings():
    print(f'''
        ==================================
                Date settings
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def stopwatch():
    print(f'''
        ==================================
                    Stopwatch
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def countdown_timer():
    print(f'''
        ==================================
                Countdown timer
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def auto_update_of_date_and_time():
    print(f'''
        ==================================
            Auto update of date and time
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        clock()
    else:
        print('Invalid option.')


def clock():
    print(f'''
        ==================================
                    Clock
        ==================================
        1. Alarm clock
        2. Clock settings
        3. Date settings
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        7. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        alarm_clock()
    elif user_option == '2':
        clock_settings()
    elif user_option == '3':
        date_settings()
    elif user_option == '4':
        stopwatch()
    elif user_option == '5':
        countdown_timer()
    elif user_option == '6':
        auto_update_of_date_and_time()
    elif user_option == '7':
        main_menu()
    else:
        print('Invalid option.')


def profiles():
    print(f'''
        ==================================
                    Profiles
        ==================================
        1. Back
    ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


def sim_services():
    print(f'''
            ==================================
                        Sim services
            ==================================
            1. Back
        ''')
    user_option = input('Pick a number to proceed: ')
    if user_option == '1':
        main_menu()
    else:
        print('Invalid option.')


if userOption == '1':
    phone_book()
elif userOption == '2':
    messages()
elif userOption == '3':
    chat()
elif userOption == '4':
    call_register()
elif userOption == '5':
    tones()
elif userOption == '6':
    settings()
elif userOption == '7':
    call_divert()
elif userOption == '8':
    games()
elif userOption == '9':
    calculator()
elif userOption == '10':
    reminders()
elif userOption == '11':
    clock()
elif userOption == '12':
    profiles()
elif userOption == '13':
    sim_services()
else:
    print('Invalid option.')
