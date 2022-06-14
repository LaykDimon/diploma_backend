import random

from . import parsers
from .dictionary import questions, default_ans, greet, ty_replies
from . import utils

class Friday:

    _cmd = str()
    _reply = str()

    @classmethod
    def listen(self, cmd: str) -> None:
        self._cmd = cmd
        self.read(self._cmd)
        self._reply = self.think(self._cmd)

    @classmethod
    def reply(self) -> str:
        return self._reply[0].upper() + self._reply[1:]

    @classmethod
    def read(self, cmd: str) -> None:
        self._cmd = parsers.parse_case(self._cmd)
        self._cmd = parsers.parse_abbr(self._cmd)

    @classmethod
    def think(self, cmd: str) -> str:
        if cmd.startswith("say "):
            return cmd.replace("say ", "")
        if "thank" in cmd:
            return ty_replies[random.randint(0, len(ty_replies) - 1)] + ", Sir"
        if all([i in cmd for i in ["what", "time"]]):
            return parsers.parse_time()
        if all([i in cmd for i in ["what", "battery"]]):
            return parsers.parse_battery_data()
        if all([i in cmd for i in ["what", "weather"]]):
            return utils.get_weather_data()
        if any([cmd.startswith(i) for i in questions]):
            return utils.get_wiki_data(cmd)
        if any([i in cmd for i in greet]):
            return greet[random.randint(0, len(greet) - 1)] + " !"
        return default_ans[random.randint(0, len(default_ans) - 1)]



if __name__ == "__main__":
    Friday.listen("what's the time")
    print(Friday.reply())
