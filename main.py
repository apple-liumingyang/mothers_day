import multidict
import numpy.random
import matplotlib.pyplot as plt
from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator


def transform_format(rgb):
    """
    该函数用于去除杂色
    :param rgb: 原始 RGB 颜色组
    :return: 去除杂色之后的 RGB 颜色组
    """

    if rgb[0] > 245 and rgb[1] > 245 and rgb[2] > 245:
        rgb[0] = rgb[1] = rgb[2] = 255
    return rgb


def gen_cloud(file_path, name):
    words = multidict.MultiDict()

    # 初始化两个最大权重的
    words.add('母亲节快乐', 10)
    words.add(name, 12)

    # 随意插入新的词语
    for i in range(1000):
        words.add('妈妈', numpy.random.randint(1, 5))
        words.add('您辛苦了', numpy.random.randint(1, 5))
        words.add(name, numpy.random.randint(1, 5))

    # 设定图片
    bimg = imread(file_path)
    for color in range(len(bimg)):
        bimg[color] = list(map(transform_format, bimg[color]))

    word_cloud = WordCloud(
        background_color='white',
        mask=bimg,
        font_path='fonts/PingFang Bold.ttf'
    ).generate_from_frequencies(words)

    # 生成词云
    bimg_colors = ImageColorGenerator(bimg)

    # 渲染词云
    plt.axis('off')
    plt.imshow(word_cloud.recolor(color_func=bimg_colors))
    plt.savefig(f'{name}.png')
    plt.show()


def main():
    gen_cloud('images/mother.jpeg', '母亲节快乐')


if __name__ == '__main__':
    main()
