# -*- coding: utf-8 -*-
from pathlib import Path

from fastapi_babel import Babel, BabelConfigs

babel = Babel(
    configs=BabelConfigs(
        ROOT_DIR=str(Path(__file__).resolve().parent),
        BABEL_DEFAULT_LOCALE="en",
        BABEL_TRANSLATION_DIRECTORY="lang",
    ),
)

if __name__ == "__main__":
    babel.run_cli()
