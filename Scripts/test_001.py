import pytest,allure

class Test_001:
    @allure.step(title = "这是第一条测试用例")
    def test_01(self):
        # print("test_01---->")

        assert 1
    @allure.step(title = "这是第二条测试用例")
    def test_02(self):
        # print("test_02----->")
        assert 0