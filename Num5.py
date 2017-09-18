import time


# Mock controller functions

def get_height():
	height = float(input())
	return height

def set_thrust(new_thrust):
	thrust = new_thrust

KP = 1.0
KD = 1.0
KI = 1.0

# Main
isRunning = True
def main():

	prev_time = time.time()

	# PID Variables
	desired_height = float(input("Desired Height: "))
	prev_error = 0.0
	integral = 0.0

	# Main Time Loop Controls
	while isRunning:

		# System Time Loop Controls
		curr_time = time.time()
		delta_time = curr_time - prev_time  # don't be alarmed this actually works Python scopes are weird
		prev_time = time.time()

		# PID
		error = desired_height - get_height()
		integral += error * delta_time
		derivative = (error - prev_error) / delta_time

		output = KP * error + KI * integral + KD * derivative
		set_thrust(output)

		prev_error = error

main()
