from pyscc import Component, component_element, component_group


class Profile(Component):

    @component_element
    def user_profile_header(self):
        return "profile.text-center>h1"

    @component_element
    def latest_task(self):
        return "profile.text-center>h4>a"

    @component_group
    def stats(self):
        return {
            "_": "div#stats>table>tbody>tr",
            "total": "td:nth-child(1)",
            "completed": "td:nth-child(2)",
            "incomplete": "td:nth-child(3)"
        }
