from dataclasses import dataclass

@dataclass 
class Config:
    bounding_area = [[240,397], [374,504]]
    threshold = [[95,56,101],[127,224,255]]