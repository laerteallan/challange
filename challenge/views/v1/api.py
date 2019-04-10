
from webargs import ValidationError, fields
# from webargs.tornadoparser import parser

from challenge.views.v1 import ViewsChallenge


def validate_field_null(value):
    if not value:
        raise ValidationError("Param Invalid")


class Api(ViewsChallenge):
    __urls__ = ["{}/api".format(ViewsChallenge._version)]
    _contract = {
        "partner": fields.Str(required=True, validate=validate_field_null),
        "pageNumber": fields.Int(required=True)
    }

    async def get(self, *args, **kwargs):
        await self.finish("teste")
