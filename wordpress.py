# This was used in combination with wordcloud.py
# This script gets all the words from my wordpress site and create a wordcloud.txt
# and then wordcloud.py will use that txt file to generate a wordcloud image with the words that appear the most

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts
from wordpress_xmlrpc import WordPressTerm
from wordpress_xmlrpc.methods import posts
from os import path
from decryption import load_key, decrypt_message
import re

def remove_html_tags(text):

    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

password = decrypt_message(b'abcd')    # replace password here 
email = # put the email associated with wordpress account here

client = Client('https://kennyl.us/xmlrpc.php', email, password)
data = []
offset = 0
increment = 100
while True:
    wp_posts = client.call(posts.GetPosts({'number': increment, 'offset': offset}))
    if len(wp_posts) == 0:
        break # no more posts returned
    with open("temp.txt", "w", encoding ="utf-8") as file:
        for post in wp_posts:
            file.write(post.title)
            file.write(post.content)
    offset = offset + increment

dirname = path.dirname(__file__)
original_text = open(path.join(dirname, 'temp.txt'),'r',encoding='utf-8').read()
text_without_html = remove_html_tags(original_text)

with open("wordcloud.txt", "w", encoding="utf-8") as file:
    file.write(text_without_html)
 

