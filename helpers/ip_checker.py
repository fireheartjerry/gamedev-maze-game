from hashlib import sha256, sha512, md5
import socket

USER_IP = socket.gethostbyname(socket.gethostname())

VALID_256 = {
    "999ceb3f42c9f82b65419d88d5aa53f5677fe813077488855cf81ff243199e65"
}

VALID_512 = {
    "3d8fb9ceb13edfa6173b0fce93daf5ee68fc372e4fd33db2242bece7913d42e00dab059814909a4b8249d1d51308ca46f52dcf89f7819f05026f80d290282aef"
}

VALID_MD5 = {
    "e8b24934679afcb5bf2706163c0cb2fa"
}

print(USER_IP)