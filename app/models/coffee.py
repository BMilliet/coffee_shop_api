import json


def coffee_from_json(selected_json):
    result = json.loads(json.dumps(selected_json))
    return Coffee(result['name'], result['description'])


class Coffee:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_db_values(self) -> str:
        return "(0, '{name}', '{desc}')".format(name=self.name,
                                                desc=self.description)
