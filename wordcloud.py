# This was used in combination of wordpress.py
# wordpress.py gets all the post from my wordpress site and then output a file wordcloud.txt
# This script will then create a word cloud image with the words that appear the most
# cover.png was used as the shape that contains all those words

import numpy
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image



shape = numpy.array(Image.open("cover.png"))

stopwords= set(STOPWORDS)
stopwords.update(["nbsp","will","need","one","using","name","use","file","right","click","new","now"])

dirname = path.dirname(__file__)
    
text = open(path.join(dirname, 'wordcloud.txt'),'r',encoding='utf-8').read()

wordcloud = WordCloud(stopwords=stopwords, max_words=500, background_color="white", contour_width=5, mask=shape, contour_color='black').generate(text)

plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")

plt.show()
