from django import template
register = template.Library()

@register.simple_tag
def getCaptchaSiteKey():
    """
        :Template Tag Function: to return the captcha site key
        :param: None
        :type: None
        :return: site key
        :return type: string
    """
    return '6Lc0NdQcAAAAAJP_NqDUhfo4Ysbj05aRD9V_qcRC'