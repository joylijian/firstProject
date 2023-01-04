import pytest


@pytest.mark.hanshu  # 标记测试用例为函数，用于分组执行
def test_AA():
    print("函数函数函数函数")


class TestLogin02:
    @pytest.mark.run(order=3)  # 用于改变测试用例的执行顺序
    def test_05(self):
        print("pytest学习！222222222222")

    @pytest.mark.run(order=1)  # 失败的测试用例
    def test_03(self):
        print("pytest学习！33333333")
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_04(self):
        print("pytest学习！44444444444")

    @pytest.mark.skip(reason="测试跳过")  # 无条件跳过
    def test_BB(self):
        print("被跳过！")

    @pytest.mark.skipif(num=10, reason="测试跳过")  # 有条件跳过
    def test_CC(self):
        print("被跳过！")


if __name__ == '__main__':
    pytest.main()
