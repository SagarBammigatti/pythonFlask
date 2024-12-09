from dataclasses import dataclass

@dataclass
class XRayMap:
    xRayImage: float
    kVp_est: float
    Filter_Material: float
    Filter_Thickness: float


