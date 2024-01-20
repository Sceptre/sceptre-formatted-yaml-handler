# -*- coding: utf-8 -*-

from template_handler.custom import Custom


class TestCustom:
    handler = Custom(name="test")

    def setup_method(self):
        self.handler.argument = "test"

    def test_custom(self):
        self.handler.handle()
