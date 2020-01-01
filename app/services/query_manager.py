from .db_query import *


def select_all() -> str:
    return SELECTALL


def select_where(id) -> str:
    return SELECTWHEREID + id


def delete_where(id) -> str:
    return DELETEWHEREID + id


def insert_new(values) -> str:
    return INSERTNEW + values
