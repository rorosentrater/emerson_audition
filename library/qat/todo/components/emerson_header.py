# encoding: UTF-8
from pyscc import Component, component_element, component_group


class Header(Component):

    @component_group
    def header_option(self):
        return {
            'shop': 'a#shopMenuDropdownToggle',
            'brands': '//li/a/span[text()="Brands"]',
            'education': '//li/a/span[text()="Education"]',
            'wellevate': '//li/a/span[text()="Wellevate"]',
            'quality': '//li/a/span[text()="Quality"]'
        }

    @component_group
    def shop_categories(self):
        return {
            '_': '//ul[@id="mega-menu-shop-by"] /li',
            'condition': '/a[contains(text(),"CONDITION")]',
            'category': '/a[contains(text(),"CATEGORY")]',
            'brand': '/a[contains(text(),"BRAND")]',
            'new_products': '/a[contains(text(),"NEW PRODUCTS")]',
            'quality_partners': '/a[contains(text(),"QUALITY PARTNERS")]'
        }

    @component_group
    def shop_condition_options(self):
        # Only works if category is in focus
        return {
            '_': '//li[contains(@class, "active")]//ul/li',
            'adrenal_and_stress': '/a[contains(text(),"Adrenal and Stress")]',
            'allergy': '/a[contains(text(),"Allergy Support")]',
            'blood_sugar': '/a[contains(text(),"Blood Sugar Support")]',
            'bone_support': '/a[contains(text(),"Bone Support")]',
            'brain_and_nervous': '/a[contains(text(),"Brain & Nervous System Support")]',
            'cardiovascular': '/a[contains(text(),"Cardiovascular Support")]',
            'cellular_health': '/a[contains(text(),"Cellular Health")]',
            'dermatological': '/a[contains(text(),"Dermatological Support")]',
            'detoxification': '/a[contains(text(),"Detoxification")]',
            'energy': '/a[contains(text(),"Energy")]',
            'eye_and_ear': '/a[contains(text(),"Eye & Ear Support")]',
            'gastrointestinal': '/a[contains(text(),"Gastrointestinal Health")]',
            'hormone': '/a[contains(text(),"Hormone Support")]',
            'immune': '/a[contains(text(),"Immune Support")]',
            'Mens_Health': '/a[contains(text(),"Men’s Health")]',
            'mood': '/a[contains(text(),"Mood Support")]',
            'musculoskeletal': '/a[contains(text(),"Musculoskeletal Support")]',
            'pain_and_inflammation': '/a[contains(text(),"Pain & Inflammation Support")]',
            'respiratory_support': '/a[contains(text(),"Respiratory Support")]',
            'sleep': '/a[contains(text(),"Sleep Support")]',
            'urinary': '/a[contains(text(),"Urinary Support")]',
            'weight': '/a[contains(text(),"Weight Management")]',
            'womens_health': "/a[contains(text(),\"Women's Health\")]"
        }


