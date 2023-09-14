import requests   # type: ignore
import time
import threading


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time it took: {end - start} seconds")

    return inner


def retrieve_image(image_url):
    requests.get(image_url)


def create_threads(num_of_threads, image_urls):
    threads = []
    for index in range(num_of_threads):
        threads.append(threading.Thread(
            target=retrieve_image, args=(image_urls[index],)))
    return threads


@timer
def start_threads(threads):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main():
    image_urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
        "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
        "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
        "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png"]
    num_threads = 4
    threads = create_threads(num_threads, image_urls)
    start_threads(threads)


if __name__ == '__main__':
    main()
