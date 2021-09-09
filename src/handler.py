from Controllers import (dailyreport, option)

handler = {
    'submit' : dailyreport.submit,
    'clear' : dailyreport.clear,
    'restore': dailyreport.restore,
    'settings' : option.create_display,
    'save' : option.save
}