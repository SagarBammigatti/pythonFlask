from dataclasses import dataclass

@dataclass
class CalibrationData:
    xRayImage: float
    kVp: float
    Filter_Material: float
    Filter_Thickness: float


