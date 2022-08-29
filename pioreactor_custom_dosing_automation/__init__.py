from pioreactor.automations.dosing.base import DosingAutomationJobContrib
from pioreactor.config import config

__all__ = ['MyCustomDosingAutomation']

# the class doesn't need to be in __init__, but your __init__ should reference the class, typically
# by importing it into the __init__. This is needed so the class is "registered" with pioreactor codebase.
class MyCustomDosingAutomation(DosingAutomationJobContrib):
    """
    This is just an example class of a dosing automation - it doesn't do anything but print.

    On the RPi's command line, you can invoke this class using

    $ pio run dosing_control --automation-name my_custom_dosing_automation --volume 1.0

    And if installed correctly, you'll find this also in the Pioreactor web UI.
    """

    automation_name = "my_custom_dosing_automation"

    def __init__(self, volume, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.volume = volume

    def execute(self):
        self.logger.info(f"I'm executing {self.volume} now...")
        self.logger.info(f"This config value is set in additional_config.ini: {config.get('custom_dosing', 'test_value', fallback='missing')}")
        return


