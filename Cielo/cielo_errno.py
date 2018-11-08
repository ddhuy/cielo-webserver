import httplib

# Re-use http status codes as Cielo error codes
EID_CONTINUE = httplib.CONTINUE
EID_SWITCHING_PROTOCOLS = httplib.SWITCHING_PROTOCOLS
EID_PROCESSING = httplib.PROCESSING
EID_OK = httplib.OK
EID_CREATED = httplib.CREATED
EID_ACCEPTED = httplib.ACCEPTED
EID_NON_AUTHORITATIVE_INFORMATION = httplib.NON_AUTHORITATIVE_INFORMATION
EID_NO_CONTENT = httplib.NO_CONTENT
EID_RESET_CONTENT = httplib.RESET_CONTENT
EID_PARTIAL_CONTENT = httplib.PARTIAL_CONTENT
EID_MULTI_STATUS = httplib.MULTI_STATUS
EID_IM_USED = httplib.IM_USED
EID_MULTIPLE_CHOICES = httplib.MULTIPLE_CHOICES
EID_MOVED_PERMANENTLY = httplib.MOVED_PERMANENTLY
EID_FOUND = httplib.FOUND
EID_SEE_OTHER = httplib.SEE_OTHER
EID_NOT_MODIFIED = httplib.NOT_MODIFIED
EID_USE_PROXY = httplib.USE_PROXY
EID_TEMPORARY_REDIRECT = httplib.TEMPORARY_REDIRECT
EID_BAD_REQUEST = httplib.BAD_REQUEST
EID_UNAUTHORIZED = httplib.UNAUTHORIZED
EID_PAYMENT_REQUIRED = httplib.PAYMENT_REQUIRED
EID_FORBIDDEN = httplib.FORBIDDEN
EID_NOT_FOUND = httplib.NOT_FOUND
EID_METHOD_NOT_ALLOWED = httplib.METHOD_NOT_ALLOWED
EID_NOT_ACCEPTABLE = httplib.NOT_ACCEPTABLE
EID_PROXY_AUTHENTICATION_REQUIRED = httplib.PROXY_AUTHENTICATION_REQUIRED
EID_REQUEST_TIMEOUT = httplib.REQUEST_TIMEOUT
EID_CONFLICT = httplib.CONFLICT
EID_GONE = httplib.GONE
EID_LENGTH_REQUIRED = httplib.LENGTH_REQUIRED
EID_PRECONDITION_FAILED = httplib.PRECONDITION_FAILED
EID_REQUEST_ENTITY_TOO_LARGE = httplib.REQUEST_ENTITY_TOO_LARGE
EID_REQUEST_URI_TOO_LONG = httplib.REQUEST_URI_TOO_LONG
EID_UNSUPPORTED_MEDIA_TYPE = httplib.UNSUPPORTED_MEDIA_TYPE
EID_REQUESTED_RANGE_NOT_SATISFIABLE = httplib.REQUESTED_RANGE_NOT_SATISFIABLE
EID_EXPECTATION_FAILED = httplib.EXPECTATION_FAILED
EID_UNPROCESSABLE_ENTITY = httplib.UNPROCESSABLE_ENTITY
EID_LOCKED = httplib.LOCKED
EID_FAILED_DEPENDENCY = httplib.FAILED_DEPENDENCY
EID_UPGRADE_REQUIRED = httplib.UPGRADE_REQUIRED
EID_INTERNAL_SERVER_ERROR = httplib.INTERNAL_SERVER_ERROR
EID_NOT_IMPLEMENTED = httplib.NOT_IMPLEMENTED
EID_BAD_GATEWAY = httplib.BAD_GATEWAY
EID_SERVICE_UNAVAILABLE = httplib.SERVICE_UNAVAILABLE
EID_GATEWAY_TIMEOUT = httplib.GATEWAY_TIMEOUT
EID_HTTP_VERSION_NOT_SUPPORTED = httplib.HTTP_VERSION_NOT_SUPPORTED
EID_INSUFFICIENT_STORAGE = httplib.INSUFFICIENT_STORAGE
EID_NOT_EXTENDED = httplib.NOT_EXTENDED