from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from services.data_storage.road import RoadDataStorage


class RoadDataStorageAggregator:
    def __init__(self):
        self.data_storages = []
        self.car_travel_time: list[int] = []

    def add_data_storage(self, data_storage: 'RoadDataStorage') -> None:
        self.data_storages.append(data_storage)

    def prepare_data(self):
        self.gather_car_travel_time()

    def gather_car_travel_time(self):
        self.car_travel_time = []
        for data_storage in self.data_storages:
            self.car_travel_time.extend(data_storage.car_travel_time)
