from flask_assets import Bundle
common_css = Bundle(
    'css/main.css',
    'css/materialize.min.css',
    filters='cssmin',
    output='public/css/common.css'
)
common_js = Bundle(
    'js/jquery-3.2.1.min.js',
    'js/materialize.min.js',
    Bundle(
        'js/main.js',
        filters='jsmin'
    ),
    output='public/js/common.js'
)
