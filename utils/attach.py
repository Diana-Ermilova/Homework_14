import allure
from allure_commons.types import AttachmentType
import logging
import json
from requests import Response

def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

def add_logs(browser, log_type='browser'):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type=log_type))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

def add_video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')

def log_response(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + str(response.request.body))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)

def attach_response(response: Response):

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=response.request.body,
            name="Request body",
            attachment_type=AttachmentType.TEXT,
            extension=".txt",
        )
        if 'json' in response.headers.get('content-type', ''):
            allure.attach(
                body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                name="Response",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )
        else:
            allure.attach(
                body=response.text,
                name="Response",
                attachment_type=AttachmentType.TEXT,
                extension="html",
            )

