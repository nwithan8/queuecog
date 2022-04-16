from typing import List

from arcacog import ArcaCogConfig


class Config(ArcaCogConfig):
    def __init__(self, config_files: List[str]):
        super().__init__(folder="queuecog", name="Queue", config_files=config_files)

    @property
    def queue_types(self):
        return self.get(key='QueueTypes', default=[])
