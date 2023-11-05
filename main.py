import os
from io import BytesIO
from urllib import request

from PIL import Image


class OnePiecePage:
    def __init__(self, chapter: int, page: int) -> None:
        self.chapter = chapter
        self.page = page

    def getUrl(self) -> str:
        return f"https://cdn.readonepiece.com/file/mangap/2/1{str(self.chapter).rjust(4, '0')}000/{self.page}.jpeg"

    def loadPage(self) -> Image.Image:
        # The response is either an image, or a JSON stating that the page doesn't exist (with the status code 404).
        try:
            req = request.Request(self.getUrl(), headers={"User-Agent": "Mozilla/5.0"})
            res = request.urlopen(req).read()
            return Image.open(BytesIO(res))
        except KeyboardInterrupt:
            exit()
        except:
            raise RuntimeError(f"Could not load chapter {chapter}, page {page}")

    def loadAndSave(self) -> None:
        pageDir = f"chapters/{chapter}"
        if not os.path.exists(pageDir):
            os.makedirs(pageDir)
        self.loadPage().save(f"{pageDir}/{page}.jpeg")
        print(f"Saved chapter {chapter}, page {page}")


if __name__ == "__main__":
    chapter = 1
    while chapter <= 100:
        page = 1
        fetchedAnyPage = False
        while True:
            try:
                OnePiecePage(chapter, page).loadAndSave()
            except KeyboardInterrupt:
                exit()
            except RuntimeError:
                break
            fetchedAnyPage = True
            page += 1
        if not fetchedAnyPage:
            break
        chapter += 1
