def process(task):
    count = 0
    min_work = min(task)
    max_work = max(task)
    min_work_index = task.index(min_work)
    task.pop(min_work_index)
    task.insert(min_work_index, (max_work + min_work))
    count += min_work
    return task, count, min_work_index


task = [int(x) for x in input().split(', ')]
index = int(input())

result = 0

for _ in range(len(task)):
    task, count, min_index = process(task)
    result += count

    if index == min_index:
        break

print(result)