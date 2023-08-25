# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log")

# TODO: Try out each of the log levels
logging.debug("This is a DEBUG-LEVEL message")
logging.info("This is a INFO-LEVEL message")
logging.warning("This is a WARNING-LEVEL message")
logging.error("This is a ERROR-LEVEL message")
logging.critical("This is a CRITICAL-LEVEL message")

# TODO: Output formatted strings to the log
x = 'String'
y = 100
logging.info(f"Here is a {x} variable and int: {y}")