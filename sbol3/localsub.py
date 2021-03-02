import math

from . import *
# Feature is not exported
from .feature import Feature
from .typing import *


class LocalSubComponent(Feature):
    """LocalSubComponent serves as a way to create a placeholder in more
    complex Components, such as a variable to be filled in later or a
    composite that exists only within the context of the parent
    Component.

    """

    def __init__(self, types: List[str],
                 *, locations: List[Location] = None,
                 roles: List[str] = None, orientation: str = None,
                 name: str = None, description: str = None,
                 derived_from: List[str] = None,
                 generated_by: List[str] = None,
                 measures: List[SBOLObject] = None,
                 identity: str = None,
                 type_uri: str = SBOL_LOCAL_SUBCOMPONENT) -> None:
        super().__init__(identity=identity, type_uri=type_uri,
                         roles=roles, orientation=orientation, name=name,
                         description=description, derived_from=derived_from,
                         generated_by=generated_by, measures=measures)
        self.types: uri_list = URIProperty(self, SBOL_TYPE, 1, math.inf,
                                           initial_value=types)
        self.locations = OwnedObject(self, SBOL_LOCATION, 0, math.inf,
                                     initial_value=locations,
                                     type_constraint=Location)


def build_local_subcomponent(identity: str,
                             *, type_uri: str = SBOL_LOCAL_SUBCOMPONENT) -> SBOLObject:
    missing = PYSBOL3_MISSING
    obj = LocalSubComponent([missing], identity=identity, type_uri=type_uri)
    # Remove the dummy values
    obj._properties[SBOL_TYPE] = []
    return obj


Document.register_builder(SBOL_LOCAL_SUBCOMPONENT, build_local_subcomponent)
