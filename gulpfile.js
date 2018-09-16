const gulp = require('gulp');
const cleanCSS = require('gulp-clean-css');
const rename = require('gulp-rename');
const uglify = require('gulp-uglify');

const paths = {
  styles: {
    src: 'libs/css/*.css',
    dest: 'material_admin/static/material_admin/css/'
  },
  scripts: {
    src: 'libs/js/*.js',
    dest: 'material_admin/static/material_admin/js/'
  }
};

gulp.task('minify-css', function () {
    return gulp.src(paths.styles.src)
    .pipe(cleanCSS())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(paths.styles.dest));
});


gulp.task('uglify-js', function() {
  return gulp.src(paths.scripts.src)
    .pipe(uglify())
    .pipe(rename({
      suffix: '.min'
    }))
    .pipe(gulp.dest(paths.scripts.dest))
});

gulp.task('default', ['minify-css', 'uglify-js']);
