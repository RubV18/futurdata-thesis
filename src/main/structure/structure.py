import json
from datetime import datetime
from typing import List, Optional

class Action:
    def __init__(self, id: Optional[int] = None, image: Optional[str] = None, time: Optional[datetime] = None):
        self.id = id
        self.image = image
        self.time = time

    def to_dict(self):
        return {
            'id': self.id,
            'image': self.image,
            'time': self.time
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

class BasicAction(Action):
    def __init__(self, id: Optional[int] = None, time: Optional[datetime] = None, 
                 type_: Optional[str] = None, tool: Optional[str] = None, location: Optional[str] = None,
                 prev_level_id: Optional[int] = None, next_level_id: Optional[int] = None, 
                 action_anomaly: Optional[str] = None, image_address: Optional[str] = None):
        super().__init__(id, image_address, time)
        self.type = type_
        self.tool = tool
        self.location = location
        self.prev_level_id = prev_level_id
        self.next_level_id = next_level_id
        self.action_anomaly = action_anomaly
        self.image_address = image_address

    def to_dict(self):
        print(f'location {self.location}')
        base_dict = super().to_dict()
        base_dict.update({
            'type': 'Basic',
            'tool': self.tool,
            'location': self.location,
            'prev_level_id': self.prev_level_id,
            'next_level_id': self.next_level_id,
            'action_anomaly': self.action_anomaly,
            'image_address': self.image_address
        })
        return base_dict

class ComposedAction(Action):
    def __init__(self, id: Optional[int] = None, image: Optional[str] = None, time: Optional[datetime] = None,
                 actions: Optional[List[Action]] = None, next_level_id: Optional[int] = None, prev_level_id: Optional[int] = None):
        super().__init__(id, image, time)
        self.actions = actions if actions is not None else []
        self.next_level_id = next_level_id
        self.prev_level_id = prev_level_id

    def to_dict(self):
        base_dict = super().to_dict()
        base_dict.update({
            'type' : 'Composed',
            'actions': [action.to_dict() for action in self.actions],
            'next_level_id': self.next_level_id,
            'prev_level_id': self.prev_level_id
        })
        return base_dict


class BasicObject:
    def __init__(self, object_id=None, level_id=None, name=None, color=None, serial_number=None, weight=None, bucket=None, quality=None):
        self.object_id = object_id
        self.level_id = level_id
        self.name = name
        self.color = color
        self.serial_number = serial_number
        self.weight = weight
        self.bucket = bucket
        self.quality = quality

    def to_dict(self):
        return {
            'type' : 'Basic',
            'object_id': self.object_id,
            'level_id': self.level_id,
            'name': self.name,
            'color': self.color,
            'serial_number': self.serial_number,
            'weight': self.weight,
            'bucket': self.bucket,
            'quality': self.quality
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

class ComposedObjects:
    def __init__(self, object_id=None, level_id=None, basic_objects=[]):
        self.object_id = object_id
        self.level_id = level_id
        self.basic_objects = basic_objects

    def to_dict(self):
        return {
            'type' : 'Composed',
            'object_id': self.object_id,
            'level_id': self.level_id,
            'basic_objects': [obj.to_dict() for obj in self.basic_objects]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)




class Tool:
    def __init__(self, name = None, type = None):
        self.name = name
        self.type = type


    def to_dict(self):
        return {
            
            'name': self.name,
            'type': self.type
            
        }