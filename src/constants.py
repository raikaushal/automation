
class Urls:
    """web urls"""
    BASE_URL = "https://epds.bihar.gov.in/smdel/"
    SEARCH_MEMBER_URL = "https://epds.bihar.gov.in/smdel/Operator/SearchMember.aspx"


class Attributes:
    """Html tags attributes"""
    USERNAME_ID = "ContentPlaceHolder2_TxtUid"
    PASSWORD_ID = "ContentPlaceHolder2_TxtPwd"
    LOGIN_BUTTON_NAME = "ctl00$ContentPlaceHolder2$BtnLogin"
    DISTRIC_NAME = "ctl00$ContentPlaceHolder1$ddldistrict"
    SUBDIVISION_NAME = "ctl00$ContentPlaceHolder1$ddlsubdivision"
    BLOCK_TOWN_NAME = "ctl00$ContentPlaceHolder1$ddlBlockTown"
    RC_NUMBER = "ContentPlaceHolder1_txtrcnumber"
    SEARCH_BUTTON_ID = "ContentPlaceHolder1_btnsearch"
    # This might change in future
    MEMBER_LINK_XPATH = '//*[@id="ContentPlaceHolder1_gridview_member"]/tbody/tr[2]/td[12]'
    TABLE_ID = "gridview_member"
    ROW_XPATH = ".//tr"
    DATA_XPATH = ".//td"
    CHECK_BOX_ID = "gridview_member_chkSelect_[INDEX]"
    NOTICE_ISSUE_NUMBER = "txtnoticeissueno"
    ORDER_ISSUE_NUMBER = "txtorderissueno"
    NOTICE_ISSUE_DATE = "txtnotieissuedate"
    ORDER_ISSUE_DATE = "txtorderissuedate"
    SOURCE_OF_INFO_DELETION = "ddlsourceofdeletion"
    REASON_FOR_DELETON = "ddldelitionregion"
    NOTICE_UPLOAD = "filenotice"
    ORDER_UPLOAD = "fileOrder"
    FINAL_SUBMIT = "btnUpload"
    MO_NAME = "txtmo"


class Constants:
    "literal constants"
    INDEX = "[INDEX]"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    ENV = "ENV"
    RC_NUM = 'Ration Card Number'
    NOTICE_NUM = 'Notice No'
    NOTICE_DATE = 'Notice Date '
    ORDER_NO = 'Order No '
    ORDER_DATE = 'Order date '
