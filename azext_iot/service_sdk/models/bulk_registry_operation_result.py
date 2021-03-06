# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkRegistryOperationResult(Model):
    """Encapsulates the result of a bulk registry operation.

    :param is_successful: Whether or not the operation was successful.
    :type is_successful: bool
    :param errors: If the operation was not successful, this contains an array
     of DeviceRegistryOperationError objects.
    :type errors: list[~service.models.DeviceRegistryOperationError]
    :param warnings: If the operation was partially successful, this contains
     an array of DeviceRegistryOperationWarning objects.
    :type warnings: list[~service.models.DeviceRegistryOperationWarning]
    """

    _attribute_map = {
        'is_successful': {'key': 'isSuccessful', 'type': 'bool'},
        'errors': {'key': 'errors', 'type': '[DeviceRegistryOperationError]'},
        'warnings': {'key': 'warnings', 'type': '[DeviceRegistryOperationWarning]'},
    }

    def __init__(self, is_successful=None, errors=None, warnings=None):
        super(BulkRegistryOperationResult, self).__init__()
        self.is_successful = is_successful
        self.errors = errors
        self.warnings = warnings
