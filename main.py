import time

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys


def start_monitor(driver):
    while 1:
        script = """
        window.ended = false
        var videos = document.querySelectorAll('video');
        videos.forEach((video) => {video.addEventListener('ended', (e) => {
            window.ended = true
        })})

        return videos;
        """
        videos = driver.execute_script(script)
        if videos:
            print('Reels page loaded')
            break

        time.sleep(0.5)

    while 1:
        script = """
        return window.ended;
        """
        ended = driver.execute_script(script)

        if ended:
            driver.find_element(by='tag name', value='body').send_keys(Keys.ARROW_DOWN)

            script = """
            window.ended = false
            var videos = document.querySelectorAll('video');
            videos.forEach((video) => {video.addEventListener('ended', (e) => {
                window.ended = true
            })})

            return videos;
            """
            driver.execute_script(script)

        time.sleep(0.01)

        if 'reels' not in driver.current_url:
            print('Stop monitoring reels')
            break


def main():
    driver = Firefox()

    while 1:
        if 'reels' in driver.current_url:
            print('Monitoring reels')
            start_monitor(driver)

        time.sleep(0.5)


if __name__ == '__main__':
    main()