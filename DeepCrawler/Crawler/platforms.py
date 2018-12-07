class Platforms:
    GOOGLE = 1
    NAVER_BLOG = 2

    @staticmethod
    def toInt(type):
        result = None
        if type == "Naver_Blog":
            result = Platforms.NAVER_BLOG
        elif type == "Google":
            result = Platforms.GOOGLE
        else:
            assert False,"Platform error"
        return result
