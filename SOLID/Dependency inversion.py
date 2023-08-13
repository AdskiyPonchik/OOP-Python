import sys
import time

"""The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. 
Instead, both should depend on abstractions.
As you can see, the Logger class now depends on the INotifier interface, not on the TerminalPrinter or FilePrinter classes. 
This makes the Logger class more flexible, because it can be used with any class that implements the INotifier interface.
By following the DIP, you can create code that is more flexible and easier to maintain. 
This is because your code will not be tightly coupled to specific implementations."""

class INotifier:
    def write(self, msg):
        pass


class TerminalPrinter(INotifier):
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter(INotifier):
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%m-%d %H:%m:%s', time.localtime())

    def log(self, message, notifier):
        notifier.write(f"{self.prefix} {message}")


logger = Logger()
logger.log("Starting the program...", TerminalPrinter())
logger.log("An error!", FilePrinter())
