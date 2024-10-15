import requests
import pandas
import numpy
import matplotlib.pyplot
from PIL import Image, ImageFilter

URL = 'https://alfabank.ru/'
response = requests.get(URL)


class requests:
    if response.status_code == 200:

        data = response.url
        print(f'Статус ответа: OK [код 200]')

    else:
        print('Ошибка при выполнении запроса')


class Pandas:
    data = pandas.read_fwf(r'C:\Users\DanilKuchinsky\PycharmProjects\module11_1')
    print(data.head())


class Numpy:
    arr = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    sum = numpy.sum(arr)
    flip = numpy.flip(arr)

    print(arr)
    print(sum)
    print(flip)


class matplotlib:
    x = [5, 4, 3, 2, 1]
    y = [10, 20, 15, 25, 30]

    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.xlabel('ось X')
    matplotlib.pyplot.ylabel('ось Y')
    matplotlib.pyplot.title('Пример линейного графика')
    matplotlib.pyplot.show()


class Pillow:
    image = Image.open(r'C:\Users\DanilKuchinsky\PycharmProjects\module11_1')
    resized_image = image.resize((800, 600))
    resized_image.save('resized_image.jpg')

    blurred_image = image.filter(Image)
    blurred_image.save('blurred_image.jpg')

    image.save('converted_image.jpg')
    image.save('converted_image.gif')
