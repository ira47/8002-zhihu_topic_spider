import csv

index = 0
topic_list = []
html_head = 'https://www.zhihu.com/topic/'
html_tail = '/hot'

read = open('Data_sort.csv', 'r', newline='')
reader = csv.reader(read)
write = open('topic_final.csv', 'w', newline='')
writer = csv.writer(write)
for row in reader:
    topic_id = row[1]
    topic_name = row[0]
    topic_viewer = row[2]
    url = html_head + topic_id + html_tail

    if topic_id not in topic_list:
        writer.writerow([topic_id, topic_name, topic_viewer, url])
        topic_list.append(topic_id)

    index += 1
    if index % 1000 == 0:
        print(index)
