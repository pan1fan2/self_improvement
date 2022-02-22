import time
import threading

from aiohttp import request

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print('Done something')

# do_something()
# do_something()

# finish = time.perf_counter()

# print("Finished in {:.2f} seconds".format(finish - start)) # 2.00s

"""Try threading"""

start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second(s)...")
#     time.sleep(seconds)
#     return 'Done something'

# t1 = threading.Thread(target=do_something) # pass in the func. by itself
# t2 = threading.Thread(target=do_something) 

# t1.start() # run the thread
# t2.start()

# t1.join() # ensure the func is complete before executing 'finish'
# t2.join()

# threads = []
# # try to run 10 times
# for _ in range(10):
#     t = threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print("Finished in {:.2f} seconds".format(finish - start)) # 2.00s


# try threading pool
# import concurrent.futures
# def do_something(seconds):
#     print(f"Sleeping {seconds} second(s)...")
#     time.sleep(seconds)
#     return f'Done something...{seconds}'

# # We can use a with statement to ensure threads are cleaned up promptly
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # f1 = executor.submit(do_something,1)
#     # f2 = executor.submit(do_something,1)
#     # print(f1.result())
#     # print(f2.result())
#     secs = [5, 4, 3, 2,1]
#     # results = [executor.submit(do_something,sec) for sec in secs]

#     # for f in concurrent.futures.as_completed(results):
#     #     print(f.result())
#     results = executor.map(do_something,secs)

#     for result in results:
#         print(result)

# finish = time.perf_counter()

# print("Finished in {:.2f} seconds".format(finish - start)) # 2.00s

import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')