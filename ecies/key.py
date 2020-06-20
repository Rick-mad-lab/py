from typing import Optional
from coincurve import PrivateKey as Secp256k1SK, PublicKey as Secp256k1PK
from nacl.public import PrivateKey as Curve25519SK, PublicKey as Curve25519PK

SECP256K1 = "secp256k1"
CURVE25519 = "curve25519"
CURVES = {SECP256K1, CURVE25519}

_SK = {SECP256K1: Secp256k1SK, CURVE25519: Curve25519SK}
_PK = {SECP256K1: Secp256k1PK, CURVE25519: Curve25519PK}


class SecretKey:
    def __init__(self, secret_key: bytes, curve: str = SECP256K1):
        if curve not in CURVES:
            raise ValueError(f"Not supported curve: {curve}")
        self.__curve = curve
        self.__sk = _SK[curve](secret_key)

    @property
    def curve(self) -> str:
        return self.__curve

    @property
    def public_key(self) -> bytes:
        pass


class PublicKey:
    def __init__(self, public_key: bytes, curve: str = SECP256K1):
        if curve not in CURVES:
            raise ValueError(f"Not supported curve: {curve}")
        self.__pk = public_key
        self.__curve = curve

    @property
    def curve(self) -> str:
        return self.__curve
