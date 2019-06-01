#Класс приложений
class Attachment():
    image_path = ""
    name = ""
    description = ""
    href = ""

    def __init__(self, image_path, name, description, href):
        self.image_path = image_path
        self.name = name
        self.description = description
        self.href = href

#Инициализация массива приложений
Attachments = []

#DetailSearcher
detailSearcher = Attachment('test.png', 'DetailSearcher', 'Дескриптион типа азаза', 'DetailSearcher')
detailSearcher2 = Attachment('test.png', 'DetailSearcher2', 'Дескриптион типа азаза', 'DetailSearcher')


#Добавляем приложения в массив приложений
Attachments.append(detailSearcher)
Attachments.append(detailSearcher2)
def getAtachments():
    return Attachments
