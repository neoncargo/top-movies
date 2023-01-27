API_VERSIONS = ("@@._V1_", "@._V1_", "._V1_")
POSTFIX1 = "QL75_UY500_"


class ImgUrl:
    def __init__(self, url: str):
        for v in API_VERSIONS:
            i = url.find(v)
            if i != -1:
                break
        else:
            raise ValueError("Not found in " + url)

        self.url = url[:i]
        self.api_version = v

    def serialize(self, postfix: str = POSTFIX1) -> str:
        url = self.url + self.api_version + postfix + ".jpg"
        return url

    url: str
    api_version: str
