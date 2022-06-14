from datetime import datetime
import psutil

def parse_case(cmd: str) -> str:
    return cmd.lower().strip()

def _check_and_replace(cmd: str, to_replace: str, replace_with: str) -> str:
    if " " + to_replace + " " in cmd:
        cmd = cmd.replace(" " + to_replace + " ", " " + replace_with + " ")
    if cmd.startswith(to_replace + " "):
        cmd = cmd.replace(to_replace + " ", replace_with + " ")
    return cmd

def parse_abbr(cmd: str) -> str:
    if "'s " in cmd:
        cmd = cmd.replace("'s ", " is ")
    cmd = _check_and_replace(cmd, "ur", "your")
    cmd = _check_and_replace(cmd, "u", "you")
    cmd = _check_and_replace(cmd, "r", "are")
    cmd = _check_and_replace(cmd, "i'm", "i am")
    cmd = _check_and_replace(cmd, "rn", "right now")
    cmd = _check_and_replace(cmd, "ohk", "ok")
    cmd = _check_and_replace(cmd, "okay", "ok")
    cmd = _check_and_replace(cmd, "wat", "what")
    return cmd.strip()

def parse_time() -> str:
    today_obj = datetime.now()
    today_str = today_obj.strftime("%d %b %Y, %a, %H:%M:%S")
    return today_str

def parse_battery_data() -> str:
    battery = psutil.sensors_battery()
    data = str(int(battery.percent)) + "%, " + "Plugged in" if battery.power_plugged else "Not plugged in"
    return data

if __name__ == "__main__":
    parse_battery_data()