import random

import pytest


class TestFun:

    def setup_class(self):
        self.a = random.randint(1, 100)
        self.e = self.a
        self.f = self.a

    def teardown_class(self):
        pass

    @pytest.mark.skip(reason='我想跳过')
    def test_a(self):
        b = self.e
        print(b)

    def test_c(self):
        c = self.f
        print(c)
