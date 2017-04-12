from flask_assets import Bundle

common_css = Bundle(
    'css/vendor/bootstrap.min.css',
    'css/vendor/helper.css',
    'css/main.css',
    #'css/style.css',
    #'css/materialize.min.css',
    filters='cssmin',
    output='public/css/common.css'
)

common_js = Bundle(
    #'js/vendor/jquery.min.js',
    'js/vendor/bootstrap.min.js',
    'js/jquery-3.2.1.min.js',
    #'js/materialize.min.js',
    Bundle(
        'js/main.js',
        filters='jsmin'
    ),
    output='public/js/common.js'
)
