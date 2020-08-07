import re


class HtmlContentAnalyserService:
    @staticmethod
    def flatten_array(array):
        result_array = []
        for sublist in array:
            if type(sublist) is list:
                result_array.extend(sublist)
            else:
                result_array.append(sublist)
        return result_array

    @staticmethod
    def remove_empty_classes(classes_list):
        return list(
            filter(
                lambda item: item != "", classes_list
            )
        )

    @staticmethod
    def get_all_singular_classes(html_content):
        no_string_encapsulation_classes = re.findall(r"class=[a-z0-9]*", html_content)
        no_string_encapsulation_classes = list(
            map(
                lambda match: match.replace("class=", ""),
                no_string_encapsulation_classes
            )
        )
        return no_string_encapsulation_classes

    @staticmethod
    def get_all_multiple_classes(html_content):
        string_encapsulation_classes = re.findall(r"class=\"[ a-z0-9]*\"", html_content)
        string_encapsulation_classes = list(
            map(
                lambda match: match.replace("\"", "").replace("class=", "").split(" "),
                string_encapsulation_classes
            )
        )
        string_encapsulation_classes = HtmlContentAnalyserService.flatten_array(
            string_encapsulation_classes
        )
        return string_encapsulation_classes

    @staticmethod
    def get_all_classes(html_content):
        all_classes = []
        no_string_encapsulation_classes = HtmlContentAnalyserService.get_all_singular_classes(
            html_content
        )
        string_encapsulation_classes = HtmlContentAnalyserService.get_all_multiple_classes(html_content)

        all_classes.extend(no_string_encapsulation_classes)
        all_classes.extend(string_encapsulation_classes)

        all_classes = HtmlContentAnalyserService.remove_empty_classes(all_classes)

        return all_classes