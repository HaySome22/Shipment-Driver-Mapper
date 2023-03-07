import mapper


def test():
    shipments, drivers = open('sample_shipments.txt').read().splitlines(), open('sample_drivers.txt').read().splitlines()
    expected_map = {
        'Alpha St': 'George Washington',
        'Bravo Blvd': 'Jane Smith',
        'Charlie Crossing': 'John Doe'
    }
    shipment_driver_map, total_ss = mapper.map_shipments_to_drivers(shipments, drivers)
    assert expected_map == shipment_driver_map
    assert total_ss == 22.5
