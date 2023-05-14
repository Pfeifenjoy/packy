#!/usr/bin/env python3

import logging
from packy.engine import Engine


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    engine = Engine()
    engine.run()
