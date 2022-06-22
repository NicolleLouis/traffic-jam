class RoadDataDisplay:
    def __init__(self, storage):
        self.storage = storage

    def average_travel_time(self):
        if len(self.storage.car_travel_time) == 0:
            return None
        return sum(self.storage.car_travel_time) / len(self.storage.car_travel_time)

    def display_car_travel_time(self, verbose=False) -> None:
        self.storage.prepare_data()
        if len(self.storage.car_travel_time) == 0:
            print("No car arrived")
            return

        if verbose:
            print("Raw data:")
            print(self.storage.car_travel_time)
        print(f"Number of car analysed: {len(self.storage.car_travel_time)}")
        print(f"Fastest: {min(self.storage.car_travel_time)}")
        print(f"Slowest: {max(self.storage.car_travel_time)}")
        print(f"Average: {self.average_travel_time()}")
