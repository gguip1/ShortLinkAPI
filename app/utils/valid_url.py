import re

def valid_url(url: str) -> str:
    if not re.match(r"^(http://|https://)", url):
        return "http://" + url  # 기본적으로 http:// 추가
    return url
