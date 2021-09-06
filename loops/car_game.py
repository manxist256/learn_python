car_started = False
while True:
    cmd = input("> ")
    if cmd.lower() == "help":
        print("start -> to start car")
        print("stop -> to stop car")
        print("quit -> to quit from game")
    elif cmd.lower() == "start":
        if car_started:
            print("Car is already started!")
        else:
            car_started = True
            print("Car started!")
    elif cmd.lower() == "stop":
        if car_started:
            car_started = False
            print("Car stopped!")
        else:
            print("Start the car first!")
    elif cmd.lower() == "quit":
        print("Quit called!")
        break
    else:
        print("We don't understand this command!")



