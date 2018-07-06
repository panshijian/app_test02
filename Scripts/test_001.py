import pytest,allure

class Test_001:
    @allure.step(title = "这是第一条测试用例")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_01(self):
        # print("test_01---->")
        allure.attach("描述","1.点击登录")
        allure.attach("描述","2.点击使用邮箱登录")
        assert 1
    @allure.step(title = "这是第二条测试用例")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)


    def test_02(self):
        # print("test_02----->")
        allure.attach("描述","3.输入邮箱账号")
        allure.attach("描述","4.输入密码")
        assert 0