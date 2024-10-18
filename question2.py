attendees = int(input("Enter number of attendees: "))
pass
catering_choice = input("what catering service would you like (veggie delight or gourmet meals)?")

venue = "large hall" if attendees > 100 else "conference room"
audio = "audio system" if attendees > 200 else "projector" if attendees > 50 else "no additional equipment"
catering_choice = "veggie delight" if catering_choice == "veggie delight" else "gourmet meals"


print(f"Recommended venue: {venue}")

print(f"Recommended equipment: {audio}")

print(f"recommended catering: {catering_choice}")



# Based on the corrected code from Task 1, further enhance your
# code to recommend additional things like "audio system" or "projector"
# based on the number of attendees.