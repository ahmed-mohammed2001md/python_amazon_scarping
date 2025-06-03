# =================
# = File Dirs
# =================


SAVE_DATA_DIR = 'outputs'


# =================
# = sleep timer
# =================


MIN_SCARPING_SESSION = 10
MAX_SCARPING_SESSION = 15

MIN_SLEEP_DELAY = 5
MAX_SLEEP_DELAY = 10

MIN_CAPTCHA_DELAY = 10
MAX_CAPTCHA_DELAY = 15


# ====================
# = Elements Selctors
# ====================

TITLE = '#title'
CURRENT_PRICE = '.a-price-whole'
LIST_PRICE = '.a-price.a-text-price > :first-child'
DISSCOUNT = 'span.a-size-large.a-color-price.savingPriceOverride.aok-align-center.reinventPriceSavingsPercentageMargin.savingsPercentage'
RATING = '.a-declarative > .a-size-base.a-color-base'
ASIN = lambda url: url[url.index('dp/') + 3 : url.index('dp/') + 13]
REVIEWS_COUNT = '#cm_cr_dp_d_rating_histogram .averageStarRatingNumerical span'
SELLER = '#bylineInfo'
AVAILABILITY = '#availability'
MAIN_IMG = '#imgTagWrapperId'
PRODUCT_OVER_VIEW = '#productOverview_feature_div #poExpander table tbody'
SIDE_IMGS = '#altImages ul'
SIZES = '#inline-twister-row-size_name #tp-inline-twister-dim-values-container > ul'
COLORS = '#inline-twister-expander-content-color_name ul'
STYLES = '#inline-twister-row-style_name #inline-twister-expander-content-style_name #tp-inline-twister-dim-values-container ul'
EDITIONS = '#twister_feature_div #tp-inline-twister-dim-values-container ul'
