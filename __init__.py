from src.repository import Repository, TextFileRepository, BinaryRepository
from src.services import Services
from src.ui import Ui


def start():
    _repo = BinaryRepository("data.bin")
    _services = Services(_repo)
    _ui = Ui(_services)

    _ui.start()


start()
