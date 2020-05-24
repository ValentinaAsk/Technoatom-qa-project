import time
from selenium.webdriver import ActionChains
from tests.base_ui import BaseCase
from ui.fixtures import *


class TestUIMaimPage(BaseCase):

    @allure.title("Масштабируемость окна приложения")
    @pytest.mark.UI_MAIN
    def test_window_size(self, auto):
        """ Корректность меню при уменьшении страницы.
        Уменьшение окна и поиск кнопки home.
        Кнопка Home видима и доступна.
        """

        self.base_page = auto

        self.driver.set_window_size(350, 750)
        time.sleep(4)
        assert self.base_page.find(self.main_page.locators.HOME_BUTTON).is_displayed()
        self.driver.maximize_window()

    @allure.title("Наличие идентификатора пользователя(имя и vk_id)")
    @pytest.mark.UI_MAIN
    def test_log_info(self, auto):
        """ Наличие и корректность информации о текущем пользователе в правом верхем углу.
        Поиск объекта с данными.
        Имя и vk_id успешно отображены.
        """

        self.base_page = auto
        vk_id = self.base_page.find(self.main_page.locators.LOG_VK_ID, timeout=3).text
        name = self.base_page.find(self.main_page.locators.LOG_USERNAME, timeout=3).text

        vk_id = int(vk_id.split()[-1])
        assert vk_id == 1

        name = name.split()[-1]
        assert name == self.base_page.user

    @allure.title("Наличие факта о языке программирования python")
    @pytest.mark.UI_MAIN
    def test_python_fact(self, auto):
        """ Отображение в нижней части страницы случайного мотивационного факта о python.
        Поиск объекта с данными.
        Факт присутствует.
        """
        self.base_page = auto
        fact = self.base_page.find(self.main_page.locators.FACT_PYTHON_DIV, timeout=3).text
        assert fact

    @allure.title("Корректность ссылки на страницу с исторей питона")
    @pytest.mark.UI_MAIN
    def test_python_history_link(self, auto):
        """Корректность ссылки на страницу с исторей питона.
        Нажатие на кпопку "Python history" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.PYTHON_HISTORY_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        title = self.driver.title

        assert 'History' in title
        assert 'Python' in title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с информацией о flask")
    @pytest.mark.UI_MAIN
    def test_flask_link(self, auto):
        """Корректность ссылки на страницу с информацией о flask.
        Нажатие на кпопку "About flask" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.FLASK_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        title = self.driver.title

        assert title in ['flask', 'Flask']

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с информацией о centos")
    @pytest.mark.UI_MAIN
    def test_linux_centos_link(self, auto):
        """Корректность ссылки на страницу с информацией о centos.
        Нажатие на кпопку "Download centos7" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.LINUX_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.CENTOS_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        title = self.driver.title

        assert title in ['centos','Centos']

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с новостями о wireshark")
    @pytest.mark.UI_MAIN
    def test_wireshark_news_link(self, auto):
        """Корректность ссылки на страницу с новостями о wireshark.
        Нажатие на кпопку "wireshark news" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.NEWS_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        title = self.driver.title

        assert title in ['News', 'news']
        assert title in ['Wireshark', 'wireshark']

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с установщиком wireshark")
    @pytest.mark.UI_MAIN
    def test_wireshark_download_link(self, auto):
        """Корректность ссылки на страницу с установщиком wireshark.
        Нажатие на кпопку "wireshark download" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.DOWNLOAD_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'Download' in self.driver.title or 'download' in self.driver.current_url
        assert 'Wireshark' in self.driver.title or 'wireshark' in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с примерами TCP")
    @pytest.mark.UI_MAIN
    def test_tcp_example(self, auto):
        """Корректность ссылки на страницу с примерами TCP.
        Нажатие на кпопку "TCPDump Examples" в выдвигающемся меню.
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        events = self.base_page.find(self.main_page.locators.NETWORK_BUTTON, timeout=3)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.base_page.find(self.main_page.locators.TCPEXAMP_BUTTON).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        title = self.driver.title

        assert title in ['Tcpdump', 'tcpdump']
        assert 'Examples' in title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с будущем интернета")
    @pytest.mark.UI_MAIN
    def test_future_link(self, auto):
        """Корректность ссылки на страницу с информацией о centos.
        Нажатие на иконку под надписью "Future of Internet".
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        self.base_page.find(self.main_page.locators.FUT_INTERNET_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'future' in self.driver.current_url
        assert 'internet' in self.driver.current_url

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с API")
    @pytest.mark.UI_MAIN
    def test_api_link(self, auto):
        """Корректность ссылки на страницу с API.
        Нажатие на иконку под надписью "What is an API?".
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        self.base_page.find(self.main_page.locators.API_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert self.driver.title in ['Application programming interface', 'API']

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу с SMTP")
    @pytest.mark.UI_MAIN
    def test_smtp_link(self, auto):
        """Корректность ссылки на страницу с SMTP.
        Нажатие на иконку под надписью "Lets talk about SMTP?".
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        self.base_page.find(self.main_page.locators.SMTP_BUTTON, timeout=3).click()

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'SMTP' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])

    @allure.title("Корректность ссылки на страницу питона")
    @pytest.mark.UI_MAIN
    def test_python_link(self, auto):
        """Корректность ссылки на страницу питона.
        Нажатие на кпопку "Python".
        Новая вкладка с корректной страницей.
        """

        self.base_page = auto
        self.base_page.find(self.main_page.locators.PYTHON_BUTTON, timeout=3).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

        assert 'python' in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(windows[0])










#
# class LinkDataWithActionChain:
#
#     python_history = ('PYTHON_BUTTON', 'PYTHON_HISTORY_BUTTON', ['python', 'history'])
#     flask = ('PYTHON_BUTTON', 'FLASK_BUTTON', ['flask'])
#
#     linux_centos = ('LINUX_BUTTON', 'CENTOS_BUTTON', ['centos'])
#
#     wireshark_news = ('NETWORK_BUTTON', 'NEWS_BUTTON', ['wireshark', 'news'])
#     wireshark_download = ('NETWORK_BUTTON', 'DOWNLOAD_BUTTON', ['wireshark', 'downloads'])
#     tcp_example = ('NETWORK_BUTTON', 'TCPEXAMP_BUTTON', ['tcp'])
#
#
# class LinkData:
#     future = ('FUT_INTERNET_BUTTON', [])
#     api = ('API_BUTTON', ['API'])
#     smtp = ('SMTP_BUTTON', ['SMTP'])
#     python = ('PYTHON_BUTTON', ['python'])
