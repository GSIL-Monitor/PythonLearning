from bs4 import BeautifulSoup

# import os

with open('D:/workspace/python/tt.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    host_select_path = '''div.container.new-discussion-timeline.experiment-repo-nav > div.repository-content > div.file > div.blob-wrapper.data.type-text > table > tbody > tr > td.blob-code blob-code-inner-js-file-line'''
    hosts = Soup.select(host_select_path)
    print (hosts)

    # //*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[50]/td[2]
