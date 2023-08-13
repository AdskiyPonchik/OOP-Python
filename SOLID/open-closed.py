import sys
import time
"""The open-closed principle (OCP) states that software entities (classes, modules, functions, and so on) should be open for extension, but closed for modification. 
This means that you should be able to add new functionality to a class without having to modify the existing code.
The Logger class is open for extension because you can create new subclasses that inherit from the Logger class. For example, the CustomLogger class inherits from the Logger class and overrides the prefix property to use a different date format.
The Logger class is closed for modification because you do not need to modify the existing code to add new functionality. 
For example, if you want to add a new logging level, you can simply create a new subclass of the Logger class that defines the new logging level.
The OCP is an important principle in software design because it helps to make code more maintainable and extensible. 
By following the OCP, you can create code that is easier to change and adapt to new requirements.
Here is a brief explanation of how the OCP applies to the my code:
The Logger class is open for extension because you can create new subclasses that inherit from the Logger class. 
This allows you to add new functionality to the Logger class without having to modify the existing code.
The Logger class is closed for modification because you do not need to modify the existing code to add new functionality. 
This is because you can simply create new subclasses of the Logger class that define the new functionality."""
class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    def log(self, message):
        sys.stderr.write(f"{self.prefix} --> {message}\n")

class CustomLogger(Logger):
    def __init__(self):
        super().__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())

logger = Logger()
logger.log('An error has happened!')

c_logger = CustomLogger()
c_logger.log('Custom logger message!')