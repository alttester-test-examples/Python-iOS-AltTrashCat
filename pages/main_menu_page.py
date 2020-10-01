from pages.base_page import BasePage
from altunityrunner import By 

class MainMenuPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/StoreButton', timeout=2)
    
    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/OpenLeaderboard', timeout=2)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/SettingButton', timeout=2)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/MissionButton', timeout=2)

    @property
    def run_button(self):   
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/StartButton', timeout=2)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharName', timeout=2)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Loadout/ThemeZone', timeout=2)

    def is_displayed(self):
        if self.store_button and self.leader_board_button and self.settings_button \
            and self.mission_button and self.run_button and self.character_name and self.theme_name:
            return True

    def press_run(self):
        self.run_button.tap()
