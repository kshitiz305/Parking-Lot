import random
import json
import boto3


class ParkingLot:
    def __init__(self, square_footage, spot_size):
        self.square_footage = square_footage
        self.spot_size = spot_size
        self.num_spots = self.square_footage // self.spot_size
        self.lot = [None for _ in range(self.num_spots)]

    def park(self, car, spot):
        if self.lot[spot] is None:
            self.lot[spot] = car
            return f"Car with license plate {car.license_plate} parked successfully in spot {spot}"
        else:
            return f"Car with license plate {car.license_plate} was not able to park in spot {spot}"

    def map_to_json(self):
        mapping = {}
        for i, car in enumerate(self.lot):
            if car is not None:
                mapping[i] = car.license_plate
        return mapping

    def save_to_file(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.map_to_json(), f)

    def upload_to_s3(self, file_name, bucket_name):
        s3 = boto3.client("s3")
        s3.upload_file(file_name, bucket_name, file_name)


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate


def main(cars, parking_lot):
    while len(cars) > 0 and None in parking_lot.lot:
        car = cars.pop(0)
        parked = False
        while not parked:
            spot = random.randint(0, len(parking_lot.lot) - 1)
            status = parking_lot.park(car, spot)
            if "successfully" in status:
                print(status)
                parked = True
            else:
                print(status)


# Example usage
cars = [Car("ABC1234"), Car("DEF4567"), Car("GHI7890")]
parking_lot = ParkingLot(2000, 96)
main(cars, parking_lot)

# Example usage
parking_lot.save_to_file("mapping.json")

# Example usage
parking_lot.upload_to_s3("mapping.json", "my-s3-bucket")
