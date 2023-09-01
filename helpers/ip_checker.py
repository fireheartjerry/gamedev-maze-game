from hashlib import sha256, sha512, md5
import socket

VALID_256 = {
    "999ceb3f42c9f82b65419d88d5aa53f5677fe813077488855cf81ff243199e65"
}

VALID_512 = {
    "3d8fb9ceb13edfa6173b0fce93daf5ee68fc372e4fd33db2242bece7913d42e00dab059814909a4b8249d1d51308ca46f52dcf89f7819f05026f80d290282aef"
}

VALID_MD5 = {
    "e8b24934679afcb5bf2706163c0cb2fa"
}

def ip_check():
    """Checks the IP of the current user to verify if they can use admin features.
    """
    def get_sha256(s: str):
        return sha256(s.strip().encode('utf-8')).hexdigest()

    def get_sha512(s: str):
        return sha512(s.strip().encode('utf-8')).hexdigest()

    def get_md5(s: str):
        return md5(s.strip().encode('utf-8')).hexdigest()

    IP = socket.gethostbyname(socket.gethostname())

    if get_md5(IP) not in VALID_MD5:
        raise PermissionError("Access denied: You are not authorized to access the map maker. MD5 hash failed")

    if get_sha256(IP) not in VALID_256:
        raise PermissionError("Access denied: You are not authorized to access the map maker. SHA-256 hash failed")

    if get_sha512(IP) not in VALID_512:
        raise PermissionError("Access denied: You are not authorized to access the map maker. SHA-512 hash failed")

    return True