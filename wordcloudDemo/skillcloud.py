from wordcloud import WordCloud

# Read the whole text.

text = '''
hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive ,hive
hivesql, hivesql, hivesql, hivesql, hivesql, hivesql,
Hadoop,Hadoop,Hadoop,Hadoop,Hadoop,Hadoop,Hadoop,Hadoop
spark,spark,spark,spark,spark,spark,spark,
mysql,mysql,mysql mysql,mysql,mysql,mysql,mysql,mysql
hbase,hbase,hbase,hbase,hbase,hbase,
python,python,python,python,python,python,python,python,python
shell,shell,shell,shell,shell,shell,shell,shell
linux,linux,linux,linux,linux,linux,linux,linux,linux
'''
# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
