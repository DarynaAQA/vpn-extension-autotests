class BaseLocators:
    MainWindow = 'qa-main-wrapper'
    BurgerMenuButton = 'main-head__btn'
    LogoPlanetVpn = 'main-head__logo'
    LoginIcon = 'qa-head-col-login'
    ButtonSelectCountry = 'qa-select-country'
    CurrentLocation = 'qa-status-country'
    ConnectionProtection = 'qa-status-block'
    PlanetIcon = 'animation-box'
    ConnectButton = 'qa-connect-button'
    IndicatorAutoconnect = 'qa-icon-connect'
    IndicatorAdblocker = 'qa-icon-block-ads'
    IndicatorCookies = 'qa-icon-cookies'
    IndicatorTrackers = 'qa-icon-trackers'
    IndicatorHistory = 'qa-icon-history'
    IndicatorSmartFilters = 'qa-icon-filters'
    Banner = 'qa-main-banner'
    Title = 'qa-head-title'
    PopupAutoconnectStatus = 'popup__title'
    PopupAdBlockerStatus = 'qa-popup-adblocker-status'
    PopupCookiesStatus = 'qa-popup-cookies-status'
    PopupTrackersStatus = 'qa-popup-trackers-status'
    PopupHistoryStatus = 'qa-popup-history-status'
    PopupSmartFiltersStatus = 'qa-popup-smart-filters-status'
    PanelIndicators = 'indicators-icons'
    BannerPremium = 'qa-banner'
    CONNECT_STATUS = 'qa-status-protection'
    INDICATOR_PROTECTED = 'qa-status-indicator-protected'
    IP_INFO_IP = 'text-green-05'
    IP_CITY = '//*[@id="city-string"]/div/span/span[2]/span'  # IP info website
    IP_COUNTRY_CODE = '//*[@id="country-string"]/div/span/span[2]/span'  # IP info website
    CONNECT_IS_NOT_SECURE = 'unprotected'
    WHY_DO_I_NEED_A_VPN = '0'
    SPAN_WHY_DO_I_NEED_A_VPN = 'answer-0'
    ITS_FREE = '1'
    SPAN_ITS_FREE = 'answer-1'
    HOW_TO_USE = '2'
    SPAN_HOW_TO_USE = 'answer-2'
    WHERE_IS_MY_PASSWORD = '3'
    SPAN_WHERE_IS_MY_PASSWORD = 'answer-3'
    AFTER_THE_PURCHASE = '4'
    SPAN_AFTER_THE_PURCHASE = 'answer-4'
    HOW_MANY_DEVICES = '5'
    SPAN_HOW_MANY_DEVICES = 'answer-5'
    WHY_DOES_SPEED = '6'
    SPAN_WHY_DOES_SPEED = 'answer-6'
    DO_YOU_FOLLOW_USERS = '7'
    SPAN_DO_YOU_FOLLOW_USERS = 'answer-7'
    DO_YOU_HAVE_ANY_QUESTIONS = 'qa-form-head-questions'
    INPUT_YOUR_NAME = 'qa-faq-form-input-name'
    INPUT_YOUR_EMAIL = 'qa-faq-form-input-email'
    TEXT_AREA_CAN_WE_HELP_YOU = 'qa-faq-form-textarea'
    SUBMIT_BUTTON_GREEN = 'qa-faq-form-button-send'
    CONNECT_BUTTON_GREEN = 'v-button--green'
    CONNECTING_BUTTON_BLUE_GRAY = 'v-button--grey'
    BUTTON_CONNECTED_RED = 'v-button--red'
    BUTTON_LOGIN = 'qa-auth-btn-login'
    RATE_POP_UP = 'modal__box'
    DONT_SHOW_AGAIN_BUTTON = 'v-checkbox__checkmark'
    CLOSE_BUTTON = '/html/body/div/div[6]/div/div/div[1]'
    SelectServer = 'select-country'
    AvailableLocations = 'qa-head-available-locations'
    ConnectStatus = '//div[contains(text(), "Connection is secure")]'
    FaqTitle = 'qa-head-faq'
    MoreInformationText = 'qa-faq-help'
    GetPremiumButton = 'qa-button-premium'
    PlanetLogo = 'main-head'
    LogoutButton = 'qa-main-head-btn-logout'
    RedButton = 'qa-interstitial-button-red'
    ConnectSecure = '//*[contains(text(), "Connection is secure")]'
    DisconnectButton = '//*[contains(text(), "Disconnect")]'
    AdvertisingFreeUser = 'interstitial-content'
    WhiteButton = 'qa-interstitial-button-white'
    ClosePopUp = 'timer'


class PremiumBenefits:
    WindowPremiumBenefits = 'modal-premium'
    CloseButton = 'modal-premium__close'
    StartOrdering = 'qa-modal-premium-btn'


class AuthLocators:
    AuthorizationTitle = 'qa-signin-head'


