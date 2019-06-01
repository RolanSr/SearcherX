#Класс приложений
class Attachment():
    image_path = ""
    name = ""
    description = ""
    href = ""

    def __init__(self, image_path, name, href):
        self.image_path = image_path
        self.name = name
        self.href = href

#Инициализация массива приложений
Attachments = []

#DetailSearcher
detailSearcher = Attachment('detailsearcher.png', 'DetailSearcher','main/detailsearcher/')
detailSearcher.description = "Поиск автозапчастей по их артикулу (номер ОЕМ)"


#expressadds
expressadds = Attachment('expressadds.png', 'ExpressAdds','main/expressadds/')
expressadds.description = "Автономное размещение объявлений на интернет ресурсах вроде: olx.kz, market.kz, kolesa,lz и т.д"

#Добавляем приложения в массив приложений
Attachments.append(detailSearcher)
Attachments.append(expressadds)


def getAtachments():
    return Attachments
