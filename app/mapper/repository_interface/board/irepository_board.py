from abc import ABC, abstractmethod
from typing import List

from app.mapper.models.boards import Boards


class IBoardRepository(ABC):
    @abstractmethod
    def get_all_boards(self) -> List[Boards]:
        pass
