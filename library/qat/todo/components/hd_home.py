from pyscc import Component, component_element, component_elements, component_group


class Home(Component):

    @component_element
    def todo_logo(self):
        return "h1.logo.animated.slideInDown"

    @component_group
    def social_links(self):
        return {
            "twitter": "i.fi-social-twitter",
            "linkedin": "i.fi-social-linkedin",
            "github": "i.fi-social-github"
        }

    @component_element
    def tasks_logo(self):
        return "div.seven.columns>h1.logo"

    @component_element
    def create_task_logo(self):
        return "div.five.columns>h1.logo"

    @component_elements
    def task_elements(self):
        return "todo-task"

    @component_group
    def task_details(self):
        return {
            "_": "todo-task#${id}",
            "checkbox": "todo-task>h4>input[type=checkbox]",
            "title": "todo-task>h4",
            "date_time": "todo-task>span",
            "assignee": "#assignee"
        }

    @component_group
    def task_creation(self):
        return {
            "_": "form",
            "task_assignee": "#taskAssignee",
            "task_title": "#taskTitle",
            "task_content": "#taskContent",
            "create_task_button": "button.is-success.u-pull-right"
        }

    @component_element
    def delete_button(self):
        return "#deleteTasks"
