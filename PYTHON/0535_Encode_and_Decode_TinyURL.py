# 20/09/2026
# Medium
# LeetCode 535: Encode and Decode TinyURL using basic dictionary and counter mapping.

class Codec:
    def __init__(self):
        self.url_map = {}
        self.count = 0
    def encode(self, longUrl: str) -> str:
        self.count += 1
        short_url = "http://tinyurl.com/" + str(self.count)
        self.url_map[short_url] = longUrl
        return short_url
    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]
if __name__ == "__main__":
    obj = Codec()
    tiny = obj.encode("https://leetcode.com/problems/design-tinyurl")
    print(tiny)
    print(obj.decode(tiny))