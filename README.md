# Shipment Driver Mapper

A command line application that maps shipments to drivers while maximizing total suitability score (SS).

The implementation uses SciPy's linear sum assignment function to determine the optimal mappings with the highest total SS.

### Prerequisites

- Ensure Python3 is installed
- Install the requirements: `pip install -r requirements.txt`

### Run app
`python3 mapper.py <shipments> <drivers>`

_shipments_ and _drivers_ are paths to text files containing their respective contents. The files must be newline separated.

Using the sample files for example:
`python3 mapper.py sample_shipments.txt sample_drivers.txt`

### Run tests

`python3 -m pytest tests/`