
from time import sleep

#For Whole Steps

def Motor(distance_in_mm, speed_in_mm_per_second):
    # set to whatever digital pin is in STEP
    step_pin = 1;

    # change this value based on how far extruder moves for one rev
    mm_per_rev = 34.25;

    steps_per_rev = 200;
    HIGH = 10;
    LOW = 0;

    # Use the input of distance_in_mm to find distance_in_revs
    distance_in_steps = steps_per_rev * (mm_per_rev ** -1 * distance_in_mm);

    distance_in_steps = round(distance_in_steps)
    distance_in_steps = int(distance_in_steps)
    print(distance_in_steps)
    # Use the input of speed_in_mm_per_second to find delay
    delay = 0.5 * (speed_in_mm_per_second ** -1 * distance_in_mm / distance_in_steps)

    for x in range(distance_in_steps):

        from main import arm
        arm.set_cgpio_analog(step_pin, HIGH)
        sleep(delay)
        arm.set_cgpio_analog(step_pin, LOW)
        sleep(delay)

    return

