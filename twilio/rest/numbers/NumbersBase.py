r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

from typing import Optional

from twilio.base.domain import Domain
from twilio.rest import Client
from twilio.rest.numbers.v1 import V1
from twilio.rest.numbers.v2 import V2


class NumbersBase(Domain):
    def __init__(self, twilio: Client):
        """
        Initialize the Numbers Domain

        :returns: Domain for Numbers
        """
        super().__init__(twilio, "https://numbers.twilio.com")
        self._v1: Optional[V1] = None
        self._v2: Optional[V2] = None

    @property
    def v1(self) -> V1:
        """
        :returns: Versions v1 of Numbers
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def v2(self) -> V2:
        """
        :returns: Versions v2 of Numbers
        """
        if self._v2 is None:
            self._v2 = V2(self)
        return self._v2

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers>"
