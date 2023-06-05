from structures import Coordinates
from exceptions import CantGetCoordinates
import geocoder


def get_gps_coordinates() -> Coordinates:
    return _get_coordinates_output()


def _get_coordinates_output() -> Coordinates:
    try:
        g = geocoder.ip('me')
        if g.lat is None or g.lng is None:
            raise CantGetCoordinates
        return Coordinates(latitude=g.lat, longitude=g.lng, city=g.city)
    except Exception:
        raise CantGetCoordinates


if __name__ == "__main__":
    get_gps_coordinates()
