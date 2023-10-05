# -*- coding: utf-8 -*-

"""
ccimercuryapigatewaypostman

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DashboardGetdashboardviewrequest(object):

    """Implementation of the '/dashboard/getdashboardviewrequest' model.

    TODO: type model description here.

    Attributes:
        user_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": 'User_Id'
    }

    def __init__(self,
                 user_id=None):
        """Constructor for the DashboardGetdashboardviewrequest class"""

        # Initialize members of the class
        self.user_id = user_id 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        user_id = dictionary.get("User_Id") if dictionary.get("User_Id") else None
        # Return an object of this model
        return cls(user_id)
