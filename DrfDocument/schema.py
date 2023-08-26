from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.openapi import AutoSchema


        
class OpenApiTokenAuthSchema(OpenApiAuthenticationExtension):
    target_class = 'webapp.authentication.UserTokenAuthentication'
    name = 'jwtAuth'

    def get_security_definition(self, auto_schema: AutoSchema):
        return {
            "type":"apiToken",
            "in":"header",
            "name":"X-JWT-Assertion",
            "description":(
            "Token-based authentication",
            "Token-based authentication"
            )
        }