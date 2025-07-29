# Stub for normal sensor values
def sensor_stub():
    return {
        'temperature_in_c': 50,
        'precipitation': 70,
        'humidity': 26,
        'wind_speed_kmph': 52
    }


# Stub to expose bug: high precipitation, low wind speed
def sensor_stub_high_precip_low_wind():
    return {
        'temperature_in_c': 30,
        'precipitation': 70,  # High precipitation (>60)
        'humidity': 40,
        'wind_speed_kmph': 40   # Low wind speed (<50)
    }


# Weather report logic
def report(sensor_reader):
    readings = sensor_reader()
    weather = "Sunny Day"

    if readings['temperature_in_c'] > 25:
        if 20 <= readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['wind_speed_kmph'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


# Test for stormy/rainy weather
def test_rainy():
    weather = report(sensor_stub)
    print(weather)
    assert("rain" in weather)


# Test for high precipitation, low wind speed
def test_high_precipitation():
    weather = report(sensor_stub_high_precip_low_wind)
    print(weather)
    # Should predict rain, but currently does not
    assert("rain" in weather or "Rain" in weather)


if __name__ == '__main__':
    test_rainy()
    test_high_precipitation()
    print("All is well (maybe!)")
