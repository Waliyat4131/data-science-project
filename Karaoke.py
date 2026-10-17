queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

print()                                 # start from 1, we use i +1
print("Options: add / next / remove / quit")

def show_queue(queue):
    """print everyone currently in the queue"""
    print()
    print("current queue:")
    print()
    for i, item in enumerate(queue): # the enumerate in this let us access index and item in queue
        name, song = item
        print(f"{i +1} {name} - {song}") # Since list index in python starts from 0, if we want to make our own index


def prompt_for_singer():
    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()
    return name, song

def add_singer(queue):
    """Ask for the singer and add them to the queue """
    name, song = prompt_for_singer()
    queue.append((name, song))
    print(f"Added {name} to the queue")
    

def next_singer(queue):
    if len(queue) == 0:
        print("Oops! There is no one to call up")
        return
    name, song = queue.pop(0)
    print(f"Next up: {name} with {song}!")


def remove_singer(queue):
    """remove singer from queue"""
    name = input("Who do you want to remove? ").strip().title()
    print()
    for singer in queue:
        if singer[0] == name:
            queue.remove(singer)
            print(f"Removed {name} from the queue")
            return
    print(f"There is no one name {name} in the queue")
        




def run_app(queue):
    print("=" * 44)
    print("Welcome to the Sing Out: A Karaoke Queue Manager") 
    print("=" * 44)

    is_running = True
    while is_running:
        show_queue(queue)
        
        command = input(">").strip().lower()
        
        if command == "quit":
            is_running = False
            print("The queue is closed. Good night")
        elif command == "add":
            add_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        else:
            print(f"Sorry, I dont know the command '{command}'")

run_app(queue)



