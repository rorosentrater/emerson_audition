# encoding: UTF-8
from pyscc import Component, component_group


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

    @component_group
    def shop_category_nutritional_sups(self):
        return {
            '_': '//li[@ng-if="category.category == \'Nutritional Supplements\'"]',
            'nutritional_supplements': '/a',
            'amino_acids': '/ul/li/a[contains(text(), "Amino Acids")]',
            'antioxidants': '/ul/li/a[contains(text(), "Antioxidants")]',
            'coq10': '/ul/li/a[contains(text(), "CoQ10")]',
            'enzymes': '/ul/li/a[contains(text(), "Enzymes")]',
            'greens_powders': '/ul/li/a[contains(text(), "Greens Powders")]',
            'herbal_products': '/ul/li/a[contains(text(), "Herbal Products")]',
            'magnesium': '/ul/li/a[contains(text(), "Magnesium")]',
            'medical_foods': '/ul/li/a[contains(text(), "Medical Foods")]',
            'omegas': '/ul/li/a[contains(text(), "Omegas")]',
            'phospholipids': '/ul/li/a[contains(text(), "Phospholipids")]',
            'probiotics': '/ul/li/a[contains(text(), "Probiotics")]',
            'Protein Powders': '/ul/li/a[contains(text(), "Protein Powders")]',
        }

    @component_group
    def shop_category_addl_options(self):
        return {
            '_': '//div[@class="addl-categories flex"]/div/div/ul/li',
            'acupuncture': '/a[contains(text(), "Acupuncture & Oriental Medicine")]',
            'animal_health': '/a[contains(text(), "Animal Health")]',
            'ayurvedic': '/a[contains(text(), "Ayurvedic Formulas")]',
            'childrens': '/a[contains(text(), "Children’s Health")]',
            'food_beverage': '/a[contains(text(), "Food & Beverage")]',
            'homeopathic': '/a[contains(text(), "Homeopathic Products")]',
            'household_ess': '/a[contains(text(), "Household Essentials")]',
            'medical_supplies': '/a[contains(text(), "Medical Supplies")]',
            'prescription': '/a[contains(text(), "Prescription Items (Rx)")]',
            'skin_care': '/a[contains(text(), "Skin & Personal Care")]',
            'sports_fitness': '/a[contains(text(), "Sports & Fitness")]',
            'vitamins_minerals': '/a[contains(text(), "Vitamins & Minerals")]',

        }

    @component_group
    def shop_brand_options(self):
        return {
            '_': '//h3[contains(text(), "Featured Brands")]/..',
            'brand1_logo': '/div/div[1]/div/div[@class="brand-logo"]',
            'brand1_shop': '/div/div[1]/div/div[@class="brand-summary"]/p/a',
            'brand2_logo': '/div/div[2]/div/div[@class="brand-logo"]',
            'brand2_shop': '/div/div[2]/div/div[@class="brand-summary"]/p/a',
            'brand3_logo': '/div/div[3]/div/div[@class="brand-logo"]',
            'brand3_shop': '/div/div[3]/div/div[@class="brand-summary"]/p/a',
            'all': '/div/div/ul/li/a[@href="brands/directory/All"]',
            'a_g': '/div/div/ul/li/a[@href="brands/directory/a-g"]',
            'h_l': '/div/div/ul/li/a[@href="brands/directory/h-l"]',
            'm_r': '/div/div/ul/li/a[@href="brands/directory/m-r"]',
            's_z': '/div/div/ul/li/a[@href="href="brands/directory/s-z"]'
        }
