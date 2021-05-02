const gulp = require('gulp');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const uglify = require('gulp-uglify');
const sass = require('gulp-dart-sass');
const gulpautoprefixer = require('gulp-autoprefixer');
const path = require('path');


const paths = {
  styles: {
    src: 'libs/sass/*.scss',
    dest: 'material/static/material/admin/css/'
  },
  scripts: {
    src: 'libs/js/*.js',
    dest: 'material/static/material/admin/js/'
  }
};



gulp.task('sass', function () {
  return gulp.src(paths.styles.src)
    .pipe(sass().on('error', sass.logError))
    .pipe(gulpautoprefixer({overrideBrowserslist: 'defaults'}))
    .pipe(cleanCSS())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(paths.styles.dest));

});

gulp.task('watch', function() {
  gulp.watch(paths.styles.src, gulp.series('sass'));  // Watch all the .scss files, then run the sass task
});


gulp.task('uglify-js', function() {
  return gulp.src(paths.scripts.src)
    .pipe(uglify())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(paths.scripts.dest))
});

gulp.task('default', gulp.series('sass','uglify-js'));
