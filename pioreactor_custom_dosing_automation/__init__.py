from pioreactor.background_jobs.subjobs.dosing_automation import DosingAutomationContrib
from pioreactor.config import config

__all__ = ['MyCustomDosingAutomation']


class MyCustomDosingAutomation(DosingAutomationContrib):

    key = "my_custom_dosing_automation"

    def __init__(self, volume):
        self.volume = volume

    def execute(self):
        print(f"I'm executing {self.volume} now...")
        print(f"This config value is set in additional_config.ini: {config['custom_dosing']['test_value']}")


