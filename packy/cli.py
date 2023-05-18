import logging

from packy.engine import Engine


def main() -> int:
    logging.basicConfig(level=logging.DEBUG)

    engine = Engine()
    engine.run()

    return 0
