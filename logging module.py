import logging

# Configure logging
logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Program Started")

# Debugging information
logging.debug("Program execution started")

try:
    a = 10
    b = 2

    logging.info("Performing division")

    result = a / b

    print("Result:", result)
    logging.info("Division completed successfully")

    # Generate an error
    x = 10
    y = 0

    result = x / y

except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    logging.exception("Exception occurred")

finally:
    print("Program Ended")
    logging.info("Program execution ended")
