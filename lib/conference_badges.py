
# name = 'Victor'
# names = ['John', 'Kevin', 'Hum', 'Joel','Bilnas']
def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_msg = []
    for n in names:
        badge_msg.append(f'Hello, my name is {n}.')
    return badge_msg
        

def assign_rooms(names):
    room_assignment = []
    rooms = range(1, 7)

    for i, n in enumerate(names):
        if i < len(rooms):
            room_num = rooms[i]
            room_assignment.append(f'Hello, {n}! You\'ll be assigned to room {room_num}!')
        
    return room_assignment


def printer(names):
    badges = batch_badge_creator(names)
    room_assignment = assign_rooms(names)

    for bagde in badges:
        print(bagde)

    for assignment in room_assignment:
        print(assignment)
   