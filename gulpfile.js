var gulp = require('gulp');
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');

var jsFiles = ['*.js', 'src/**/*.js'];

gulp.task('default', ['sass:watch']);

gulp.task('sass', function () {
  return gulp.src('./public/sass/styles.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./public/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./public/sass/**/*.scss', ['sass', 'inject']);
});

gulp.task('jshint', function(){
   return gulp.src(jsFiles)
    .pipe(jshint())
    .pipe(jshint.reporter('jshint-stylish', {
       verbose: true
   }));
});

gulp.task('inject', function(){
    var wiredep = require('wiredep').stream;
    var inject = require('gulp-inject');

    var injectSrc = gulp.src(['./public/css/*.css',
                             './public/js/*.js'], {read: false});
    var injectOptions = {
        ignorePath: '/public'
    };

    var options = {
        bowerJson: require('./bower.json'),
        directory: './public/lib',
        ignorePath: '../../public'
    };

    return gulp.src('./hello/templates/*.html')
        .pipe(wiredep(options))
        .pipe(inject(injectSrc, injectOptions))
        .pipe(gulp.dest('./hello/templates'));

});
