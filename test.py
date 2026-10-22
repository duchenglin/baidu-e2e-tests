import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="96b41475-2bde-4c61-aa0d-e63776ecf97c",
    name="Verify Baidu Homepage Elements and Title",
    tc_id="TC-2",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"baidu_search_button_visible": "true", "baidu_search_button_clickable": "true", "baidu_logo_displayed": "true", "page_title_check": "\u767e\u5ea6\u4e00\u4e0b\uff0c\u4f60\u5c31\u77e5\u9053", "search_input_field_present": "true", "search_input_field_enabled": "true"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.baidu.com', instruction_id='cb268bf58e224ac29fcd46c09338578e'):
        await page.goto("https://www.baidu.com")
    
    async with testmu.step('Navigate to https://www.baidu.com', instruction_id='800524d6dadc4ddaa76dd6e9f9f054b6'):
        await page.goto("https://www.baidu.com")
    
    async with testmu.step('Checking whether the Baidu search button is visible'):
        set_var('baidu_search_button_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {35: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r=el(35).getBoundingClientRect(), s=getComputedStyle(el(35)); return r.width>0 && r.height>0 && s.display!=='none' && s.visibility!=='hidden' && s.opacity!=='0'; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="百度一下"i]'], query='whether the search button with the text “百度一下” is present (in the central search form)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the search button with the text “百度一下” is visible'))
    
    async with testmu.step('Checking whether the Baidu search button is clickable'):
        set_var('baidu_search_button_clickable', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {35: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r=el(35).getBoundingClientRect(), s=getComputedStyle(el(35)); return !el(35).disabled && r.width>0 && r.height>0 && s.pointerEvents!=='none' && s.display!=='none' && s.visibility!=='hidden'; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=button[name="百度一下"i]'], query='whether the search button with the text “百度一下” clickable is present (in the central search form)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the search button with the text “百度一下” is clickable'))
    
    async with testmu.step('whether the Baidu logo is present (above the central search field)', instruction_id='20e83b5607d54c67a5617d26372dd161'):
        set_var('baidu_logo_displayed', await testmu.vision_query(page, "whether the Baidu logo is present (above the central search field)", "", expected_value='true'))
    
    async with testmu.step('Reading the current page title', instruction_id='ca81dc38c7a742019359d59c0632b8bd'):
        set_var('page_title_check', await page.title())
    
    async with testmu.step('Checking whether the search input field is present'):
        set_var('search_input_field_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {29: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const r=el(29).getBoundingClientRect(), s=getComputedStyle(el(29)); return r.width>0 && r.height>0 && s.display!=='none' && s.visibility!=='hidden'; })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=textbox[name="美股收盘：SpaceX涨超7%"i]'], query='whether the search input field is present (in the central search form)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the search input field is present'))
    
    async with testmu.step('Checking whether the search input field is enabled'):
        set_var('search_input_field_enabled', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {29: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!el(29).disabled && !el(29).readOnly);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=textbox[name="美股收盘：SpaceX涨超7%"i]'], query='whether the search input field enabled is present (in the central search form)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the search input field is enabled'))
    
    async with testmu.step('the Baidu logo is displayed on the page', instruction_id='660b3de387b1450bacb2e8e84aae2985'):
        await testmu.verify_assertion(page, 'the Baidu logo is displayed on the page', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the Baidu logo is displayed on the page', 'store_key': 'baidu_logo_displayed', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{baidu_logo_displayed}}', 'variable_refs': {'{{baidu_logo_displayed}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'Baidu logo displayed on the page', 'claim': 'the Baidu logo is displayed on the page'})
    
    async with testmu.step('the search input field is present and enabled', instruction_id='d85c01bb0a5c4305a98c00d905bc66fb'):
        await testmu.verify_assertion(page, 'the search input field is present and enabled', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the search input field is present', 'store_key': 'search_input_field_present', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{search_input_field_present}}', 'variable_refs': {'{{search_input_field_present}}': 'true'}, 'json_path': None}, {'description': 'the search input field is enabled', 'store_key': 'search_input_field_enabled', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{search_input_field_enabled}}', 'variable_refs': {'{{search_input_field_enabled}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'search input field present and enabled', 'claim': 'the search input field is present and enabled'})
    
    async with testmu.step('the search button with the text “百度一下” is visible and clickable', instruction_id='85c708d4e2f54be2bf4301a9ffedb7de'):
        await testmu.verify_assertion(page, 'the search button with the text “百度一下” is visible and clickable', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the search button with the text “百度一下” is visible', 'store_key': 'baidu_search_button_visible', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{baidu_search_button_visible}}', 'variable_refs': {'{{baidu_search_button_visible}}': 'true'}, 'json_path': None}, {'description': 'the search button with the text “百度一下” is clickable', 'store_key': 'baidu_search_button_clickable', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{baidu_search_button_clickable}}', 'variable_refs': {'{{baidu_search_button_clickable}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'search button with the text “百度一下” visible and clickable', 'claim': 'the search button with the text “百度一下” is visible and clickable'})
    
    async with testmu.step('the page title is “百度一下，你就知道”', instruction_id='4ee312ac3ce640258dd4466c89fa38ea'):
        await testmu.verify_assertion(page, 'the page title is “百度一下，你就知道”', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the page title is “百度一下，你就知道”', 'store_key': 'page_title_check', 'expected_value': '百度一下，你就知道', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{page_title_check}}', 'variable_refs': {'{{page_title_check}}': '百度一下，你就知道'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'page title', 'claim': 'the page title is “百度一下，你就知道”'})


if __name__ == "__main__":
    testmu.run(test)