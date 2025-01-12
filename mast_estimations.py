import math

# Utils

def get_truncated_cone_volume(base_radius: float, top_radius: float, height: float) -> float:
    '''Returns the volume of a truncated cone.
    '''
    return (
        math.pi
        * height
        * (base_radius ** 2 + base_radius * top_radius + top_radius ** 2)
        / 3
    )

# Constants
## Mast calculations
# Urban small steel mast
# Since we assume urban antennas are mounted on rooftops, (or other)
# buildings, we use constant value and not the antenna site data.
# These values are coherent with the UTAMO results
OUTER_DIAMETER_URBAN = 0.15  # m, taken from Antenna mast in UTAMO
WALL_THICKNESS_URBAN = 0.01  # m, taken from Antenna mast in UTAMO
INNER_DIAMETER_URBAN = OUTER_DIAMETER_URBAN - 2 * WALL_THICKNESS_URBAN
HEIGHT_URBAN = 5  # m, taken from Antenna mast in UTAMO
STEEL_DENSITY = 7800  # kg/m^3, taken from internet, also used in UTAMO
STEEL_CARBON_FOOTPRINT = 2  # kgCO2/kg, deduced from UTAMO
SERVICE_LIFE_URBAN = 20  # years, taken from UTAMO

# Rural and suburban concrete tower
BASE_DIAMETER_SCALING_CONCRETE = 23.4 # scaling factor for the base diameter
TOP_DIAMETER_OFFSET_CONCRETE = 1 # m, deduced from UTAMO
CONCRETE_DENSITY = 2000  # kg/m^3, deduced from UTAMO
# according to the height of the mast, reverse engineered from UTAMO
FOUNDATION_SCALING_CONCRETE = 3.2
CONCRETE_CARBON_FOOTPRINT = 0.15  # kgCO2/kg, deduced from UTAMO
SERVICE_LIFE_CONCRETE = 100  # years, taken from UTAMO
WALL_THICKNESS_CONCRETE = 0.2  # m, taken from UTAMO

# Rural and suburban steel scaffolding
WALL_THICKNESS_STEEL = 0.005  # m, taken from UTAMO
TUBE_PER_SEGMENT_STEEL = 20 # arbitraly deduced from UTAMO, the geometry
# description is not clear
SEGMENT_HEIGHT_RATIO_STEEL = 40  # taken from UTAMO
TUBE_DIAMETER_RATIO_STEEL = 0.0018  # deduced from UTAMO
SERVICE_LIFE_RURAL_SUBURBAN_STEEL = 40  # years, taken from UTAMO

# Other
STEEL_PROPORTION_RURAL = 0.5  # taken from UTAMO
TOWER_PROPORTION_SUBURBAN = 0.5  # taken from UTAMO

def get_urban_mast_cost() -> float:
    '''Returns the carbon cost in kgCO2/year of a steel mast in an urban
    area.
    '''
    volume = (
        math.pi
        * ((OUTER_DIAMETER_URBAN / 2) ** 2 - (INNER_DIAMETER_URBAN / 2) ** 2)
        * HEIGHT_URBAN
    )
    mass = volume * STEEL_DENSITY
    total_cost = mass * STEEL_CARBON_FOOTPRINT
    return total_cost / SERVICE_LIFE_URBAN

def get_concrete_mast_cost(height: float) -> float:
    '''Returns the carbon cost in kgCO2/year of a concrete antenna mast.
    '''
    base_diameter = height / BASE_DIAMETER_SCALING_CONCRETE
    top_diameter = base_diameter - TOP_DIAMETER_OFFSET_CONCRETE
    volume = get_truncated_cone_volume(
        base_diameter / 2,
        top_diameter / 2,
        height
    ) - get_truncated_cone_volume(
        (base_diameter - 2*WALL_THICKNESS_CONCRETE) / 2,
        (top_diameter - 2*WALL_THICKNESS_CONCRETE) / 2,
        height
    )
    mast_mass = volume * CONCRETE_DENSITY
    total_mass = mast_mass + mast_mass * FOUNDATION_SCALING_CONCRETE
    total_cost = total_mass * CONCRETE_CARBON_FOOTPRINT
    return total_cost / SERVICE_LIFE_CONCRETE

def get_steel_mast_cost(height: float) -> float:
    '''Returns the carbon cost in kgCO2/year of a steel antenna mast.
    '''
    segment_length = height / SEGMENT_HEIGHT_RATIO_STEEL
    tube_diameter = height * TUBE_DIAMETER_RATIO_STEEL
    tube_volume = (
        math.pi
        * (tube_diameter / 2) ** 2
        * segment_length
    ) - (
        math.pi
        * ((tube_diameter - 2 * WALL_THICKNESS_STEEL) / 2) ** 2
        * segment_length
    )
    segment_count = height / segment_length
    segment_volume = TUBE_PER_SEGMENT_STEEL * tube_volume
    steel_volume = segment_volume * segment_count
    steel_mass = steel_volume * STEEL_DENSITY
    steel_cost = steel_mass * STEEL_CARBON_FOOTPRINT
    concrete_mass = steel_mass * FOUNDATION_SCALING_CONCRETE
    concrete_cost = concrete_mass * CONCRETE_CARBON_FOOTPRINT
    total_cost = steel_cost + concrete_cost
    return total_cost / SERVICE_LIFE_RURAL_SUBURBAN_STEEL

def get_rural_mast_cost(height: float) -> float:
    '''Returns the carbon cost in kgCO2/year of a rural antenna mast.
    '''
    return STEEL_PROPORTION_RURAL * get_steel_mast_cost(height) + (
        (1 - STEEL_PROPORTION_RURAL) * get_concrete_mast_cost(height)
    )
    
def get_suburban_mast_cost(height: float) -> float:
    '''Returns the carbon cost in kgCO2/year of a suburban antenna mast.
    '''
    return TOWER_PROPORTION_SUBURBAN*get_rural_mast_cost(height)

if __name__ == "__main__":
    print(get_urban_mast_cost())
    print(get_suburban_mast_cost(35))
    print(get_rural_mast_cost(40))

