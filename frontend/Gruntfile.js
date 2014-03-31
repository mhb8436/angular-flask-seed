module.exports = function(grunt) {

  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-open');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-connect');

  grunt.initConfig({
    shell: {
      options : {
        stdout: true
      },
      npm_install: {
        command: 'npm install'
      },
      bower_install: {
        command: './node_modules/.bin/bower install'
      }
    },

    connect: {
      options: {
        base: 'app/'
      },
      webserver: {
        options: {
          port: 8888,
          keepalive: true
        }
      },
      devserver: {
        options: {
          port: 8888
        }
      }
    },

    open: {
      devserver: {
        path: 'http://localhost:8888'
      }
    },

    watch: {
      assets: {
        files: ['app/assets/vendor/**/*.js','app/js/**/*.js'],
        tasks: ['concat']
      }
    },

    concat: {
      scripts: {
        options: {
          separator: ';'
        },
        dest: './app/build/app.js',
        src: [
          'app/assets/vendor/underscore.js',
          'app/assets/vendor/angular.js',
          'app/assets/vendor/angular-route.js',
          'app/assets/vendor/angular-resource.js',
          'app/assets/vendor/angular-cookies.js',
          'app/assets/vendor/angular-loader.js',
          'app/assets/vendor/angular-sanitize.js',
          'app/assets/vendor/angular-animate.js',
          'app/js/lib/router.js',
          'app/js/config/config.js',
          'app/js/services/**/*.js',
          'app/js/directives/**/*.js',
          'app/js/controllers/**/*.js',
          'app/js/filters/**/*.js',
          'app/js/config/routes.js',
          'app/js/app.js'
          
        ]
      }
    }
  });

  grunt.registerTask('install', ['shell:npm_install','shell:bower_install']);
  grunt.registerTask('default', ['dev']);
  grunt.registerTask('dev', ['install', 'concat', 'connect:devserver', 'open:devserver', 'watch:assets']);
  grunt.registerTask('serve', ['connect:webserver']);
};
