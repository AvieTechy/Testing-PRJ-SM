import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('https://with-bugs.practicesoftwaretesting.com/#/')

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Hand Tools_nav-link active'))

// Verification
WebUI.verifyElementPresent(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Hand Tools_nav-link active'), 10, FailureHandling.STOP_ON_FAILURE)

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Home_nav-link dropdown-toggle show'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Home_dropdown-item'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Rentals_nav-link'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_Contakt_nav-link'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.selectOptionByValue(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/select_Sorth_form-select'), 
    sort_value, true)

WebUI.selectOptionByValue(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/select_Sorth_form-select'), 
    '', true)

WebUI.setText(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Search_form-control ng-untouched ng-p_459ff9'), 
    search_value)

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Search_form-control ng-untouched ng-p_459ff9'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/button_Search_btn btn-warning'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Hammer_category_id'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Hand Saw_category_id'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Wrench_category_id'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Screwdriver_category_id'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Pliers_category_id'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Grinder_category_id'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/label'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Sander_category_id'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/label_1'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/input_Brand name 1_brand_id'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/span'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/a_1'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/div_Brand name 2_col-md-9'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img_Filters_card-img-top'))

WebUI.click(findTestObject('Object Repository/Page_Practice Software Testing - Toolshop -_8413b3/img'))

WebUI.closeBrowser()

