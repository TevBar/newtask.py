#task 1 on the birds and the caves. FIX THE ERRORS

place= input(f"Choose a place: forest or cave?")
action = input("Choose an action:climb a tree or cross a river or light a torch or proceed in the dark?")

final_message = ""

if place == "forest":
    if action == "climb tree":
        final_message += "you found a birds nest!"
    else: 
        action == "cross a river"
        final_message += "you found a boat!"
elif place == "cave":
    if action == "light a torch":
        final_message += "you found a bear!"
    elif action == "proceed in the dark":
        final_message += "you just fell into a family of bears run!!"
    else:
        pass
else: 
    final_message += "you are lost!"

print(final_message)