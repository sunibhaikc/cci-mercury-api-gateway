# -*- coding: utf-8 -*-

"""
ccimercuryapigatewaypostman

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TemplateFilterDelTemplateRequest(object):

    """Implementation of the '/templateFilter/delTemplateRequest' model.

    TODO: type model description here.

    Attributes:
        user_id (str): TODO: type description here.
        template_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": 'userId',
        "template_id": 'templateId'
    }

    def __init__(self,
                 user_id=None,
                 template_id=None):
        """Constructor for the TemplateFilterDelTemplateRequest class"""

        # Initialize members of the class
        self.user_id = user_id 
        self.template_id = template_id 

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
        template_id = dictionary.get("templateId") if dictionary.get("templateId") else None
        # Return an object of this model
        return cls(user_id,
                   template_id)
