"""Main module."""
from xml.etree import ElementTree

def process_audit_results(xml_audit_results):
    benchmark_element_expected = ElementTree.parse(xml_audit_results[0]).getroot()
    benchmark_element_observed = ElementTree.parse(xml_audit_results[1]).getroot()

    expected_results = {}
    observed_results = {}
    ns = {'xccdf': 'http://checklists.nist.gov/xccdf/1.2'}
    for expected_rule_result in benchmark_element_expected.findall(
        ".//xccdf:TestResult/xccdf:rule-result", ns):
        idref = expected_rule_result.attrib.get("idref")
        result = expected_rule_result.find("xccdf:result", ns)
        expected_results[idref] = result.text

    for observed_rule_result in benchmark_element_observed.findall(
        ".//xccdf:TestResult/xccdf:rule-result", ns):
        idref = observed_rule_result.attrib.get("idref")
        result = observed_rule_result.find("xccdf:result", ns)
        observed_results[idref] = result.text

    expected_rule_idrefs = expected_results.keys()
    observed_rule_idrefs = observed_results.keys()

    if expected_rule_idrefs != observed_rule_idrefs:
        print("The rules in each audit result XML differ.")

    result_diff_count = 0
    for expected_rule_idref in expected_rule_idrefs:
        expected_result = expected_results[expected_rule_idref]
        observed_result = observed_results[expected_rule_idref]
        if expected_result != observed_result:
            result_diff_count = result_diff_count + 1
            rule_description_element = benchmark_element_expected.find(
        ".//xccdf:Rule[@id='{}']/xccdf:title".format(expected_rule_idref), ns)
            rule_description = rule_description_element.text
            print("{}. {} \n\t{}\n\t\t was {} but {} was expected".format(result_diff_count, expected_rule_idref, rule_description, observed_result, expected_result))

    return benchmark_element_expected
