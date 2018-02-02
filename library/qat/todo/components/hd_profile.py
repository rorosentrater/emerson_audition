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
            "total": "div#stats>table>tbody>tr>td:nth-child(1)",
            "completed": "div#stats>table>tbody>tr>td:nth-child(2)",
            "incomplete": "div#stats>table>tbody>tr>td:nth-child(3)"
        }
