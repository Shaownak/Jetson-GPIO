import jetson.GPIO as GPIO


# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin number
gpio_pin = 18

# Set the pin as input
GPIO.setup(gpio_pin, GPIO.IN)

# Read the input value
input_value = GPIO.input(gpio_pin)

# Print the input value
print("Input value:", input_value)

# Cleanup GPIO settings
GPIO.cleanup()


# For installing GPIO library
# $ sudo apt-get install python3-gpiozero
# sudo pip install Jetson.GPIO
