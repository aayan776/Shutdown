import time
print("Are you sure you want to shutdown?")
running_programs = ["Steam", "Microsoft_word", "VScode_studio", "Chrome"]
def shutdown():
    for programs in running_programs:
        closing = programs
        print("Shutting down", programs,"...")
        time.sleep(1)
    print("Are you sure you want to shutdown pc?")
    print("Yes or No?")
    second_check = input().lower
    if second_check == "yes" or second_check == "y":
        print("Shutdown complete")
    elif second_check == "no" or second_check == "n":
        shutdown()
print("Do you want to shutdown computer?")
print("Yes or No?")
first_check = input().lower()
if first_check == "yes" or first_check == "y":
    shutdown()