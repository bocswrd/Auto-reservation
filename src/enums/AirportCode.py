from enum import Enum


class AirportCode(Enum):
    """
    IATA airport codes for major airports in Japan.
    """

    HND = "東京（羽田）"
    SPK = "札幌（新千歳）"
    AKJ = "旭川"
    MMB = "女満別"
    KUH = "釧路"
    OBO = "帯広"
    HKD = "函館"
    SDJ = "仙台"
    NGO = "名古屋（中部）"
    UKB = "神戸"
    FUK = "福岡"
