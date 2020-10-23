from typing import Callable, Dict


def say(text: str) -> str:
    return f'Вы сказали: "{text}"'


class Processor:
    map_intent_to_action: Dict[str, Callable] = {'echo': say}

    def answer(self, intent: str, text: str) -> str:
        function = self.map_intent_to_action.get(intent, lambda x: "Nothing found")
        return function(text)
