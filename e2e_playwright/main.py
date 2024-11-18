import pytest
from pixelmatch import resgresion_visual
from report import create_report

pytest.main(["given_when_then/escenarios.py", "-v"])

resgresion_visual()

create_report()