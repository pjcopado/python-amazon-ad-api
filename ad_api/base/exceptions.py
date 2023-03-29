class AdvertisingTypeException(Exception):
    code = 888

    def __init__(self, type, error):
        try:
            self.type = type
            self.message = error
        except IndexError:
            pass
        self.error = error


class AdvertisingApiException(Exception):
    code = 999

    def __init__(self, error):
        try:
            self.amzn_code = error
        except IndexError:
            pass
        self.error = error


class AdvertisingApiBadRequestException(AdvertisingApiException):
    """
    400	Request has missing or invalid parameters and cannot be parsed.
    """

    code = 400

    def __init__(self, error):
        super(AdvertisingApiBadRequestException, self).__init__(error)


class AdvertisingApiForbiddenException(AdvertisingApiException):
    """
    403	Indicates access to the resource is forbidden. Possible reasons include Access Denied, Unauthorized, Expired Token, or Invalid Signature.
    """

    code = 403

    def __init__(self, error):
        super(AdvertisingApiForbiddenException, self).__init__(error)


class AdvertisingApiNotFoundException(AdvertisingApiException):
    """
    404	The resource specified does not exist.
    """

    code = 404

    def __init__(self, error, headers=None):
        super(AdvertisingApiNotFoundException, self).__init__(error, headers)


class AdvertisingApiStateConflictException(AdvertisingApiException):
    """
    409	The resource specified conflicts with the current state.
    """

    code = 409

    def __init__(self, error, headers=None):
        super(AdvertisingApiStateConflictException, self).__init__(error, headers)


class AdvertisingApiTooLargeException(AdvertisingApiException):
    """
    413	The request size exceeded the maximum accepted size.
    """

    code = 413

    def __init__(self, error, headers=None):
        super(AdvertisingApiTooLargeException, self).__init__(error, headers)


class AdvertisingApiUnsupportedFormatException(AdvertisingApiException):
    """
    415	The request payload is in an unsupported format.
    """

    code = 415

    def __init__(self, error, headers=None):
        super(AdvertisingApiUnsupportedFormatException, self).__init__(error, headers)


class AdvertisingApiRequestThrottledException(AdvertisingApiException):
    """
    429	The frequency of requests was greater than allowed.
    """

    code = 429

    def __init__(self, error, headers=None):
        super(AdvertisingApiRequestThrottledException, self).__init__(error, headers)


class AdvertisingApiServerException(AdvertisingApiException):
    """
    500	An unexpected condition occurred that prevented the server from fulfilling the request.
    """

    code = 500

    def __init__(self, error, headers=None):
        super(AdvertisingApiServerException, self).__init__(error, headers)


class AdvertisingApiTemporarilyUnavailableException(AdvertisingApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """

    code = 503

    def __init__(self, error, headers=None):
        super(AdvertisingApiTemporarilyUnavailableException, self).__init__(
            error, headers
        )


class AdvertisingApiGatewayTimeoutException(AdvertisingApiException):
    """
    503	Temporary overloading or maintenance of the server.
    """

    code = 504

    def __init__(self, error, headers=None):
        super(AdvertisingApiGatewayTimeoutException, self).__init__(error, headers)


class MissingScopeException(Exception):
    pass


def get_exception_for_code(code: int):
    return {
        400: AdvertisingApiBadRequestException,
        403: AdvertisingApiForbiddenException,
        404: AdvertisingApiNotFoundException,
        409: AdvertisingApiStateConflictException,
        413: AdvertisingApiTooLargeException,
        415: AdvertisingApiUnsupportedFormatException,
        429: AdvertisingApiRequestThrottledException,
        500: AdvertisingApiServerException,
        503: AdvertisingApiTemporarilyUnavailableException,
        504: AdvertisingApiGatewayTimeoutException,
    }.get(code, AdvertisingApiException)


def get_exception_for_content(content: object):
    return {"UNAUTHORIZED": AdvertisingApiForbiddenException}.get(
        content.get("code"), AdvertisingApiException
    )
