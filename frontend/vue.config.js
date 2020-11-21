const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    // on Windows you might want to set publicPath: "http://127.0.0.1:8080/" 
    publicPath: "https://questbackend-2.herokuapp.com/", 
    outputDir: './dist/',

    chainWebpack: config => {

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: './webpack-stats.json'}])

        config.output
            .filename('bundle.js')

        config.optimization
        	.splitChunks(false)

        config.resolve.alias
            .set('__STATIC__', 'static')

        config.devServer
            // the first 3 lines of the following code have been added to the configuration
            .public('https://questbackend-2.herokuapp.com')    
            .host('questbackend-2.herokuapp.com')    
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(true)
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": ["\*"]})

    },

    // uncomment before executing 'npm run build' 
    css: {
        extract: {
          filename: 'bundle.css',
          chunkFilename: 'bundle.css',
        },
    }

};

//{"status":"done","publicPath":"http://127.0.0.1:8000/","chunks":{"app":[{"name":"bundle.css","publicPath":"http://127.0.0.1:8000/static/bundle.css","path":"F:\\vuetifyapps\\quest\\QuestionTime\\frontend\\dist\\bundle.css"},{"name":"bundle.js","publicPath":"http://127.0.0.1:8000/static/bundle.js","path":"F:\\vuetifyapps\\quest\\QuestionTime\\frontend\\dist\\bundle.js"},{"name":"bundle.css.map","publicPath":"http://127.0.0.1:8000/static/bundle.css.map","path":"F:\\vuetifyapps\\quest\\QuestionTime\\frontend\\dist\\bundle.css.map"},{"name":"bundle.js.map","publicPath":"http://127.0.0.1:8000/static/bundle.js.map","path":"F:\\vuetifyapps\\quest\\QuestionTime\\frontend\\dist\\bundle.js.map"}]}}