from pyscc import Component, component_element, component_elements, component_group


class SearchResults(Component):

    @component_element
    def filter_results_button(self):
        return 'p.btn-filter:nth-child(1)'  # Using :nth-child because there is a second hidden identical button in DOM

    @component_element
    def clear_all_button(self):
        return 'a.btn-clear'

    @component_group
    def master_categories(self):
        return {
            '_': '//product-filter/div/ul/li',
            'by_condition': '/span[contains(text(), "By Condition")]',
            'by_category': '/span[contains(text(), "By Category")]',
            'by_brand': '/span[contains(text(), "By Brand")]',
            'by_diet': '/span[contains(text(), "By Dietary Consideration")]',
            'inc_ingredient': '/span[contains(text(), "Include Ingredient")]',
            'exc_ingredient': '/span[contains(text(), "Exclude Ingredient")]',
            'by_quality_partner': '/span[contains(text(), "By Quality Partner")]',
            'by_delivery': '/span[contains(text(), "By Delivery Format")]',
            'by_dosage': '/span[contains(text(), "By Dosage")]'
        }

    @component_elements
    def product_items(self):
        return 'li.product-item-list'

