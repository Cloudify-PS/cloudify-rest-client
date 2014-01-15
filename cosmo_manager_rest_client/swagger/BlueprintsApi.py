#!/usr/bin/env python
"""
WordAPI.py
Copyright 2012 Wordnik, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import requests
from urllib2 import HTTPError


class BlueprintsApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient

    def upload(self, tar_file_obj, **kwargs):
        """Upload a new blueprint to Cloudify

        Args:
            tar_file_obj, File object of the tar gzipped
                blueprint directory (required)
            application_file_name, : File name of yaml containing
                the main blueprint. (optional)

        Returns: BlueprintState
        """

        allParams = ['body', 'application_file_name']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' "
                                "to method upload" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/blueprints'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('application_file_name' in params):
            queryParams['application_file_name'] = self.apiClient.toPathValue(
                params['application_file_name'])
        postData = (params['body'] if 'body' in params else None)

        def file_gen():
            buffer_size = 8192
            while True:
                read_bytes = tar_file_obj.read(buffer_size)
                yield read_bytes
                if len(read_bytes) < buffer_size:
                    return

        url = '{0}{1}'.format(self.apiClient.apiServer, resourcePath)
        response = requests.post(url,
                                 params=queryParams,
                                 data=file_gen())

        if response.status_code != 201:
            raise HTTPError(url, response.status_code,
                            response.content, response.headers, None)

        responseObject = self.apiClient.deserialize(response.json(),
                                                    'BlueprintState')
        return responseObject

    def list(self, **kwargs):
        """Returns a list a submitted blueprints.
        Args:
        Returns: list[BlueprintState]
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                "to method list" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/blueprints'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if response is None:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'list[BlueprintState]')
        return responseObject

    def getById(self, blueprint_id, **kwargs):
        """Returns a blueprint by its id.
        Args:
            blueprint_id, :  (optional)
        Returns: BlueprintState
        """

        allParams = ['blueprint_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to"
                                " method getById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/blueprints/{blueprint_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('blueprint_id' in params):
            replacement = str(self.apiClient.toPathValue(
                params['blueprint_id']))
            resourcePath = resourcePath.replace('{' + 'blueprint_id' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if response is None:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'BlueprintState')
        return responseObject

    def validate(self, blueprint_id, **kwargs):
        """Validates a given blueprint.

        Args:
            blueprint_id, :  (optional)

        Returns: BlueprintValidationStatus
        """

        allParams = ['blueprint_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to"
                                " method validate" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/blueprints/{blueprint_id}/validate'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('blueprint_id' in params):
            replacement = str(self.apiClient.toPathValue(
                params['blueprint_id']))
            resourcePath = resourcePath.replace('{' + 'blueprint_id' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if response is None:
            return None

        responseObject = self.apiClient.deserialize(
            response,
            'BlueprintValidationStatus')
        return responseObject

    def delete(self, blueprint_id, **kwargs):
        """Deletes a given blueprint.

        Args:
            blueprint_id: str

        Returns: BlueprintState
        """

        allParams = ['blueprint_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' "
                                "to method delete" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/blueprints'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'DELETE'

        queryParams = {}
        headerParams = {}

        if ('blueprint_id' in params):
            replacement = str(self.apiClient.toPathValue(
                params['blueprint_id']))
            resourcePath = resourcePath.replace('{' + 'blueprint_id' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if response is None:
            return None

        responseObject = self.apiClient.deserialize(
            response,
            'BlueprintState')
        return responseObject
