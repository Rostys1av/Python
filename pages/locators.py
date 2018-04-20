from selenium.webdriver.common.by import By


class LoginRegistrationPopup():
    INPUTMAILLOGIN_loc      = (By.ID, 'in_login')
    INPUTPASSLOGIN_loc      = (By.ID, 'in_password')
    CHECKBOXREMEMBER_loc    = (By.XPATH, '//label[@for="mycheckbox1"]')
    EYEPASS_loc             = (By.XPATH, '//I[@class="ochi_pass"]')
    BTNLOGIN_loc            = (By.ID,'open_go_login')
    BTNFORGOTPASS_loc       = (By.ID,'form_forget_password')
    BTNFACEBOOK_loc         = (By.XPATH,'//i[@class="fa fa-facebook"]')
    BTNGOOGLEPLUS_loc       = (By.XPATH,'//i[@class="fa fa-google-plus"]')
    BTNTWITTER_loc          = (By.XPATH,'//i[@class="fa fa-twitter"]')
    BTNLINKEDIN_loc         = (By.XPATH,'//i[@class="fa fa-linkedin"]')
    INPUTNICK_loc           = (By.ID,'in_nickname')
    INPUTMAILREG_loc        = (By.ID,'in_email')
    SELECTCOUNTRY_loc       = (By.ID,'in_select_country')
    CHECKBOXSUBCRIBE_loc    = (By.XPATH,'//label[@for="mycheckbox2"]')
    BTNSIGNUP_loc           = (By.ID,'open_register')
    BTNCLOSEPOPUP_loc       = (By.ID,'//I[@class="ic ic-close"]')

class AboutUsPage():
    BTNJOINUSNOW_loc        = (By.ID,'header_href_about_us')


