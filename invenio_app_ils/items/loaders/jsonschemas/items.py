# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Items schema for marshmallow loader."""

from invenio_records_rest.schemas import RecordMetadataSchemaJSONV1
from marshmallow import EXCLUDE, Schema, fields, validate

from invenio_app_ils.items.api import Item
from invenio_app_ils.records.loaders.schemas.price import PriceSchema


class ISBNSchema(Schema):
    """ISBN schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    description = fields.Str()
    value = fields.Str(required=True)


class ItemSchemaV1(RecordMetadataSchemaJSONV1):
    """Item schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    acquisition_pid = fields.Str()
    barcode = fields.Str()
    circulation_restriction = fields.Str(
        required=True, validate=validate.OneOf(Item.CIRCULATION_RESTRICTIONS)
    )
    description = fields.Str()
    document_pid = fields.Str(required=True)  # TODO: validate
    internal_location_pid = fields.Str(required=True)  # TODO: validate
    internal_notes = fields.Str()
    isbn = fields.Nested(ISBNSchema)
    legacy_id = fields.Str()
    legacy_library_id = fields.Str()
    medium = fields.Str(required=True, validate=validate.OneOf(Item.MEDIUMS))
    number_of_pages = fields.Int()
    physical_description = fields.Str()
    price = fields.Nested(PriceSchema)
    shelf = fields.Str()
    status = fields.Str(required=True, validate=validate.OneOf(Item.STATUSES))
