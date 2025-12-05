#Self-Driven Car Simulation with Steering, Acceleration, and Pathfinding (Dijkstra’s Algorithm)

from os import name


class Car:
    def __init__(self,speed,brand,color,steering_angle):
        self.speed = speed
        self.brand = brand
        self.color = color
        self.steering_angle = steering_angle

    def turn_left(self,angle):
        self.steering_angle = self.steering_angle-angle
        
    def drive_left(self,angle):
        self.turn_left(angle)

    def turn_right(self,angle):
        self.steering_angle = self.steering_angle+angle

    def drive_right(self,angle):
        self.turn_right(angle)

#function to handle steering manoeuvres


'''def steering_manoeuvre(car):
    print("Steering angle before turning left: {}".format(car.steering_angle))
    car.drive_left(int(input("Enter steering angle to turn left: ")))
    print("Steering angle now: {}".format(car.steering_angle))
    car.drive_right(int(input("Enter steering angle to turn right: ")))
    print("Steering angle now: {}".format(car.steering_angle))'''



#function to turn on headlights

'''def turn_on_headlights():print("Headlights are now ON.")'''


class Airbag:
    def burst(self):
        print("Airbag deployed")

    def shrink(self):
        print("Airbag deflated safely")

def airbags_burstout(event_id):
    if event_id == "401":
        airbag = Airbag()
        airbag.burst()
        airbag.shrink()
        print("Passenger rescued")
        return True

    return False

class Accelerator():
    def __init__(self,acceleration):
        self.acceleration = acceleration
    
    def push(self):
        self.acceleration += 10
        print("Car accelerated to {} km/h".format(self.acceleration))

    def release(self):
        self.acceleration -= 10
        print("Car decelerated to {} km/h".format(self.acceleration))

    def stay(self):
        print("Car is maintaining speed at {} km/h".format(self.acceleration))

#devise a logic to indicate an accident
class Accident():

    #define scoring functions
    
    @staticmethod
    def speed_score(speed):
        return min(max(speed / 100, 0), 1)   # normalize 0 → 1

    @staticmethod
    def force_score(force):
        return min(max((force - 60) / 40, 0), 1)
    
    @staticmethod
    def calculate_impact(vehicle_type, vehicle_type_weight, speed, force, collider_type, collision_factor):
        v_weight = vehicle_type_weight
        c_factor = collision_factor

        s_score = Accident.speed_score(speed)
        f_score = Accident.force_score(force)

        impact = (v_weight * s_score * f_score * c_factor) * 100
        return round(impact, 2)

if __name__ == "__main__":    
    #calculate impact formula based on vehicle in video
    #define vehicle type weights and collision factors
    VEHICLE_TYPE_WEIGHT = {
        "suv": 1.3,        # heavier → more inertia → higher damage potential
        "sedan": 1.0,
        "hatchback": 0.8
    }

    COLLISION_FACTOR = {
        "car": 1.0,
        "suv": 1.2,
        "truck": 1.8,
        "bus": 2.0,
        "motorcycle": 0.5
    }
    vehicle_type = "suv"      # example vehicle type
    vehicle_type_weight = VEHICLE_TYPE_WEIGHT[vehicle_type]
    collision_factor = COLLISION_FACTOR[vehicle_type]
    speed = 85                # example speed in km/h
    mass = 1500               # example mass in kg

    accn = Accelerator(5)        # example acceleration in m/s²
    force = mass*accn.acceleration          # example force in arbitrary units
    
    collider_type = "truck"   #example collider type

    #event accident impact calculation
    #trigger api call to airbags deployment if impact score exceeds threshold
    Acc1 = Accident()
    impact_score = Acc1.calculate_impact(vehicle_type, vehicle_type_weight, speed, force, collider_type, collision_factor)
    print("Calculated Impact Score:", impact_score)

    if impact_score > 80:
        print("High structural damage. Replace bumper, hood, headlights, airbags.")
    elif impact_score > 60:
        print("Moderate damage. Replace bumper, grills, radiator holders.")
    elif impact_score > 40:
        print("External damage. Minor dents, repaint.")
    else:
        print("Light impact. Cosmetic repair only.")


'''if __name__ == "__main__":
    cars_list = ["Skoda","Jaguar","Lamborghini","Ferrari","Porsche","Amaze","City","Ameo"]
    prices_list = [2_000_000, 5_000_000, 5_000_000, 6_000_000, 7_000_000]
    print("Enter the brand of car you want to buy from the following list:")
    print(cars_list)
    user_choice = input()
    if user_choice in cars_list:
        index = cars_list.index(user_choice)
        print("The price of the {} is: {}".format(user_choice,prices_list[index]))
        print("Do you want to buy it? (yes/no)")
        buy_choice = input().lower()
        if buy_choice == "yes":
            print("Congratulations on your new {}!".format(user_choice))
        else:
            print("Thank you for visiting our dealership.")
        car = Car(0,user_choice,"Red",0)

    acc=Accelerator(0)
    acc.push()
    acc.stay()
    acc.release()
class Stereo:
    def __init__(self,volume):
        self.volume = volume
        self.default_mode = "AUX"

    def volume_up(self):
        self.volume += 5
        print("Stereo volume increased to {}".format(self.volume))

    def volume_down(self):
        self.volume -= 5
        print("Stereo volume decreased to {}".format(self.volume))

    def change_track(self,track_name):
        print("Changing track to {}".format(track_name))

    def connect_bluetooth(self,device_name):
        print("Connected to Bluetooth device: {}".format(device_name))

class Wiper:
    def __init__(self,wiper):
        self.wiper = wiper
        self.speed = 1
    #innovative method names for improving existing wiper functionality
    def automatic_wipe(self):
        print("Wipers are now set to automatic mode.")
        print("Let's play your favorite song while driving!")
<<<<<<< HEAD

=======
        
>>>>>>> c52aa4e (added airbag deployment)
if __name__ == "__main__":
    print("MENU")
    print("1. Perform steering manoeuvre")
    print("2. Put on headlights")
    print("Enter your choice (1/2):")

choice = input.lower()

if choice == 1:
    steering_manoeuvre(car)
elif choice == 2:
    print("Headlights are now ON.") = input().lower()
else:
    print("Invalid choice.")

#define an engineering dimension for the car
car_length_meters = 4.5  # length of the car in meters

#define a source function using dijkstra's algorithm
print("Calculating shortest paths using Dijkstra's algorithm...")
print("Enter source map gps coordinates:")
src_coordinate1,src_coordinate2 = input()
print(:"Enter destination map gps coordinates:")
dst_coordinate1,dst_coordinate2 = input()
def dijkstra(src_coordinate, dst_coordinate, graph):
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda node: shortest_distances[node])
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = shortest_distances[current_node] + weight
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
    return shortest_distances'''