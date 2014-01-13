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


class ExecutionsApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient

    def getById(self, execution_id, **kwargs):
        """Returns the execution state by its id.
        Args:
            execution_id, str: ID of the execution that needs to
                be fetched (required)
        Returns: Execution
        """

        allParams = ['execution_id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' "
                                "to method getById" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/executions/{execution_id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        if ('execution_id' in params):
            replacement = str(self.apiClient.toPathValue(
                params['execution_id']))
            resourcePath = resourcePath.replace('{' + 'execution_id' + '}',
                                                replacement)
        postData = (params['body'] if 'body' in params else None)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'Execution')
        return responseObject