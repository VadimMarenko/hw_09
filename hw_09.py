
phone_book = {"Jessie": "0971234567",
              "Bill": "+380689876543"}

def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except TypeError: 
            return "Enter the data correctly"
        except KeyError:
            return "Enter the data correctly"
        except ValueError:
            return "Enter the data correctly"
        except IndexError:
            return "Enter the data correctly"

        return result
    return wrapper

def greeting(*args):
    result = "How can I help you?"
    return result

def checking_args(*args):
    if args[0].isalpha():
        name = args[0].capitalize()
        phone = args[1]
        if (phone.startswith("+") and phone[1:].isnumeric()) or phone.isnumeric():            
            pass
        else:       
            return "Give me name and phone please"
    elif args[0].isdigit():
        return "Give me name and phone please"
    
@input_error
def add(*args):
    result = checking_args(*args)
    if result:
        return result
    else:
        name = args[0].capitalize()
        phone = args[1]
        phone_book.update({name: phone})
    return f"Added name {name} with phone number {phone}"

@input_error
def change(*args): 
    result = checking_args(*args)
    if result:
        return result
    else:
        name = args[0].capitalize()
        phone = args[1]    
        if name in phone_book.keys():
            phone_book[name] = phone
            return f"{name}'s phone number change to {phone}"
        
@input_error
def phone(*args):
    if args[0].isalpha:
        name = args[0].capitalize()
        if name in phone_book.keys():
            phone = phone_book[name]
            return f"{name} has phone number {phone}"
        else:
            return f"Name '{name}' was not found"
    else:
        return "Give me name please"
        
    
    
def show(*args):
    result = []
    result = phone_book
    return result

def bye(*args):
    return "Good bye!"

def no_command(*args):    
    return "Unknown command. Supported commands\n\nadd name number\nchange name number\nphone name\nshow all\nexit"

commands = {greeting: ("hello", ),
            add: ("add", ),
            change: ("change", ),
            phone: ("phone", ),
            show: ("show all", ),
            bye: ("good bye", "close", "exit")}

def parser(text: str) -> tuple[callable, tuple[str]|None]:
    for key, value in commands.items():
        for val in value:
            if text.startswith(val):                                
                return key, text.replace(val, "").strip().split()
            
    return no_command, ""

def main():
    while True:
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if result == "Good bye!":
            break
        
if __name__ == "__main__":
    main()
    