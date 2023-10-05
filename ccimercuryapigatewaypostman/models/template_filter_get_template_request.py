# -*- coding: utf-8 -*-

"""
ccimercuryapigatewaypostman

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TemplateFilterGetTemplateRequest(object):

    """Implementation of the '/templateFilter/getTemplateRequest' model.

    TODO: type model description here.

    Attributes:
        user_id (str): TODO: type description here.
        page_name (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": 'userId',
        "page_name": 'pageName'
    }

    def __init__(self,
                 user_id=None,
                 page_name=None):
        """Constructor for the TemplateFilterGetTemplateRequest class"""

        # Initialize members of the class
        self.user_id = user_id 
        self.page_name = page_name 

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
        user_id = dictionary.get("userId") if dictionary.get("userId") else None
        page_name = dictionary.get("pageName") if dictionary.get("pageName") else None
        # Return an object of this model
        return cls(user_id,
                   page_name)
