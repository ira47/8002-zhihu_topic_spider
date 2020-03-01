import csv

index = 0
topic_list = []
read = open('Data_sort.csv', 'r', newline='')
reader = csv.reader(read)
write = open('topic_final.csv', 'w', newline='')
writer = csv.writer(write)
for row in reader:
    topic_id = row[1]
    topic_name = row[0]
    topic_viewer = row[2]

    if topic_id not in topic_list:
        writer.writerow([topic_id, topic_name, topic_viewer])
        topic_list.append(topic_id)

    index += 1
    if index % 1000 == 0:
        print(index)
