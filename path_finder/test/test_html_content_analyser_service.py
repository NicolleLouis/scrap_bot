from ddt import ddt, data, unpack
from django.test import TestCase

from path_finder.services.html_content_analyser import HtmlContentAnalyserService


@ddt
class HtmlContentAnalyserServiceTestCase(TestCase):
    def setUp(self):
        pass

    @data(
        (
                "<div>class=test</div>",
                ["test"]
        ),
        (
                "<div>class=test</div>"
                "<div>class=testbis</div>",
                ["test", "testbis"]
        ),
        (
                "<div>class=\"test testbis\"/div>",
                ["test", "testbis"]
        ),
        (
                "<div>class=\"test testbis\"/div>"
                "<div>class=\"joker jokerbis\"/div>",
                ["test", "testbis", "joker", "jokerbis"]
        ),
        (
                "<div>class=test/div>"
                "<div>class=\"joker jokerbis\"/div>",
                ["test", "joker", "jokerbis"]
        ),
        (
                "class=site-title-nav",
                ["site-title-nav"]
        )
    )
    @unpack
    def test_update_url(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.get_all_classes(value),
            result
        )

    @data(
        (
                ["", "otter"],
                ["otter"]
        ),
        (
                ["otter"],
                ["otter"]
        ),
    )
    @unpack
    def test_(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.remove_empty_classes(value),
            result
        )

    @data(
        (
                "<div>class=test</div>",
                ["test"]
        ),
        (
                "<div>class=test</div>"
                "<div>class=testbis</div>",
                ["test", "testbis"]
        ),
    )
    @unpack
    def test_get_all_singular_classes(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.get_all_singular_classes(value),
            result
        )

    @data(
        (
                "<div>class=\"test testbis\"/div>",
                ["test", "testbis"]
        ),
        (
                "<div>class=\"test testbis\"/div>"
                "<div>class=\"joker jokerbis\"/div>",
                ["test", "testbis", "joker", "jokerbis"]
        ),
    )
    @unpack
    def test_get_all_multiple_classes(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.get_all_multiple_classes(value),
            result
        )

    @data(
        (
                ["test", "testbis"],
                ["test", "testbis"]
        ),
        (
                [["test", "testbis"], ["joker", "jokerbis"]],
                ["test", "testbis", "joker", "jokerbis"]
        ),
        (
                [["test", "testbis"]],
                ["test", "testbis"]
        ),
    )
    @unpack
    def test_flatten_array(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.flatten_array(value),
            result
        )

    @data(
        (
                ["a", "b"],
                [
                    {
                        "value": "a",
                        "occurences": 1
                    },
                    {
                        "value": "b",
                        "occurences": 1
                    },
                ]
        ),
        (
                ["a", "b", "a"],
                [
                    {
                        "value": "a",
                        "occurences": 2
                    },
                    {
                        "value": "b",
                        "occurences": 1
                    },
                ]
        ),
    )
    @unpack
    def test_count_class_occurences(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.count_class_occurences(value),
            result
        )

    @data(
        (
                "<div>class=\"test testbis\"/div>",
                [
                    {
                        'occurences': 1,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ]
        ),
        (
                "<div>class=\"test test\"/div>",
                [
                    {
                        'occurences': 2,
                        'value': 'test'
                    }
                ]
        ),
        (
                "<div>class=\"test testbis\"/div>"
                "<div>class=test",
                [
                    {
                        'occurences': 2,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ]
        ),
        (
                "<div>class=\"test testbis testbis\"/div>",
                [
                    {
                        'occurences': 2,
                        'value': 'testbis'
                    },
                    {
                        'occurences': 1,
                        'value': 'test'
                    }
                ]
        ),
    )
    @unpack
    def test_get_classes_with_occurences(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.get_classes_with_occurences(value),
            result
        )

    @data(
        (
                [
                    {
                        'occurences': 1,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ],
                [
                    {
                        'occurences': 1,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ],
        ),
        (
                [
                    {
                        'occurences': 1,
                        'value': 'test'
                    },
                    {
                        'occurences': 2,
                        'value': 'testbis'
                    }
                ],
                [
                    {
                        'occurences': 2,
                        'value': 'testbis'
                    },
                    {
                        'occurences': 1,
                        'value': 'test'
                    }
                ],
        ),
        (
                [
                    {
                        'occurences': 2,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ],
                [
                    {
                        'occurences': 2,
                        'value': 'test'
                    },
                    {
                        'occurences': 1,
                        'value': 'testbis'
                    }
                ],
        ),
    )
    @unpack
    def test_order_classes_and_occurences(self, value, result):
        self.assertEqual(
            HtmlContentAnalyserService.order_classes_and_occurences(value),
            result
        )
