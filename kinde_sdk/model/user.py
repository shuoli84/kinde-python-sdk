# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kinde_sdk import schemas  # noqa: F401


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            provided_id = schemas.StrSchema
            preferred_email = schemas.StrSchema
            last_name = schemas.StrSchema
            first_name = schemas.StrSchema
            is_suspended = schemas.BoolSchema
            picture = schemas.StrSchema
            
            
            class total_sign_ins(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'total_sign_ins':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class failed_sign_ins(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'failed_sign_ins':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class last_signed_in(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_signed_in':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class created_on(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'created_on':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "provided_id": provided_id,
                "preferred_email": preferred_email,
                "last_name": last_name,
                "first_name": first_name,
                "is_suspended": is_suspended,
                "picture": picture,
                "total_sign_ins": total_sign_ins,
                "failed_sign_ins": failed_sign_ins,
                "last_signed_in": last_signed_in,
                "created_on": created_on,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provided_id"]) -> MetaOapg.properties.provided_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preferred_email"]) -> MetaOapg.properties.preferred_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_suspended"]) -> MetaOapg.properties.is_suspended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["picture"]) -> MetaOapg.properties.picture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_sign_ins"]) -> MetaOapg.properties.total_sign_ins: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["failed_sign_ins"]) -> MetaOapg.properties.failed_sign_ins: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_signed_in"]) -> MetaOapg.properties.last_signed_in: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_on"]) -> MetaOapg.properties.created_on: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "provided_id", "preferred_email", "last_name", "first_name", "is_suspended", "picture", "total_sign_ins", "failed_sign_ins", "last_signed_in", "created_on", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provided_id"]) -> typing.Union[MetaOapg.properties.provided_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preferred_email"]) -> typing.Union[MetaOapg.properties.preferred_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_suspended"]) -> typing.Union[MetaOapg.properties.is_suspended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["picture"]) -> typing.Union[MetaOapg.properties.picture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_sign_ins"]) -> typing.Union[MetaOapg.properties.total_sign_ins, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["failed_sign_ins"]) -> typing.Union[MetaOapg.properties.failed_sign_ins, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_signed_in"]) -> typing.Union[MetaOapg.properties.last_signed_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_on"]) -> typing.Union[MetaOapg.properties.created_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "provided_id", "preferred_email", "last_name", "first_name", "is_suspended", "picture", "total_sign_ins", "failed_sign_ins", "last_signed_in", "created_on", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        provided_id: typing.Union[MetaOapg.properties.provided_id, str, schemas.Unset] = schemas.unset,
        preferred_email: typing.Union[MetaOapg.properties.preferred_email, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        is_suspended: typing.Union[MetaOapg.properties.is_suspended, bool, schemas.Unset] = schemas.unset,
        picture: typing.Union[MetaOapg.properties.picture, str, schemas.Unset] = schemas.unset,
        total_sign_ins: typing.Union[MetaOapg.properties.total_sign_ins, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        failed_sign_ins: typing.Union[MetaOapg.properties.failed_sign_ins, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_signed_in: typing.Union[MetaOapg.properties.last_signed_in, None, str, schemas.Unset] = schemas.unset,
        created_on: typing.Union[MetaOapg.properties.created_on, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            id=id,
            provided_id=provided_id,
            preferred_email=preferred_email,
            last_name=last_name,
            first_name=first_name,
            is_suspended=is_suspended,
            picture=picture,
            total_sign_ins=total_sign_ins,
            failed_sign_ins=failed_sign_ins,
            last_signed_in=last_signed_in,
            created_on=created_on,
            _configuration=_configuration,
            **kwargs,
        )
