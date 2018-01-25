from pyscc import Component, component_element,  component_group


class Home(Component):

    @component_element
    def logo(self):
        return 'a h1.logo.animated.slideInDown'

    @component_element
    def task_header(self):
        return '.seven.columns h1.logo'

    @component_element
    def create_header(self):
        return '.five.columns h1.logo'

    @component_group
    def social(self):
        return {
            'social': '#social',
            'twitter': 'a i.ico.ico-mat.fi-social-twitter',
            'linkedin': 'a i.ico.ico-mat.fi-social-linkedin',
            'github': 'a i.ico.ico-mat.fi-social-github'
        }

    @component_group
    def task(self):
        return {
            'task': 'todo-task',
            'checkbox': 'input[type="checkbox"]',
            'created_content': 'todo-task > h4',
            'date': 'todo-task i.ico.ico-left.fi-calendar',
            'assignee': 'todo-task #assignee',
            'delete': '#deleteTasks'
        }

    @component_group
    def create(self):
        return {
            'form': 'create-todo > form',
            'assignee': '#taskAssignee',
            'title': '#taskTitle',
            'content': '#taskContent',
            'create': '.is-success.u-pull-right'
        }
