#Imports and Initialisations
import math
import sys

point_1 = [1,1]
point_2 = [2,2]
not_done = True
first_time = False          #Set to True when we have a compass module
last_loc = [0,0]


#int main() type part of the script
while(not_done):
    [current_loc, final_dest] = read_from_serial()
    [direction, speed] = where_to_go(current_loc, last_loc, final_dest, first_time)
    control_car(direction, speed)

    if(current_loc == final_dest):
        not_done = False


print('You have reached your final destination')


#Function Definitions

def where_to_go(current_place, last_place, final_dest, first_time_in_f):
    output = ['direction', 'speed']
    if(first_time_in_f):
        current_bearing = read_from_compass()
        first_time_in_f = False
    else:
        current_bearing = length_and_angle(last_place, current_place)[1]

    ideal_bearing = length_and_angle(current_place, final_dest)[1]
    if(ideal_bearing < current_bearing):
        output[0] = 'left'
    elif(ideal_bearing > current_bearing):
        output[0] = 'right'
    else:
        output[0] = 'straight'

    #Do some processing to work out if we go forwards or backwards
    # for now just say forwards all the time
    output[1] = 'forwards'
    return output

def length_and_angle(current_point, destination):
    diff_x = destination[0] - current_point[0]
    diff_y = destination[1] - current_point[1]

    result = [-1,-1]
    result[0] = sqrt(pow(diff_x,2) + pow(diff_y,2));
    result[1] = asin(diff_y/diff_x) * 180 / 3.14159265;
    return result

def read_from_serial():
    #Fill in with your parsing stuff

def read_from_compass():
    #Fill in with code for reading compass bearing from the SPI of
    # the raspberry pi
    pass

def control_car(direc, speed_in_f):
    #Fill in with code which assigns a pin high or low to control if
    # the car goes forwars or backwards and also a PWM output which
    # controls the servo controlling the steering to decide if it
    # goes right or left.
    pass
