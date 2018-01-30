from pyscc import Component, component_element, component_elements, component_group


class Home(Component):

    @component_element
    def task_header(self):
        return '.seven.columns h1.logo'

    @component_element
    def create_header(self):
        return '.five.columns h1.logo'

    @component_elements
    def items(self):
        return 'todo-list > ul > li'

    @component_group
    def task(self):
        return {
            '_': 'todo-list',
            'task': 'todo-task',
            'checkbox': 'input[type="checkbox"]',
            'created_content': 'h4',
            'date': 'i.ico.ico-left.fi-calendar',
            'assignee': '#assignee',
            'delete': '#deleteTasks'
        }

    @component_group
    def create(self):
        return {
            '_': 'create-todo',
            'assignee': '#taskAssignee',
            'title': '#taskTitle',
            'content': '#taskContent',
            'create': '.is-success.u-pull-right'
        }
